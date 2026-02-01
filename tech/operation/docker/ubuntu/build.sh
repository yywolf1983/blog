#cat ~/.ssh/authorized_keys > authorized_keys
docker login -u admin -p Rrvc3wK9KBXiyHe http://3.1.119.56:8090
#docker build -t 3.1.119.56:8090/base/ubuntu:latest .
docker buildx build --platform linux/amd64 --load -t 3.1.119.56:8090/base/ubuntu:latest -f Dockerfile .
docker push 3.1.119.56:8090/base/ubuntu:latest
#docker rmi 3.1.119.56:8090/aws/ubuntu:latest
