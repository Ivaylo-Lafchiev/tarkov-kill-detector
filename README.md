# tarkov-kill-detector
Uses Nvidia Highlights to detect whenever a player has been shot dead by watching the highlights directory for new files.

To run, simply start `index.exe`

If you want to use your own sound, place a `sound.wav` file in the same directory as the executable.

Make sure your Nvidia Highlights is set to save to the directory listed in the prompt, and "Escape from Tarkov" directory exists inside.

Build from src: 

 `pip install pyinstaller`

 `pyinstaller -F --add-data "sound.wav;." index.py`
 
 
