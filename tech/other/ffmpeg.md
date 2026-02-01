---
---

# ffmpeg
    mplayer -vo caca dianziyilabao.mov
    mplayer -vo caca dianziyilabao.mov  > /dev/pts/4  hehe
    ffmpeg -vcodec copy -acodec copy -i orginalfile -ss 00:01:30 -t 0:0:20 newfile 从电影文件中剪辑出片段，选择任意的长度和开始时间

ffmpeg -f x11grab -s 800×600 -r 25 -i :0.0 -sameq out.mpg

合并视频
根据文件列表合并文件
file 'input1.mkv'
file 'input2.mkv'
file 'input3.mkv'

ffmpeg -f concat -safe 0 -i file.txt -c copy output.mp4


分割视频
ffmpeg -i naples.mp4 naples%d.jpg

视频合并
ffmpeg -r 24 -start_number 123 -i naples%d.jpg  -vf fps=24  video.mp4

音频提取
ffmpeg -i naples.mp4 -acodec copy -vn -y out.flv
ffmpeg -i naples.mp4 -f mp3 -vn naples.mp3

合并音频
ffmpeg -i video.mp4  -i naples.mp3 -vcodec mpeg4 -acodec copy video2.mp4

## ffmpeg直播
sudo dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf -y install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

sudo dnf -y install ffmpeg
sudo dnf -y install ffmpeg-devel

https://github.com/ossrs/srs.git
https://github.com/videojs/video.js

ffmpeg -re -rtsp_transport tcp -i "rtsp://192.168.0.222:554/live/av0" -preset ultrafast -vcodec libx264 -vprofile baseline -acodec aac -ar 44100 -strict -2 -ac 1 -f flv -r 10 -s 1280x720 -q 10 "rtmp://ip:1935/live/livestream"

ffmpeg -re -rtsp_transport tcp -i rtsp://192.168.0.222:554/live/av0 -vcodec libx264 -vprofile baseline  -b:v 400k -s 720x576 -r 25 -f flv rtmp://ip:1935/live/livestream


http://ip:8085/live/livestream.m3u8
rtmp://ip/live/livestream


ffmpeg -re -rtsp_transport tcp -i "rtsp://192.168.0.222:554/live/av0" -vcodec libx264 -vprofile baseline -f flv "rtmp://ip:1935/live/livestream"