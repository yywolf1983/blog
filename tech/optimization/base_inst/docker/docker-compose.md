pip install docker-compose

默认文件
docker-compose.yml
version: '3.7'
services:
  web:
    build: ./web/
    image: harbor.usda.one/aws/myredis
    ports:
     - "5000:5000"

  redis:
   # 指定镜像
   container_name: redis-1
   image: redis:5.0.5
   restart: always
   environment:
     - REDIS_DIR=/data/redis
     - TZ=Asia/Shanghai
   ports:
     # 端口映射
     - 6379:6379
   volumes:
     # 目录映射 从外向内
     - "/data/redis/conf:/data/conf"
     - "/data/redis/:/data/"
     - /etc/localtime:/etc/localtime:ro
   command:
     # 执行的命令
     redis-server

   networks:
    - host


$ docker-compose -f server.yml up -d
$ docker-compose build
$ docker-compose push