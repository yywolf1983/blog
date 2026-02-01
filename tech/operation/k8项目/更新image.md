nginx

docker login http://47.108.235.230:8090 -u admin -p Harbor1234567890

imageName[1]=k8s.gcr.io/kube-apiserver:v1.22.3
imageName[2]=k8s.gcr.io/kube-controller-manager:v1.22.3
imageName[3]=k8s.gcr.io/kube-scheduler:v1.22.3
imageName[4]=k8s.gcr.io/kube-proxy:v1.22.3
imageName[5]=k8s.gcr.io/pause:3.5
imageName[6]=k8s.gcr.io/etcd:3.5.0-0
imageName[7]=k8s.gcr.io/coredns/coredns:v1.8.4
imageName[8]=gcr.io/k8s-minikube/storage-provisioner:v5
imageName[9]=quay.io/coreos/flannel:v0.15.1

imageName[10]=kubernetesui/dashboard:v2.3.1
imageName[11]=kubernetesui/metrics-scraper:v1.0.7

imageName[12]=k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1
imageName[13]=gcr.io/google-samples/xtrabackup:1.0

#Õ∆ÀÕ
for name in ${imageName[*]}; do
docker pull $name
docker tag $name 47.108.235.230:8090/base/$name
docker push 47.108.235.230:8090/base/$name
done

#ªÒ»°
for name in ${imageName[*]}; do
sudo docker pull 47.108.235.230:8090/base/$name
sudo docker tag 47.108.235.230:8090/base/$name $name
sudo docker rmi 47.108.235.230:8090/base/$name
done
