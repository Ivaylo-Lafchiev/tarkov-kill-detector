import os
import time
import sys
import winsound
import os.path
path_to_watch = os.path.join(
    os.environ['TEMP'], "highlights", "Escape From Tarkov")
print('Watching %temp%/highlights: ' + path_to_watch)
before = dict([(f, None) for f in os.listdir(path_to_watch)])
if os.path.isfile('sound.wav'):
  filePath = 'sound.wav'
elif hasattr(sys, "_MEIPASS"):
  filePath = os.path.join(sys._MEIPASS, 'sound.wav')
print('Using sound file path: ' + filePath)
while 1:
    time.sleep(0.1)
    after = dict([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:
        print("Added: ", ", ".join(added))
        winsound.PlaySound(filePath, winsound.SND_ASYNC)
    if removed:
        print("Removed: ", ", ".join (removed))
    before = after
