# Name replacement script for Custom Street World Tour (CSWT)
Changes character names in-game without needing to modify the ISO or manually inject bytes into memory
![image](https://user-images.githubusercontent.com/83397594/153533310-8102e3f8-719d-47e5-8709-835b3fe8b6ed.png)


## Requirements
- This script assumes you've already patched an NTSC-U Fortune Street ISO with [Custom Street World Tour](https://github.com/FortuneStreetModding/CustomStreetWorldTour)
- Python 3.6 or later
- [Dolphin Emulator](https://dolphin-emu.org/)
- [py-dolphin-memory-engine](https://github.com/henriquegemignani/py-dolphin-memory-engine) (optional if using the Windows release binary) (use `pip install dolphin-memory-engine` to install)

## How to use
1. Start emulation of CSWT in Dolphin
2. Run `namereplace.py` (or [namereplace.exe](https://github.com/mask1n/fortune-street-stuff/releases/) for Windows users if you're using the release version)
3. After selecting your characters and advancing to the board selection screen, you'll be prompted to input each player's name
4. Enjoy! 😃

## TODO:
- Support for PAL CSWT and vanilla Fortune/Boom/Itadaki Street ISOs

## Links
- [Custom Street Discord server](https://discord.gg/DE9Hn7T)
- [Dolphin Memory Engine](https://github.com/aldelaro5/Dolphin-memory-engine) standalone tool for Linux/Windows
