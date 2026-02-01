netsh wlan set hostednetwork mode=allow ssid=lijingpeng key=12345678
netsh wlan start hostednetwork
cmd.exe


此命令有三个参数，
mode：是否启用虚拟WiFi网卡，改为disallow则为禁用。
ssid：无线网名称，最好用英文(以wuminPC为例)。
key：无线网密码，八个以上字符(以wuminWiFi为例)。

以上三个参数可以单独使用，例如只使用mode=disallow可以直接禁用虚拟Wifi网卡。


在连接网络的网卡中开启共享！


然后运行如下
netsh wlan start hostednetwork

查看链接
netsh wlan show hostednetwork


WLAN Autoconfig
rem net start mpssvc   (启动Windows Firewall服务)

set name=%date:~0,10%_%TIME:~0,2%-%TIME:~3,2%-%TIME:~6,2%

开启windows 防火墙
netsh firewall set portopening all 3299 aqzt.com-3299 enable
netsh firewall set portopening TCP 3389 aqzt.com-3298 enable  CUSTOM 1.1.1.11

netsh firewall delete portopening all 3299
