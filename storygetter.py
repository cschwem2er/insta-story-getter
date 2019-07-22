from selenium import webdriver
import time
import urllib.request
import sys
import optparse
import platform
from pathlib import Path
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)


parser = optparse.OptionParser()

parser.add_option('-a', '--account',
    action="store", dest="account",
    help="The instagram account, from which the story will be downloaded", default="nasa")
parser.add_option('-u', '--username',
    action="store", dest="username",
    help="Your instagram-username or email", default=None)
parser.add_option('-p', '--password',
    action="store", dest="password",
    help="Your instagram-password", default=None)

options, args = parser.parse_args()

if options.username:
	username = options.username
else:
	print('You have\'nt defined a username!')
	print('Press enter to exit')
	input()
	sys.exit()

if options.password:
	password = options.password
else:
	print('You have\'nt defined a password!')
	print('Press enter to exit')
	input()
	sys.exit()


name = options.account
insturl = 'https://instagram.com/stories/' + name + '/'

if platform.system() == "Windows":
	relpath = '\drivers\chromedriver.exe'
else:
	relpath = '\drivers\chromedriver'

path = Path().absolute()
webdriverpath = str(path) + relpath

try:
	driver = webdriver.Chrome(executable_path= webdriverpath)
	driver.get(insturl)
	try:
		assert 'Stories' in driver.title
	except:
		if name in driver.title:
			driver.close()
			print('This instagram account does not have a story!')
			print('Press enter to exit')
			input()
			sys.exit()
		else:
			driver.close()
			print('This instagram acoount does not exist!')
			print('Press enter to exit')
			input()
			sys.exit()

	try:
		user = driver.find_element_by_name("username")
		passwd = driver.find_element_by_name("password")
	except:
		time.sleep(1)
	user.send_keys(username)
	time.sleep(1)
	passwd.send_keys(password)
	try:
		button = driver.find_element_by_css_selector('.L3NKy')
		button.click()
	except:
		pass
	time.sleep(7)
	next = driver.find_element_by_css_selector('.h_zdq')
	next.click()
	time.sleep(1)
	links = ['None', None]
	vids = []
	while True:
		try:
			try:
				#try downloading the image
				#if it fails its a video
				try:
					elem = driver.find_element_by_class_name("y-yJ5")
					url = elem.get_attribute("src")
				except:
					raise Exception
				if url in (None, 'None'):
					raise Exception
				elif url in links:
					nextbuttom = driver.find_element_by_class_name("ow3u_").click()
				else:
					links.append(url)
					print("Got src (IMAGE)")
			except:
				try:
					vids.append(driver.find_element_by_tag_name('source').get_attribute("src"))
					print("Got src (VIDEO)")
				except:
					url = "None"

				if url in links:
					pass
					nextbuttom = driver.find_element_by_class_name("ow3u_").click()
				else:
					links.append(url)
		except:
			#if it cant find anything, the story is over, and the browser exits
			break


		time.sleep(.5)
	driver.close()
	print('Downloading images...')

	for i in range(0, len(links)):
		if links[i] != None and links[i] != 'None':
			nameimg = name + "\'s story " + str(i) + '.jpg'
			print('Downloading: ' + nameimg)
			currlink = links[i]
			urllib.request.urlretrieve(currlink, nameimg)
			print("Sucess!")
		else:
			pass

	print('Downloading videos')
	for i in range(0, len(vids)):
		nameimg = name + "\'s story " + str(i) + '.mp4'
		print('Downloading: ' + nameimg)
		currlink = vids[i]
		urllib.request.urlretrieve(currlink, nameimg)
		print("Sucess")

	print('Everything has been downloaded!')
	print('Press enter to exit')
	raise Exception
except:
	input()
	sys.exit()
