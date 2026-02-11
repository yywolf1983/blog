mac

DBeaver   数据库管理
GIF Brewery   动画制作
Typora Markdown   Markdown编辑器
腾讯柠檬          app 清理
LogGuru-Mac       iphone 日志
stretchly         小息工具
GPG Suite         gpg 工具
go2shell          访达快速开启shell
runcat            cpu 内存监控
Jumpcut           剪切板
https://kantu.qq.com/  看图软件

brew install mitmproxy 代理软件

Hyper     终端软件

Sabaki  一个围棋打谱软件

ish
apk add tzdata
cp - /usr/share/zoneinfo/Asia/Singapore /etc/localtime

pass 命令行密码管理
pass find 
pass show 
pass edit
pass add

solc
sudo npm install -g solc solc-cli --save-dev
brew install solidity
brew link solidity


Barrier  一个神奇的屏幕共享软件
 /Users/yy/Library/Application\ Support/barrier/SSL
 C:\Users\yy\AppData\Local\Barrier\SSL
openssl req -x509 -nodes -days 365 -subj /CN=Barrier -newkey rsa:4096 -keyout Barrier.pem -out Barrier.pem

Markmap  文本脑图神器

syncthing 一个很好的同步软件

touch bar pet.  

edex-ui     一个装逼的终端
shotcut     视频编辑
Another-Redis-Desktop-Manager  

easy new file
fliqlo    屏幕保护
XnViewMP

brew install freerdp 
安装 XQuartz
启动 XQuartz
freerdp

FreeMyDesktop    隐藏桌面文件

olive-macos  视频编辑  https://www.olivevideoeditor.org


brew install gcc@8 


u盘启动
https://unetbootin.github.io/

Tunnelblick       vpn git 上
Typeeto           蓝牙键盘 很赞
Mounty.dmg        NTFS 免费
Understand        源码神器 可惜太贵
ezip              解压软件

Aria2GUI

aria2c -D url     控制台下载
aria2c -c -s 10
aria2c --conf-path=/etc/aria2/aria2.conf -D 启动 rpc

aria2c --enable-rpc --rpc-allow-origin-all --rpc-listen-port=6880 -d /data/ceph/soft/ --rpc-listen-all -D

vi aria2.conf  
# 文件保存目录
dir=/data/soft
# 启用磁盘缓存, 0为禁用缓存, 需1.16以上版本, 默认:16M
disk-cache=32M
# 断点续传
continue=true

#开启rpc
enable-rpc=true
rpc-listen-port=6800

rpc-listen-all=true

# 是否启用 RPC 服务的 SSL/TLS 加密,
# 启用加密后 RPC 服务需要使用 https 或者 wss 协议连接
rpc-secure=true
# 在 RPC 服务中启用 SSL/TLS 加密时的证书文件(.pem/.crt)
rpc-certificate=/root/xxx.pem
# 在 RPC 服务中启用 SSL/TLS 加密时的私钥文件(.key)
rpc-private-key=/root/xxx.key

cat > /etc/systemd/system/aria2c.service << EOF
[Unit]
Description=Aria2c download manager
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/aria2c --conf-path=/etc/aria2/aria2.conf
TimeoutStopSec=20
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF


ariang web客户端
https://github.com/mayswind/AriaNg.git



iina       播放器

Foxmail      Email

Itsycal      可爱的日历软件

xnip        截图软件

fish http://fishshell.com/


重新安装系统
开机 顶一生后
command+R
进入系统工具
按住option 进入启动选择


调度中心 可以关闭仪表盘


screencapture   命令行截图
screen sharing.app   vnc



可以删除的软件列表
Cd /V-/M-

Notes.app 备忘录
Home.app  家庭
Dictionary.app 字典
Podcasts.app   播客
Stocks.app  股市
GarageBand.app 库乐队
VoiceMemos.app 语音备忘录
TV.app         电视


权限
关闭 Rootless。重启按住 Command+R，进入恢复模式，打开Terminal。
csrutil disable
重启即可。如果要恢复默认，那么
csrutil enable

/private/var/folders
查找
com.apple.dock.launchpad 
sqlite db
修改 apps 里面的数据


设置 安全 打开防火墙

允许第三方开发者
sudo spctl --master-disable


Mac iTerm2登陆CentOS提示warning: setlocale: LC_CTYPE: cannot change locale (UTF-8): No such file or directory
编辑~/.bashrc或者~/.zshrc文件，添加
export LC_ALL=en_US.UTF-8  
export LANG=en_US.UTF-8


电源参数
pmset -g custom
查看唤醒
pmset -g assertions

安装命令行开发工具
Xcode-select --install

from matplotlib.backends import _macosx
echo backend: TkAgg > ~/.matplotlib/matplotlibrc


defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES

/etc/profile
export  LANG="EN_US.UTF-8"

 warning: setlocale: LC_CTYPE: cannot change locale (UTF-8): No such file or directory
