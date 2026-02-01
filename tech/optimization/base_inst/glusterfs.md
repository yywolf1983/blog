base

yum -y install flex
yum -y install bison

yum install xfsprogs wget

yum install fuse fuse-libs

http://www.gluster.org/

wget http://123.57.172.95/soft/glusterfs-3.7.20.tar.gz --http-user=yywolf1983 --http-passwd=rongfeng

编译安装
yum install -y libacl-devel userspace-rcu-devel libxml2-devel sqlite-devel readline-devel openssl-devel
yum install -y fuse fuse-devel libibverbs-devel
yum install -y aclocal autoconf aotuheader automake libtool
yum install -y python-devel 手动安装的python 不需要这个
yum install -y flex bison libaio-devel librdmacm-devel lvm2-devel glib2-devel  libcmocka-devel  
yum -y install libacl-devel

#add
vi /usr/include/libaio.h
typedef enum io_iocb_cmd {
        ……
        IO_CMD_PWRITEV = 8,
} io_iocb_cmd_t;

编译安装 python 要加上 CFLAGS=-fPIC 这个参数
centos 6 最高可安装 glusterfs-3.7.20

tar -xzf glusterfs-version.tar.gz
cd glusterfs-version
./configure —prefix=/data/glusterfs
make
make insatll

ldconfig
glusterfs —version

chkconfig glusterd on

mkdir /home/dir1
chmod 1777 /home/dir1


glusterd

创建集群 并添加机器
gluster peer probe test1
添加机器
gluster peer probe tb231
gluster peer probe tb95
gluster peer probe tb03

vi /etc/profile
export PATH=$PATH:$JAVA_HOME/bin:/data/glusterfs/sbin
source /etc/profile

gluster peer status
gluster peer detach  剔除机器


gluster volume create vol1 replica 2 transport tcp test1:/vol_data force
replica   多副本为成立？？？？
force  root下执行

权限设置
gluster volume set rongfeng auth.allow 10.*



添加块
gluster volume add-brick rongfeng tb03:/data/storage

分片存储
gluster volume create mamm-volume stripe 2 node1:/media node2:/media

gluster volume start  mamm-volume
gluster volume stop   mamm-volume
gluster volume delete mamm-volume

mount -t glusterfs -o log-level=INFO,log-file=./client.log,transport=tcp lememaster:/val01 /mnt/glusterfs
or
glusterfs --log-level=INFO --log-file=/data/client.log --volfile-server-transport=tcp --volfile-id=rongfeng --volfile-server=tb03 /data/glfs


gluster volume status
gluster volume info

扩展卷
gluster volume add-brick mamm-volume [strip|repli <count>] brick1...
收缩卷
gluster volume remove-brick mamm-volume [repl <count>] brick1...


数据迁移
gluster volume replace-brick mamm-volume old-brick new-brick [start|pause|abort|status|commit]
#迁移需要完成一系列的事务，假如我们准备将mamm卷中的brick3替换为brick5
#启动迁移过程
$gluster volume replace-brick mamm-volume node3:/exp3 node5:/exp5 start
#暂停迁移过程
$gluster volume replace-brick mamm-volume node3:/exp3 node5:/exp5 pause
#中止迁移过程
$gluster volume replace-brick mamm-volume node3:/exp3 node5:/exp5 abort
#查看迁移状态
$gluster volume replace-brick mamm-volume node3:/exp3 node5:/exp5 status
#迁移完成后提交完成
$gluster volume replace-brick mamm-volume node3:/exp3 node5:/exp5 commit


当对卷进行了扩展或收缩后，需要对卷的数据进行重新均衡。
$gluster volume rebalance mamm-volume start|stop|status

top
gluster volume top mamm-vol {open|read|write|opendir|readdir} brick node1:/exp1 list-cnt 1

触发副本自愈
$gluster volume heal mamm-volume #只修复有问题的文件
$gluster volume heal mamm-volume full #修复所有文件
$gluster volume heal mamm-volume info #查看自愈详情
$gluster volume heal mamm-volume info healed|heal-failed|split-brain

