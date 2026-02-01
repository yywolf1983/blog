k8s  kubernetes

![k8s网络原理](./img/k8s_net.png)

##  安装步骤
### 1.关闭 iptables

### 2.闭 selinux
  ansible all -m shell -a "setenforce 0"
  ansible all -m shell -a "getenforce"
  ansible all -m shell -a "sed -i \"s/^SELINUX=.*$/SELINUX=disabled/g\" /etc/selinux/config"

### 3.安装docker
clush -b -a curl -o /etc/yum.repos.d/docker-ce.repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

####  从阿里云安装最新docker
      yum remove docker  docker-common docker-selinux docker-engine
      ansible all -m shell -a "yum install docker-ce"

#### > 启动docker
    ansible all -m shell -a systemctl daemon-reload
    ansible all -m shell -a systemctl start docker
    ansible all -m shell -a "docker info"
    ansible all -m shell -a "systemctl enable docker"

##### >> 查看防火墙 FORWARD 开启
    ansible all -m shell -a "iptables -vnL"

    关闭防火墙
    systemctl disable firewalld

#### > 查看桥接参数 bridge
    ansible all -m shell -a "sysctl -a | grep bridge"

cat  >> /etc/sysctl.conf << EOF
net.bridge.bridge-nf-call-iptables = 1
EOF

cat << EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

sysctl -p /etc/sysctl.d/k8s.conf 

sysctl -p

#### > 开启 ipvs
/usr/lib/modules/3.10.0-957.el7.x86_64/kernel/net/netfilter/ipvs

/etc/sysconfig/modules/ipvs.modules


#### >
Environment="http_proxy="
Environment="no_proxy="

### 使用谷歌镜像
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kubelet kubeadm kubectl
EOF


### 使用阿里云镜像
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF

ansible all -m shell -a "src=/etc/yum.repos.d/kubernetes.repo dest=/etc/yum.repos.d/kubernete.repo"

yum list all | grep ^kuber

ansible all -m shell -a "yum -y makecache"

节点网络 service网络
pod网络 flannel,calico

ansible all -m shell -a "yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes"

rpm -ql kubelet
  /etc/kubernetes/manifests
  /etc/sysconfig/kubelet
  /usr/bin/kubelet
  /usr/lib/systemd/system/kubelet.service

rpm -ql kubeadm
  /usr/bin/kubeadm
  /usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf

### 如果没有关闭 swp
vi /etc/sysconfig/kubelet
KUBELET_EXTRA_ARGS="--fail-swap-on=false"

打印配置信息
kubeadm config print init-defaults


获取镜像信息 
kubeadm config images list
kubeadm config images pull

