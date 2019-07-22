<div align="center">
<h1>insta-story-getter</h1>
[![HitCount](http://hits.dwyl.io/therealhe1ko/insta-story-getter.svg)](http://hits.dwyl.io/therealhe1ko/insta-story-getter)
</div>
A python script, which downloads images and videos from instagram-stories


###### Requirements:
Python3
Python3-Selenium

Google Chrome has to be installed.


###### Usage:

###### Windows:


storygetter.py -a ACCOUNT -u YOURACCOUNT -p YOURPASSWORD

###### Linux:


cd insta-story-getter

cd drivers 

chmod +x chromedriver 

cd /insta-story-getter 

python3 storygetter.py -a ACCOUNT -u YOURACCOUNT -p YOURPASSWORD 

## Common Errors:

##### The program starts, but nothing happens
That means, theres something wrong with the chrome installation or the chrome driver. You can try downloading a new driver from: [This Site](https://sites.google.com/a/chromium.org/chromedriver/downloads "Download Chrome driver"). (Could work if you've got an older / or newer chrome version), the standart-driver is on version 75. If you downloaded it, rename it to 'chromedriver.exe' and put it in the insta-story-getter/drivers folder.

If you don't see your error here, open a issue.
