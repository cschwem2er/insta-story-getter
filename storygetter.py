#!/usr/bin/python3

from selenium import webdriver
import time
import requests
import sys
import platform
from pathlib import Path
import logging
import os
import os.path
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import SessionNotCreatedException
from getpass import getpass
import subprocess
import shutil
import configparser
import optparse
LOGGER.setLevel(logging.WARNING)
from extractimages import extractfrvid

parser = optparse.OptionParser()
parser.add_option('--savedstory', action='store_true', dest='sast', help='Scrape saved stories')

options, args = parser.parse_args()

Config = configparser.ConfigParser()
Config.read("default.ini")

# Red colored text
def prRed(skk): print("\033[91m{}\033[00m" .format(skk))


# Green colored text
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))

if not os.path.isfile('drivers/chromedriver'):
	prRed('Can\'t find the chromedriver! Have you installed it? View the README.md for more information')
	exit()


subprocess.call('clear')

if options.sast:
    	prRed('Warning: This feature is in ALPHA-State!')

imgs = list()
vids = list()

relpath = 'drivers/chromedriver'

speed = 0.2

path = Path().absolute()
webdriverpath = os.path.join(path, relpath)

def getcred(yes):
	global name
	if yes:
		name = 'all'
		global url
		url = input('URL of Story: ')
	else:
		name = input('User: ')
		insturl = 'https://instagram.com/stories/' + name + '/'
	global username
	global password
	if Config.get('Default_Creds', 'username') == 'johndoe':
		print('\nYour instagram username of email')
		username = input('Username/Email: ')
	else:
		username = Config.get('Default_Creds', 'username')
	if Config.get('Default_Creds', 'password') == 'hunter':
		print('\nYour instagram password')
		password = getpass('Password: ')
	else:
		password = Config.get('Default_Creds', 'password')


def checkexist():
	global driver
	try:
		driver = webdriver.Chrome(executable_path= webdriverpath)
		driver.get('https://instagram.com/{}'.format(name))
	except SessionNotCreatedException as e:
		prRed('Your Version of Chromedriver is outdated. Please download the one matching your Chrome installation:')
		print(e)
		exit()
	try:
		assert name in driver.title
	except:
		return False
	else:
		return True

def checkstatus():
	try:
		priv = driver.find_element_by_class_name("rkEop")
	except:
		return True
	else:
		return False

def checkstory():
	print('[INFO] Checking if User has a story')
	driver.get('https://instagram.com/stories/{}'.format(name))
	cururl = driver.current_url
	if cururl[:34] != 'https://www.instagram.com/stories/':
		return False
	else:
		return True

def dl():
	print('\n[INFO] Story ended!')
	driver.close()
	print('[INFO] Downloading images...')
	if not os.path.exists('img'):
		os.makedirs('img')
	if not os.path.exists('vid'):
		os.makedirs('vid')
	i = 1
	for item in imgs:
		if item != None:
			r = requests.get(item, stream=True)
			fn = "img/{}{}.jpg".format(name, i)
			print('[INFO] Downloading: {}'.format(fn))
			with open(fn, 'wb') as f:
				shutil.copyfileobj(r.raw, f)
			del r
			i += 1
	print('\n[INFO] Downloading videos...')
	i = 1
	for item in vids:
		r = requests.get(item, stream=True)
		fn = "vid/{}{}.mp4".format(name, i)
		print('[INFO] Downloading: {}'.format(fn))
		with open(fn, 'wb') as f:
			shutil.copyfileobj(r.raw, f)
		del r
		i += 1
	prGreen('\n[INFO] All Images & Videos are downloaded!')

def captstory():
	time.sleep(1)
	print('[INFO] Getting src of story...')
	while True:
		if driver.current_url == 'https://www.instagram.com/':
			break
		try:
			obj = driver.find_element_by_class_name("OFkrO")
		except:
			obj = driver.find_element_by_class_name("y-yJ5")
			if obj.get_attribute("src") not in imgs and not None:
				print('[INFO] Got IMG-Src!')
				imgs.append(obj.get_attribute("src"))
			else:
				driver.find_element_by_class_name("ow3u_").click()
				time.sleep(speed)
		else:
			obj = driver.find_elements_by_tag_name("source")
			if obj[0].get_attribute("src") not in vids:
				print('[INFO] Got VID-Src!')
				vids.append(obj[0].get_attribute("src"))
			else:
				driver.find_element_by_class_name("ow3u_").click()
				time.sleep(speed)
	dl()

def waitforlogin():
	while True:
		try:
			driver.find_element_by_class_name("sqdOP.yWX7d._4pI4F._8A5w5").click()
		except:
			try:
				error = driver.find_element_by_id("slfErrorAlert")
			except:
				pass
			else:
				driver.close()
				prRed('[ERROR] You have entered a wrong password or username!')
				exit()
		else:
			prGreen('[INFO] Logged in!')
			return
		time.sleep(0.5)

def login():
	print('[INFO] Logging you in...')
	time.sleep(0.5)
	uname = driver.find_element_by_name('username')
	uname.send_keys(username)
	psw = driver.find_element_by_name('password')
	psw.send_keys(password)
	time.sleep(1)
	btn = driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF").click()

def waitforpage(url):
	while True:
		if driver.current_url == url:
			return
		else:
			time.sleep(0.5)

def checklogin():
	while True:
		if driver.current_url == 'https://www.instagram.com/':
			return
		try:
			driver.find_element_by_id("slfErrorAlert")
		except:
			pass
		else:
			driver.close()
			prRed('[ERROR] You have entered a wrong username or password!')
			exit()

def privstory():
	driver.get('https://instagram.com/accounts/login/')
	login()
	checklogin()
	waitforpage('https://www.instagram.com/')
	driver.get('https://instagram.com/stories/{}/'.format(name))
	waitforlogin()
	captstory()

def extractfun():
	print('Do you want to convert the videos into images?')
	choice = input('Y / N > ')
	if choice in ('y', 'Y'):
		extractfrvid()

def main():
	print('Insta-Story-Getter by therealhe1ko\n')
	print('Please enter the profile:')
	getcred(False)
	subprocess.call('clear')

	print('[INFO] Checking if user exists...')
	if not checkexist():
		prRed('[ERROR] This user does not exist!')
		exit()
	else:
		print('[INFO] User exists')

	print('[INFO] Checking if user is public or private')
	if not checkstatus():
		print('[INFO] User is private')
		privstory()
	else:
		print('[INFO] User is public')
		if not checkstory():
			prRed('[ERROR] This user has no story!')
			driver.close()
			exit()
		else:
			prGreen('[INFO] This user has a story')
			login()
			waitforlogin()
			captstory()
	extractfun()

def mainsast():
	print('Insta-Story-Getter by therealhe1ko\n')
	print('Please enter the profile:')
	getcred(True)
	checkexist()
	subprocess.call('clear')
	print('[INFO] Checking if user exists...')
	driver.get(url)
	time.sleep(1)
	login()
	waitforlogin()
	captstory()
	extractfun()

if not options.sast:
	main()
else:
	mainsast()

exit()
