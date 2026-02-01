ip a/addr/address del/delete 192.168.0.130/24 dev eth1

ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

timedatectl list-timezones |grep -E "Shanghai|UTC"
timedatectl set-timezone Asia/Shanghai


vi /etc/sysconfig/network-scripts/ifcfg-enp2s0
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=static       #change
DEFROUTE=yes           #change
IPV4_FAILURE_FATAL=no
IPADDR=192.168.0.130   #new
NETMASK=255.255.255.0  #new
GATEWAY=192.168.0.1    #new
NAME=enp3s0
UUID=4f02b20a-67cc-430d-ad0b-5e57c8770485
DEVICE=enp3s0
ONBOOT=yes             #change

service network restart

sed -i "49s/#PermitRootLogin yes/PermitRootLogin no/g" /etc/ssh/sshd_config
sed -i "49s/#PermitRootLogin yes/PermitRootLogin no/g" /etc/ssh/sshd_config
systemctl restart sshd.service

del_id="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCWeZ0OttKdkCgo24W+L0/epl4rhOEihqbsShS2EAa7uL1gmKY5/sTRn+ii/hk6BFXdjHZ6omPCIt/tFeYnl7n+jlplXML/x75GOBlFOi1+6+h48F1BnWzY0Prq0vtOf/NDQ7uMS6Fdxjh4w/ABujOh8iYu+OVm3/1nG/UOImVFAUqNa0iVvVymPFfFqMZWScMDV/5lDM7AUz9MKCHWOTquoAazPtmbSAtfDuw7xPT4aW7RRO3/WIL7unzMuSrHwjPLMxx8Nxnk036AYFdVQacl3Ojru7moD5D1DdRJc9a6TpFojU/IwgdujIjuEJX7//VgeMJHCKl+ZeL007iAnIpd mysql"
sed -i 's#'"$del_id"'#DEL-VER#g;/DEL-VER/d' ~/.ssh/authorized_keys

#自动部署key
public_id="ssh-rsa ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCFNo+HSM6nDeDsU+Ub31uj/riMa79bTMddRuh8TR6gBUUzgMsVuy9CeJa0OFyqbFz2yg3oEh2dboLY79SEfClPVY8daOmT7A7YxHGSVg7NmZ0RnYVG1SdiSBaInNOetOWVGcrA5rn/voxVOmQoGE1ABa26Qb33T0MIuhJKPuUYMZYGqRVTMZeRXFbvqXS2yrjgOeTo9mJu62T0A0CGi2zoFG9/wq/0/X21ZvSgQoo7E2lg3CaCsG2a0ug9Ex5WL6+aNrE8fvfdOWexVsfUpHiCRH84pyf55uIxb9ZanWKqO6fNCqQR5IKwtnqzQjQFt7u8QFoewqdxqoitoSvDlT2N rsa-key-20211125"

mkdir -p ~/.ssh/
chmod 700 ~/.ssh/
sed -i 's#'"$public_id"'#DEL-VER#g;/DEL-VER/d' ~/.ssh/authorized_keys

echo "${public_id}" >> ~/.ssh/authorized_keys

cat ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys


#如下脚本需要改进 要根据key判断是否已经认证
for i in $(cat ~/.ssh/config  | grep  "host .*$" | awk '{print $2}')
do 
  echo $i
  /usr/bin/expect -c "
      spawn /usr/bin/ssh $i
      expect {
      \"(yes/no)?\" {send \"yes\r\"; exp_continue;}
      \"~]#\" {send \"exit\r\";}
      }
     expect eof"
done


hostname=bhg3

aa=`head -n 2 /dev/urandom  | base64 -w 0 | head -c32`;  echo ${aa} ; echo ${aa} | passwd root --stdin

强制密码登录
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no

iptables -F
iptables -X

iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
#或者
systemctl stop firewalld.service
systemctl disable firewalld.service




hostnamectl set-hostname bhg4

hostname=lianghua

ansible ${hostname} -m shell -a  "hostname"


ansible ${hostname} -m shell -a  "getenforce"

setenforce 0
getenforce
sed -i 's/^SELINUX=.*$/SELINUX=disabled/g' /etc/selinux/config
cat /etc/selinux/config


ansible ${hostname} -m shell -a  "date -R"
修改时区
ansible ${hostname} -m shell -a  "ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime"


cat > /etc/resolv.conf << EOF
nameserver 223.5.5.5
nameserver 223.6.6.6
EOF


wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
或

ansible ${hostname} -m shell -a "curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo"

## 安装基础工具
ansible ${hostname} -m shell -a "yum -y install ntp wget bind-utils fontconfig mkfontscale"



ansible ${hostname} -m copy -a "src=youhua.sh dest=~/youhua.sh"

## 优化

cat >> /etc/security/limits.conf << EOF
#
###custom
#
*           soft   nofile       20480
*           hard   nofile       65535
*           soft   nproc        20480
*           hard   nproc        65535
EOF


