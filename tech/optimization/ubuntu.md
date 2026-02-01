sudo apt-get autoremove 
sudo apt-get purge gnome
sudo apt-get autoclean
sudo apt-get clean

apt list -i | grep gnome | awk -F "/" '{print $1}' |xargs sudo apt -y remove

安装gnome
sudo apt install task-mate-desktop
sudo apt-get install mate-desktop-environment-extras

kde
sudo apt -y install task-kde-desktop
https://github.com/vinceliuice/Qogir-kde
https://github.com/vinceliuice/Qogir-icon-theme.git
https://github.com/horst3180/arc-theme.git
https://github.com/PapirusDevelopmentTeam/papirus-icon-theme.git
latte-dock

lightdm
sudo vi /etc/lightdm/lightdm-gtk-greeter.conf
background=/home/yy/yy/geek.jpg

update-alternatives --config desktop-background


##  
sudo apt install i3-wm rofi sakura pcmanfm xcompmgr tint2 im-config fcitx cmatrix cmatrix-xfont ttf-wqy-zenhei flameshot tilda feh language-pack-zh-hans-base i3status i3lock curl bsdmainutils
sudo apt install fcitx5 fcitx5-pinyin
sudo apt install arc-theme papirus-icon-theme
sudo apt install w3m-img imagemagick neofetch jp2a


neofetch --w3m /home/td/aaa/yy/logo.png

/etc/profile.d/neo.sh

dpkg-reconfigure locales

xcompmgr 透明效果 
obs 视频编辑录制
pcmanfm  首选文件管理器
ranger   命令行资源管理器
oneko    一只捉鼠标的小猫
okular   pdf
rofi -show drun

样式
sudo apt install pekwm-themes
https://github.com/okraits/pekwm-theme-m0nst4.git

关闭显示器
xset dpms force off


隧道
ssh lh-01 -D 5600 -N
防止断开
-o StrictHostKeyChecking=no -o TCPKeepAlive=yes -o ServerAliveInterval=30
测试隧道
curl -x socks5://localhost:5600 https://api.d7home.com/getip


切换到用户命令行下，选择输入工具fcitx：
im-config -c

## 安装字体
sudo mkdir /usr/share/fonts/myttf
sudo cp * /usr/share/fonts/myttf
mkfontscale 
fc-cache -fv

## 填充壁纸
feh --bg-fill ~/Pictures/wallpapers/mybackground.jpg

## 关闭屏幕
xset dpms force off
force standby 强制待机
force suspend 强制休眠
force off 强制关闭屏幕
force on 打开节能模式

git config --global user.email "yywolf1983@gmail.com"
git config --global user.name "yywolf"
git cola

sudo dpkg-reconfigure console-setup
sudo dpkg-reconfigure lightdm

cat /etc/X11/default-display-manager

LANG=C

sudo apt install openssh-server
sudo systemctl status ssh
sudo ufw allow ssh


网卡静态设置
auto eth0
iface eth0 inet dhcp
iface eth0 inet static
address 10.16.3.99
netmask 255.255.255.0
network 10.16.3.0
broadcast 10.16.3.255
