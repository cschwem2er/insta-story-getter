<div align="center">
<h1>insta-story-getter</h1>
</div>
A python script, which downloads images and videos from instagram-stories


###### Requirements:
Python3

Python3-Selenium

Google Chrome

#### Installation
##### Installing the program
```
git clone https://github.com/therealhe1ko/insta-story-getter

cd insta-story-getter

pip3 install -r requirements.txt
```

##### Installing the chromedriver
1. Get the version of your Google Chrome installation
2. Goto [this Link](https://sites.google.com/a/chromium.org/chromedriver/) and download the chromedriver for your version
3. Create the directory **drivers** in this folder
4. Put the **chromedriver** file into it
5. Change the permission so that it can be executed:
``` chmod +x drivers/chromedriver ```

#### Usage:

Only supports linux!
```
./storygetter.py
```

## Common Errors:

##### The program starts, but nothing happens
That means, theres something wrong with the chrome installation or the chrome driver. You can try downloading a new driver from: [This Site](https://sites.google.com/a/chromium.org/chromedriver/downloads "Download Chrome driver"). (Could work if you've got an older / or newer chrome version), the standart-driver is on version 75. If you downloaded it, rename it to 'chromedriver.exe' and put it in the insta-story-getter/drivers folder.

##### Certian images were not downloaded
They were downloaded but they are in the 'vid' folder (if there are stickers or gifs in the image, it counts as a video)

##### Why do i have to put my username and password?
If you access a story on the instagram website you need to log in, in order to see the story
Don't worry. Your username or password do not get saved or sent anywhere, if you dont trust me just look into the code ;)

If you don't see your error here, open a issue.
