REmote DIctionary Server

查看现有的redis密码：config get requirepass
设置redis密码config set requirepass  xxxxxxx

wget http://download.redis.io/releases/redis-5.0.7.tar.gz

make MALLOC=libc
yum install tcl
make test

make
make PREFIX=/data/redis install

cp redis.conf /data/redis

#哨兵模式
redis-sentinel

系统优化
echo "vm.overcommit_memory=1" >> /etc/sysctl.conf
echo 1 > /proc/sys/vm/overcommit_memory

echo 1024 > /proc/sys/net/core/somaxconn

echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never >  /sys/kernel/mm/transparent_hugepage/defrag

echo "fs.file-max = 100000" >> /etc/sysctl.conf
sysctl -p

cat >> /usr/lib/systemd/system/redis.service << "EOF" 
[Unit]
Description=redis-server
After=network.target

[Service]
Type=forking
ExecStart=/data/redis/bin/redis-server   /data/redis/redis.conf
PrivateTmp=true

[Install]
WantedBy=multi-user.target

EOF


systemctl enable redis.service
systemctl start redis.service
systemctl status redis.service


集群
cp ./src/redis-trib.rb /data/redis-cluster/redis-1/bin/

echo 1000 >/proc/sys/net/core/somaxconn   #Specifies the maximum listen backlog.
echo 1 > /proc/sys/vm/overcommit_memory
overcommit_memory文件指定了内核针对内存分配的策略，其值可以是0、1、2。                               
0， 表示内核将检查是否有足够的可用内存供应用进程使用；如果有足够的可用内存，内存申请允许；否则，内存申请失败，并把错误返回给应用进程。
1， 表示内核允许分配所有的物理内存，而不管当前的内存状态如何。
2， 表示内核允许分配超过所有物理内存和交换空间总和的内存
echo never > /sys/kernel/mm/transparent_hugepage/enabled

redis.conf
dir /data/redis
logfile /data/redis/redis.log
daemonize yes
requirepass redis99876 #设置密码
bind xxxxxxxxx
save 10 30

#开启 aof
appendonly yes
appendfilename "appendonly.aof"
#每秒同步缓存
appendfsync everysec



rc.local
/data/redis/bin/redis-server /data/redis/redis.conf

#Master slave (只需要在从机下设置主机ip port和认证)
slaveof 192.168.1.100 6379  
masterauth redis123

#打开redis集群  
cluster-enabled yes  
#节点互连超时的阀值  
cluster-node-timeout 15000
#cluster配置文件(启动自动生成)  
cluster-config-file nodes-6379.conf  
#部署在同一机器的redis实例，把auto-aof-rewrite搓开，防止瞬间fork所有redis进程做rewrite,占用大量内存
auto-aof-rewrite-percentage 80-100  


bin/redis-server redis.conf &

redis-cli

auth youpasswd

RANDOMKEY  获取随机key

ping 查看存活

get

select 切换库
redis.conf

# 后台进程
daemonize yes
pidfile /www/redis-cluster/redis-1/redis.pid
bind 192.168.1.150
port 12001
timeout 0
tcp-keepalive 0
requirepass test123456
loglevel notice
logfile stdout
databases 16
save 900 1
save 300 10
save 60 10000
stop-writes-on-bgsave-error yes
rdbcompression yes
rdbchecksum yes
dbfilename dump.rdb
dir ./
slave-serve-stale-data yes
#slave 只读
slave-read-only yes
repl-disable-tcp-nodelay no
slave-priority 100
#打开aof持久化
appendonly no
#每秒一次aof写  
appendfsync everysec
#关闭在aof rewrite的时候对新的写操作进行fsync  
no-appendfsync-on-rewrite no
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
lua-time-limit 5000
slowlog-log-slower-than 10000
slowlog-max-len 128
hash-max-ziplist-entries 512
hash-max-ziplist-value 64
list-max-ziplist-entries 512
list-max-ziplist-value 64
set-max-intset-entries 512
zset-max-ziplist-entries 128
zset-max-ziplist-value 64
activerehashing yes
client-output-buffer-limit normal 0 0 0
client-output-buffer-limit slave 256mb 64mb 60
client-output-buffer-limit pubsub 32mb 8mb 60
hz 10

#打开redis集群  
cluster-enabled yes  
#节点互连超时的阀值  
cluster-node-timeout 15000
#cluster配置文件(启动自动生成)  
cluster-config-file nodes-6379.conf  
#部署在同一机器的redis实例，把auto-aof-rewrite搓开，防止瞬间fork所有redis进程做rewrite,占用大量内存
auto-aof-rewrite-percentage 80-100  

#内存耗尽时采用的淘汰策略:  
# volatile-lru -> remove the key with an expire set using an LRU algorithm  
# allkeys-lru -> remove any key accordingly to the LRU algorithm  
# volatile-random -> remove a random key with an expire set  
# allkeys-random -> remove a random key, any key  
# volatile-ttl -> remove the key with the nearest expire time (minor TTL)  
# noeviction -> don't expire at all, just return an error on write operations  
maxmemory-policy allkeys-lru  
redis 集群

需要ruby
 yum -y install ruby

gem source -r https://rubygems.org/
gem source -a http://mirrors.aliyun.com/rubygems/

gem install redis

先启动所有节点

