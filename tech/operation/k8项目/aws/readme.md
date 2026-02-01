创建集群
eksctl create cluster \
 --name my-cluster \
 --version 1.21 \
 --without-nodegroup

## aws 常用

aws sts get-caller-identity
aws configure

aws eks update-kubeconfig --region ap-southeast-1 --name awsn

aws eks update-kubeconfig --name awsn --region ap-southeast-1  --role-arn arn:aws:iam::539123627321:role/admin


## 使用 ECR库
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 539123627321.dkr.ecr.ap-southeast-1.amazonaws.com


docker tag bk:latest 539123627321.dkr.ecr.ap-southeast-1.amazonaws.com/bk:latest
docker push 539123627321.dkr.ecr.ap-southeast-1.amazonaws.com/bk:latest

## 切换 eks集群

export KUBECONFIG=/Users/yy/Downloads/k8s.yml

aws eks update-kubeconfig --region ap-southeast-1 --name aws

kubectl get svc --all-namespaces

dashboard 安装

kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml


cat << EOF > eks-admin-service-account.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: eks-admin
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: eks-admin
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: eks-admin
  namespace: kube-system
EOF

kubectl apply -f eks-admin-service-account.yaml

kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}')

kubectl port-forward services/kubernetes-dashboard 8000:443 --address 0.0.0.0

关闭 https  失效
kubectl patch svc kubernetes-dashboard  -p '"spec": {"type": "NodePort","ports": [{"port": 443,"nodePort": 31000}]}' -n kubernetes-dashboard


http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#!/login

#PROXY-START/

location ^~ /
{
    proxy_pass http://127.0.0.1:8001;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header REMOTE-HOST $remote_addr;
    
    add_header X-Cache $upstream_cache_status;
    
    #Set Nginx Cache
    
    
    set $static_fileWLqIPMyw 0;
    if ( $uri ~* "\.(gif|png|jpg|css|js|woff|woff2)$" )
    {
    	set $static_fileWLqIPMyw 1;
    	expires 12h;
        }
    if ( $static_fileWLqIPMyw = 0 )
    {
    add_header Cache-Control no-cache;
    }
}

#PROXY-END/

## rancher

docker run --privileged -d --restart=unless-stopped -p 8086:80 -p 8443:443 --name rancher rancher/rancher:v2.7.1

docker logs  rancher 2>&1 | grep "Bootstrap Password:"

https://13.214.254.61:8443
1bAxn7Sr6c3lMpTT


kubectl port-forward -n test service/mysql 3306:3306


使用 Prometheus 监控 Kubernetes 集群

helm repo update

helm search repo prometheus

def-pass:prom-operator



kubectl --namespace default port-forward  prometheus-node-grafana-79f97c569b-r9v5v 9091 --address 0.0.0.0 
kubectl --namespace default port-forward  services/prometheus-node-prometheus-prometheus 9092:9090 --address 0.0.0.0 


curl -H 'Host:grafana.arche.network' http://3.0.99.10/

prometheus-node-grafana.default.svc.cluster.local

service 
网格 Istio

kubectl --namespace test port-forward  ingress/nacos-in 8848:8848 --address 0.0.0.0 

kubectl port-forward services/kubernetes-dashboard 8000:443 --address 0.0.0.0 -n  kubernetes-dashboard

kubectl port-forward services/prometheus-grafana -n default --address 0.0.0.0 8081:80

kubectl port-forward services/prometheus-prometheus-oper-prometheus --address 0.0.0.0 9100:9090


kubectl config use-context arn:aws:eks:ap-southeast-1:539123627321:cluster/aws

kubectl proxy --port=3000 --address=0.0.0.0 --accept-hosts='.*'

http://rancher-monitoring-prometheus.cattle-monitoring-system:9090/



## aws redis
  
aws elasticache describe-cache-clusters
aws elasticache describe-cache-clusters --show-cache-node-info
aws elasticache describe-cache-clusters --cache-cluster-id  redis-0001-001 --show-cache-node-info



## aws back

### etcd 物理部署

```text
date;
CACERT="/opt/kubernetes/ssl/ca.pem"
CERT="/opt/kubernetes/ssl/server.pem"
EKY="/opt/kubernetes/ssl/server-key.pem"
ENDPOINTS="127.0.0.1:2379"

ETCDCTL_API=3 etcdctl \
--cacert="${CACERT}" --cert="${CERT}" --key="${EKY}" \
--endpoints=${ENDPOINTS} \
snapshot save /backup/etcd-snapshot-`date +%Y%m%d`.db

# 备份保留30天
find /backup/ -name *.db -mtime +30 -exec rm -f {} \;
```

### 恢复
1.停止所有 Master 上 kube-apiserver 服务

systemctl stop kube-apiserver

2.停止集群中所有 ETCD 服务
systemctl stop etcd

3.移除所有 ETCD 存储目录下数据
mv /etcd/data /etcd/data.bak

4.从备份文件中恢复数据
ETCDCTL_API=3 etcdctl snapshot restore /backup/etcd-snapshot-xx.db  

5.启动 etcd
systemctl start etcd

6.启动 apiserver
systemctl start kube-apiserver

7.检查服务是否正常


## 安装成本监控

https://docs.aws.amazon.com/eks/latest/userguide/cost-monitoring.html

helm upgrade -i kubecost oci://public.ecr.aws/kubecost/cost-analyzer --version 1.97.0 \
    --namespace kubecost --create-namespace \
    -f https://raw.githubusercontent.com/kubecost/cost-analyzer-helm-chart/develop/cost-analyzer/values-eks-cost-monitoring.yaml

kubectl get pods -n kubecost

kubectl port-forward --namespace kubecost deployment/kubecost-cost-analyzer 9090

helm uninstall kubecost --namespace kubecost
kubectl delete ns kubecost

## 启用监控面板

kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml

具体安装查询权限

kubectl apply -f eks-admin-service-account.yaml

kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}')

kubectl port-forward services/kubernetes-dashboard 8000:443 --address 0.0.0.0 -n  kubernetes-dashboard
