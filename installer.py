#!/usr/bin/python3
import requests
import subprocess
from shutil import which
import os
import json
import sys
from zipfile import ZipFile

platforms = ('linux', 'windows', 'nx')
subprocess.call("clear")
print("--- Chromedriver installation ---")
print("--- Preparing to install chromedriver for chrome ---")
print("--- Trying to open chrome ---\n")
print("--- Copy your chrome version under: 'Help' | 'About Google Chrome' ---")
print("--- After that close chrome ---\n\n")
if (which("google-chrome") is not None):
    subprocess.call("google-chrome")
else:
    print("ERROR: Google-Chrome is not installed or in Path!")
    exit()
print("\n\n--- Fetching newest version of version.json ---")
r = requests.get('https://raw.githubusercontent.com/cschwem2er/insta-story-getter/master/version.json')
versions = r.text
versions = json.loads(versions)
print("--- Newest version.json has been downloaded ---")
print("\n--- Please paste your chrome-version below: ---")
if not os.path.isdir("drivers"):
    os.makedirs("drivers")
print("--- Only the first number is important: XX.x.xxxx.xx")
while True:
    ver = input('version > ')
    try:
        getlink = versions[ver]
    except KeyError:
        print('\nERROR: This version is not supported')
        print('Make sure you only use the first number e.g. 86\n')
    else:
        break
print('\nWe detected that you are using "{}"'.format(sys.platform))
print("\n--- We got everything we need! ---")
print("\n--- Downloading the archive ---")
r = requests.get(versions[ver][platforms.index(sys.platform)])
open("drivers/driver.zip", "wb").write(r.content)
print("--- Download complete ---")
print("\n--- Unpacking the archive ---")
zf = ZipFile("drivers/driver.zip", "r")
zf.extractall("drivers")
zf.close()
print("--- Chromedriver was extracted ---")
print("--- Adding execution permissions ---")
try:
    subprocess.call(['chmod', "777", 'drivers/chromedriver'])
except:
    print("Error: Could not set permissions, you need to set it manually")
    exit()
else:
    print("--- Execution permission was added ---")
print("\n--- Cleaning up ---")
os.remove("drivers/driver.zip")
print("--- Chromedriver was installed sucessfully! ---")
print("--- You may open storygetter.py now! ---")
