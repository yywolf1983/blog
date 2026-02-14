# Podman 使用指南

Podman 是一个无守护进程的容器运行时工具，与 Docker 兼容，可用于管理容器和镜像。本指南涵盖了 Podman 的安装、配置和常用操作。

## 一、安装和初始化

### 1. 手动下载虚拟机镜像
从国内镜像站下载，例如清华源（约1.5GB）：
```bash
curl -LO https://mirrors.tuna.tsinghua.edu.cn/podman/machine-os-wsl/latest/podman-machine-default-amd64.tar.xz
```

### 2. 导入镜像并初始化
```bash
# 导入镜像（需指定镜像路径）
podman machine init --image-path ./podman-machine-default-amd64.tar.xz

# 启动虚拟机
podman machine start
```

### 3. Mac 系统特殊安装
```bash
# Mac 上需要安装 krunkit
brew tap slp/krun
brew install krunkit

# 启动虚拟机
podman machine start
```

## 二、基本操作

### 1. 虚拟机管理
```bash
# 启动虚拟机
podman machine start

# 停止虚拟机
podman machine stop

# 强制删除虚拟机（会丢失其中的所有容器和镜像）
podman machine rm -f

# 重新初始化
podman machine init

# 查看虚拟机列表
podman machine list

# 查看虚拟机详细信息
podman machine inspect

# 连接到虚拟机
podman machine ssh
```

### 2. 版本和信息查看
```bash
# 查看 Podman 版本信息
podman version

# 查看系统信息
podman info
```
### 3.添加其他源
``` yaml
sudo tee /etc/containers/registries.conf.d/xuanyuan.conf <<EOF
[[registry]]
location = "docker.io"

[[registry.mirror]]
location = "docker.xuanyuan.me/docker.io"
EOF
```

## 三、容器管理

### 1. 容器操作
```bash
# 查看容器状态（使用 podman-compose）
podman-compose ps

# 或查看所有容器
podman ps -a

# 启动所有容器
podman start $(podman ps -aq)

# 列出所有容器名称
podman ps -a --format "{{.Names}}"

# 进入容器
podman exec -it <container_name> /bin/sh

# 复制文件到容器
podman cp file 容器名或ID:/path/
```

### 2. 端口管理
```bash
# 查看所有端口映射
podman port -a
```

## 四、镜像管理
```bash
# 加载本地镜像
podman load -i debian12-rootfs.tar.gz

# 查看镜像列表
podman images

# 为镜像添加标签
podman tag 05338089a283 debian:12

# 构建镜像
podman build -t my-nginx:1.0 .
```

## 五、配置文件

### 1. 配置文件位置
```bash
~/.config/containers/registries.conf
/etc/containers/registries.conf
```

### 2. 镜像源配置
推荐使用国内镜像源，例如：
```bash
https://github.com/DaoCloud/public-image-mirror
```

配置示例：
```toml
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

## 六、系统服务

### 1. 生成 systemd 服务
```bash
# 为每个容器生成 systemd 服务
for CONTAINER in $(podman ps -a --format "{{.Names}}"); do
    echo "为容器 $CONTAINER 生成服务..."
    podman generate systemd --name $CONTAINER --files --new 
    sudo mv container-$CONTAINER.service  /etc/systemd/system/
    sudo restorecon /etc/systemd/system/container-$CONTAINER.service
    sudo systemctl daemon-reload
    sudo systemctl enable container-$CONTAINER.service 
    sudo systemctl start container-$CONTAINER.service
    sudo systemctl disable container-$CONTAINER.service

done

# 为用户生成 systemd 服务
podman generate systemd --name myapp --files --user
```

### 2. 安装管理工具
```bash
# 连接到虚拟机
podman machine ssh

# 启用用户覆盖层
sudo bootc usroverlay

# 安装 cockpit 和 cockpit-podman
sudo dnf install cockpit cockpit-podman -y

# 启用并启动 cockpit 服务
sudo systemctl enable --now cockpit.socket
sudo systemctl status cockpit.socket

# 端口转发，以便在本地访问 cockpit
podman machine ssh -- -N -L 9090:localhost:9090
```

## 七、网络配置

### 1. 允许使用 80 端口
```bash
# 编辑 sysctl 配置
sudo vi /etc/sysctl.conf

# 添加以下内容
net.ipv4.ip_unprivileged_port_start=80

# 应用配置
sudo sysctl -p
```

### 2. IPv6 配置
```bash
# 创建 IPv6 网络
podman network create --subnet fd00:1234:5678::/64 --ipv6 docker_nginx-ipv6-net

# 运行支持 IPv6 的容器
podman run -d --name my-nginx --network nginx-ipv6-net --ip6 fd00:1234:5678::10  -p '0.0.0.0:80:80'  -p '[::]:8080:80' my-nginx:1.0

# 查看容器状态和端口映射
podman ps -f name=my-nginx
podman port my-nginx

# 启用 IPv6 转发
echo "net.ipv6.conf.all.forwarding = 1" | sudo tee -a /etc/sysctl.conf
echo "net.ipv6.conf.default.forwarding=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# 检查 IPv6 转发状态
if [ $(cat /proc/sys/net/ipv6/conf/all/forwarding 2>/dev/null) -eq 1 ]; then 
    echo "IPv6 转发已启用"; 
else 
    echo "IPv6 转发已禁用"; 
fi

# 检查是否有默认路由
ip -6 route | grep default

# 如果没有输出，需要添加默认路由
# 先获取网关地址（通常以 fe80:: 开头）
ip -6 neigh show

# 添加默认路由（示例，实际网关可能不同）
sudo ip -6 route add default via fe80::1 dev eth0

# 查看 IPv6 地址
ip -6 addr show | grep inet6
# 如果只有 fe80:: 开头的地址，说明只有链路本地地址
# 需要获取全局 IPv6 地址

# 启用 IPv6
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=0
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=0
sudo sysctl -w net.ipv6.conf.eth0.disable_ipv6=0

# 重启网络
sudo systemctl restart systemd-networkd

# 手动添加 IPv6 地址和默认路由（示例）
sudo ip addr add 2409:8a70:1033:3fa1::your_suffix/64 dev eth0
sudo ip -6 route add default via 2409:8a70:1033:3fa1::1
```

## 八、Docker 兼容配置
```bash
# 设置 DOCKER_HOST 环境变量，使 Docker 命令兼容 Podman
export DOCKER_HOST="unix://$(podman machine inspect --format '{{.ConnectionInfo.PodmanSocket.Path}}')"

echo $DOCKER_HOST
```

## 九、其他实用命令

### 1. 挂载主机目录
```bash
# 挂载 Windows 目录到容器
podman run --rm -v "d:\download\aaa\blog:/blog" ubi8-micro ls /blog
```

### 2. 容器内操作
```bash
# 进入容器
podman exec -it my-nginx /bin/sh
```