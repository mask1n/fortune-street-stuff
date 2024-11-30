import dolphin_memory_engine as dolphin
import time
import os
import csv
from externals import character_set, languages, user_lang

# Init text language pack (will default to English if user's language unsupported)
text_lang = 'en'
if user_lang in languages:
    text_lang = user_lang

lang_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'lang',f"{text_lang}.csv")
text = {}

with open(lang_file_path, 'r', encoding='utf-16') as lang_file: # language CSVs must be encoded as UTF-16BE
    try:
        reader = csv.reader(lang_file)
        for row in reader:
            key = row[0]
            value = row[1]

            text[key] = value

    except OSError as error:
        print("Language file couldn't be opened: ", error)
        input("")
        exit()

header_lines = [text['header_1'],text['header_2'],text['header_3'],text['header_4'],text['header_5'],text['header_6'],text['header_7'],text['header_1']]
for line in header_lines:
    print(line)
time.sleep(0.25)

# Initalise character name for replacement
clearname = bytes([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

def exit_prompt():
    input(text['exit']) # "Press ENTER to exit."
    exit()

# Hooks into currently running Dolphin process (emulation needs to already be started)
dolphin.hook()
if not dolphin.is_hooked():
    print(text['no_hook']) # "Couldn't hook into Dolphin.")
    print(text['no_hook2']) # "Please make sure that emulation has started, then re-run this program."
    exit_prompt()
else:
    print(text['hooked']) # "Hooked into Dolphin!"
    gameid = dolphin.read_bytes(0x80000000, 6).decode('utf-8') # reads the game ID as a string
    
# 'Scene' refers to which screen the game's currently on (for this purpose, to guarantee that the main function starts
# after characters have been selected)
game_info = {
    "ST7E01": {"name": text['ntsc_name'], "base_ptr": 0x8081727C, "scene_addr": 0x808162EB}, # ST7J = Fortune Street
    "ST7P01": {"name": text['pal_name'], "base_ptr": 0x8081747C, "scene_addr": 0x808164EB}, # ST7P = Boom Street
    "ST7E02": {"name": text['ntsc_mod'], "base_ptr": 0x8081727C, "scene_addr": 0x808162EB},
    "ST7P02": {"name": text['pal_mod'], "base_ptr": 0x8081747C, "scene_addr": 0x808164EB},
    "ST7JGD": {"name": text['jp_name'], "base_ptr": 0x8081717C, "scene_addr": 0x808161EB}, # ST7JG = Itadaki Street
    "ST7J02": {"name": text['jp_mod'], "base_ptr": 0x8081717C, "scene_addr": 0x808161EB}
}

if gameid in game_info: # Detects which version of the game is running
    game_name = game_info[gameid]["name"]
    base_ptr = game_info[gameid]["base_ptr"]
    scene_addr = game_info[gameid]["scene_addr"]
    base_addr = int.from_bytes(dolphin.read_bytes(base_ptr, 4))
    print(text['game_detected'].format(game_name)) # "{game_name} detected"
else:
    print(text['unsupported']) # "The currently running game is not supported by this program."
    exit_prompt()

def nameentry():
    players = [
        {'player': 1, 'address': base_addr + 0x21C},
        {'player': 2, 'address': base_addr + 0x2A0},
        {'player': 3, 'address': base_addr + 0x324},
        {'player': 4, 'address': base_addr + 0x3A8}
    ]

    # Grab character names from game memory (22 being the byte length of the longest name (Donkey Kong))
    # Character names are encoded in UTF-16BE
    for player in players:
        player['name'] = dolphin.read_bytes(player['address'], 22).decode('utf-16be').replace('\x00', '')
    
    ## Showtime 8)
    print(text['ok']) # "OK, ready to go!"
    print(text['char_limit_explain']) # "Please make sure each player's name fits within 18 characters."
    time.sleep(0.85)
    print("")

    def get_name_input(player_name):
        while True:
            name_input = input(text['who'].format(player_name)) # "Who's playing as {player_name}? "
            invalid_chars = set(name_input) - character_set  # subtract any characters in name_input that are from charset
            if invalid_chars:                               # if there's anything left in invalid_chars, the name itself is invalid 
                print(text['invalid_character'].format(invalid_chars)) # "Sorry, try entering a name without these characters: {invalid_chars}"
                continue
            if len(name_input) > 18:
                len_diff = len(name_input)-18
                print(text['too_long_name'].format(name_input, len_diff)) #"{name_input} exceeds the character limit by {len_diff}!"
                continue
            return name_input

    for player in players: # Take user input, encode it, blank out the original character name then replace it with the new one
        player['new_name'] = get_name_input(player['name']).encode('utf-16be')
        dolphin.write_bytes(player["address"],clearname)
        dolphin.write_bytes(player["address"],player['new_name'])

    print("")
    print(text['done']) # "All done!"
    exit_prompt()

# Wait until players are at the map selection screen before allowing them to input their names
def waitformapselect():
    print(text['waiting'])
    #print("Waiting for the board select screen...")
    scene = (dolphin.read_byte(scene_addr))
    while scene!= 7:
        scene = (dolphin.read_byte(scene_addr))
    nameentry()


if __name__ == "__main__":
    waitformapselect()