
git clone https://github.com/kubernetes-sigs/descheduler
cd descheduler

kubectl create -f kubernetes/base/rbac.yaml
kubectl create -f kubernetes/base/configmap.yaml
kubectl create -f kubernetes/job/job.yaml

kubectl create -f kubernetes/cronjob/cronjob.yaml

kubectl top node 

官方默认策略
cat kubernetes/base/configmap.yaml