修改 /etc/ssh_config 文件，注释（#）其中的 SendEnv LANG LC_*，然后保存重启终端即可。


开机启动
launchctl load /System/Library/LaunchDaemons/com.apple.metadata.mds.plist

控制面板 项目
/Library/PreferencePanes

   截屏
   command+shift+3  全屏
   command+shift+4  区域
   command+shift+G  finder输入目录

  command＋control＋D  翻译

  F4 菜单
  F3 窗口列表
  command + F3 显示桌面

Command+M: 最小化窗口
Command+T: 在浏览器中打开新的选项卡
Command+W: 关闭窗口
Command+Q: 退出程序
Command+H: 隐藏窗口

   fish
      set -x VERSIONER_PYTHON_PREFER_32_BIT yes

   sudo  dtruss   mac 下得 starce

sudo chown root mtr
sudo chmod u+s mtr

env | grep SHELL

cat /etc/shells




$ sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

brew install coreutils

npm install -g browser-sync
browser-sync start --server --files "css/*.css"

brew install zsh
git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
chsh -s `which zsh`
sed -i '/^ZSH_THEME=/c\ZSH_THEME="xiong-chiamiov-plus"' ~/.zshrc

sed -i '/^ZSH_THEME=/c\ZSH_THEME="random"' ~/.zshrc



random 随机样式


## arm brew 

cd /opt # 切换到 /opt 目录
mkdir homebrew # 创建 homebrew 目录
curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew

sudo chown -R $(whoami) /opt/homebrew


使用清华大学镜像
cd "$(brew --repo)"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git

cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git

brew update

阿里源
# 替换brew.git
cd "$(brew --repo)"
git remote set-url origin https://mirrors.aliyun.com/homebrew/brew.git
# 替换homebrew-core.git
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.aliyun.com/homebrew/homebrew-core.git
# 刷新源
brew update




fink
macports
https://www.macports.org/install.php

清华源
sudo vi /opt/local/etc/macports/sources.conf
rsync://mirrors.tuna.tsinghua.edu.cn/macports/release/ports/ [default]

sudo vi /opt/local/etc/macports/macports.conf
rsync_server           mirrors.tuna.tsinghua.edu.cn
rsync_dir              macports/release/base/

sudo port -v sync	
sudo port -v selfupdate	

# 重新加载macports文件信息
sudo port -v sync				

# 更新ports tree和MacPorts版本，强烈推荐第一次运行的时候使用-v参数，显示详细的更新过程。
sudo port -v selfupdate

# 查看Mac Port中当前可用的软件包及其版本
port list

# 搜索索引中的软件
port search name

# 查看包详细信息
port info name

# 查看包详细信赖信息`
port deps name

# 查看安装时允许客户定制的参数
port variants name

# 列出文件详细信息
port contents llvm-11

# 安装新软件
sudo port install name

# 安装完毕之后，清除安装时产生的临时文件
sudo port clean --all name

# 卸载软件
sudo port uninstall name

# 查看有更新的软件以及版本
port outdated

# 升级可以更新的软件
sudo port upgrade outdated

# 彻底删除
sudo port -f uninstall installed
sudo port clean all
sudo rm -rf \
/opt/local \
/Applications/DarwinPorts \
/Applications/MacPorts \
/Library/LaunchDaemons/org.macports.* \
/Library/Receipts/DarwinPorts*.pkg \
/Library/Receipts/MacPorts*.pkg \
/Library/StartupItems/DarwinPortsStartup \
/Library/Tcl/darwinports1.0 \
/Library/Tcl/macports1.0 \
~/.macports





⌘——Command ()
⌃ ——Control
⌥——Option (alt)
⇧——Shift

⇪——Caps Lock

fn——功能键就是fn

^a 行首
^e 行尾


zsh


下载一个 .oh-my-zsh 配置（推荐有）git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh创建新配置NOTE: 如果你已经有一个 .zshrc 文件，那么备份一下吧cp ~/.zshrc ~/.zshrc.origcp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc把 zsh 设置成默认的 shell:chsh -s /bin/zsh

rm brew


/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install qt5
brew link --force qt5
brew linkapps qt5

export QT_QPA_PLATFORM='offscreen'

brew update     升级brew
brew outdated   查看那些软件需要升级
brew upgrade    升级系统

sudo rm -rf /usr/local/.git
rm -rf Library .git .gitignore bin/brew README.md share/man/man1/brew
rm -rf ~/Library/Caches/Homebrew

###  国内源

mkdir -p /opt/homebrew/Library/Taps/homebrew
cd /opt/homebrew/Library/Taps/homebrew
git clone https://mirrors.ustc.edu.cn/homebrew-core.git

# 查看brew镜像源
git -C "$(brew --repo)" remote -v
# 查看homebrew-core镜像源
git -C "$(brew --repo homebrew/core)" remote -v
# 查看homebrew-cask镜像源（需要安装后才能查看）
git -C "$(brew --repo homebrew/cask)" remote -v 

