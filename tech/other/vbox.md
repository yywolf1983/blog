在vbox下安装增强功能到内置系统

VBoxManage  信息查看
pacman -S libvncserver
VBoxManage [-q|--nologo] startvm <uuid>|<name> [--type gui|sdl|headless]
VBoxHeadless -startvm "dcsvr08"  无图形启动
VBoxManage startvm Ubuntu --type headless  无图形启动
VBoxManage startvm dcsvr08 poweroff 关机
VBoxManage controlvm dcsvr08 poweroff 关机
VBoxManage list runningvms  查看

xp认不到网卡 到网卡驱动里找

yum install kernel-devel kernel-headers

vbox 数据空间
lsmod | grep vboxfs
pacman -S virtualbox-ose
linux
modprobe vboxvfs
mount -t   vboxsf  数据空间名称   /home/wrsg/share/
mount.vboxsf e /e  最新的用这种方法

sudo gedit /etc/fstab
在打开的界面文件中加入如下一行
tum /mnt/share vboxsf rw 0 0
d  /root/d   vboxsf  defaults,iocharset=utf8,fmask=333,dmask=002  0 0
widows
net use x: \\vboxsvr\sharename

gentoo
/usr/src/vboxguest-4.1.18
make && make install


net开启
VBoxManage modifyvm "VM name" --natpf1 "guestssh,tcp,,2222,,22"
VBoxManage modifyvm "WinXP" –natpf1 delete "http"
注意 natpf 就是 nat port forwarding的缩写
@echo off
:start
cls
echo.
echo.
"D:\Program Files\Oracle\VirtualBox\VBoxManage" list runningvms
echo      *********   虚拟机   *********
echo          ---i--- 启动 Ubuntu
echo          ---u--- 关闭 Ubuntu
echo          ---q--- exit
set /p st=
cls
if /I "%ST%"=="i" goto inst
if /I "%st%"=="u" goto unstall
if /I "%st%"=="q" goto exit

goto start

:inst
"D:\Program Files\Oracle\VirtualBox\VBoxManage" startvm Ubuntu --type headless
"D:\Program Files\Oracle\VirtualBox\VBoxManage" list runningvms
pause
goto start

:unstall
"D:\Program Files\Oracle\VirtualBox\VBoxManage" list runningvms
"D:\Program Files\Oracle\VirtualBox\VBoxManage" controlvm Ubuntu poweroff
"D:\Program Files\Oracle\VirtualBox\VBoxManage" list runningvms
pause
goto start

:exit
@echo on



#vbox 设置脚本
#!/bin/sh

vm="hd1"

if [[ "$1" == "run" ]]; then     #如果是linux的话打印linux字符串
    VBoxManage startvm ${vm} --type headless
elif [ "$1" == "off" ]; then
    VBoxManage controlvm ${vm} poweroff
elif [ "$1" == "list" ]; then
    VBoxManage list runningvms
else
    echo "What? run off list"
fi     #ifend