cat >>/etc/sysctl.conf <<"EOF"
vm.swappiness=0
#增加tcp支持的队列数
net.ipv4.tcp_max_syn_backlog = 65535
#减少断开连接时 ，资源回收
net.ipv4.tcp_max_tw_buckets = 8000
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_fin_timeout = 10
#改变本地的端口范围
net.ipv4.ip_local_port_range = 1024 65535
#允许更多的连接进入队列
net.ipv4.tcp_max_syn_backlog = 4096  
#对于只在本地使用的数据库服务器
net.ipv4.tcp_fin_timeout = 30
#端口监听队列
net.core.somaxconn=65535
#TCP分配发送缓存区的大小受参数net.ipv4.tcp_wmem配置影响
#其中在tcp_rmem"中的第一个值是为你们的TCP连接所需分配的最少字节数。该值默认是4K，最大的话8MB之多。
net.ipv4.tcp_rmem = 4096 87380 8388608
#接受数据的速率
net.core.netdev_max_backlog=65535
net.core.wmem_default=87380
net.core.wmem_max=16777216
net.core.rmem_default=87380
net.core.rmem_max=16777216
#最大打开文件数
fs.file-max = 655350
EOF


ansible ${hostname} -m shell -a "sh youhua.sh"

ansible ${hostname} -m shell -a "sysctl -p"

ansible ${hostname} -m shell -a "cat /proc/sys/fs/file-max"
ansible ${hostname} -m shell -a "cat /proc/sys/fs/nr_open"



base.sh

cat >> /var/spool/cron/root << "EOF"
00 10 * * * /usr/sbin/ntpdate -u cn.pool.ntp.org > /dev/null 2>&1; /sbin/hwclock -w
EOF

crontab -l
date

sed -i 's/\#Port\ 22$/Port\ 22369/g' /etc/ssh/sshd_config
cat /etc/ssh/sshd_config | grep 22369

sed -i 's/^.*UseDNS.*$/UseDNS no/g' /etc/ssh/sshd_config
cat /etc/ssh/sshd_config | grep UseDNS

sed -i 's/^.*ClientAliveInterval.*$/ClientAliveInterval 60/g' /etc/ssh/sshd_config
cat /etc/ssh/sshd_config  | grep ClientAliveInterval


sed -i 's/^.*GSSAPIAuthentication.*$/GSSAPIAuthentication yes/g' /etc/ssh/sshd_config
cat /etc/ssh/sshd_config  | grep GSSAPIAuthentication

sed -i 's/^.*GSSAPIAuthentication.*$/GSSAPIAuthentication yes/g' /etc/ssh/sshd_config
cat /etc/ssh/sshd_config  | grep GSSAPIAuthentication

service sshd restart
ss -anp | grep 22

ansible ${hostname} -m copy -a  "src=base.sh dest=~/base.sh"
ansible ${hostname} -m shell -a  "bash base.sh"


#处理磁盘
ansible ${hostname} -m shell -a "mkdir -p /data"

ansible ${hostname} -m shell -a "fdisk -l"
ansible ${hostname} -m shell -a "echo \"n
p
1


w
\" | fdisk /dev/vdb"
ansible ${hostname} -m shell -a "echo -e \"\n\n\n\" | mkfs.ext4 /dev/vdb1"
ansible ${hostname} -m shell -a "echo \"/dev/vdb1 /data            ext4    defaults        1 1\" >> /etc/fstab"
ansible ${hostname} -m shell -a "cat /etc/fstab"
ansible ${hostname} -m shell -a "mount -a"
ansible ${hostname} -m shell -a "ls /data"
ansible ${hostname} -m shell -a "df -h"




ansible ${hostname} -m shell -a mkdir -p /data/home/{logs,web,games,product,code}

ansible ${hostname} -m shell -a "crontab -l"

00 10 * * * /usr/sbin/ntpdate -u cn.pool.ntp.org > /dev/null 2>&1; /sbin/hwclock -w
01 00 * * * /usr/bin/sh /data/mysql_back.sh > /dev/null 2>&1
01 00 * * * /usr/bin/find /home/games/ -name info.log -size +200M | xargs -I files sh -c 'echo "" > $1' -- files > /dev/null 2>&1



# 日志清理脚本
/data/clear_log.sh

path="/home"
find ${path} -type f -name "*.log" -size +1024M  -or -name "*.txt" -size +1024M | xargs -I files sh -c 'cp $1 $1.`date +%Y%m%d`.log.back; > $1' -- files > /dev/null 2>&1
find ${path} -type f -name "*.log.back" -ctime +7 -exec rm -f {} \; > /dev/null 2>&1

path="/data/mysql-8.0.18"
find ${path} -type f -name "*.log" -size +1024M  -or -name "*.txt" -size +1024M | xargs -I files sh -c 'cp $1 $1.`date +%Y%m%d`.log.back; > $1' -- files > /dev/null 2>&1
find ${path} -type f -name "*.log.back" -ctime +7 -exec rm -f {} \; > /dev/null 2>&1

add_cron.sh
cat >> /var/spool/cron/root << EOF
10 6 * * * /usr/bin/sh /data/clear_log.sh > /dev/null 2>&1
EOF


