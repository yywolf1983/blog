cd /etc/docker

#生成一个私钥用aes加密
openssl genrsa -aes256 -passout pass:passwd  -out ca-key.pem 2048

#生成CA公钥
openssl req -new -x509 -days 365 -key ca-key.pem -passin pass:passwd -sha256 -out ca.pem -subj "/C=NL/ST=./L=./O=./CN=."

#生成服务器私钥
openssl genrsa -out server-key.pem 2048

#生成服务器证书生成文件
openssl req -subj "/CN=10.168.4.187" -new -key server-key.pem -out server.csr

#用 CA公钥 ca.pem CA私钥 ca-key.pem 生成服务器公钥
openssl x509 -req -days 365 -in server.csr -CA ca.pem -CAkey ca-key.pem -passin "pass:passwd" -CAcreateserial -out server-cert.pem

#建立一个客户端私钥
openssl genrsa -out key.pem 2048

#创建客户端证书的申请文件
openssl req -subj '/CN=client' -new -key key.pem -out client.csr

sh -c 'echo "extendedKeyUsage=clientAuth" > extfile.cnf'

#生成证书文件
openssl x509 -req -days 365 -in client.csr -CA ca.pem -CAkey ca-key.pem -passin "pass:passwd" -CAcreateserial -out cert.pem -extfile extfile.cnf

chmod 0400 ca-key.pem key.pem server-key.pem
chmod 0444 ca.pem server-cert.pem cert.pem

vi /lib/systemd/system/docker.service

启动时候添加
--tlsverify \
--tlscacert=/etc/docker/ca.pem \
--tlscert=/etc/docker/server-cert.pem \
--tlskey=/etc/docker/server-key.pem \
-H 0.0.0.0:2375

systemctl daemon-reload
systemctl restart docker

docker -H 10.168.4.187:2375 --tls --tlscacert=/etc/docker/ca.pem --tlscert=/etc/docker/cert.pem --tlskey=/etc/docker/key.pem info

查看证书信息
openssl x509 -in cert.pem -inform pem -noout -text

-new    :说明生成证书请求文件
-x509   :说明生成自签名证书
-key    :指定已有的秘钥文件生成秘钥请求，只与生成证书请求选项-new配合。
