# download_vedio_mp3_youtube


from youtube download mp4 or mp3 file

parser.add_argument('--url')

parser.add_argument('--l', '-use -l to download the vedio of playlist')

parser.add_argument('-o', '--output', '-use -o add download output path')

parser.add_argument('--mp3','- use --mp3 to download mp3 file')





use --url download one vedio

exp: python3 mp3_convert.py --url 'https://www.youtube.com/watch?v=pO8O4q3Tl2M&list=PLMDSacPyadX3BmHhYzgoYYLAL0my0srKk&index=13' -o '/Users/zhang/Downloads/YouTube/test'


use --l download the playlist vedio

exp: python3 mp3_convert.py --l 'https://www.youtube.com/watch?v=pO8O4q3Tl2M&list=PLMDSacPyadX3BmHhYzgoYYLAL0my0srKk&index=13' -o '/Users/zhang/Downloads/YouTube/test' 

use --mp3 download the mp3 file 

exp: python3 mp3_convert.py --l 'https://www.youtube.com/watch?v=pO8O4q3Tl2M&list=PLMDSacPyadX3BmHhYzgoYYLAL0my0srKk&index=13' -o '/Users/zhang/Downloads/YouTube/test' --mp3 Ture
