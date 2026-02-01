
# 1. docker in docker

sudo ln -s /Users/yy/.docker/run/docker.sock /var/run/docker.sock

docker run -d -it --privileged --name my-docker \
-v /var/run/docker.sock:/Users/yy/.docker/run/docker.sock \
docker

docker exec -it my-docker sh

docker run -d --name my-nginx nginx 



# 用docker 管理docker

cat Dockerfile
FROM alpine:latest
RUN apk add --no-cache docker

docker run -d -it --privileged --name docker-cli-st \
-v /var/run/docker.sock:/var/run/docker.sock \
docker-cli

docker exec -it docker-cli-st sh