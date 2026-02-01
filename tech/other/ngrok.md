yum -y install zlib-devel openssl-devel perl hg cpio expat-devel gettext-devel curl curl-devel perl-ExtUtils-MakeMaker hg wget gcc gcc-c++ git

//请下载合适自己的go语言包  我是centos 6.8 64位 所以选择以下包
wget https://dl.google.com/go/go1.13.5.linux-amd64.tar.gz
tar -C /usr/local -xvf go1.13.5.linux-amd64.tar.gz

cat >> /etc/profile << EOF
export PATH=\$PATH:/usr/local/go/bin
EOF

//检测是否安装成功go
source /etc/profile
go version

mkdir -p /data/ngrok
cd /data/ngrok
git clone https://github.com/inconshreveable/ngrok.git

生成证书
cd /data/ngrok
mkdir -p cert
cd cert

export NGROK_DOMAIN="nones.top"
openssl genrsa -out rootCA.key 2048
openssl req -x509 -new -nodes -key rootCA.key -subj "/CN=$NGROK_DOMAIN" -days 5000 -out rootCA.pem

openssl genrsa -out server.key 2048
openssl req -new -key server.key -subj "/CN=$NGROK_DOMAIN" -out server.csr
openssl x509 -req -in server.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out server.crt -days 5000

#证书编译时会使用
yes | cp rootCA.pem ../assets/client/tls/ngrokroot.crt
yes | cp server.crt ../assets/server/tls/snakeoil.crt
yes | cp server.key ../assets/server/tls/snakeoil.key


编译生成ngrok
go env //查看环境
GOOS=linux GOARCH=amd64 make release-server
GOOS=linux GOARCH=amd64 make release-client 
GOOS=windows GOARCH=amd64 make release-client 




cd /ngrok/ngrok
setsid ./bin/ngrokd -tlsKey="assets/server/tls/snakeoil.key" -tlsCrt="assets/server/tls/snakeoil.crt" -domain="nones.top"  -httpAddr=":8080" -httpsAddr=":8443" -tunnelAddr=":8083"

# 使用免费证书
但编译前要拷贝证书过来
[b]客户端用证书[/b]
cp /etc/letsencrypt/live/nones.top/chain.pem /data/ngrok/assets/client/tls/ngrokroot.crt 

[b]服务器端用证书[/b]
cp /etc/letsencrypt/live/nones.top/cert.pem /data/ngrok/assets/server/tls/snakeoil.crt
cp /etc/letsencrypt/live/nones.top/privkey.pem assets/server/tls/snakeoil.key

setsid /data/ngrok/bin/ngrokd -tlsKey="/etc/letsencrypt/live/nones.top/privkey.pem" -tlsCrt="/etc/letsencrypt/live/nones.top/fullchain.pem" -domain="nones.top"  -httpAddr=":8080" -httpsAddr=":8443" -tunnelAddr=":8083" -log=ngrokd.log


复杂配置ngrok.cfg
web_addr: 192.168.1.22:4040
authtoken: ---- autkkey ----
console_ui: false
log: /data/ngrok/ngrok.log

tunnels:
  http8003:
    proto: http
    addr: 8003

  #http2822:
  #  proto: http
  #  addr: 2822

  ssh22:
    proto: tcp
    addr: 22369

./ngrok start -config=ngrok.conf web  #启动web服务

./ngrok start -config=ngrok.conf web tcp  #同时启动两个服务
./ngrok start -config=ngrok.conf --all  #启动所有服务


//出现以下内容表示成功链接：
ngrok

Tunnel Status                 online
Version                       1.7/1.7
Forwarding                    http://test.myngrok.com:8081 -> 127.0.0.1:80
Forwarding                    https://test.myngrok.com:8081 -> 127.0.0.1:80
Web Interface                 127.0.0.1:4040
# Conn                        0
Avg Conn Time                 0.00ms


编译生成win64位客户端（其他自行编译测试）
GOOS=windows GOARCH=amd64 make release-client
#编译成功后会在ngrok/bin/下面生成一个windows_amd64目录下面有ngrok.exe
#Linux 平台 32 位系统：GOOS=linux GOARCH=386
#Linux 平台 64 位系统：GOOS=linux GOARCH=amd64
#Windows 平台 32 位系统：GOOS=windows GOARCH=386
#Windows 平台 64 位系统：GOOS=windows GOARCH=amd64
#MAC 平台 32 位系统：GOOS=darwin GOARCH=386
#MAC 平台 64 位系统：GOOS=darwin GOARCH=amd64
#ARM 平台：GOOS=linux GOARCH=arm
