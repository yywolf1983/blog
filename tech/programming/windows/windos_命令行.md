tasklist | findstr 3804

control userpasswords2

certutil -hashfile xxx MD5
certutil -hashfile xxx SHA1
certutil -hashfile xxx SHA256

自动锁屏
rundll32.exe user32.dll,LockWorkStation

gpedit.msc
secpol.msc

## 环境变量
$Env:Path += ";c:\temp"


net start "task scheduler"
showdown -h -t 0

AT 23:59 /every:M,T,W,Th,F,S,Su   每天执行

HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions
PingIntervalSecs"=dword:0000001e   putty 不超时

创建一个1G的文件
fsutil file createnew c:\1GB.txt 1073741824

启动nginx
taskkill.exe /F /IM "nginx*"
start D:\nginx-1.16.0\nginx.exe
timeout /T 2
tasklist.exe | findstr nginx
timeout /T 10
start http://127.0.0.1

统计行数
find /v /c ""
find /i /c "TIME_WAIT"


WSL安装 ssh
sudo apt-get install openssh-server openssh-client openssh-sftp-server  

文件路径
C:\Users\yy\AppData\Local\Packages\TheDebianProject.DebianGNULinux_76v4gfsz19hv4\LocalState\rootfs\home\yy\.ssh

sudo cat > /etc/init.wsl << EOF
#! /bin/sh
/etc/init.d/cron $1
/etc/init.d/ssh $1
EOF

win+r -> shell:startup
ununtu18.04.vbs
Set ws = CreateObject("Wscript.Shell")
ws.run "wsl -d Ubuntu-18.04 -u root /etc/init.wsl start", vbhide


rem 彻底休眠
rem C:\Windows\System32\rundll32.exe powrprof.dll,SetSuspendState Hibemate

rem 关闭屏幕
@echo off
powershell (Add-Type '[DllImport(\"user32.dll\")]^public static extern int SendMessage(int hWnd, int hMsg, int wParam, int lParam);' -Name a -Pas)::SendMessage(-1,0x0112,0xF170,2)
@echo on
