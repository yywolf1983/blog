auto_dhcp

 echo off
 cls
 title 清除IP设置
 echo 正在清除IP地址，请稍候……
 netsh interface ip set address name="本地连接" source=dhcp
 echo 正在清除DNS设置，请稍候……
 netsh interface ip set dns name="本地连接" source=dhcp
 echo 删除IP设置，设置为自动。
 echo            ***************    恭喜你，命令成功完成！*************
 pause
Static IP 保留的是一种记忆

 echo off
 cls
 title 设置IP
 echo 正在设置IP地址，请稍候……
 rem 房子
 netsh interface ip set address "本地连接" static 192.168.1.115 255.255.255.0 192.168.1.1 1
 rem 天台
 netsh interface ip add address "本地连接" static 172.23.151.250 255.255.255.0 172.23.151.1 1
 rem 车管所
 netsh interface ip add address "本地连接" static 10.118.143.22 255.255.255.0 10.118.143.129 1
 rem 温州支队
 netsh interface ip add address "本地连接" static 172.16.202.18 255.255.255.0 172.16.202.1 1
 rem 10.119.128.18 温州dns

 rem netsh interface ip add address name="本地连接" source=dhcp
 echo 正在更改DNS设置，请稍候……
 netsh interface ip set dns "本地连接" static 8.8.8.8 primary
 netsh interface ip add dns name = "本地连接" addr=8.8.4.4
 netsh interface ip add dns "本地连接" static 202.101.172.35
 netsh interface ip add dns name = "本地连接" addr=202.101.172.47
 rem netsh interface ip add dns name="本地连接" source=dhcp
 rem netsh interface ip set dns "本地连接" static 202.101.172.35 primary
 rem netsh interface ip add dns name = "本地连接" addr=202.101.172.47
 echo                       ******恭喜你，修改完成！******
 pause

 rem 主出口
 rem route add 0.0.0.0 mask 0.0.0.0 192.168.0.1 metric 1 if 12
 rem 特定出口
 rem route add 172.23.151.0 mask 255.255.255.0 172.23.151.1 metric 1 if 14
 rem 删除
 rem route delete 0.0.0.0 mask 255.255.255.0 192.168.0.1