# 修改brew镜像源
git -C "$(brew --repo)" remote set-url origin https://mirrors.ustc.edu.cn/brew.git
# 修改homebrew-core镜像源
git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
# 修改homebrew-cask镜像源（需要安装后才能修改）
git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git
# 更新
brew update

### 恢复源
git -C "$(brew --repo)" remote set-url origin https://github.com/Homebrew/brew.git
git -C "$(brew --repo homebrew/core)" remote set-url origin https://github.com/Homebrew/homebrew-core.git
git -C "$(brew --repo homebrew/cask)" remote set-url origin https://github.com/Homebrew/homebrew-cask.git
brew update


brew update
brew install wget
brew install readline
brew install md5sha1sum  

iterm2  神器
sudo scutil --set HostName



alias -s py=vi       # 在命令行直接输入 python 文件，会用 vim 中打开，以下类似


alias mg="cd /Users/yy/Documents && ls -l /Users/yy/Documents | awk '{if(\$9!=\"\") print \"echo  ---- \"  \$9  \" ---- \&\& cd \" \$9 \" \&\& git status \&\& cd ..\"}'> abc && sh abc && rm -f abc"

ls -l | awk '{if($9!="") print "echo  \"\\033[38;05;196m" $9 "\\033[m\" && cd  "$9 " && git status && cd .."}'  >abc && sh abc && rm -f abc


设置休眠级别
pmset -g
sudo pmset -a hibernatemode 25
sudo pmset -b tcpkeepalive 0      此模式下合盖即断网

在访达上显示完整路径
defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES

运行“终端”程序，执行以下命令：

1、调整每一列显示图标数量，7 表示每一列显示7个，在我的电脑上，7个个人觉得比较不错
defaults write com.apple.dock springboard-rows -int 7

2、调整每一行显示图标数量，这里我用的是8
defaults write com.apple.dock springboard-columns -int 7

3、由于修改了每一页显示图标数量，可能需要重置Launchpad
defaults write com.apple.dock ResetLaunchPad -bool TRUE;killall Dock

以下是恢复默认大小的命令（在Terminal执行即可）：
defaults write com.apple.dock springboard-rows Default
defaults write com.apple.dock springboard-columns Default
killall Dock


驱动位置
ls /System/Library/Extensions/

查看usb驱动
system_profiler SPUSBDataType

卸载
rm -rf /System/Library/Extensions/XXXX.kext
 是的,删除老的驱动是这样的!
rm -rf /System/Library/Extensions.kextcache
  mac系统有缓存机制,这个是把系统缓存的驱动也干掉!
rm -rf /System/Library/Extensions.mkext
跟上面差不多的意思.
kextcache -k /System/Library/Extensions
这个还是清除缓存的驱动



第 1 步，删除框架：
sudo rm -rf /Library/Frameworks/Python.framework/Versions/x.x
第 2步，删除应用目录：

sudo rm -rf "/Applications/Python x.x"
第 3 步，删除指向 Python 的连接：

cd /usr/local/bin/
ls -l /usr/local/bin | grep '../Library/Frameworks/Python.framework/Versions/x.x' | awk '{print $9}' | tr -d @ | xargs rm


diskutil list
dd if={ISO_IMAGE_HERE_} of=/dev/disk1 bs=1m

ios 转 dmg
hdiutil convert -format UDRW -o ~/linux.dmg /tmp/linux.iso


pv -petr ubuntu-11.10-desktop-i386.iso | dd of=/dev/disk2 bs=1m
diskutil eject /dev/disk1


Mac: ld: library not found for -lgcc_s.10.4
cd /usr/local/lib sudo ln -s ../../lib/libSystem.B.dylib libgcc_s.10.4.dylib

launchctl
/Library/LaunchDaemons/
/Library/LaunchAgents/
~/Library/LaunchAgents/


vi /etc/passwd
ish 后台执行
~/.zshrc
cat /dev/location > /dev/null &

vi /etc/passwd
zsh

mkdir -p /mnt/ipad
mount -t ios . aaa
git 慢解决办法
mount -t ios-unsafe . aaa
git config --global pack.threads "1"


mac 安装linux

curl https://alx.sh | sh

删除分区
diskutil list
diskutil eraseVolume JHFS+ drive /drive/YourDiskIdentifier


mac m1 删除自带应用

csrutil disable
csrutil authenticated-root disable

csrutil status

mkdir ~/mnt

sudo mount -o nobrowse -t apfs /dev/disk3s1 $HOME/mnt

sudo bless --mount "$HOME/mnt/System/Library/CoreServices/" --setBoot --create-snapshot

sudo reboot

intel 芯片
sudo bless --folder /Users/apple/System/Library/CoreServices --bootefi --create-snapshot
