export DOCKER_PATH="/Users/yy/docker"
export nginx_port=80

mkdir -p ${DOCKER_PATH}/nginx/
mkdir -p ${DOCKER_PATH}/nginx/conf.d/
cp nginx.conf ${DOCKER_PATH}/nginx/
cp default.conf ${DOCKER_PATH}/nginx/conf.d/
/usr/local/bin/docker-compose -f nginx.yml up -d
