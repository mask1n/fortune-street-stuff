import time
import dolphin_memory_engine

## 30 bytes for clearing out names
blanks = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
clearname = bytes(blanks)

## Name decoding and entry routine
def nameentry():
    cswtp1 = 0x8160411C
    cswtp2 = 0x816041A0
    cswtp3 = 0x81604224
    cswtp4 = 0x816042A8
    cswtpalp1 = 0x8160507C
    cswtpalp2 = 0x81605100
    cswtpalp3 = 0x81605184
    cswtpalp4 = 0x81605208
    basep1 = 0x816072FC
    basep2 = 0x81607380
    basep3 = 0x81607404
    basep4 = 0x81607488
    if gameid == "ST7E01" or gameid == "ST7P01" or gameid == "ST7JGD":
        p1 = basep1
        p2 = basep2
        p3 = basep3
        p4 = basep4
    else:
        if gameid=="ST7E02":
            p1 = cswtp1
            p2 = cswtp2
            p3 = cswtp3
            p4 = cswtp4
        else:
                if gameid=="ST7P02":
                    p1 = cswtpalp1
                    p2 = cswtpalp2
                    p3 = cswtpalp3
                    p4 = cswtpalp4

    ## Grab character names from game memory
    ## (22 being the length of the longest name (Donkey Kong))
    ## (character names are encoded in memory in UTF-16BE)
    p1name = (dolphin_memory_engine.read_bytes((p1), 22))
    p2name = (dolphin_memory_engine.read_bytes((p2), 22))
    p3name = (dolphin_memory_engine.read_bytes((p3), 22))
    p4name = (dolphin_memory_engine.read_bytes((p4), 22))
    ### Convert names from byte array to UTF-8 text then remove the filler null characters
    p1name = str(p1name.decode('utf-16be'))
    p1name = p1name.replace('\x00', '')
    p2name = str(p2name.decode('utf-16be'))
    p2name = p2name.replace('\x00', '')
    p3name = str(p3name.decode('utf-16be'))
    p3name = p3name.replace('\x00', '')
    p4name = str(p4name.decode('utf-16be'))
    p4name = p4name.replace('\x00', '')
    ## Showtime 8)
    print("OK, ready to go!")
    time.sleep(0.85)
    p1input = input("Who's controlling " + (p1name) + "? ")
    p2input = input("Who's controlling " + (p2name) + "? ")
    p3input = input("Who's controlling " + (p3name) + "? ")
    p4input = input("Who's controlling " + (p4name) + "? ")
    ## Encode player names in UTF-16BE
    p1sub = p1input.encode('utf-16be')
    p2sub = p2input.encode('utf-16be')
    p3sub = p3input.encode('utf-16be')
    p4sub = p4input.encode('utf-16be')
    ## Blank out player names before insertion
    dolphin_memory_engine.write_bytes((p1), clearname)
    dolphin_memory_engine.write_bytes((p2), clearname)
    dolphin_memory_engine.write_bytes((p3), clearname)
    dolphin_memory_engine.write_bytes((p4), clearname)
    ## Inject new names
    dolphin_memory_engine.write_bytes((p1), p1sub)
    dolphin_memory_engine.write_bytes((p2), p2sub)
    dolphin_memory_engine.write_bytes((p3), p3sub)
    dolphin_memory_engine.write_bytes((p4), p4sub)
    print("All done! Press ENTER to exit.")
    print("Any feedback or questions, please contact")
    input("@mask1n in the Custom Street Discord")

## Wait until players are at the map selection screen
## before allowing them to input their names
printed=False
def waitformapselect(printed):
    ntscscene = 0x808162EB
    palscene = 0x808164EB
    jpscene = 0x808161EB
    print("Waiting for the board select screen...")
    if gameid == "ST7E01" or gameid == "ST7E02":
        scenergn = ntscscene
    elif gameid == "ST7P01" or gameid == "ST7P02":
            scenergn = palscene
    elif gameid == "ST7JGD":
            scenergn = jpscene
    scene = (dolphin_memory_engine.read_byte(scenergn))
    if scene == 7:
        nameentry()
    else:
        while scene!= 7:
            scene = (dolphin_memory_engine.read_byte(scenergn))
            time.sleep(0.1)
    if scene == 7:
        nameentry()

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
if gameid== "ST7E01":
    print("Fortune Street detected")
elif gameid== "ST7P01":
    print("Boom Street detected")
elif gameid== "ST7E02" or gameid== "ST7P02":
    print("Custom Street World Tour detected")
elif gameid== "ST7JGD":
    print("いただきストリートWii detected")
elif gameid!="ST7E01" or gameid!="ST7E02" or gameid!="ST7P01" or gameid!="ST7P02" or gameid!="ST7JGD":
        input("Game not supported, sorry!")
        exit()
waitformapselect(False)