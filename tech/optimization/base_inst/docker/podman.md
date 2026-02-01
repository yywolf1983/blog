# 1. 手动下载虚拟机镜像（约1.5GB）
# 从国内镜像站下载，例如清华源：
curl -LO https://mirrors.tuna.tsinghua.edu.cn/podman/machine-os-wsl/latest/podman-machine-default-amd64.tar.xz

# 2. 导入镜像（需指定镜像路径）
podman machine init --image-path ./podman-machine-default-amd64.tar.xz

# 3. 启动虚拟机
podman machine start


# 停止虚拟机
podman machine stop
# 强制删除虚拟机（会丢失其中的所有容器和镜像）
podman machine rm -f
# 重新初始化
podman machine init
# mac 上需要安装这个
brew tap slp/krun
brew install krunkit
# 再次启动
podman machine start

# 查看 Podman 版本信息
podman version

# 或查看系统信息
podman info


podman-compose ps
# 或
podman ps -a

export DOCKER_HOST="unix://$(podman machine inspect --format '{{.ConnectionInfo.PodmanSocket.Path}}')"
echo $DOCKER_HOST

podman machine ssh

~/.config/containers/registries.conf
/etc/containers/registries.conf

https://github.com/DaoCloud/public-image-mirror

```
unqualified-search-registries = ["docker.io"]

[[registry]]
prefix = "docker.io"
location = "docker.m.daocloud.io"
insecure = false

[[registry.mirror]]
location = "docker.xuanyuan.me"
insecure = false

[[registry.mirror]]
location = "docker.1ms.run"
insecure = false

```

# 强制使用80
sudo vi /etc/sysctl.conf
net.ipv4.ip_unprivileged_port_start=80
sudo sysctl -p


# 安装管理工具
podman machine ssh
sudo bootc usroverlay
sudo dnf install cockpit cockpit-podman -y

sudo systemctl enable --now cockpit.socket
sudo systemctl status cockpit.socket

podman machine ssh -- -N -L 9090:localhost:9090


podman machine list
podman machine inspect
podman port -a

# 启动所有
podman start $(podman ps -aq)
podman ps -a --format "{{.Names}}"

# 为每个容器生成systemd服务 XXXXXXX 这里不成功
for CONTAINER in $(podman ps -a --format "{{.Names}}"); do
    echo "为容器 $CONTAINER 生成服务..."
    podman generate systemd --name $CONTAINER --files --new 
    sudo mv container-$CONTAINER.service  /etc/systemd/system/
    #ls -l /etc/systemd/system/container-$CONTAINER.service 
    sudo restorecon /etc/systemd/system/container-$CONTAINER.service
    sudo systemctl daemon-reload
    sudo systemctl enable container-$CONTAINER.service 
    sudo systemctl start container-$CONTAINER.service
    sudo systemctl disable container-$CONTAINER.service
done
同上
podman generate systemd --name myapp --files --user


podman machine inspect
podman machine ssh


podman exec -it <container_name> /bin/sh
podman cp file 容器名或ID:/path/



podman run --rm -v "d:\download\aaa\blog:/blog" ubi8-micro ls /blog


podman load -i debian12-rootfs.tar.gz
podman images
podman tag 05338089a283 debian:12


podman build -t my-nginx:1.0 .

podman exec -it my-nginx /bin/sh