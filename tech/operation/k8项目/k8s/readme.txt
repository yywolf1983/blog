cat <<EOF >./kustomization.yaml
secretGenerator:
- name: mysql-pass
  literals:
  - password=123456
EOF


cat <<EOF >>./kustomization.yaml
resources:
  - mysql-deployment.yaml
  - nginx-deployment.yaml
EOF

kubectl apply -k ./


openssl req -new -nodes -newkey rsa:2048 -keyout private.key -subj "/C=CN/ST=ZheJiang/L=HangZhou/O=D7home/OU=ITinfo/CN=*.abc.com" -out www.crt
openssl req -new -x509 -key private.key -subj "/C=CN/ST=ZheJiang/L=HangZhou/O=D7home/OU=ITinfo/CN=*.abc.com" -out www.pem -days 3650


kubectl create configmap nginx-csr --from-file=www.pem --from-file=private.key

kubectl create configmap nginx-config --from-file=./nginx.conf  --from-file=./default.conf

kubectl create configmap nginx-index --from-file=./index.html


## 安装 metrics 做k8 核心监控
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

kubectl -n kube-system get pods -l k8s-app=metrics-server

可以通过 kubectl proxy 来访问 Metrics API：
    http://127.0.0.1:8001/apis/metrics.k8s.io/v1beta1/nodes
    http://127.0.0.1:8001/apis/metrics.k8s.io/v1beta1/nodes/<node-name>
    http://127.0.0.1:8001/apis/metrics.k8s.io/v1beta1/pods
    http://127.0.0.1:8001/apis/metrics.k8s.io/v1beta1/namespace/<namespace-name>/pods/<pod-name>

也可以直接通过 kubectl 命令来访问这些 API，比如
    kubectl get --raw /apis/metrics.k8s.io/v1beta1/nodes
    kubectl get --raw /apis/metrics.k8s.io/v1beta1/pods
    kubectl get --raw /apis/metrics.k8s.io/v1beta1/nodes/<node-name>
    kubectl get --raw /apis/metrics.k8s.io/v1beta1/namespace/<namespace-name>/pods/<pod-name>


kubectl get svc
kubectl get ingresses.


grafana 默认密码
prom-operator