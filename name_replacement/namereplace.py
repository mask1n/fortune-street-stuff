import time
import dolphin_memory_engine

## 30 bytes for clearing out names
blanks = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
clearname = bytes(blanks)

## Hooks into currently running Dolphin process
## (emulation needs to already be started)
## Also checks to see if user is running CSWT via Game ID
dolphin_memory_engine.hook()
if not dolphin_memory_engine.is_hooked():
    print("Couldn't hook into Dolphin :(")
    input("Please make sure that emulation's started, then run this script again.")
    exit()
else:
    print("Hooked into Dolphin!")
    gameid= str(dolphin_memory_engine.read_bytes(0x80000000, 6))
    gameid= ((gameid)[2:-1]) ##truncate b' and ' from gameid (the first two and last character)
    print("Game ID: " + (gameid))
if gameid!= "ST7E02":
    input("This script currently only supports the NTSC version of CSWT, sorry!")
    exit()
else:

## (use these once PAL and vanilla ISOs are supported)
    cswtp1 = ("0x8160411D")
    cswtp2 = ("0x816041A1")
    cswtp3 = ("0x81604225")
    cswtp4 = ("0x816042A9")

## Name decoding and entry routine
def nameentry():
    ## Grab character names from game memory
    ## (22 being the length of the longest name (Donkey Kong))
    ## (character names are encoded in memory in UTF-16LE)
    p1name = (dolphin_memory_engine.read_bytes(0x8160411D, 22))
    p2name = (dolphin_memory_engine.read_bytes(0x816041A1, 22))
    p3name = (dolphin_memory_engine.read_bytes(0x81604225, 22))
    p4name = (dolphin_memory_engine.read_bytes(0x816042A9, 22))
    ### Convert names from byte array to UTF-8 text then remove the filler null characters
    p1name = str(p1name.decode('utf-8'))
    p1name = p1name.replace('\x00', '')
    p2name = str(p2name.decode('utf-8'))
    p2name = p2name.replace('\x00', '')
    p3name = str(p3name.decode('utf-8'))
    p3name = p3name.replace('\x00', '')
    p4name = str(p4name.decode('utf-8'))
    p4name = p4name.replace('\x00', '')
    ## Showtime 8)
    print("OK, ready to go!")
    time.sleep(0.85)
    p1input = input("Who's controlling " + (p1name) + "? ")
    p2input = input("Who's controlling " + (p2name) + "? ")
    p3input = input("Who's controlling " + (p3name) + "? ")
    p4input = input("Who's controlling " + (p4name) + "? ")
    ## Encode player names in UTF-16LE
    p1sub = p1input.encode('utf-16le')
    p2sub = p2input.encode('utf-16le')
    p3sub = p3input.encode('utf-16le')
    p4sub = p4input.encode('utf-16le')
    ## Blank out player names before insertion
    dolphin_memory_engine.write_bytes(0x8160411D, clearname)
    dolphin_memory_engine.write_bytes(0x816041A1, clearname)
    dolphin_memory_engine.write_bytes(0x81604225, clearname)
    dolphin_memory_engine.write_bytes(0x816042A9, clearname)
    ## Inject new names
    dolphin_memory_engine.write_bytes(0x8160411D, p1sub)
    dolphin_memory_engine.write_bytes(0x816041A1, p2sub)
    dolphin_memory_engine.write_bytes(0x81604225, p3sub)
    dolphin_memory_engine.write_bytes(0x816042A9, p4sub)
    ## TODO: If first character of a player's name is in Hiragana/Katakana (between 8152-8396),
    ##       write 0x30 to the byte preceding the offset for said player
    ## note: Kanji isn't possible (or accepted in Mii names at all)
    ##       so maybe read the first two bytes to see if they're above 889F
    ##       [low priority atm since lack of Japanese-speaking playerbase]
    ##    dolphin_memory_engine.write_bytes(0x8160411C, b'\x30')
    ##    dolphin_memory_engine.write_bytes(0x816041A0, b'\x30')
    ##    dolphin_memory_engine.write_bytes(0x81604224, b'\x30')
    ##    dolphin_memory_engine.write_bytes(0x816042A8, b'\x30')
    print("All done! Press ENTER to exit.")
    print("Any feedback or questions, please contact")
    input("@mask1n in the Custom Street Discord")

## Wait until players are at the map selection screen
## before allowing them to input their names
printed=False
def waitformapselect(printed):
    print("Waiting for the board select screen...")
    scene = (dolphin_memory_engine.read_byte(0x808162EB))
    if scene == 7:
        nameentry()
    else:
        while scene!= 7:
            scene = (dolphin_memory_engine.read_byte(0x808162EB))
            time.sleep(0.1)
    if scene == 7:
        nameentry()

waitformapselect(False)