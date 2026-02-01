
#网络不通处理
pkill docker
iptables -t nat -F
ifconfig docker0 down
systemctl restart docker.service

#docker 文件清理
见：docker_log.sh

docker php 安装插件
docker-php-ext-install pdo pdo_mysq


apt update
apt install -y libwebp-dev libjpeg-dev libpng-dev libfreetype6-dev 
docker-php-ext-configure gd --with-webp-dir=/usr/include/webp --with-jpeg-dir=/usr/include --with-png-dir=/usr/include --with-freetype-dir=/usr/include/freetype2
docker-php-ext-install gd
php -m | grep gd

ALTER USER ‘native‘@‘localhost‘ IDENTIFIED WITH mysql_native_password


