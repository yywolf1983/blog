
LXC
    chroot，根切换，从容器内的角度来看，仿佛真的有自己的根树
    namespaces：名称空间，负责将资源隔离，比如pid，网络，mnt，user，uts等
    CGroups：控制组，负责控制资源的分配

docker run --name first-mysql -p 3306:3306 -e MYSQL\_ROOT\_PASSWORD=123456 -d mariadb

Harbor docker 仓库

yum remove docker \
              docker-common \
              docker-selinux \
              docker-engine

yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2

yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

yum install docker-ce

systemctl start docker

yum remove docker-ce 
rm -rf /var/lib/docker

阿里云镜像加速
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://sgwhfezw.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker

yum -y install docker-ce
systemctl start docker


vi /lib/systemd/system/docker.service
-H 0.0.0.0:2375
systemctl daemon-reload
systemctl restart docker


添加到用户组 sudo gpasswd -a <当前登陆用户名> docker
从用户组中删除： sudo gpasswd -d <当前登陆用户名> docker


docker context create my-remote-docker --docker "host=ssh://username@host:port"

docker context create my-remote-docker --docker "host=ssh://ubuntu@3.1.119.56:22"

## 国内镜像
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["http://hub-mirror.c.163.com"]
}
{
  "registry-mirrors": ["https://xxxxx.mirror.aliyuncs.com"]
}
EOF

## 卸载docker
yum remove docker-ce
rm -rf /var/lib/docker


service docker start
docker version
docker info

docker search    #查找容器
docker pull <image>  #下载容器
docker images： 列出images
docker images -a ：列出所有的images（包含历史）
docker images --timageree ：显示镜像的所有层(layer)
docker rmi  <image ID>： 删除一个或多个image


docker history ubuntu


# 制作原始镜像
# 下载 rmp 包

yum install epel-release -y
yum install -y \
https://www.dwhd.org/wp-content/uploads/2016/06/febootstrap-3.21-4.el6_.x86_64.rpm \
https://www.dwhd.org/wp-content/uploads/2016/06/fakechroot-libs-2.9-24.5.el6_1.1.x86_64.rpm \
https://www.dwhd.org/wp-content/uploads/2016/06/febootstrap-supermin-helper-3.21-4.el6_.x86_64.rpm \
https://www.dwhd.org/wp-content/uploads/2016/06/fakechroot-2.9-24.5.el6_1.1.x86_64.rpm

 yumdownloader fakeroot fakeroot-libs febootstrap

# 安装 rpm 包
yum install yum-utils
rpm -ivh .rpm

yum install febootstrap

febootstrap -i bash -i yum centos7 centos7-image https://mirror.tuna.tsinghua.edu.cn/centos/7/os/x86_64/

-i vim-minimal -i tar -i gzip -i wget 
-i iputils -i iproute -i tar -i gzip
(-i 安装package， centos7 操作系统版本，centos6-image安装目录，最后是源地址)

cd centos7-image/
tar -c .|docker import - centos7:base

docker tag centos7:base 192.168.2.25:5000/centos7:base
docker push 192.168.2.25:5000/base_mysql

docker run -i -t centos7.7 /bin/bash #此方式运行的容器，退出后容器就会关闭。
 --restart=always  开机启动
docker exec -it <docker_name> /bin/bash    #进入运行中的docker
lpasswd

复制 docker
docker build -t test_run .
docker run -i -t xxx /bin/bash 运行shell
docker run -name mytomcat  -v /外部目录:/内部目录:rw  -p 外部绑定:80:80 -p 127.0.0.1:3306:3306 -d -t test_run
setenforce 0   目录无法读写需要关闭 selinux
docker exec -i -t xxx /bin/bash  进入shell
docker exec --user 0 -i -t 6325b246d7ed /bin/bash
docker exec -i -t xxxxxx mkdir -p /data/tools/yywolf/web
docker exec -i -t xxxxxx mv /data/mysql_data.back /data/tools/yywolf/data

docker run --name myenv -v /Users/yy/src/mysrc/nones:/data/www/nones:rw -p 8086:8086 -d -t centos

重启策略：

使用在Docker run的时候使用--restart参数来设置。
no - Container不重启
on-failure - container推出状态非0时重启
always - 始终重启

iptables 设置错误后
ip link delete docker0
systemctl restart docker


docker build -t jdk .



docker run -d -p 127.0.0.1:5001:22 <容器id> /usr/sbin/sshd-D   后台方式运行
docker run -d -p 127.0.0.1:2222:22 -p 3306:3306  centos6-ssh

基础命令

docker stop <容器id> #停止运行的容器

docker save debian02 > /root/debian02.tar #debian02镜像打包

