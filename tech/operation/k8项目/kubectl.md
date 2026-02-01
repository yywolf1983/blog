
kubectl -n mfi get deployments | grep nginx

kubectl scale -n mfi-test deployment g-app-metapi-xyz  --replicas=0

kubectl -n mfi-test get deployments tnginx -o yaml


kubectl describe pods ubuntu-86dbffd4c-t97xj   -n test

kubectl get pods -n kube-system

kubectl logs tg-quant-6d94c4cb-qv78z -n trigger

kubectl get pods -A

kubectl delete pod kube-flannel-ds-7zrjt -n kube-system

kubectl exec -ti  ubuntu-7c86f79fd4-rm982  -n mfi-test /bin/bash

kubectl rollout restart deployment -n mfi  wormhole-canoe 

kubectl logs ubuntu-84d964f554-rxmb7 -n mfi-test

kubectl get pvc test -n test -oyaml
kubectl get deployment ubuntu -n test  -oyaml


kubectl cp  mfi-test/g-meta-mpi-6b69db97cf-dsdsg:log/2023-03-06-07.error.0.log abc.log

rancher 监控设置

alertmanager-rancher-monitoring-alertmanager 

--config.file=/etc/alertmanager/config/alertmanager.yaml 

kubectl create secret generic -n cattle-monitoring-system alertmanager-config --from-file=alertmanager.yaml=/Users/yy/aaa/block-insight/config/rancher/alertmanager.yaml --from-file=rancher_defaults.tmpl=/Users/yy/aaa/block-insight/config/rancher/rancher_defaults.tmpl

kubectl delete secret alertmanager-config -n cattle-monitoring-system 


修改 rancher 配置
kubectl -n cattle-monitoring-system get pods

kubectl -n cattle-monitoring-system exec -it prometheus-rancher-monitoring-prometheus-0 -- /bin/sh

ls /etc/prometheus/rules/prometheus-rancher-monitoring-prometheus-rulefiles-0/

kubectl get PrometheusRule -n cattle-monitoring-system
kubectl edit PrometheusRule rancher-monitoring-general.rules -n cattle-monitoring-system


##  亲和性设置

kubectl get node ip-192-168-19-131 --show-labels

kubectl label node ip-192-168-19-131 disktype=ssd


1、 ssh ubuntu@3.1.119.56
2、 kubectl get pods -n mfi |grep satsorder-pr
3、 kubectl exec -ti  satsorder-pr-8694cf76b9-zbpdw  -n mfi /bin/bash

kubectl logs -n mfi -f satsorder-pr-8694cf76b9-zbpdw

## 更新 configmap

kubectl -n mfi-test describe configmaps tnginx

kubectl -n mfi-test delete configmap tnginx
kubectl -n mfi-test create configmap tnginx \
       --from-file=/Users/yy/aaa/block-insight/config/all.conf
kubectl rollout restart -n mfi-test deployment tnginx
kubectl  -n mfi-test get pods | grep tnginx


kubectl -n mfi-test get configmap tnginx
kubectl -n mfi-test get configmap tnginx -o yaml > tnginx.yaml

kubectl -n mfi-test apply -f nginx.yaml

kubectl -n mfi-test edit configmap tnginx