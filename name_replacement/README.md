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
- Although Hiragana and Katakana are supported for Japanese names (as well as various symbols), there are only 139 Kanji that render correctly in-game. These include the following:

  一三上下中了二人介代伊会伝保修入内出力加勇勝北協原友取口可名和品営土地基堂報多大天太夫妙子安定小山島工常平幸広式後志恵悟愛成手持揮文新明晶曲月有望木本株業楽横次正武歩水河海渉渡片理由画登白目直相真知石社神竜管範純細絵緒置美義良英草裕貴賢軽辺近連達部野量金長間関陽雄雅集青香馬高黒

## Links
- [Custom Street Discord server](https://discord.gg/DE9Hn7T)
- [Dolphin Memory Engine](https://github.com/aldelaro5/Dolphin-memory-engine) standalone tool for Linux/Windows

## Shoutouts
- _Deflaktor_ for assistance with finding pointers
