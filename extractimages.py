#! /usr/bin/python3
import os

def extractfrvid():
    try:
        os.popen('ffmpeg -version').read()
    except:
        print('FFMPEG needs to be installed!')

    files = os.listdir('vid')

    for file in files:
        cmd = 'ffmpeg -ss 0.5 -i {} -vframes 1 -f image2 {}.jpg > /dev/null'.format('vid/{}'.format(file), 'img/%03d{}'.format(file[:-4]))
        os.popen(cmd).read()

if __name__ == "__main__":
    extractfrvid()