
## 基础软件

moc       音乐播放
smplayer  视频
Remmina   远程

sakura    控制台

httpie

rdesktop 
gimp 
inkscape
yed
libreoffice 
feh  看图

transmageddon  视频转码
recordmydes   桌面录像
gnuplot  (绘图工具库)

ibus ibus-pinyin
ibus-daemon -rxd

bind dns服务器

unetbootin

Xvfb  命令行虚拟图形环境

gunicorn
jmeter
ZooKeeper

freerdp


### 安装ifconfig
yum -y install net-tools


# 查询物理CPU个数
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l

# 查看每个物理CPU中core的核数(即个数)
cat /proc/cpuinfo| grep "cpu cores"| uniq

# 查看逻辑CPU的个数
cat /proc/cpuinfo| grep "processor"| wc -l

# 查看总线程数量
grep 'processor' /proc/cpuinfo | sort -u | wc -l

# 查看CPU信息（型号）
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c

./minerd --url=stratum+tcp://scrypt.eu-west.nicehash.com:3333 --userpass=3Bi5PswCQyHgGHTemZuErckgExLM8BGsWQ:x

./minerd --url=stratum+tcp://sha256.usa-west.nicehash.com:3334 --userpass=3Bi5PswCQyHgGHTemZuErckgExLM8BGsWQ:x

./minerd --url=stratum+tcp://scrypt.eu-west.nicehash.com:3333 --userpass=3Bi5PswCQyHgGHTemZuErckgExLM8BGsWQ.app8:x -t 60
查看显卡

lspci | grep -i vga


$env:path="C:\Python27;"+$env:path

windows
设置代理
netsh winhttp set proxy 127.0.0.1:1080
取消代理
netsh winhttp reset proxy
查看代理
netsh winhttp show proxy

export all_proxy="socks5://127.0.0.1:1080"

## 输入法
vi /etc/profile
export XIM=”ibus”
export XIM_PROGRAM=”ibus”
export XMODIFIERS=”@im=ibus”
export GTK_IM_MODULE=”ibus”
export QT_IM_MODULE=”ibus”

vnc 里输入异常
export XMODIFIERS=@im=SCIM
export GTK_IM_MODULE=SCIM


## 其他技巧
设置系统启动后进入文本界面：
systemctl set-default multi-user.target

设置系统启动后进入图形界面：
systemctl set-default graphical.target

重置xorg
yum install xorg-x11-server-Xorg
Xorg -configure :0
cp /root/xorg.conf.new /etc/X11/xorg.conf
startx

### 启用swap
dd if=/dev/zero of=/swapfile bs=1k count=2048000
mkswap /swapfile
swapon /swapfile
/swapfile  swap  swap    defaults 0 0


yum groupinstall xfce
vi ~/.xinitrc
xscreensaver &
conky -d &
xfce4-session


## 备忘录

archlinux 安装笔记
yywolf1983 发表于 2013-07-29




https://aur.archlinux.org/cgit/aur.git/snapshot/debtap.tar.gz

tar zvxf ~/Downloads/debtap.tar.gz -C ~/arch
cd ~/arch/debtap
makepkg -s
sudo pacman -U debtap-3.1.4-2-any.pkg.tar.xz

OR

sudo pacman -S yaourt
sudo yaourt -S debtap

更新debtap数据库
sudo debtap -u

使用debtap转换deb包
debtap xxx.deb

安装
sudo pacman -U xxx.pkg



sudo pacman -Sy fcitx5-chinese-addons fcitx5-configtool

修改～/.xprofile，添加以下几行：

export QT_IM_MODULE=fcitx
export GTK_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"