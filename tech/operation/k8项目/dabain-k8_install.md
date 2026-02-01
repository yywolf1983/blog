cat << EOF >/etc/network/interfaces   #编辑网网卡配置文件
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug eth0
iface eth0 inet static   #static表示使用固定ip，dhcp表述使用动态ip
address 192.168.3.95  #设置ip地址
netmask 255.255.255.0  #设置子网掩码
gateway 192.168.3.1    #设置网关
#network 192.168.2.0
#broadcast 192.168.2.255
EOF

systemctl restart networking 

hostnamectl set-hostname m1

sudo iptables -P INPUT ACCEPT   
sudo iptables -P OUTPUT ACCEPT  
sudo iptables -P FORWARD ACCEPT

vi /etc/sudoers
td ALL=(ALL) NOPASSWD:ALL


curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun

curl -sSL https://get.daocloud.io/docker | sh

sudo apt-get remove docker docker-engine docker.io containerd runc

sudo apt-get update


sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common
    
curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/debian/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/debian \
  $(lsb_release -cs) \
  stable"
  
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo docker run hello-world


## install k8s

cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
br_netfilter
EOF

cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sudo sysctl --system

sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl

curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

cat <<EOF > /etc/apt/sources.list.d/kubernetes.list 
deb http://mirrors.ustc.edu.cn/kubernetes/apt kubernetes-xenial main
EOF

sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl

kubeadm config images list

for i in `kubeadm config images list`; do
  imageName=${i#k8s.gcr.io/}
  sudo docker pull registry.aliyuncs.com/google_containers/$imageName
  sudo docker tag registry.aliyuncs.com/google_containers/$imageName k8s.gcr.io/$imageName
  sudo docker rmi registry.aliyuncs.com/google_containers/$imageName
done;

quay.io/coreos/flannel:v0.15.1

修改仓库地址
cat <<EOF > /etc/docker/daemon.json
{
   "insecure-registries": ["47.108.235.230:8090"],
   "exec-opts": ["native.cgroupdriver=systemd"]
}
EOF

sudo systemctl daemon-reload
sudo systemctl restart docker

docker login http://47.108.235.230:8090 -u admin -p Harbor1234567890

vim /usr/lib/systemd/system/docker.service

sudo systemctl enable kubelet
sudo systemctl start kubelet

# 关闭swap 很重要
sudo swapoff -a

主节点上初始化
sudo kubeadm init \
  --apiserver-advertise-address=192.168.3.93 \
  --service-cidr=10.96.0.0/12 \
  --pod-network-cidr=10.244.0.0/16 \
  --ignore-preflight-errors=Swap
  
  --kubernetes-version='v1.22.0'
  
第一个参数是主节点的 ip 地址
第二个参数是为 service 另指定一个 ip 地址段
第三个参数是为 pod 网络指定的 ip 地址段

sudo kubeadm token create --print-join-command

### 重置配置
sudo kubeadm reset
sudo rm -rf /etc/cni/net.d


sudo mkdir -p /root/.kube
sudo cp -i /etc/kubernetes/admin.conf /root/.kube/config
sudo chown $(id -u):$(id -g) /root/.kube/config

kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

查看集群状态
curl -k https://localhost:6443/livez\?verbose
curl -k https://localhost:6443/readyz\?verbose


kubectl get pods -n kube-system



