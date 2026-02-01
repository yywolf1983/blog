
lvs+keepalived


```
#!/bin/bash

# varsion 0.0.2
# 如果nginx挂掉 就干掉 keepalived

A=`ps -C nginx --no-header |wc -l`                ## 查看是否有 nginx进程 把值赋给变量A
if [ $A -eq 0 ]; ## 如果没有进程值得为 零
then
                /usr/local/nginx/sbin/nginx
                sleep 3
                if [ `ps -C nginx --no-header |wc -l` -eq 0 ];
                then
                      killall keepalived -9       ## 则结束 keepalived 进程
                fi
fi
```

Linux Virtual Server

VS/NAT  类似防火墙 必须过负载调度器
VS/TUN  IP tunneling ip隧道 将vip报文中目标地址获取配置到本地ip隧道上
VS/DR   MAC转发 相对VS/TUN没有ip隧道开销

调度算法
轮叫调度(Round-Robin Scheduling)
加权轮叫调度(Weighted Round-Robin Scheduling)
最小连接调度(Least-Connection Scheduling)
加权最小连接调度(Weighted Least-Connection Scheduling)
基于局部性的最少链接(Locality-Based Least Connections Scheduling)
带复制的基于局部性最少链接(Locality-Based Least Connections with Replication ）
目标地址散列调度(Destination Hashing Scheduling)
源地址散列调度(Source Hashing Scheduling)


yywolf1983 发表于 2013-07-29 13:26:28 删除 编辑

LVS是Linux Virtual Server的简写，意即Linux虚拟服务器，是一个虚拟的服务器集群系统。本项目在1998年5月由章文嵩博士成立，是中国国内最早出现的自由软件项目之一。目前有三种IP负载均衡技术（VS/NAT、VS/TUN和VS/DR）；
十种调度算法（rr|wrr|lc|wlc|lblc|lblcr|dh|sh|sed|nq）。

lvs的三种模式(按照出现的时间顺序来排列);
1; nat模式 (回复包要经过DIRECTOR, 这种模式最早出现, 最成熟, 但是调度器是瓶颈, 所以这个模式现在比较少用; tunneling模式和直接路由模式是后来为了解决某些问题而出现的);
2; tunneling模式;(回复包不需要经过DIRECTOR, 这种模式只要调度器和真实服务器的路由可达即可, 所以应用起来比较广, 回复包的时候直接通过各自的路由器出去, 所以比较方便配置, 只要realserver支持tunneling即可)
3; 直接路由模式;(回复包不需要经过DIRECTOR, 这种模式要求RS与DIRECTOR中间不能用路由器隔开, 回为这个模式只改变目标的mac地址)

lvs的十种算法;
1; 四种静态算法(假设服务器为a, b, c! 后面的数字代表服务器的权重);

1: rr: abc, abc, abc
2: wrr: a3b2c1, aababc aababc
3: dh: 目标hash;(根据目标地址选择服务器)
4: sh: 源hash;(根据源地址选择服务器)

2; 六种动态算法;
1: lc: ci最小, (ci指established状态的数量)处理能力比较强的计算机就一直回复;
2: wlc: ci/wi最小, (wi指weight的值)针对处理能力强的计算机weight调大一点;
3: lblc: 基于wlc, cache, 如果有一台已经跟服务器在连接, 那就一直使用这一台;如果负载太重(ci<wi), 则wlc选择一台, 就一直这台;
4: lblcr: 基于lblc, 只是cache集群;如果每台负载都过重, wlc选一台; 如果一台没有用, remove掉;
5: sed: (ci+1)/wi最小;一开始就把weight用上;
6: nq: 基于sed选一台, 如果没过载, 一直就这台, 有过载, 再使用sed再选一台;(ci<wi)


Keepalvied
Keepalived在这里主要用作RealServer的健康状态检查以及LoadBalance主机和BackUP主机之间failover的实现

arping  -s 源 目的地
LVS
   请求方式
        NAT 透明代理 （量小） 1000c/s
        TUN ip tunneling (ip隧道)  ip报文传送 操作系统限制 直接传回应用ip  25000c/s
        DR  非对称请求 （同一局域网） 25000c/s

   调度算法
        Round Robin  轮叫
        Weighted Round Robin  加权轮叫
        Least Connections  最少连接
        Weighted Least Connections 加权最少连接
        Locality-Based Least Connections 局部最少连接  用于cache集群
        (LBLCR)  带复制的基于局部性最少链接（Locality-Based Least Connections with Replication）
        Destination Hashing 目标地址散列
        Source Hashing  源地址散列


1; VIP: Virtual IP(虚拟ip, 主要是提供用户进行访问的);
2; RIP: REAL SERVER IP(真实服务器ip, 主要是提供服务的, 主要的服务器有http服务器);
3; CIP: CLIENT IP(客户端ip, 用来访问虚报ip);
4; DIP: DEVICE IP(设备的ip, 作为REAL SERVER的Gateway, 这个最好也是用虚拟ip, 这个ip是在nat模式下才使用, 配置nat模式最好使用两张网卡);
5; DIRECTOR: 调度器(是指安装ipvsadm的那台机器);
6; RS: REAL SERVER(真实的服务器, 里面有安装服务器, 比如web, mail等等;)


查看lvs 模块
lsmod | grep ip
modprobe ip_vs
modprobe -l | grep “ipvs”

/etc/sysctl.conf
net.ipv4.ip_forward = 1
sysctl -p

虚拟ip地址的广播地址是它本身，子网掩码255.255.255.255。
用本身做广播地址和把子网掩码设成4个255就不会造成ip地址冲突了，否则lvs将不能正常转发访问请求。
/sbin/ifconfig eth0:0 $VIP1 broadcast $VIP1 netmask 255.255.255.255 up
/sbin/ifconfig eth0:1 $VIP2 broadcast $VIP2 netmask 255.255.255.255 up

/sbin/route add -host $VIP1 dev eth0:0
/sbin/route add -host $VIP2 dev eth0:1

ipvsadm –C 清空ipvs转发表。
配置负载均衡(使用dr模式, 调度算法为wrr, weight统一配置成5);
ipvsadm –A –t 192.168.2.149:80 –s wrr
ipvsadm –a –t 192.168.2.149:80 –r 192.168.2.31:80 –g –w 5
ipvsadm –a –t 192.168.2.149:80 –r 192.168.2.32:80 –g –w 5

/sbin/ipvsadm

配置IPVS(/etc/sysconfig/ipvsadm)，添加Real Server：
-A -t 192.168.136.10:80 -s rr
-a -t 192.168.136.10:80 -r 192.168.136.11:80 -i
-a -t 192.168.136.10:80 -r 192.168.136.12:80 -i
-a -t 192.168.136.10:80 -r 192.168.136.101:80 -i
-a -t 192.168.136.10:80 -r 192.168.136.102:80 -i
-a -t 192.168.136.10:80 -r 192.168.136.103:80 -i

echo "1" >/proc/sys/net/ipv4/ip_forward启用ip转发功能。

查看
ipvsadm -Ln

watch ipvsadm -lnc -stats
ipvsadm -Ln -c

在负载机上执行
ifconfig lo:0 192.168.2.12 netmask 255.255.255.255 broadcast 192.168.2.12
route add default gw 192.168.2.12

echo "1" > /proc/sys/net/ipv4/conf/lo/arp_ignore
echo "2" > /proc/sys/net/ipv4/conf/lo/arp_announce
echo "1" > /proc/sys/net/ipv4/conf/all/arp_ignore
echo "2" > /proc/sys/net/ipv4/conf/all/arp_announce

命令选项解释：

有两种命令选项格式，长的和短的，具有相同的意思。在实际使用时，两种都可以。

-A –add-service 在内核的虚拟服务器表中添加一条新的虚拟服务器记录。也就是增加一台新的虚拟服务器。
-E –edit-service 编辑内核虚拟服务器表中的一条虚拟服务器记录。
-D –delete-service 删除内核虚拟服务器表中的一条虚拟服务器记录。
-C –clear 清除内核虚拟服务器表中的所有记录。
-R –restore 恢复虚拟服务器规则
-S –save 保存虚拟服务器规则，输出为-R 选项可读的格式
-a –add-server 在内核虚拟服务器表的一条记录里添加一条新的真实服务器
记录。也就是在一个虚拟服务器中增加一台新的真实服务器
-e –edit-server 编辑一条虚拟服务器记录中的某条真实服务器记录
-d –delete-server 删除一条虚拟服务器记录中的某条真实服务器记录
-L|-l –list 显示内核虚拟服务器表
-Z –zero 虚拟服务表计数器清零（清空当前的连接数量等）
–set tcp tcpfin udp 设置连接超时值
–start-daemon 启动同步守护进程。他后面可以是master 或backup，用来说
明LVS Router 是master 或是backup。在这个功能上也可以采用keepalived 的

VRRP 功能。
–stop-daemon 停止同步守护进程
-h –help 显示帮助信息

其他的选项:
-t –tcp-service service-address 说明虚拟服务器提供的是tcp 的服务  [vip:port] or [real-server-ip:port]
-u –udp-service service-address 说明虚拟服务器提供的是udp 的服务  [vip:port] or [real-server-ip:port]
-f –fwmark-service fwmark 说明是经过iptables 标记过的服务类型。
-s –scheduler scheduler 使用的调度算法，有这样几个选项

rr|wrr|lc|wlc|lblc|lblcr|dh|sh|sed|nq,

默认的调度算法是： wlc.

-p –persistent [timeout] 持久稳固的服务。这个选项的意思是来自同一个客户的多次请求，将被同一台真实的服务器处理。timeout 的默认值为300 秒。
-M –netmask netmask persistent granularity mask
-r –real-server server-address 真实的服务器[Real-Server:port]
-g –gatewaying 指定LVS 的工作模式为直接路由模式（也是LVS 默认的模式）
-i –ipip 指定LVS 的工作模式为隧道模式
-m –masquerading 指定LVS 的工作模式为NAT 模式
-w –weight weight 真实服务器的权值
–mcast-interface interface 指定组播的同步接口
-c –connection 显示LVS 目前的连接 如：ipvsadm -L -c
–timeout 显示tcp tcpfin udp 的timeout 值 如：ipvsadm -L –timeout
–daemon 显示同步守护进程状态
–stats 显示统计信息
–rate 显示速率信息
–sort 对虚拟服务器和真实服务器排序输出
–numeric -n 输出IP 地址和端口的数字形式


1. 下载相关软件包
#mkdir /usr/local/src/lvs
#cd /usr/local/src/lvs
#wget
http://www.linuxvirtualserver.org/software/kernel-2.6/ipvsadm-1.24.tar.gz
#wget
http://www.keepalived.org/software/keepalived-1.1.15.tar.gz

2. 安装LVS和Keepalived
#lsmod |grep ip_vs
#uname -r

#tar zxvf ipvsadm-1.24.tar.gz
#cd ipvsadm-1.24
#make && make install
#find / -name ipvsadm  # 查看ipvsadm的位置

#tar zxvf keepalived-1.1.15.tar.gz
#cd keepalived-1.1.15
#./configure  && make && make install
#find / -name keepalived  # 查看keepalived位置

#cp /usr/local/etc/rc.d/init.d/keepalived /etc/rc.d/init.d/
#cp /usr/local/etc/sysconfig/keepalived /etc/sysconfig/
#mkdir /etc/keepalived
#cp /usr/local/etc/keepalived/keepalived.conf /etc/keepalived/
#cp /usr/local/sbin/keepalived /usr/sbin/
#service keepalived start|stop     #做成系统启动服务方便管理.

yum install ipvsadm keepalived

vi /etc/keepalived/keepalived.conf

#Configuration File for keepalived

global_defs {
   notification_email {
         cnseek@gmail.com
   }
   notification_email_from sns-lvs@gmail.com  #指定发件人
   smtp_server 127.0.0.1
  # smtp_connect_timeout 30
   router_id LVS_DEVEL #邮件通知的标识, keepalived的日志文件在/var/log/syslog, 可以在这个文件查看状态即可;
  }

#可分配虚拟组 未理解
vrrp_sync_group VG1 {  #监控多个网段的实例
    VI_1  #实例名称
    VI_2
}
vrrp_sync_group VGM {
group {
    VI_HA
}
}

vrrp_script chk_redis {
    script "/etc/keepalived/scripts/redis_check.sh"   ###监控脚本
    interval 2                                        ###监控时间
}

# 20081013 written by :netseek
# VIP1
vrrp_instance VI_1 {
    state MASTER             #备份服务器上将MASTER改为BACKUP
    interface eth0
    virtual_router_id 51 #注意：这是唯一，主辅都一样 mcast_src_ip 58.22.XXX.207 #(广播的源IP，设置为本机外网IP，与VIP同一网卡)
    priority 100    # 备份服务上将100改为99   优先级 权重
    advert_int 1    # 检查间隔，默认为1秒
    authentication {  # 一下两行相同
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        61.164.122.8
        #(如果有多个VIP，继续换行填写.)
    }
    notify_master /path/xx.sh #指定当切换到master时，执行的脚本
    netify_backup /path/xx.sh #指定当切换到backup时，执行的脚本
    notify_fault "path/xx.sh VG_1" #故障时执行的脚本
    notify_stop /path/xx.sh
    smtp_alert #使用global_defs中提供的邮件地址和smtp服务器发送邮件通知
}

做nginx负载时不需lvs配置
virtual_server 61.164.122.8 80 {
    delay_loop 10                  #(每隔10秒查询realserver状态)
    lb_algo wrr                  #(lvs 算法)
    lb_kind DR                  #(Direct Route)
    persistence_timeout 60        #(会话保持时间 同一IP的连接60秒内被分配到同一台realserver)
    protocol TCP                #(用TCP协议检查realserver状态)

    #persistence_granularity <NETMASK> #lvs会话保持粒度
    #virtualhost <string> #检查的web服务器的虚拟主机（host：头）
    #sorry_server<IPADDR> <port> #备用机，所有realserver失效后启用

    real_server 61.164.122.9 80 {
        weight 3               #(权重)

        #inhibit_on_failure #在服务器健康检查失效时，将其设为0，而不是直接从ipvs中删除
        #notify_up <string> | <quoted-string> #在检测到server up后执行脚本
        #notify_down <string> | <quoted-string> #在检测到server down后执行脚本

        TCP_CHECK {
        connect_timeout 10       #(10秒无响应超时)
        nb_get_retry 3           #重连次数
        delay_before_retry 3      #重连间隔时间
        connect_port 80          #健康检查的端口的端口
        }
    }

    real_server 61.164.122.10 80 {
        weight 3
        TCP_CHECK {  #SSL_GET  #HTTP_GET
        connect_timeout 10
        nb_get_retry 3
        delay_before_retry 3
        connect_port 80
        }

        #HTTP_GET | SSL_GET{
        url{ #检查url，可以指定多个
             path /
             digest <string> #检查后的摘要信息
             status_code 200 #检查的返回状态码
            }
        connect_port <port>
        bindto <IPADD>
        connect_timeout 5
        nb_get_retry 3
        delay_before_retry 2
      }


        SMTP_CHECK{
        host{
        connect_ip <IP ADDRESS>
        connect_port <port> #默认检查25端口
        bindto <IP ADDRESS>
             }
        connect_timeout 5
        retry 3
        delay_before_retry 2
        helo_name <string> | <quoted-string> #smtp helo请求命令参数，可选
        }

        MISC_CHECK{
        misc_path <string> | <quoted-string> #外部脚本路径
        misc_timeout #脚本执行超时时间
        misc_dynamic #如设置该项，则退出状态码会用来动态调整服务器的权重，返回0 正常，不修改；返回1，

        检查失败，权重改为0；返回2-255，正常，权重设置为：返回状态码-2
        }

     }
}

