import dolphin_memory_engine
import time
from game_font import charset

## 18 bytes for clearing out names
clearname = bytes([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# Hooks into currently running Dolphin process (emulation needs to already be started)
dolphin_memory_engine.hook()
if not dolphin_memory_engine.is_hooked():
    print("Couldn't hook into Dolphin :(")
    print("Any feedback or questions, please contact")
    input("@mask1n in the Custom Street Discord")
    quit()
else:
    print("Hooked into Dolphin!")
    gameid = dolphin_memory_engine.read_bytes(0x80000000, 6).decode('utf-8') # reads the game ID as a string
    
# 'Scene' refers to which screen the game's currently on (for this purpose, to guarantee that the main function starts
# after characters have been selected)
game_info = {
    "ST7E01": {"name": "Fortune Street", "base_ptr": 0x8081727C, "scene_addr": 0x808162EB},
    "ST7P01": {"name": "Boom Street", "base_ptr": 0x8081747C, "scene_addr": 0x808164EB},
    "ST7E02": {"name": "Fortune Street mod", "base_ptr": 0x8081727C, "scene_addr": 0x808162EB},
    "ST7P02": {"name": "Boom Street mod", "base_ptr": 0x8081747C, "scene_addr": 0x808164EB},
    "ST7JGD": {"name": "いただきストリートWii", "base_ptr": 0x8081717C, "scene_addr": 0x808161EB},
    "ST7J02": {"name": "いただきストリートWii mod", "base_ptr": 0x8081717C, "scene_addr": 0x808161EB}
}

if gameid in game_info: # Detects which version of the game is running
    game_name = game_info[gameid]["name"]
    base_ptr = game_info[gameid]["base_ptr"]
    scene_addr = game_info[gameid]["scene_addr"]
    base_addr = int.from_bytes(dolphin_memory_engine.read_bytes(base_ptr, 4))
    print(f"{game_name} detected")
else:
    input("Game not supported, sorry!")
    exit()

def nameentry():
    p1 = base_addr + 0x21C
    p2 = base_addr + 0x2A0
    p3 = base_addr + 0x324
    p4 = base_addr + 0x3A8

    # Grab character names from game memory (22 being the byte length of the longest name (Donkey Kong))
    # Character names are encoded in UTF-16BE
    p1name = dolphin_memory_engine.read_bytes(p1, 22).decode('utf-16be').replace('\x00', '')
    p2name = dolphin_memory_engine.read_bytes(p2, 22).decode('utf-16be').replace('\x00', '')
    p3name = dolphin_memory_engine.read_bytes(p3, 22).decode('utf-16be').replace('\x00', '')
    p4name = dolphin_memory_engine.read_bytes(p4, 22).decode('utf-16be').replace('\x00', '')
    
    ## Showtime 8)
    print("OK, ready to go!")
    print("Please make sure each player's name fits within 18 characters.")
    time.sleep(0.85)
    print("")

    def get_name_input(player_name):
        while True:
            name_input = input(f"Who's playing as {player_name}? ")
            invalid_chars = set(name_input) - set(charset)  # subtract any characters in name_input that are from charset
            if invalid_chars:                               # if there's anything left in invalid_chars, the name itself is invalid 
                print(f"Sorry, try entering a name without these characters: {invalid_chars}")
                continue
            if len(name_input) > 18:
                print(f"{name_input} exceeds the character limit by {len(name_input)-18}!")
                continue
                #name_input = input("Please enter a shorter name: ")
            return name_input

    p1input = get_name_input(p1name)
    p2input = get_name_input(p2name)
    p3input = get_name_input(p3name)
    p4input = get_name_input(p4name)
    
    # Encode player names in UTF-16BE
    p1sub = p1input.encode('utf-16be')
    p2sub = p2input.encode('utf-16be')
    p3sub = p3input.encode('utf-16be')
    p4sub = p4input.encode('utf-16be')
    
    # Blank out player names before insertion
    dolphin_memory_engine.write_bytes(p1, clearname)
    dolphin_memory_engine.write_bytes(p2, clearname)
    dolphin_memory_engine.write_bytes(p3, clearname)
    dolphin_memory_engine.write_bytes(p4, clearname)
    
    # Inject new names
    dolphin_memory_engine.write_bytes(p1, p1sub)
    dolphin_memory_engine.write_bytes(p2, p2sub)
    dolphin_memory_engine.write_bytes(p3, p3sub)
    dolphin_memory_engine.write_bytes(p4, p4sub)
    print("")
    print("All done! Press ENTER to exit.")
    print("Any feedback or questions, please contact")
    input("@mask1n in the Custom Street Discord")
    quit()

# Wait until players are at the map selection screen before allowing them to input their names
def waitformapselect():
    print("Waiting for the board select screen...")
    scene = (dolphin_memory_engine.read_byte(scene_addr))
    while scene!= 7:
        scene = (dolphin_memory_engine.read_byte(scene_addr))
    nameentry()

waitformapselect()