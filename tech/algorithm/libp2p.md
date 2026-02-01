# p2p to rust

网络地址转换 (NAT)
 Kademlia DHT

## 基础协议 
https://github.com/libp2p/specs/

## core 抽象

### 寻址

/ip4/127.0.0.1/tcp/5002/p2p/QmdPU7PfRyKehdrP5A3WqmjyD6bhVpU1mLGKppa2FjGDjZ/p2p-circuit/p2p/QmVT6GYwjeeAF5TR485Yc58S3xRF5EFsZ5YAF4VcP3URHt

### 建立连接

消息编码
https://en.bitcoinwiki.org/wiki/Base58#Alphabet_Base58

### peer ID 和密钥 

ipns 
发布订阅消息
SECIO握手

密钥类型
    RSA
    Ed25519
    Secp256k1
    ECDSA

## 规范

 https://github.com/libp2p/specs/

### ping

    默认发送32个随机字节 服务器响应相同字节。 客户端测量 RTT 时间。

   RTT 来回通信延迟（Round-trip delay time），在双方通信中，发讯方的信号（Signal）传播（Propagation）到收讯方的时间（意即：传播延迟（Propagation delay）），加上收讯方回传消息到发讯方的时间 。

### NAT发现

    发送消息给中继，中继回应多个节点列表，然后等待对方回拨。以确认是不是在NAT后。

### identify  识别

ipfs/id/1.0.0

### Kademlia DHT

BitTorrent DHT 

对等路由
值存储和检索
内容提供广播和发现 

https://en.wikipedia.org/wiki/Kademlia

### mDNS

TXT dnslink=/ipns/k51qz..

### mplex 多路复用

https://github.com/maxogden/multiplex

### noise 安全握手 

 Diffie-Hellman 密钥交换

### 明文传输

### 密钥共享

AES-CTR，Salsa20

### pub/sub 消息传递系统

https://github.com/libp2p/research-pubsub 
https://github.com/libp2p/pubsub-notes 

gossipsub

### TURN 中继网络

全称为Traversal Using Relay NAT

### Rendezvous 

### SECIO 安全
协议弃用 被tls替代
libp2p 的流安全传输。 SECIO 包装的流使用安全 会话来加密所有流量。

### TLS 

使用TLS 1.3

### WebRTC
### WebTransport