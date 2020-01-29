# tarkov-kill-detector
Uses Nvidia Highlights to detect whenever a player has been shot dead by watching the highlights directory for new files.


Build: 

`pip install pyinstaller`
`pyinstaller -F --add-data "sound.wav;." index.py`