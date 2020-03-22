import os
import time
import sys
import os.path
import requests
import uuid 
import winsound
import winreg
REG_PATH = "SOFTWARE\\TKD"

def set_reg(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def del_reg(name):
    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        return True
    except WindowsError:
        return None

def get_reg(name):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

if (len(sys.argv) == 2 and sys.argv[1] == "clear"):
    del_reg("KEY")
    print('Cleared license key...')
    os.system('pause')
    exit(0)

savedKey = get_reg("KEY")
if (savedKey != None):
    licenseKey = savedKey
else:
    licenseKey = input("Enter License Key: ")
    print("Key is: " + licenseKey)

macAddress = hex(uuid.getnode())
url = "https://3ugitj20bb.execute-api.eu-west-2.amazonaws.com/default/authLambda?key={0}&mac={1}".format(licenseKey, macAddress)
payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data = payload)

if (response.status_code != 200):
    print(response.text)
    print("Exiting...")
    os.system('pause')
    exit(1)
else:
    print('Valid license key')

set_reg("KEY", licenseKey)

path_to_watch = os.path.join(
    os.environ['TEMP'], "highlights", "Escape From Tarkov")

if not os.path.exists(path_to_watch):
    os.makedirs(path_to_watch)

print('Watching: ' + path_to_watch)
before = dict([(f, None) for f in os.listdir(path_to_watch)])

filePath = 'sound.wav'
if hasattr(sys, "_MEIPASS"):
    filePath = os.path.join(sys._MEIPASS, 'sound.wav')
print('Using sound file path: ' + os.path.abspath(filePath))
while 1:
    time.sleep(0.1)
    after = dict([(f, None) for f in os.listdir(path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:
        print("Added: ", ", ".join(added))
        winsound.PlaySound(filePath, winsound.SND_ASYNC)
    if removed:
        print("Removed: ", ", ".join(removed))
    before = after
