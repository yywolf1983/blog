
集群初始化 得到3主3从
kubectl get pods -l app=redis-cluster -o jsonpath=' {range.items[*]}{.status.podIP}:6379 '
kubectl exec -it redis-cluster-0 -- redis-cli --cluster create --cluster-replicas 1 
 
添加节点
kubectl scale statefulset redis-cluster --replicas=8

让第一个新节点作为主节点加入集群：

nmid=`kubectl get pod redis-cluster-6 -o jsonpath=' {.status.podIP}':6379`
mid=`kubectl get pod redis-cluster-0 -o jsonpath=' {.status.podIP}':6379`

echo ${nmid} ${mid}

kubectl exec redis-cluster-0 -- redis-cli --cluster add-node ${nmid} ${mid}

第二个新节点应该作为从节点加入集群。这将自动绑定到具有最少从站的主站

nmid=`kubectl get pod redis-cluster-7 -o jsonpath=' {.status.podIP}':6379`
mid=`kubectl get pod redis-cluster-0 -o jsonpath=' {.status.podIP}':6379`
echo ${nmid} ${mid}

kubectl exec redis-cluster-0 -- redis-cli --cluster add-node --cluster-slave ${nmid} ${mid}
 
 
自动平衡
kubectl exec redis-cluster-0 -- redis-cli --cluster rebalance --cluster-use-empty-masters \
$(kubectl get pod redis-cluster-0 -o jsonpath='{.status.podIP}':6379)
 
 
删除从节点
kubectl exec redis-cluster-7 -- redis-cli cluster nodes | grep myself
5b0bfc8f89c4b52f44e41f7e54a631ede647a8f1 172.17.0.14:6379@16379 myself,slave 5c86373c48c4b1cc1a8570637a32ce04e9758870 0 1638350883000 7 connected

mip=`kubectl get pod redis-cluster-0 -o jsonpath='{.status.podIP}':6379` 
kubectl exec redis-cluster-0 -- redis-cli --cluster del-node ${mip} 5b0bfc8f89c4b52f44e41f7e54a631ede647a8f1


删除主节点
kubectl exec redis-cluster-6 -- redis-cli cluster nodes | grep myself
5c86373c48c4b1cc1a8570637a32ce04e9758870 172.17.0.13:6379@16379 myself,master - 0 1638350983000 8 connected 0-1364 5461-6826 10923-12287

kubectl exec redis-cluster-6 -- redis-cli cluster nodes | grep master | grep -v myself
c637a178c72d1c937f0add5c9e7da78c14806a89 172.17.0.5:6379@16379 master - 0 1638351018882 1 connected 1365-5460
3b3713ff1818764baf5710d19ee8b18d5a06ecb3 172.17.0.8:6379@16379 master - 0 1638351017000 3 connected 12288-16383
f91b21ca321e8cd24d65d371a5de25db6c355d18 172.17.0.7:6379@16379 master - 0 1638351019886 2 connected 6827-10922

kubectl exec redis-cluster-0 -- redis-cli --cluster reshard --cluster-yes \
--cluster-from 5c86373c48c4b1cc1a8570637a32ce04e9758870 \
--cluster-to c637a178c72d1c937f0add5c9e7da78c14806a89 \
--cluster-slots 16384 \
$(kubectl get pod redis-cluster-0 -o jsonpath='{.status.podIP}':6379)


重新分片
mip=`kubectl get pod redis-cluster-0 -o jsonpath='{.status.podIP}':6379`
kubectl exec redis-cluster-0 -- redis-cli --cluster del-node ${mip} 3b3713ff1818764baf5710d19ee8b18d5a06ecb3

重新平衡
mastid=`kubectl get pod redis-cluster-0 -o jsonpath=' {.status.podIP}':6379`
kubectl exec redis-cluster-0 -- redis-cli --cluster rebalance --cluster-use-empty-masters ${mastid}
 
缩容
kubectl scale statefulset redis-cluster --replicas=6

清理
kubectl delete statefulset,svc,configmap,pvc -l app=redis-cluster

查看集群状态
mip=`kubectl get pod redis-cluster-0 -o jsonpath='{.status.podIP}':6379`
kubectl exec redis-cluster-0 -- redis-cli --cluster info ${mip} -a "passwd123"

映射代理
sudo kubectl port-forward --address 127.0.0.1 service/redis-cluster 6379:6379

重新加载配置文件
kubectl patch StatefulSet redis-cluster --patch '{"spec": {"template": {"metadata": {"annotations": {"version/config": "20211129" }}}}}'

kubectl exec redis-cluster-0 -it bash
redis-cli -c  #-c 以集群模式进入

备份
kubectl exec redis-cluster-0 -- mkdir -p /data/back
kubectl exec redis-cluster-0 -- redis-cli --cluster backup ${mip} /data/back -a "passwd123"
kubectl cp  redis-cluster-0:/data/back ./