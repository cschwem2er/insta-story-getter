<div align="center">
<h1>insta-story-getter</h1>
</div>
A python script, which downloads images and videos from instagram-stories

Only supports Linux at the moment, Windows support is being worked on

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
Run ``` installer.py ```

#### Usage:


If you want to download the story of someone:
```
./storygetter.py
```
If you want to download a saved story [May be unstable]
```
./storygetter.py --savedstory
```
Use headless (invisible Chrome):
```
./storygetter.py --headless
```

#### Setting default credentials up

You just need to change the username and/or password in the default.ini file.


## Common Errors:

##### Certian images were not downloaded
They were downloaded but they are in the 'vid' folder (if there are stickers or gifs in the image, it counts as a video)

##### Why do i have to put my username and password?
If you access a story on the instagram website you need to log in, in order to see the story

Don't worry. Your username or password do not get saved or sent anywhere, if you dont trust me just look into the code ;)

If you don't see your error here, open a issue.
