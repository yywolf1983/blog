
# docker
sudo docker login 47.108.235.230:8090 -u admin -p Harbor1234567890
sudo docker build -t "mynginx" .
sudo docker tag  mynginx 47.108.235.230:8090/base/mynginx
docker push 47.108.235.230:8090/base/mynginx


StatefulSet
Deployments 
  
https://github.com/prymitive/karma
karma  Alert dashboard for Prometheus Alertmanager 


ghcr.io/prymitive/karma:latest

upstream karma {
    server karma:8080;
}

ALERTMANAGER_URI=rancher-monitoring-alertmanager.cattle-monitoring-system:9093