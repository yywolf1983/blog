
portainer安装
docker pull portainer/portainer-ce
docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v /data/docker/portainer_data:/data portainer/portainer-ce

备份
/var/lib/docker/volumes/portainer_data/_data


## 下载所有证书
for i in $(cat ~/.ssh/config  | grep  "host .*$" | awk '{print $2}')
do 
  echo $i
  mkdir -p $i
  rsync -avz $i:/etc/docker/cert.pem $i/
  rsync -avz $i:/etc/docker/key.pem $i/
done


ansible aws -m fetch -a 'src=/etc/docker/cert.pem dest=./'
ansible aws -m fetch -a 'src=/etc/docker/key.pem dest=./'