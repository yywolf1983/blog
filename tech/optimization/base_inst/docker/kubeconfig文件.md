cat > yy-csr.json << EOF
{
  "CN": "yy",
  "hosts": [],
  "key": {
    "algo": "rsa",
    "size": 2048
  },
  "names": [
    {
      "C": "CN",
      "ST": "BeiJing",
      "L": "BeiJing",
      "O": "k8s",
      "OU": "System"
    }
  ]
}
EOF

cfssl gencert -ca=ca.crt -ca-key=ca.key -config=ca-config.json -profile=kubernetes yy-csr.json | cfssljson -bare yy


export KUBECONFIG=/Users/yy/Downloads/k8s.yml

kubectl config get-contexts


# 设置集群参数
export KUBE_APISERVER="https://192.168.2.200:6443"
kubectl config set-cluster kubernetes \
--certificate-authority=/etc/kubernetes/pki/ca.crt \
--embed-certs=true \
--server=${KUBE_APISERVER} \
--kubeconfig=yy.kubeconfig

# 设置客户端认证参数
kubectl config set-credentials yy \
--client-certificate=/etc/kubernetes/pki/yy.pem \
--client-key=/etc/kubernetes/pki/yy-key.pem \
--embed-certs=true \
--kubeconfig=yy.kubeconfig

# 设置上下文参数
kubectl config set-context kubernetes \
--cluster=kubernetes \
--user=yy \
--namespace=yy \
--kubeconfig=yy.kubeconfig

# 设置默认上下文
kubectl config use-context kubernetes --kubeconfig=yy.kubeconfig

cp -f ./yy.kubeconfig /root/.kube/config

kubectl create rolebinding devuser-admin-binding --clusterrole=admin --user=yy --namespace=yy
