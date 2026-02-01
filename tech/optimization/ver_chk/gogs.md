
gogs git 

ln -s /data/gogs /var/gogs

docker pull gogs/gogs:latest

docker run --name=gogs -d  -p 10022:22 -p 10080:3000 -v /var/gogs:/data/gogs gogs/gogs --restart=always

su - git -c "/data/gogs/gogs web" >> /dev/null 2>&1 &



version: '2.3'
services:
    gogs:
      image: gogs/gogs:latest
      restart: always
      ports:
        - "10022:22"
        - "10080:3000"
      volumes:
        - /data/gogs:/data


钩子设置

#!/bin/bash 

curl 47.108.235.230:8080


[server]
DOMAIN           = git.xingchenborui.com  #这里是域名
HTTP_PORT        = 3000  #这里是内网
EXTERNAL_URL     = http://git.xingchenborui.com/  #这里是外网访问url
DISABLE_SSH      = false
SSH_PORT         = 10022 #这里是外网
START_SSH_SERVER = false
OFFLINE_MODE     = false