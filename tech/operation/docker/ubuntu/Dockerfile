FROM ubuntu as build
run apt -y update
run apt -y install wget
run apt -y install make gcc
run apt -y install libjemalloc-dev openssl libssl-dev
copy redis.sh /redis.sh
run chmod +x /redis.sh
run bash -c /redis.sh
run apt -y remove make gcc libjemalloc-dev openssl libssl-dev

FROM ubuntu
COPY --from=build /redis-stable/src/redis-cli /usr/bin/redis-cli
run apt -y update
run apt -y install curl
run apt -y install iputils-ping
run apt -y install mysql-client
run apt -y install netcat
run apt -y install dnsutils
run apt -y install wget
run apt -y install vim
run apt -y install iproute2

RUN apt install -y openssh-server
RUN mkdir -p /var/run/sshd
RUN echo 'root:GApo+rUGU25Rc4' |chpasswd
RUN sed -i 's/^.*MaxSessions.*$/MaxSessions 2000/g' /etc/ssh/sshd_config
RUN sed -i 's/^.*MaxStartups.*$/MaxStartups 2000/g' /etc/ssh/sshd_config
RUN sed -i 's/^.*PermitRootLogin.*$/PermitRootLogin yes/g' /etc/ssh/sshd_config

run apt clean
run apt -y autoremove

run mkdir -p /root/.ssh/
run chmod 700 /root/.ssh/
ADD authorized_keys /root/.ssh/authorized_keys
run chmod 600 /root/.ssh/authorized_keys

EXPOSE 22

COPY run.sh /root/.ssh/run.sh
RUN chmod +x /root/.ssh/run.sh

ENTRYPOINT /root/.ssh/run.sh && tail -f /dev/null
