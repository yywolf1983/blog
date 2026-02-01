function installVPN(){
        echo "begin to install VPN services";
        #check wether vps suppot ppp and tun

        yum remove -y pptpd ppp
        iptables --flush POSTROUTING --table nat
        iptables --flush FORWARD
        rm -rf /etc/pptpd.conf
        rm -rf /etc/ppp

        arch=`uname -m`

        wget http://www.hi-vps.com/downloads/dkms-2.0.17.5-1.noarch.rpm
        wget http://wty.name/linux/sources/kernel_ppp_mppe-1.0.2-3dkms.noarch.rpm
        wget http://www.hi-vps.com/downloads/kernel_ppp_mppe-1.0.2-3dkms.noarch.rpm
        wget http://www.hi-vps.com/downloads/pptpd-1.3.4-2.el6.$arch.rpm
        wget http://www.hi-vps.com/downloads/ppp-2.4.5-17.0.rhel6.$arch.rpm


        yum -y install make libpcap iptables gcc-c++ logrotate tar cpio perl pam tcp_wrappers
        rpm -ivh dkms-2.0.17.5-1.noarch.rpm
        rpm -ivh kernel_ppp_mppe-1.0.2-3dkms.noarch.rpm
        rpm -qa kernel_ppp_mppe
        rpm -Uvh ppp-2.4.5-17.0.rhel6.$arch.rpm
        rpm -ivh pptpd-1.3.4-2.el6.$arch.rpm

        mknod /dev/ppp c 108 0
        echo 1 > /proc/sys/net/ipv4/ip_forward
        echo "mknod /dev/ppp c 108 0" >> /etc/rc.local
        echo "echo 1 > /proc/sys/net/ipv4/ip_forward" >> /etc/rc.local
        echo "localip 172.16.36.1" >> /etc/pptpd.conf
        echo "remoteip 172.16.36.2-254" >> /etc/pptpd.conf
        echo "ms-dns 8.8.8.8" >> /etc/ppp/options.pptpd
        echo "ms-dns 8.8.4.4" >> /etc/ppp/options.pptpd

        pass=`openssl rand 6 -base64`
        if [ "$1" != "" ]
        then pass=$1
        fi

        echo "vpn pptpd ${pass} *" >> /etc/ppp/chap-secrets

        iptables -t nat -A POSTROUTING -s 172.16.36.0/24 -j SNAT --to-source `ifconfig  | grep 'inet addr:'| grep -v '127.0.0.1' | cut -d: -f2 | awk 'NR==1 { print $1}'`
        iptables -A FORWARD -p tcp --syn -s 172.16.36.0/24 -j TCPMSS --set-mss 1356
        service iptables save

        chkconfig iptables on
        chkconfig pptpd on

        service iptables start
        service pptpd start

        echo "VPN service is installed, your VPN username is vpn, VPN password is ${pass}"

}

function repaireVPN(){
        echo "begin to repaire VPN";
        mknod /dev/ppp c 108 0
        service iptables restart
        service pptpd start
}

function addVPNuser(){
        echo "input user name:"
        read username
        echo "input password:"
        read userpassword
        echo "${username} pptpd ${userpassword} *" >> /etc/ppp/chap-secrets
        service iptables restart
        service pptpd start
}

echo "which do you want to?input the number."
echo "1. install VPN service"
echo "2. repaire VPN service"
echo "3. add VPN user"
read num

case "$num" in
[1] ) (installVPN);;
[2] ) (repaireVPN);;
[3] ) (addVPNuser);;
*) echo "nothing,exit";;
esac



客户端配置最后加入 

rcvbuf 65536
mssfix 1212
tun-mtu 1500


vpn server

1、安装ppp和iptables
yum install -y ppp iptables

2、下载pptpd的rpm包并安装
wget http://soft.vpser.net/vpn/pptpd/pptpd-1.3.4-1.rhel5.1.i386.rpm
rpm -ivh pptpd-1.3.4-1.rhel5.1.i386.rpm

3、编辑配置文件 vi /etc/pptpd.conf
需要有如下内容：
option /etc/ppp/options.pptpd
#logwtmp 注意
localip 10.1.1.1
remoteip 10.1.1.101-200

