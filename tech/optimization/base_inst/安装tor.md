
yum -y install libevent  libevent-devel automake

groupadd test
useradd -g test test

./configure --prefix=/data/tor
make && make install
cp  /data/tor/etc/tor/torrc.sample  /data/tor/etc/tor/torrc

生成私钥
ssh-keygen -t rsa -b 4096  -f private_key

bin/tor --runasdaemon 0  -f etc/tor/torrc --verify-config

Log notice file /data/tor/notices.log
Log debug file /data/tor/debug.log

DataDirectory /data/tc/tordata

HiddenServiceDir /data/tc/hidden_service/
HiddenServicePort 80 127.0.0.1:80

HiddenServiceDir /data/tc/config/
HiddenServicePort 80 127.0.0.1:80

systemctl start tor

默认路径
/var/lib/tor/hidden_service/hostname

生成认证证书
bin/tor --keygen --DataDirectory hidden
  ./tor --SigningKeyLifetime "365 days"