国内可能无法拉取 要手动下载
#### 利用阿里云拉取镜像
for i in `kubeadm config images list`; do
  imageName=${i#k8s.gcr.io/}
  docker pull registry.aliyuncs.com/google_containers/$imageName
  docker tag registry.aliyuncs.com/google_containers/$imageName k8s.gcr.io/$imageName
  docker rmi registry.aliyuncs.com/google_containers/$imageName
done;

docker image list

这一步一般忽略
kubeadm config images pull

cat > /etc/docker/daemon.json <<EOF
{
  "insecure-registries": ["47.108.235.230:8090"],
  "exec-opts": ["native.cgroupdriver=systemd"]
}
EOF

# 安装前初始化
ansible k8s -m copy -a "src=/etc/docker/daemon.json dest=/etc/docker/daemon.json"
ansible k8s -m shell -a "systemctl restart docker"
ansible k8s -m shell -a "docker info | grep Cgroup"

ansible k8s -m copy -a "src=/etc/hosts dest=/etc/hosts"


kubeadm 会自动启动kubelet

# 初始化M 配置信息
kubeadm init --apiserver-advertise-address=172.30.214.140 --apiserver-cert-extra-sans=47.108.235.230 --kubernetes-version='v1.22.0'  --pod-network-cidr='10.244.0.0/16'
如果开启swap 加上这一行
--ignore-preflight-errors=Swap
--dry-run   测试

### 重置配置
kubeadm reset
rm -rf /etc/cni/net.d

# 启动kubelet
systemctl enable kubelet && systemctl start kubelet
journalctl -xeu kubelet
systemctl status kubelet

tail -f /var/log/messages

echo $HOME
## 初始化完成后修改配置
mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config

### 环境设置
export KUBECONFIG=/etc/kubernetes/admin.conf
alias kc=kubectl
source <(kubectl completion bash | sed s/kubectl/kc/g)
swapoff –a

### 合并多个 kubeconfig 文件 多集群管理
KUBECONFIG_BAK=$KUBECONFIG
KUBECONFIG=
kubeconfigDir=$HOME/.kube/config.d
for i in $(ls $kubeconfigDir)
do
  KUBECONFIG=$KUBECONFIG:"${kubeconfigDir}/${i}"
done
export KUBECONFIG

EOF

安装网络插件 flannel

imageName='coreos/flannel:v0.14.0'
docker pull 47.108.235.230:8090/base/$imageName
docker tag 47.108.235.230:8090/base/$imageName k8s.gcr.io/$imageName
docker rmi 47.108.235.230:8090/$imageName

wget https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
kubectl apply -f kube-flannel.yml
kubectl get pods -n kube-system -o wide


### 查找问题
journalctl -f -u kubelet

### 每个node 执行 ### 可以不用
groups="k8s"
ansible $groups -m shell -a "mkdir -p /run/flannel/"
ansible $groups -m copy -a "src=/run/flannel/subnet.env dest=/run/flannel/subnet.env"

ansible $groups -m shell -a "mkdir -p /etc/cni/net.d/"
ansible $groups -m copy -a "src=/etc/cni/net.d/10-flannel.conflist dest=/etc/cni/net.d/10-flannel.conflist"

## 在node 节点安装
ansible $groups -m shell -a "yum install -y kubelet kubeadm"

ansible $groups -m shell -a "systemctl enable kubelet.service"
ansible $groups -m shell -a "systemctl enable docker.service"

#### *****
kubeadm生成的token默认24小时过期，在master上执行kubeadm token create创建新的token
kubeadm token create --print-join-command

 ansible $groups -m shell -a "systemctl enable kubelet.service"

 ansible $groups -m shell -a "kubeadm join 172.30.214.140:6443 --token jp05cp.w2hdoi0buprz8vfh --discovery-token-ca-cert-hash sha256:d1f7b269a121af353d042cdee502234b964c1548cba7dbab6ce3293c08719653"

## 用master 做node
 kubectl taint node dev node-role.kubernetes.io/master-

禁止master 做 node
 kubectl taint node dev node-role.kubernetes.io/master:NoSchedule

 kubectl describe node dev | grep Taints
 
 去掉
 kubectl label node dev node-role.kubernetes.io/node-
 加上
 kubectl label node dev node-role.kubernetes.io/node=


#### 重新注册客户端
 rm -rf /etc/kubernetes/kubelet.conf
 rm -rf /etc/kubernetes/pki/ca.crt
 rm -rf /etc/kubernetes/bootstrap-kubelet.conf 
 ss -anp | grep 10250



### 其他命令

重新注册需要
kubeadm reset

删除 node
kubectl delete node node2

cat <<EOF | sudo tee /etc/docker/daemon.json
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF

systemctl daemon-reload
systemctl restart kubelet

kubectl config view

docker load -i  load*.tar

证书信息
/etc/kubernetes/pki



kubectl proxy --port=80 --address=0.0.0.0 --accept-hosts='.*'

获取加密信息
kubectl get secret db-user-pass -o jsonpath='{.data}'
echo 'UyFCXCpkJHpEc2I9' | base64 --decode


export KUBE_APISERVER="https://192.168.2.200:6443" #填写SLB的地址
kubectl config set-cluster kubernetes  --certificate-authority=/etc/kubernetes/ssl/ca.pem  --embed-certs=true  --server=${KUBE_APISERVER}  --kubeconfig=kube-proxy.kubeconfig
kubectl config set-credentials kube-proxy  --client-certificate=/etc/kubernetes/ssl/kube-proxy.pem  --client-key=/etc/kubernetes/ssl/kube-proxy-key.pem  --embed-certs=true  --kubeconfig=kube-proxy.kubeconfig
kubectl config set-context default  --cluster=kubernetes  --user=kube-proxy  --kubeconfig=kube-proxy.kubeconfig
kubectl config use-context default --kubeconfig=kube-proxy.kubeconfig
ls kube-proxy.kubeconfig 


# 私有仓库管理   
## 另一种私有仓库 Harbor
docker pull registry:2

docker run -d \
  -p 5000:5000 \
  -v /data/registry:/var/lib/registry \
  -v /usr/local/auth:/auth \
  -e REGISTRY_AUTH=htpasswd \
  -e REGISTRY_AUTH_HTPASSWD_REALM=Registry_Realm \
  -e REGISTRY_AUTH_HTPASSWD_PATH=./passwd \
  -v /usr/local/nginx/conf/cert:/certs \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/server.pem \
  -e REGISTRY_HTTP_TLS_KEY=/certs/server.key \
  --restart=always \
  --name registry \
  registry

  docker run -d \
  -p 5000:5000 \
  -v /data/registry:/var/lib/registry \
  -v /root/auth:/auth \
  -e REGISTRY_AUTH=htpasswd \
  -e REGISTRY_AUTH_HTPASSWD_REALM="Registry Realm" \
  -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/passwd \
  --restart=always \
  --name registry \
  registry:2

  --restart=always 自动启动

生成密码
docker run --entrypoint htpasswd registry:2 -Bbn yywolf 123456

docker login -uyywolf -p123456 192.168.0.198:5000
docker logout 192.168.0.198:5000


kubectl create secret docker-registry myregistry --docker-server=192.168.0.198:5000 --docker-username=yywolf --docker-password=123456 
kubectl get secret

docker pull nginx
docker tag nginx localhost:5000/nginx:v1.0
docker push localhost:5000/nginx:v1.0

curl -u yywolf:yangyao -XGET http://localhost:5000/v2/_catalog
curl -u yywolf:yangyao -XGET http://localhost:5000/v2/<镜像名称>/tags/list
rm -rf /data/registry/docker/registry/v2/repositories/

ip link delete cni0
ip link delete flannel.1

journalctl -f -u kubelet.service

重置安装
kubeadm reset
systemctl stop kubelet
systemctl stop docker
rm -rf /var/lib/cni/
rm -rf /var/lib/kubelet/*
rm -rf /etc/cni/
ifconfig cni0 down
ifconfig flannel.1 down
ifconfig docker0 down
ip link delete cni0
ip link delete flannel.1
systemctl start docker


热升级
kubectl -n k8s-ecoysystem-apps set image deployments/helloworldapi helloworldapi=registry.wuling.com/justmine/helloworldapi:v2.3
kubectl -n k8s-ecoysystem-apps rollout status deployments/helloworldapi

回滚
kubectl -n k8s-ecoysystem-apps rollout undo deployment/helloworldapi  --to-revision=<版次>
或者
kubectl -n k8s-ecoysystem-apps rollout undo deployments/helloworldapi

### 节点维护
kubectl cordon m2
kubectl uncordon m2

### 驱逐节点
kubectl drain m2 --delete-local-data --ignore-daemonsets --force 


平滑升级系统
kubeadm upgrade plan
yum install -y kubelet kubeadm kubectl
kubeadm upgrade apply v1.7.0

![基础逻辑](img/k8s-singlenode-docker.png)

![基础逻辑2](img/kubernetes_design.jpg)


问题处理

systemctl restart kubelet

systemctl stop kubelet
systemctl stop docker
iptables --flush
iptables -tnat --flush
systemctl start kubelet
systemctl start docker

2、networkPlugin cni failed on the status hook for pod

kubeadm reset 
rm -rf /var/lib/cni/flannel/* 
rm -rf /var/lib/cni/networks/cbr0/* 
ip link delete cni0 flannel.1 

vi /run/flannel/subnet.env

删除网卡
ip addr flush dev cni0

route -n
ip route del 10.244.2.0/16

kubectl config get-contexts

kubectl config use-context docker-desktop

kubectl proxy



# 跳过 dashboard 验证
containers:
- args:
  - --auto-generate-certificates
  - --namespace=kubernetes-dashboard
  - --enable-skip-login                 # add this argument
  image: kubernetesui/dashboard:v2.2.0

kubectl edit deployment kubernetes-dashboard -n kubernetes-dashboard
kubectl patch deployment kubernetes-dashboard -n kubernetes-dashboard --type 'json' -p '[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--enable-skip-login"}]'


kubectl proxy
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login
or 
kubectl port-forward -n kubernetes-dashboard service/kubernetes-dashboard 8080:443




## 存储

kubectl describe storageclass ebs-sc

kubectl describe pv your_pv_name

kubectl -n test exec -it bash2-7c69c4bf84-fpb99  -- cat /data/out.txt

kubectl describe pv pvc-cd6fa79a-9be4-4f67-8899-1bd3c0713c88

kubectl exec -it app -- cat /data/out.txt

https://aws.amazon.com/cn/premiumsupport/knowledge-center/eks-persistent-storage/


nc -vvv -z  service-redis.default 6379

pod.servicename.namespace.svc.cluster.local