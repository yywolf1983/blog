sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
    

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -


sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
   
   
sudo apt-get update

apt-get install docker-ce

# 启动docker
sudo service docker start
sudo service docker stop
sudo service docker restart


vi /lib/systemd/system/docker.service


docker version


sudo curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose  
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version


Powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

wsl --set-default-version 2

从1升级到2
wsl --set-version Ubuntu-20.04 2

开启外网访问
netsh interface portproxy add v4tov4 listenport=80 connectaddress=127.0.0.1 listenaddress=* protocol=tcp

portainer 安装
sudo docker pull portainer/portainer-ce
sudo docker run -d -p 9000:9000 \
--restart=always \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /data/docker/portainer_data:/data \
--name portainer-test \
portainer/portainer-ce
