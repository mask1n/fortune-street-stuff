# Name Replacement Script for Itadaki/Fortune/Boom Street
Changes character names in-game without needing to modify the ISO or manually inject bytes into memory
![image](https://user-images.githubusercontent.com/83397594/153533310-8102e3f8-719d-47e5-8709-835b3fe8b6ed.png)


## Requirements
- An ISO/WBFS file of either **いただきストリートWii** (ST7JGD), **Fortune Street** (ST7E01), **Boom Street** (ST7P01) or **Custom Street World Tour** (ST7E02, ST7P02)
- Python 3.6 or later
- [Dolphin Emulator](https://dolphin-emu.org/)
- [py-dolphin-memory-engine](https://github.com/henriquegemignani/py-dolphin-memory-engine) (optional if using the Windows release binary) (use `pip install dolphin-memory-engine` to install)
- An x86_64-based version of Windows or Linux (currently DME lacks Mac support)

## How to use
1. Start emulation in Dolphin
2. Run `namereplace.py` (or [namereplace.exe](https://github.com/mask1n/fortune-street-stuff/releases/latest) for Windows users if you're using the release version)
3. After selecting your characters and advancing to the board selection screen, you'll be prompted to input each player's name.
4. Enjoy! 😃

## Limitations
- The game has an *18-character* limit for player names

## Links
- [Custom Street Discord server](https://discord.gg/DE9Hn7T)
- [Dolphin Memory Engine](https://github.com/aldelaro5/Dolphin-memory-engine) standalone tool for Linux/Windows

## Shoutouts
- _Deflaktor_ for assistance with finding pointers
