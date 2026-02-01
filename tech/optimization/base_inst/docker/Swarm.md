vim /etc/sysconfig/docker

centos7
OPTIONS='-g /cutome-path/docker -H tcp://0.0.0.0:2375'
centos6
OPTIONS='-g /mnt/docker -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock'


初始化
docker swarm init --advertise-addr 10.10.11.14

在子节点上安装
docker pull swarm

生成 token
docker run --rm swarm create
24505e3dee3fc029506d70f1851009dd l1114

添加子节点
docker run -d swarm join --addr=10.10.11.15:2375 token://24505e3dee3fc029506d70f1851009dd

列出节点
docker run --rm swarm list token://24505e3dee3fc029506d70f1851009dd

开启管理节点子节点上执行
docker run -d -p 8888:2375 swarm manage token://24505e3dee3fc029506d70f1851009dd

可以管理子节点了
docker -H 10.10.11.15:8888 info
docker -H 10.10.11.15:8888 ps


$ docker -H 192.168.20.3:8888 run -d --name web1 nginx
$ docker -H 192.168.20.3:8888 run -d --name web2 nginx
$ docker -H 192.168.20.3:8888 run -d --name web3 nginx
$ docker -H 192.168.20.3:8888 run -d --name web4 nginx
$ docker -H 192.168.20.3:8888 run -d --name web5 nginx