docker load < debian02.tar #导入镜像


docker run -h="redis-test" --name redis-test -d -p 51000:22 debian02 /etc/rc.local

docker inspect  查看容器信息

查看容器名字
docker inspect -f "{{ .Name }}" aed84ee21bde

-p 端口映射
-name 别名
run 是建立一个新的容器

docker top <container> #显示容器内运行的进程  
docker images #查询所有的镜像，默认是最近创建的排在最上。  
docker ps #查看正在运行的容器  
docker ps -l #查看最后退出的容器的ID  
docker ps -a #查看所有的容器，包括退出的。  
docker logs {容器ID|容器名称} #查询某个容器的所有操作记录。  
docker logs -f {容器ID|容器名称} #实时查看容易的操作记录。

docker rm $(docker ps -a -q) #删除所有容器  
docker rm <容器名or ID> #删除单个容器  
docker rmi <ID> #删除单个镜像  
docker rmi $(docker images | grep none | awk '{print $3}' | sort -r) #删除所有镜像
docker rm `docker ps -a|grep Exited|awk '{print $1}'`  删除已经退出的容器
docker rmi -f  `docker images | grep '<none>' | awk '{print $3}'` 删除none镜像

docker stop <容器名or ID> #停止某个容器  
docker start <容器名or ID> #启动某个容器  
docker kill <容器名or ID> #杀掉某个容器

启动后设置
docker update --restart=always <CONTAINER ID>


#制作基础镜像。
tar --numeric-owner --exclude=/proc --exclude=/sys -cvf centos6-base.tar /

docker export <CONTAINER ID> > /home/export.tar #导出  
cat centos6-base.tar | docker import - centos6-base  # 导入export.tar文件  

docker save debian> /home/save.tar #将debian容器打包  
docker load < /home/save.tar #倒入本地库

#从container中拷贝文件，当container已经关闭后，在里面的文件还可以拷贝出来。  
sudo docker cp 7bb0e258aefe:/etc/debian_version . #把容器中的/etc/debian_version拷贝到当前目录下。


高阶

进入容器
PID=$(docker inspect --format "{{ .State.Pid }}" <container>)
nsenter --target $PID --mount --uts --ipc --net --pid

挂在数据卷
docker run -d -P --name web -v /src/webapp:/opt/webapp:ro
上面的命令加载主机的 /src/webapp 目录到容器的 /opt/webapp 目录。并且只读

创建数据卷容器
sudo docker run -d -v /dbdata --name dbdata training/postgres echo Data-only container for postgres
在其他容器中挂在数据卷容器
docker run -d --volumes-from dbdata --name db1 training/postgres
还可以使用多个 --volumes-from 参数来从多个容器挂载多个数据卷。 也可以从其他已经挂载了容器卷的容器来挂载数据卷
docker run -d --name db3 --volumes-from db1 training/postgres

备份
docker run --volumes-from dbdata -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar
从本地创建一个数据卷 将数据考入本地
恢复道理相同

容器连接
docker run -d -P --name web --link db:db training/webapp python app.py
--link 参数的格式为 --link name:alias，其中 name 是要链接的容器的名称，alias 是这个连接的别名。

必须打开本地网络转发
sysctl net.ipv4.ip_forward
net.ipv4.ip_forward = 1
   docker run -h="test" --name test -d -p 51000:22 -p 8080:80  9d065db6f01e /usr/sbin/sshd -D
vi /etc/sysconfig/docker
mac os

brew install boot2docker
brew install docker

export DOCKER_HOST=tcp://127.0.0.1:4243

export PATH=$PATH:/Applications/VirtualBox.app/Contents/MacOS
boot2docker init
/Users/test/.boot2docker/boot2docker.iso

设置环境变量
eval "$(boot2docker shellinit)"

boot2docker up

sudo docker -d

boot2docker ssh，输入密码  tcuser 进到该虚拟机的控制台下

 Mac OS X(50080) --> boot2docker(40080) --> container(80)
boot2docker ssh -L 50080:localhost:40080
docker run -i -t -p 40080:80 learn/tutorial
或
VBoxManage modifyvm "boot2docker-vm" --natpf1 "tcp-port_50080:80,tcp,,50080,,40080"
vi /etc/sysconfig/docker


### 查看挂载的目录
docker inspect 889f2ebdaf42 | grep Mounts -A 20

docker pull registry

docker run -d -p 5000:5000 -v /home/user/registry-conf:/registry-conf -e DOCKER_REGISTRY_CONFIG=/registry-conf/config.yml registry

docker run -d -p 192.168.2.25:5000:5000 -v /data/registry:/var/lib/registry registry