一般只需加入后两行即可，即分配服务器IP和客户端IP范围，可自己选择合适的IP

4、编辑配置文件 vi /etc/ppp/options.pptpd
需要如下内容：
name pptpd
refuse-pap
refuse-chap
refuse-mschap
require-mschap-v2
require-mppe-128
proxyarp
lock
nobsdcomp
novj
novjccomp
nologfd
ms-dns 202.106.0.20

ms-dns 211.99.25.1

一般只需设定后两行的dns服务器地址即可，即去掉#号，把IP改为服务器的dns IP供客户端使用

5、编辑配置文件 vi /etc/ppp/chap-secrets
# Secrets for authentication using CHAP
# client   server  secret   IP addresses
  user     pptpd   passwd      *
四项分别为客户端用户名，vpn服务器名（一般不改动），登陆密码，IP分配址（*为自动），中间用空格或Tab键隔开
可加入多个用户，分行录入

6、开启ip转发功能（否则只能连到vpn服务器，不能通过vpn服务器访问外部网络），修改配置文件

vi /etc/sysctl.conf 中的相应内容如下
net.ipv4.ip_forward = 1
使配置立即生效：
/sbin/sysctl -p

7、启用日志 vi /etc/syslog.conf

追加一行：

daemon.debug /var/log/pptpd.log

重起syslog：

kill -SIGHUP `cat /var/run/syslogd.pid`

8、配置iptables

iptables -F
iptables -X
iptables -Z
iptables -t nat -F
iptables -t nat -X
iptables -t nat -Z
iptables -P INPUT   ACCEPT
iptables -P OUTPUT  ACCEPT
iptables -P FORWARD ACCEPT
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m state --state RELATED -j ACCEPT
iptables -t nat -A POSTROUTING -s 10.1.1.0/24 -j SNAT --to 69.197.183.164
/etc/init.d/iptables save
/etc/init.d/iptables restart
注意：防火墙一定要开启，否则无法通过vpn服务器访问外网

8、设置iptables和pptpd开机自动启动：
chkconfig pptpd on
chkconfig iptables on

启动pptpd

service pptpd start


开启转发
iptables --table nat --append POSTROUTING --out-interface eth0 --jump MASQUERADE
vpn client

首先要先安装ppp / pptp / pptp-setup, 如果yum找不到这3个包, 那么源码安装吧, 下载地址 http://pptpclient.sourceforge.net/.

安装完这几个包之后, 用这个命令建立vpn的配置文件

pptpsetup --create testdb --server vpn_server --username username --password password

文件会出现在/etc/ppp/peers/下面, 文件名就是testdb, 也就是--create后面的参数.

然后
# cp /usr/share/doc/ppp-2.4.5/scripts/pon /usr/sbin/
# cp /usr/share/doc/ppp-2.4.5/scripts/poff /usr/sbin/
# chmod +x /usr/sbin/pon
# chmod +x /usr/sbin/poff

使用pon开始vpn, poff结束vpn

使用 pon testdb启动后, 查看/var/log/message是否启动成功了, 如果未成功, 看是什么错误,



cat /etc/ppp/options
require-mppe
require-mppe-128
mppe-stateful
CentOS6.3中默认是lock，我把这个删除了，加上上面的内容

route add -net  192.168.110.0 netmask 255.255.255.0  gw 192.168.112.100 device ppp0
route add -net 0.0.0.0 dev ppp0





yum -y install pptpd

查看/etc/pptpd.conf中指定的option文件，如果没有指定，那就默认是/etc/ppp/pptpd-options，下面是我的默认配置文件，因此要修改/etc/ppp/pptpd-options.pptpd

localip 10.0.1.1-200
remoteip 10.0.0.1-200

vi /etc/ppp/options.pptpd
ms-dns 202.96.128.86
ms-dns 202.96.128.166

/etc/ppp/chap-secrets
# client        server  secret                  IP addresses
test pptpd 123456 *

iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -j MASQUERADE

iptables -t nat -A POSTROUTING -s 10.0.1.0/24 -o eth0 -j SNAT --to 172.31.8.226
iptables-save

service pptpd restart