/etc/init.d/keepalived restart


配置lvs或者lvs+keepalived需要注意的问题;
1; 使用client机器ping一下虚拟ip(ping 192.168.2.149), 使用arp –n查看192.168.2.149的mac地址, 必须与调度器的mac地址一样, 如果不一样, 那就是真实服务器的欺骗了交换机, 调度器就失去了作用;
2; tunnel模式的配置需要在真实服务器配置tunnel接口地址;
ifconfig tunl0 192.168.2.149 netmask 255.255.255.255 up(同时如果在同一个局域网里面测试, 也要预防arp欺骗)
3; nat模式下, 真实服务器基本不需要配置什么, 只需要把网关指向DIP即可;

ip add show
ip add
tcpdump -i eth0 port 80
tail -f /var/log/messages|grep -iE "Keepalived"



#!/bin/bash
#description : start realserver
VIP=192.168.1.98
/etc/rc.d/init.d/functions
case"$1" in
start)
echo " start LVS of REALServer"
/sbin/ifconfig lo:0 $VIP broadcast $VIP netmask 255.255.255.255 up
#抑制arp广播
echo "1" >/proc/sys/net/ipv4/conf/lo/arp_ignore
echo "2" >/proc/sys/net/ipv4/conf/lo/arp_announce
echo "1" >/proc/sys/net/ipv4/conf/all/arp_ignore
echo "2" >/proc/sys/net/ipv4/conf/all/arp_announce
;;
stop)
/sbin/ifconfig lo:0 down
echo "close LVS Directorserver"
echo "0" >/proc/sys/net/ipv4/conf/lo/arp_ignore
echo "0" >/proc/sys/net/ipv4/conf/lo/arp_announce
echo "0" >/proc/sys/net/ipv4/conf/all/arp_ignore
echo "0" >/proc/sys/net/ipv4/conf/all/arp_announce
;;
*)
echo "Usage: $0 {start|stop}"
exit 1
esac


nginx 监控脚本
# cat /etc/keepalived/check_nginx.sh
Count1=`netstat -antp |grep -v grep |grep nginx |wc -l`
if [ $Count1 -eq 0 ]; then
    /usr/local/nginx/sbin/nginx
    sleep 2
    Count2=`netstat -antp |grep -v grep |grep nginx |wc -l`
    if [ $Count2 -eq 0 ]; then
        service keepalived stop
    else
        exit 0
    fi
else
    exit 0
fi


1．LVS 基础知识汇总
LVS的算法介绍
http://www.linuxtone.org/viewthread.php?tid=69
学习LVS的三种转发模式
http://www.linuxtone.org/viewthread.php?tid=77
LVS中的IP负载均衡技术
http://www.linuxtone.org/viewthread.php?tid=68
更多的请到
http://www.linuxtone.org
负载均衡版查看
Keepalived 相关参考资料。
http://www.keepalived.org/documentation.html
