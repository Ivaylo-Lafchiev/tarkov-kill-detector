import os
import time
import sys
import os.path
import requests


try {
    f = open("demofile.txt", "r")
}
# Get user input
licenseKey = input("Enter License Key: ")
print("Key is: " + licenseKey)
url = "https://3ugitj20bb.execute-api.eu-west-2.amazonaws.com/default/authLambda?key={0}".format(licenseKey)

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data = payload)

if (response.status_code != 200):
    print(response.text)
    print("Exiting...")
    exit(1)

def playSound(path):
    try:
        import winsound
        winsound.PlaySound(filePath, winsound.SND_ASYNC)
    except ImportError:
        print('no')
try:
    os.environ['TEMP']
        
    path_to_watch = os.path.join(
    os.environ['TEMP'], "highlights", "Escape From Tarkov")
except KeyError:
    path_to_watch = os.environ['HOME']

print('Watching %temp%/highlights: ' + path_to_watch)
before = dict([(f, None) for f in os.listdir(path_to_watch)])
if os.path.isfile('sound.wav'):
    filePath = 'sound.wav'
elif hasattr(sys, "_MEIPASS"):
    filePath = os.path.join(sys._MEIPASS, 'sound.wav')
print('Using sound file path: ' + filePath)
while 1:
    time.sleep(0.1)
    after = dict([(f, None) for f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:
        print("Added: ", ", ".join(added))
        playSound(filePath)
    if removed:
        print("Removed: ", ", ".join(removed))
    before = after
