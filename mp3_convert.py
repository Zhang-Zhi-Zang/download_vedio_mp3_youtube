# -*- coding:utf-8 -*-　＃

import argparse
from pytube import YouTube, Playlist
import os

parser = argparse.ArgumentParser()

parser.add_argument('--url')
parser.add_argument('--l', '-use -l to download the vedio of playlist')
parser.add_argument('-o', '--output', '-use -o add download output path')
parser.add_argument('--mp3','- use --mp3 to download mp3 file')

arg = args = parser.parse_args()

url = arg.url
playlist = arg.l
outputs = arg.output
mp3 = arg.mp3



def main():

    temp = outputs + '/temp'
    if not os.path.isdir(temp):
        os.makedirs(temp)
    print(temp)


    if playlist:
        print(playlist)
        getvedios(playlist, temp)
    elif url:
        print(url)
        YouTube(url).streams.first().download(temp)

    getmp3(outputs)
    os.removedirs(temp)


def getvedios(playlist,output):

    pl = Playlist(playlist)
    try:
        pl.download_all(output)
    except:
        print('error')


def getmp3(output):

    temp = outputs + '/temp'
    print(temp)

    if mp3:
        print('mp3')
        for filename in os.listdir(temp):
            filepath = os.path.join(temp,filename)
            print(filepath)
            ffmpeg(filepath,output)

            print(filename)



def ffmpeg(src_path, dst_path):

    video_file_name = os.path.basename(src_path)
    name_body = video_file_name.rsplit(".", 1)[0]
    audio_name = name_body + ".mp3"
    dst_path = dst_path +"/" + audio_name

    command = "ffmpeg -i '{}' -vn -ar 44100 -ac 2 -ab 196k -f mp3 '{}'".format(src_path, dst_path)
    os.system(command)
    os.remove(src_path)

if __name__ == '__main__':

    main()

