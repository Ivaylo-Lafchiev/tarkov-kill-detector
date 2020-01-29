# tarkov-kill-detector
Uses Nvidia Highlights to detect whenever a player has been shot dead by watching the highlights directory for new files.

To run, simply start index.exe.
Make sure your Nvidia Highlights is set to save to the directory listed in the prompt.

Build from src: 

 `pip install pyinstaller`

 `pyinstaller -F --add-data "sound.wav;." index.py`
 
 
