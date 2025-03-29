# Undertale PC/Switch/Vita Save File Converter V2.1 (Javiergrandealo fork)
Inspired by JonyLuke's Undertale Save Converter (https://github.com/jonyluke/Undertale-save-converter).
This version is a complete re-write, and features full bi-directional conversion functionality.

[Project page on the GBATemp Forum](https://gbatemp.net/threads/undertale-save-game-converter-v2-with-full-bi-directional-pc-switch-conversion-ability.542897/)


## Requirements 
- Undertale
- A Modded Nintendo Switch or modded PSVita
- Python3.4 (https://www.python.org/downloads/)



## Installation and Usage
1. Download the latest release from https://github.com/Javiergrandealo/undertale-save-converter
2. Save it to a folder on your local computer.
3. Copy your game save files to the same folder.


### Converting from PC to Switch/Vita
1. Make sure you have copied your game's file0, file9, and undertale.ini files into the folder with the undertale_save_converter.py file.
   (These files are typically located in your system's %LocalAppData%\UNDERTALE\ folder on Windows)
2. Use your command prompt to browse to the folder, then execute `undertale_save_converter.py` and select the first menu option.



### Converting from Switch to PC
1. Make sure you have the undertale.sav file copied from your Nintendo Switch placed in the folder with the undertale_save_converter.py file.
   This file can be obtained from a modded switch by using tools such as Checkpoint or JKSM.
2. Use your command prompt to browse to the folder, then execute `undertale_save_converter.py` and select the second menu option.

### Converting from Vita to PC
1. Extract your save file using Apollo Save Tool using the "Export decripted save files" option
2. Use vita shell to move the save file to your pc
3. Use your command prompt to browse to the folder, then execute `undertale_save_converter.py` and select the second menu option.


### This version is cross platform so you can run this script on any machine (not only on windows)