docker commit <容器id> debian02 #把这个容器提交生成新的debian02镜像(该镜像是原始镜像与容器的整合)
docker commit <容器id> <新镜像名称>

### 标记上传镜像
docker tag base_mysql 192.168.2.25:5000/base_mysql
docker push 192.168.2.25:5000/base_mysql

### 上传到阿里云
docker login --username=yywol*****@aliyun.com registry.cn-hangzhou.aliyuncs.com
$ docker tag [ImageId] registry.cn-hangzhou.aliyuncs.com/yywolf/yy:[镜像版本号]
$ docker push registry.cn-hangzhou.aliyuncs.com/yywolf/yy:[镜像版本号]

docker pull 192.168.2.25:5000/base_mysql

curl -XGET http://192.168.2.25:5000/v2/catalog

这里设置后要重启
echo '{ "insecure-registries":    ["192.168.2.25:5000"] }' > /etc/docker/daemon.json


#Dockerfile java
FROM centos7.7:base
MAINTAINER yywolf <yywolf1983>
run wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
#copy soft/jdk-11.0.5_linux-x64_bin.tar.gz /data
WORKDIR /data
#这里会直接解压
add soft/jdk-11.0.5_linux-x64_bin.tar.gz /data/
ENV JAVA_HOME /data/jdk-11.0.5/
env CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/jre/lib/rt.jar
env PATH $JAVA_HOME/bin:$PATH
run java --version
#声明卷
#volume /data/soft
#初始化
#ENTRYPOINT source /etc/profile


Dockerfile nginx
FROM centos7.7:base
MAINTAINER yywolf <yywolf1983>

run mkdir -p /data
add nginx.tar.gz /data/

volume /data/nginx/html
WORKDIR /data/nginx/
CMD ["/data/nginx/sbin/nginx","-g","daemon off;"]

#Dockerfile sshd
FROM centos63-base
MAINTAINER yywolf <yywolf1983>
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN sed -ri 's/session    required     pam_loginuid.so/#session    required     pam_loginuid.so/g' /etc/pam.d/sshd
RUN echo 'root:123456' | chpasswd            
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
EXPOSE 22 3306
#安装 crontab
RUN /usr/bin/yum -y install vixie-cron
#USER root
#ONBUILD 子镜像中执行 神奇
CMD /usr/sbin/sshd -D   启动时执行
#End

ENTRYPOINT，表示镜像在初始化时需要执行的命令，不可被重写覆盖，需谨记
CMD，表示镜像运行默认参数，可被重写覆盖
ENTRYPOINT/CMD都只能在文件中存在一次，并且最后一个生效 多个存在，只有最后一个生效，其它无效！
需要初始化运行多个命令，彼此之间可以使用 && 隔开，但最后一个须要为无限运行的命令，需切记！


可以通过-e来设定任意的环境变量，甚至覆盖已经存在的环境变量，或者是在Dockerfile中通过ENV设定的环境变量。



cat > Dockerfile <<EOF
FROM centos7.7:base
MAINTAINER yywolf <yywolf1983>

run mkdir -p /data
add nginx.tar.gz /data/

volume /data/nginx
WORKDIR /data/nginx/
CMD ["/data/nginx/sbin/nginx","-g","daemon off;"]

EOF

docker build -t yy/nginx:v1 .

docker tag yy/nginx:v1 192.168.0.198:5000/yy/nginx:v1
docker push 192.168.0.198:5000/yy/nginx:v1

docker run -d -p 8000:80 -v /data/nginx-test:/data/nginx/html  --name nginx-test --restart=always -t yy/nginx:v1
docker ps 
docker logs nginx-test
docker stop nginx-test
docker rm nginx-test



mac docker

/Users/yy/Library/Containers/com.docker.docker/Data/vms/0/data





docker 清理
journalctl --vacuum-size=20M #设置journal 日志最大为20M不保留不必要日志。
docker image prune -a --filter "until=24h" # 清除超过创建时间超过24小时的镜像
docker container prune --filter “until=24h” #清除掉所有停掉的容器，但24内创建的除外
docker volume prune --filter “label!=keep” #除lable=keep外的volume外都清理掉(没有引用的volume)
docker system prune #清理everything：images ，containers，networks一次性清理操作可以通过docker system prune来搞定



## 查看工具

echo "alias lzd='docker run --name lzd --rm -it -v /var/run/docker.sock:/var/run/docker.sock lazyteam/lazydocker'" >> ~/.zshrc

-v /yourpath/config:/.config/jesseduffield/lazydocker


## mac 安装

brew install docker docker-compuse
brew install docker-credential-helper

~/.docker/config.json
"credsStore": "osxkeychain",