#tomcat 停机脚本
path=$(basename `pwd`)
pid=$(ps -ef | grep $path | grep -v grep | grep -v stop_tomcat.sh |  awk '{print $2}' )
if [[ $pid -ne ""  ]]
then
  kill -9 $pid
  echo "进程已结束"
else
  echo "进程不存在"
fi
#————————————————————————-

ansible ${hostname} -m shell -a -c stop_tomcat.sh --dest=/data/tomcat_c



history 设置

sed -i '/HIST_USER_IP/d' /etc/profile
echo "HIST_USER_IP=\`who -u am i 2>/dev/null| awk '{print $NF}'|sed -e 's/[()]//g'\`" >> /etc/profile
sed -i '/HISTFILESIZE=5000/d' /etc/profile
echo 'HISTFILESIZE=5000' >> /etc/profile
sed -i '/HISTSIZE=5000/d' /etc/profile
echo 'HISTSIZE=5000' >> /etc/profile
sed -i '/HISTTIMEFORMAT/d' /etc/profile
echo 'HISTTIMEFORMAT="%F?%T?${HIST_USER_IP}?`whoami`?"?' >> /etc/profile
sed -i '/export?HISTTIMEFORMAT/d' /etc/profile
echo 'export HISTTIMEFORMAT' >> /etc/profile


#ssh 配置 更改重试次数
clush -b -a "sed -i 's/^.*MaxAuthTries.*$/MaxAuthTries 5/g' /etc/ssh/sshd_config"
clush -b -a "service sshd restart"

#mysql 备份设置
clush -b -g no_group -c mysql_back.sh --dest=/usr/local/script/
clush -b -g no_group  "sed -i '/mysql_back.sh/d' /var/spool/cron/root"
cmd="*/1 00 * * * /usr/bin/sh /usr/local/script/mysql_back.sh > /dev/null 2>&1 & "
clush -b -g no_group  "echo '$cmd' >> /var/spool/cron/root"
clush -b -g no_group "crontab -l"



#重启Tomcat

/usr/bin/ssh -p 5272 -i /usr/share/tomcat/id_rsa_tomcat root@10.10.15.179 -C "/data/apache-tomcat-7.0.84/start.sh stop_y"

/usr/bin/scp -P 5272 -i /usr/share/tomcat/id_rsa_tomcat $WORKSPACE/target/weibofenqi-manager.war root@10.10.15.179:/data/apache-tomcat-7.0.84/webapps

/usr/bin/ssh -p 5272 -i /usr/share/tomcat/id_rsa_tomcat root@10.10.15.179 -C "/data/apache-tomcat-7.0.84/start.sh start_y"
重启 tomcat

username="/data/apache-tomcat-7.0.84/"

operation=$1

function stop_y()
{
echo "停止TOMCAT..."

repid=`ps -ef | grep ${username} | grep -v grep |grep -v stop_y| awk '{print $2}'`
if [[ ${repid} == "" ]];then
        echo "Stop the TOMCAT successfully"
else
        kill -9 $repid && sleep 1
fi
}

function start_y()
{
echo "启动TOMCAT..."
${username}bin/startup.sh && sleep 5 && ps -ef|grep $username|grep java

echo "is ok"
sleep 5s
}

${operation}


clean install -U -Dmaven.test.skip=true
跳过单元测试
-Dmaven.test.skip=true


ansible dev -m shell -a "echo -en \"\
\033[35m Welcome to login `hostname`\033[0m
\033[46;30;7m\
  _ __   ___  _ __   ___  ___  
 | '_ \ / _ \| '_ \ / _ \/ __| 
 | | | | (_) | | | |  __/\__ \ 
 |_| |_|\___/|_| |_|\___||___/ 
                               
\033[0m \
\033[32mTHIS IP IS\" \$(ip add show eth0 | grep inet | awk '{print \$2}' | awk -F / '{print \$1}')  \"\033[0m
\033[33m pls safely keep your passwd or key, thx's \033[0m
\" > /etc/motd " 


echo -en "\
\033[35m Welcome to login `hostname`\033[0m
\033[36m\
  _ __   ___  _ __   ___  ___  
 | '_ \ / _ \| '_ \ / _ \/ __| 
 | | | | (_) | | | |  __/\__ \ 
 |_| |_|\___/|_| |_|\___||___/ 
                               
\033[0m \
\033[32mTHIS IP IS" $(ip add show eth0 | grep inet | awk '{print $2}' | awk -F / '{print $1}')  "\033[0m
\033[33m pls safely keep your passwd or key, thx's \033[0m
" > /etc/motd 


#Kill -15 后 如果不为零 则无限等待 反过来也可以判断进程是否存在
Var iii=0 #设置变量 如果循环次数大于次 则直接kill -9
admin_id=`ps -ef | grep ${servername}${version}.jar | grep -v grep | awk '{print $2}'`
kill -15 ${admin_id}
while [ ! -z ${admin_id} ];do
      admin_id=`ps -ef | grep ${servername}${version}.jar | grep -v grep | awk '{print $2}'`
      sleep 3
      echo ${admin_id}
      let iii=iii+1
      if [ $iii -ge 10 ]
      then
         echo "shutdown ERROR "
         exit
         #kill -9 ${admin_id}
         echo $iii
      fi
done