性能profile
gluster volume profile mamm-vol start
gluster volume profile info
gluster volume profile mamm-vol stop


选项配置
$gluster volume set mamm-volume key value
no1. :  gluster volume set vol1  auth.allow  *
      gluster volume set vol1 auth.allow all

导出路径
gluster volume set vol1 server.statedump-path /mnt/
导出计数器
gluster volume statedump vol1

gluster volume info dumpfile

#卷配额
gluster volume quota limit-usage

#查看打开文件
gluster volume top volume-name open

cd /etc/glusterfs

cp glusterfsd.vol.sample glusterfsd.vol

vim glusterfsd.vol
volume brick
type storage/posix # POSIX FS translator
option directory /home/dir1 # Export this directory
end-volume
volume server
type protocol/server
option transport-type tcp/server
option transport.socket.bind-address 124.127.117.28 # Default is to listen on all interfaces
subvolumes brick
option auth.addr.brick.allow *   # Allow access to "brick" volume
end-volume


glusterfsd -f /etc/glusterfs/glusterfsd.vol -l /var/log/glusterfs/glusterfsd.log
netstat -ln | grep 6996

client
客户端必须要有FUSE的内核支持。FUSE可到http://fuse.sourceforge.net下载安装
cd /etc/glusterfs
cp glusterfs.vol.sample glusterfs.vol

vim glusterfs.vol
volume client
type protocol/client
option transport-type tcp/client
option remote-host 124.127.117.28 # IP address of the remote brick
option remote-subvolume brick # name of the remote volume
end-volume

glusterfs -f /etc/glusterfs/glusterfs.vol -l /var/log/glusterfs/glusterfs.log /mnt/
mount -t glusterfs /etc/glusterfs/glusterfs.vol /mnt/glusterfs

mount.glusterfs 127.0.0.1:/vol1 /tools
glusterfs --log-level=INFO --log-file=./client.log --volfile-server-transport=tcp --volfile-id=/vol1 --volfile-server=127.0.0.1 /tools


分布类型

stripe  分块  同一brick不能分块
replica  冗余

1。分布存储 不冗余
$gluster volume create mamm-volume node1:/media node2:/media node3:/media

2。冗余存储 指定副本数量
gluster volume create mamm-volume repl 2  node1:/media node2:/media


distributed volumes: 分布式卷，文件在不同的brick上存储
replicated volumes: 复制卷，文件冗余存储在所有brick上（复制个数与brick个数相等）
striped volumes: 条带卷，同一个文件分块存储在不同的brick上
distributed replicated volumes: 分布式复制卷，volume中的brick组成不同的"区域"，每个"区域"内有多个brick（由replica指定），文件存储在不同的"区域"中，但是在"区域"中各brick上冗余存储。
distributed striped volumes: 分布式条带卷，与分布式复制卷类似，区别是同一文件分块存储在一个"区域"内的不同brick上。


3。分块存储 不冗余
分片卷将单个文件分成小块(块大小支持配置,默认为128K)，然后将小块存储在不同的brick上，
gluster volume create mamm-volume stripe 2 node1:/media node2:/media--

4。分布存储 冗余存储 由brick数量决定
brick必须为复本数K的N倍,brick列表将以K个为一组，形成N个复本卷
gluster volume create dr-volume repl 2 node1:/exp1 node2:/exp2 node3:/exp3 node4:/exp4

若创建的卷的节点提供的bricks个数为stripe个数N倍时，将创建此类型的卷。
gluster volume create ds-volume stripe 2 node1:/exp1 node1:/exp2 [&] node2:/exp3 node2:/exp4--


4。数据将进行切片，切片在复本卷内进行复制，在不同卷间进行分布。
$gluster volume create test-volume stripe 2 replica 2 server1:/exp1 server2:/exp2 server3:/exp3 server4:/exp4-

http://blog.csdn.net/zzulp/article/details/39527441
