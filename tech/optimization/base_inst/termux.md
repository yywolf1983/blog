# termux

termux up+q 切换虚拟键盘
https://wiki.termux.com/wiki/Touch_Keyboard

termux-setup-storage 开启存储权限
termux up+q 呼出菜单

使用清华源
export EDITOR=vim
apt edit-sources
deb https://mirrors.tuna.tsinghua.edu.cn/termux stable main

sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list
sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list
sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list

pkg update


apt install apt-transport-https 支持ssh

pkg install proot
termux-chroot

pkg install openssh
sshd 端口是 8022
logcat -s 'syslog:*'  查看日志

## 安装 zsh

pkg install zsh git

git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
chsh -s `which zsh`
或
chsh -s zsh
sed -i '/^ZSH_THEME=/c\ZSH_THEME="xiong-chiamiov-plus"' ~/.zshrc

sed -i '/^ZSH_THEME=/c\ZSH_THEME="random"' ~/.zshrc

random 随机样式

mkdir -p ~/.termux && echo "extra-keys = [['ESC','/','-','HOME','UP','END','|','>'],['CTRL','TAB','ALT','LEFT','DOWN','RIGHT','~',':']]" > ~/.termux/termux.properties

$(basename $VIRTUAL_ENV)

termux-reload-settings

## 一种安装linux的办法

git clone https://github.com/YadominJinta/atilo

cd atil
chmod +x atilo
bash atilo

bash atilo list
bash atilo install ubuntu

## 直接安装 x11 卵用

pkg i -y x11-repo
pkg up -y 
pkg i -y xfce tigervnc
echo -e "#\!/bin/bash -e\nam start com.realvnc.viewer.android/com.realvnc.viewer.android.app.ConnectionChooserActivity\nexport DISPLAY=:1\nXvnc -geometry 720x1440 --SecurityTypes=None \$DISPLAY&\nsleep 1s\nopenbox-session&\nthunar&\nstartxfce4">~/startvnc ;
chmod +x ~/startvnc ;
mv -f ~/startvnc $PREFIX/bin/ ; 
startvnc

## 启用 sshkey

eval `ssh-agent -s -t 60s `
ssh-add

## 安装linux

https://github.com/EXALAB

https://github.com/EXALAB/AnLinux-Resources/tree/master/Rootfs

### 启动Linux基础包后需要安装

apt-get update
apt-get install openssh-server -y

echo "PermitRootLogin yes" > ~/.ssh/config

apt-get update
apt-get install xfce4 xfce4-terminal tightvncserver -y
apt-get install xfe -y
apt-get clean

mkdir ~/.vnc

#### vnc基础设置

    cat > ~/.vnc/xstartup << EOF
    #!/bin/bash
    xrdb $HOME/.Xresources
    startxfce4 &
    EOF

#### vncserver-start

    export USER=root
    export HOME=/root

    vncserver -geometry 1024x768 -depth 24 -name remote-desktop :1

#### vncserver-stop

    export USER=root
    export HOME=/root

    vncserver -kill :1
    rm -rf /tmp/.X1-lock
    rm -rf /tmp/.X11-unix/X1

#### 其他设置

    echo "export DISPLAY=":1"" >> /etc/profile
    source /etc/profile

### 清理

    chmod 777 -R ubuntu-fs
    rm -rf ubuntu-fs
    rm -rf ubuntu-binds
    rm -rf ubuntu.sh
    rm -rf start-ubuntu.sh
    rm -rf ssh-apt.sh
    rm -rf de-apt.sh
    rm -rf de-apt-xfce4.sh
    rm -rf de-apt-mate.sh
    rm -rf de-apt-lxqt.sh
    rm -rf de-apt-lxde.sh
    rm -rf UNI-ubuntu.sh

## 备份
tar -zcf termux-backup.tar.gz -C /data/data/com.termux/files ./home ./usr
tar -zxf termux-backup.tar.gz -C /data/data/com.termux/files --recursive-unlink --preserve-permissions

## 启动运行

~/.termux/boot
cat start-sshd
    #!/data/data/com.termux/files/usr/bin/sh
    termux-wake-lock
    sshd