#redis-trib.rb的create子命令构建  
#--replicas 则指定了为Redis Cluster中的每个Master节点配备几个Slave节点  
#节点角色由顺序决定,先master之后是slave(为方便辨认,slave的端口比master大1000)  
redis-trib.rb create --replicas 1 10.10.34.14:6380 10.10.34.14:6381 10.10.34.14:6382 10.10.34.14:7380 10.10.34.14:7381 10.10.34.14:7382  



#redis-trib.rb的check子命令构建  
#ip:port可以是集群的任意节点  
redis-trib.rb check 1 10.10.34.14:6380  

添加节点
第一个是新节点ip:port, 第二个是任意一个已存在节点ip:port
redis-trib.rb add-node 10.10.34.14:6386 10.10.34.14:6381  

node:新节点没有包含任何数据， 因为它没有包含任何slot。新加入的加点是一个主节点， 当集群需要将某个从节点升级为新的主节点时， 这个新节点不会被选中
为新节点分配slot
redis-trib.rb reshard 10.10.34.14:6386  
#根据提示选择要迁移的slot数量(ps:这里选择500)  
How many slots do you want to move (from 1 to 16384)? 500  
#选择要接受这些slot的node-id  
What is the receiving node ID? f51e26b5d5ff74f85341f06f28f125b7254e61bf  
#选择slot来源:  
#all表示从所有的master重新分配，  
#或者数据要提取slot的master节点id,最后用done结束  
Please enter all the source node IDs.  
  Type 'all' to use all the nodes as source nodes for the hash slots.  
  Type 'done' once you entered all the source nodes IDs.  
Source node #1:all  
#打印被移动的slot后，输入yes开始移动slot以及对应的数据.  
#Do you want to proceed with the proposed reshard plan (yes/no)? yes  
#结束  

添加新的slave节点
前三步操作同添加master一样
第四步:redis-cli连接上新节点shell,输入命令:cluster replicate 对应master的node-id

删除一个slave节点
#redis-trib del-node ip:port '<node-id>'  
redis-trib.rb del-node 10.10.34.14:7386 'c7ee2fca17cb79fe3c9822ced1d4f6c5e169e378'  

删除master节点之前首先要使用reshard移除master的全部slot,然后再删除当前节点(目前只能把被删除
master的slot迁移到一个节点上)

#把10.10.34.14:6386当前master迁移到10.10.34.14:6380上  
redis-trib.rb reshard 10.10.34.14:6380  
#根据提示选择要迁移的slot数量(ps:这里选择500)  
How many slots do you want to move (from 1 to 16384)? 500(被删除master的所有slot数量)  
#选择要接受这些slot的node-id(10.10.34.14:6380)  
What is the receiving node ID? c4a31c852f81686f6ed8bcd6d1b13accdc947fd2 (ps:10.10.34.14:6380的node-id)  
Please enter all the source node IDs.  
  Type 'all' to use all the nodes as source nodes for the hash slots.  
  Type 'done' once you entered all the source nodes IDs.  
Source node #1:f51e26b5d5ff74f85341f06f28f125b7254e61bf(被删除master的node-id)  
Source node #2:done  
#打印被移动的slot后，输入yes开始移动slot以及对应的数据.  
#Do you want to proceed with the proposed reshard plan (yes/no)? yes  

删除空master节点
redis-trib.rb del-node 10.10.34.14:6386 'f51e26b5d5ff74f85341f06f28f125b7254e61bf'  
集群命令

集群
CLUSTER INFO 打印集群的信息
CLUSTER NODES 列出集群当前已知的所有节点（node），以及这些节点的相关信息。
节点
CLUSTER MEET <ip> <port> 将 ip 和 port 所指定的节点添加到集群当中，让它成为集群的一份子。
CLUSTER FORGET <node_id> 从集群中移除 node_id 指定的节点。
CLUSTER REPLICATE <node_id> 将当前节点设置为 node_id 指定的节点的从节点。
CLUSTER SAVECONFIG 将节点的配置文件保存到硬盘里面。
槽(slot)
CLUSTER ADDSLOTS <slot> [slot ...] 将一个或多个槽（slot）指派（assign）给当前节点。
CLUSTER DELSLOTS <slot> [slot ...] 移除一个或多个槽对当前节点的指派。
CLUSTER FLUSHSLOTS 移除指派给当前节点的所有槽，让当前节点变成一个没有指派任何槽的节点。
CLUSTER SETSLOT <slot> NODE <node_id> 将槽 slot 指派给 node_id 指定的节点，如果槽已经指派给另一个节点，那么先让另一个节点删除该槽>，然后再进行指派。
CLUSTER SETSLOT <slot> MIGRATING <node_id> 将本节点的槽 slot 迁移到 node_id 指定的节点中。
CLUSTER SETSLOT <slot> IMPORTING <node_id> 从 node_id 指定的节点中导入槽 slot 到本节点。
CLUSTER SETSLOT <slot> STABLE 取消对槽 slot 的导入（import）或者迁移（migrate）。
键
CLUSTER KEYSLOT <key> 计算键 key 应该被放置在哪个槽上。
CLUSTER COUNTKEYSINSLOT <slot> 返回槽 slot 目前包含的键值对数量。
CLUSTER GETKEYSINSLOT <slot> <count> 返回 count 个 slot 槽中的键。
