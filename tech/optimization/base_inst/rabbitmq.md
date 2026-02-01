简介
RabbitMQ 是实现了高级消息队列协议（AMQP）的开源消息代理软件。RabbitMQ 服务器是用 Erlang 语言编写的，所以下面要安装 RabbitMQ 需要安装 Erlang。
一、安装 Erlang、Elixir

1.1 准备
yum update
yum install epel-release
yum install gcc gcc-c++ glibc-devel make ncurses-devel openssl-devel autoconf java-1.8.0-openjdk-devel git wget wxBase.x86_64

1.2 安装 Erlang
https://github.com/erlang/otp/releases
tar zxvf otp_src_22.3.4.16.tar.gz
./configure && make && make install
验证是否安装成功，输入命令：erl

1.3 安装 Elixir
因为 EPEL 中的 Elixir 版本太老，所以下面是通过源码编译安装的过程：
通过 git 下载 Elixir 源码：git clone https://github.com/elixir-lang/elixir.git
进到该目录：cd elixir/
编译：make clean test，编译完成会看到：Finished in 5.7 seconds (3.3s on load, 2.3s on tests)
配置 Path：export PATH="$PATH:/path/elixir/bin"
验证是否安装成功，输入命令：iex
二、安装 RabbitMQ
wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.1/rabbitmq-server-3.6.1-1.noarch.rpm
rpm --import https://www.rabbitmq.com/rabbitmq-signing-key-public.asc
yum install rabbitmq-server-3.6.1-1.noarch.rpm
至此已经安装完成，下面介绍启动和自动开机启动命令和配置
启动：systemctl start rabbitmq-server
开机自动启动：systemctl enable rabbitmq-server
查看 rabbitmq-server 状态：rabbitmqctl status
开启web
rabbitmq-plugins enable rabbitmq_management
安装好插件并开启服务后，可以浏览器输入localhost:15672,账号密码全输入guest即可登录。
参考
Install RabbitMQ server in CentOS 7


rabbitmqctl  add_user  Username  Password
rabbitmqctl  delete_user  Username
rabbitmqctl  change_password  Username  Newpassword
rabbitmqctl  list_users

(1) 超级管理员(administrator)
可登陆管理控制台(启用management plugin的情况下)，可查看所有的信息，并且可以对用户，策略(policy)进行操作。

(2) 监控者(monitoring)
可登陆管理控制台(启用management plugin的情况下)，同时可以查看rabbitmq节点的相关信息(进程数，内存使用情况，磁盘使用情况等)

(3) 策略制定者(policymaker)
可登陆管理控制台(启用management plugin的情况下), 同时可以对policy进行管理。但无法查看节点的相关信息(上图红框标识的部分)。
与administrator的对比，administrator能看到这些内容

(4) 普通管理者(management)
仅可登陆管理控制台(启用management plugin的情况下)，无法看到节点信息，也无法对策略进行管理。


rabbitmqctl  set_user_tags  User  Tag
----
rabbitmqctl set_user_tags yywolf1983 administrator

(1) 设置用户权限
rabbitmqctl  set_permissions  -p  VHostPath  User  ConfP  WriteP  ReadP

(2) 查看(指定hostpath)所有用户的权限信息
rabbitmqctl  list_permissions  [-p  VHostPath]

(3) 查看指定用户的权限信息
rabbitmqctl  list_user_permissions  User

(4)  清除用户的权限信息
rabbitmqctl  clear_permissions  [-p VHostPath]  User


集群安装

在 192.168.1.1、192.168.1.2、192.168.1.3 三个节点上安装，然后开启 RabbitMQ 监控插件：
rabbitmq-plugins enable rabbitmq_management

修改 /etc/hosts
加入集群 3 个节点的描述：
172.16.4.19 node1
172.16.4.20 node2
172.16.4.21 node3
设置 Erlang Cookie
Erlang Cookie 文件：/var/lib/rabbitmq/.erlang.cookie。这里将 node1 的该文件复制到 node2、node3，由于这个文件权限是 400，所以需要先修改 node2、node3 中的该文件权限为 777：
chmod 777 /var/lib/rabbitmq/.erlang.cookie

scp mq248:/var/lib/rabbitmq/.erlang.cookie /data
clush -b -w mq248,mq249,mq250 -c .erlang.cookie --dest=/var/lib/rabbitmq/.erlang.cookie

然后将 node1 中的该文件拷贝到 node2、node3，最后将权限和所属用户/组修改回来：
chmod 400 /var/lib/rabbitmq/.erlang.cookie
chown rabbitmq /var/lib/rabbitmq/.erlang.cookie
chgrp rabbitmq /var/lib/rabbitmq/.erlang.cookie

使用 -detached 参数运行各节点
rabbitmqctl stop
rabbitmq-server --detached

组成集群
将 node2、node3 与 node1 组成集群：

rabbitmqctl force_reset
service rabbitmq-server restart
rabbitmqctl stop_app
rabbitmqctl join_cluster rabbit@mq248
rabbitmqctl start_app


此时 node2 与 node3 也会自动建立连接；如果要使用内存节点，则可以使用
node2 # rabbitmqctl join_cluster --ram rabbit@node1

加入集群。
集群配置好后，可以在 RabbitMQ 任意节点上执行 rabbitmqctl cluster_status 来查看是否集群配置成功。
设置镜像队列策略
在任意一个节点上执行：
rabbitmqctl set_policy ha-all "^" '{"ha-mode":"all"}'

将所有队列设置为镜像队列，即队列会被复制到各个节点，各个节点状态保持一直。
完成这 6 个步骤后，RabbitMQ 高可用集群就已经搭建好了，最后一个步骤就是搭建均衡器。

安装并配置 HAProxy
在 192.168.1.1 上安装 HAProxy，然后修改
/etc/haproxy/haproxy.cfg：
listen rabbitmq_cluster 0.0.0.0:5672

mode tcp
balance roundrobin

server   node1 192.168.1.1:5672 check inter 2000 rise 2 fall 3  
server   node2 192.168.1.2:5672 check inter 2000 rise 2 fall 3
server   node2 192.168.1.3:5672 check inter 2000 rise 2 fall 3





rabbitmq-server



rabbitmqctl status
rabbitmqctl list_queues

rabbitmqctl stop_app
rabbitmqctl start_app

# 查看当前所有用户
$ sudo rabbitmqctl list_users

# 查看默认guest用户的权限
$ sudo rabbitmqctl list_user_permissions guest

# 由于RabbitMQ默认的账号用户名和密码都是guest。为了安全起见, 先删掉默认用户
$ sudo rabbitmqctl delete_user guest

# 添加新用户
$ sudo rabbitmqctl add_user username password

# 设置用户tag
$ sudo rabbitmqctl set_user_tags username administrator

# 赋予用户默认vhost的全部操作权限
$ sudo rabbitmqctl set_permissions -p / username ".*" ".*" ".*"

# 查看用户的权限
$ sudo rabbitmqctl list_user_permissions username


开启web 访问 15672
rabbitmq-plugins enable rabbitmq_management
