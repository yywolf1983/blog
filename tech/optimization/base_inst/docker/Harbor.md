安装docker
安装docker-compose

https://github.com/goharbor/harbor/releases

最好下载离线安装包
https://github.com/goharbor/harbor/releases/download/v2.3.1/harbor-offline-installer-v2.3.1.tgz


解压离线安装包

tar xvf harbor-offline-installer-v2.3.1.tgz -C /data      #使用tar命令解压到/usr/local/目录下

配置harbor

cd /data/harbor/    #进入到harbor目录

cp   harbor.yml.tmpl    harbor.yml

vim harbor.yml   #编辑harbor的配置文件

#修改以下内容

hostname = 192.168.100.204 #修改harbor的启动ip，这里需要依据系统ip设置

port: 80 #harbor的端口,有两个端口,http协议(80)和https协议(443)

harbor_admin_password = harbor12345   #修改harbor的admin用户的密码

data_volume: /data/harbor/data #修改harbor存储位置

注释掉https 相关配置


./prepare

./install.sh


编辑客户机/etc/docker/daemon.json文件

{"insecure-registries":["192.168.100.204:80"]}

重启客户机docker服务

systemctl restart docker   #或者(service docker restart) 


推送镜像
docker login 172.16.188.182:8089

docker tag nginx:latest 172.16.188.182:8089/base/nginx:base
docker push 172.16.188.182:8089/base/nginx:base


https 问题解决
/etc/docker/daemon.json
{ "insecure-registries":["172.16.188.182:8089"] }


设置开机启动

cat > /lib/systemd/system/harbor.service << EOF
[Unit]
Description=Harbor
After=docker.service systemd-networkd.service systemd-resolved.service
Requires=docker.service
Documentation=http://github.com/vmware/harbor

[Service]
Type=simple
Restart=on-failure
RestartSec=5

#需要注意harbor的安装位置
ExecStart=/usr/bin/docker-compose -f  /data/harbor/docker-compose.yml up
ExecStop=/usr/bin/docker-compose -f /data/harbor/docker-compose.yml down

[Install]
WantedBy=multi-user.target
EOF

systemctl enable harbor #设置harbor开机自启
systemctl start harbor #启动harbor

