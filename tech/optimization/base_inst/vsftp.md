centos7之vsftp安装和使用

1、为了调试顺利，关闭selinux，firewall，iptables

yum install gcc lrzsz vim wget

 
开始安装
 1、yum安装vsftp
1	yum -y install vsftpd
2、启动服务
1	systemctl start vsftpd.service
3、配置文件路径
1	/etc/vsftpd
 
功能一（匿名）：

 1 anonymous_enable=YES  #允许匿名访问
 2 anon_root= /data/ftp    #匿名访问的本地实际目录
 3 local_enable=YES            
 4 anon_upload_enable=YES # 允许匿名用户上传文件(须将全局的write_enable=YES,默认YES)
 5 anon_mkdir_write_enable=YES  #允许匿名用户创建目录
 6 write_enable=YES
 7 local_umask=022
 8 dirmessage_enable=YES
 9 xferlog_enable=YES
10 connect_from_port_20=YES
11 xferlog_std_format=YES
12 listen=NO
13 listen_ipv6=YES
14 
15 pam_service_name=vsftpd
16 userlist_enable=YES
17 tcp_wrappers=YES

 
功能二（虚拟用户）：
首先修改配置文件

配置文件内容（虚拟用户必须关闭虚拟用户anonymous_enable=NO）
anonymous_enable=NO
write_enable=YES
#允许本地用户访问
chroot_local_user=YES
chroot_list_enable=YES
#本地用户限制列表
chroot_list_file=/etc/vsftpd/chroot_list

#开启被动模式
pasv_promiscuous=yes

use_localtime=YES
local_enable=YES
allow_writeable_chroot=YES
xferlog_enable=YES

local_umask=022
#认证文件/etc/pam.d/vsftpd
pam_service_name=vsftpd
 
use_localtime=YES
listen_port=21
idle_session_timeout=120
data_connection_timeout=120

#启用虚拟用户
guest_enable=YES
#虚拟用户主用户(系统用户)
guest_username=ftpuser
 
#虚拟用户配置目录
user_config_dir=/etc/vsftpd/userconfig
#用户锁定在自己的目录
virtual_use_local_privs=NO
 
pasv_min_port=10060
pasv_max_port=10090
 
accept_timeout=5
connect_timeout=1
 
创建宿主用户
# 创建用户 ftpuser 指定 `/data/ftp` 目录
useradd -g root -M -d /data/ftp -s /sbin/nologin ftpuser
# 设置用户 ftpuser 的密码
passwd ftpuser
# 把 /data/ftp 的所有权给ftpuser.root
chown -R ftpuser.root /data/ftp
 
建立虚拟用户文件
touch /etc/vsftpd/vuser_passwd
# 编辑虚拟用户名单文件：（
# 第一行账号，第二行密码，注意：不能使用root做用户名，系统保留）
vi /etc/vsftpd/vuser_passwd 
# 编辑内容，下面是 vuser_passwd 内容
ftp1
sdwlftp1@12345678
ftp2
12345678
:wq!#保存退出
　
生成虚拟用户数据文件
db_load -T -t hash -f /etc/vsftpd/vuser_passwd /etc/vsftpd/vuser_passwd.db
chmod 600 /etc/vsftpd/vuser_passwd.db
  
创建用户配置
mkdir -p /etc/vsftpd/userconfig # 建立虚拟用户个人vsftp的配置文件
cd /etc/vsftpd/userconfig     # 进入目录
touch ftp1 ftp2
 
每个文件（ftp1和ftp2写入如下内容，local_root=/data/ftp/ftp1#这里写入这个用户的实际存储路劲）
local_root=/data/ftp/ftp1
write_enable=YES
#为YES时候，文件的其他人必须有读的权限才允许下载
anon_world_readable_only=NO
#不允许虚拟用户打开本地目录
virtual_use_local_privs=NO
anon_upload_enable=YES
anon_mkdir_write_enable=YES
anon_other_write_enable=YES
#用户不锁在主目录
allow_writeable_chroot=YES
#虚拟用户用 anon_umask
anon_umask=022 

目录 777-022 文件 666-022 文件没有执行权限
 
创建用户目录
#mkdir -p /data/ftp/ftp1
#mkdir -p /data/ftp/ftp2
　
在这里添加用户名
/etc/vsftpd/chroot_list
  
生成虚拟用户的PAM文件
cd /etc/pam.d/
#备份vsftpd文件
cp vsftpd vsftpd.bak
修改vsftpd文件内容（加入第二和第三行，下面的都全部注释，注意下面是64位操作系统，如果是32位的话lib64需要改成lib）

#%PAM-1.0
auth    required /lib64/security/pam_userdb.so db=/etc/vsftpd/vuser_passwd
account required /lib64/security/pam_userdb.so db=/etc/vsftpd/vuser_passwd

auth    sufficient /lib64/security/pam_userdb.so db=/etc/vsftpd/vuser_passwd
account sufficient /lib64/security/pam_userdb.so db=/etc/vsftpd/vuser_passwd


#session    optional     pam_keyinit.so    force revoke
#auth       required    pam_listfile.so item=user sense=deny file=/etc/vsftpd/ftpusers onerr=succeed
#auth       required    pam_shells.so
#auth       include     password-auth
#account    include     password-auth
#session    required     pam_loginuid.so
#session    include     password-auth

 
service vsftpd restart
 

tail -f /var/log/secure
tail -f /var/log/messages

修改端口号
1、在/etc/vsftpd/vsftpd.conf文件中增加listen_port=2121（这里修改为2121）
2、在vim /etc/services文件中修改如下内容
ftp             2121/tcp
ftp             2121/udp 

注意：上面修改的只是链接端口号，既然更改了连接端口号，别忘记访问的时候修改端口。
 
既然我们设置的是被动模式（服务器被动打开数据端口，只有在数据链接的时候才会使用，下面我们用ftp工具能成功连接，当打开某个文件夹的时候（请求数据的时候），才会使用该端口，但是我这里使用了iptables，之允许了2121通过我们设置的是10060到10090端口，具体如下）







lftp

set ftp:ssl-allow no
set ftp:use-feat false