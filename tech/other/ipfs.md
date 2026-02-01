ipfs

ipfs-update install

export IPFS_PATH=/data/ipfs

ipfs init

ipfs cat /ipfs/QmS4ustL54uo8FzR9455qaxZwuMiUhyvMcX9Ba8nUH4uVv/readme

ipfs daemon

查看连接
ipfs swarm peers

下载
ipfs cat /ipfs/your_hash > init.jpg

上传 每次更改重新添加
ipfs add init.jpg
ipfs add -r 添加目录

web
https://ipfs.arche.network/ipfs/Qmd5dsPyc8FzhY5ouMENAP3jahFKB6UKrscTN69Vu1nDAB
https://ipfsapi.arche.network/webui

查看当前版本
ipfs name resolve

重新上传 同时得到ipns地址
ipfs name publish USERCID
指定key
ipfs name publish USERCID -k ok

生成ipns 地址
ipfs name publish /ipfs/QmUvquVHsYZcD21LSvaPyD8eyLyNmxLcfgbwQVm69hHox1  -k yy

added QmV1QAp9tZpuA9jnu9w5DpRem1vAJvwAPvrvLdS6dYFy67 dao/index.html
added QmQTkgbFyaYddoBAGq4fUo4tZMAQEUNxKV63xpYrX2xgZg dao/nft.jpg
added QmefgdpMv5L2okhCkSbg9BR5iPUyJWErGiPFXaNEE3eG9W dao/yy
added QmVDDj1CZE5db1U4Mgv7Hq8L7kS2rYnPKgyMrPTsPJEyJC dao

本地查看ipns
http://k51qzi5uqu5dge5fevbzzbkdli32v8nw05smee7858s4u17w2ku4wlcj5naabb.ipns.localhost:8080/

https://ipfs.arche.network/ipns/k51qzi5uqu5dge5fevbzzbkdli32v8nw05smee7858s4u17w2ku4wlcj5naabb

新建key
ipfs key gen KEYNANME

ipfs key list -l

导出key
ipfs key export ok -o ok

倒入
ipfs key import ok ok

修改配置
ipfs config Addresses.Gateway /ip4/0.0.0.0/tcp/8080
ipfs config Addresses.API /ip4/0.0.0.0/tcp/5001


允许跨域
ipfs config --json API.HTTPHeaders.Access-Control-Allow-Origin '["http://13.214.254.61:5001"]'
ipfs config --json API.HTTPHeaders.Access-Control-Allow-Methods '["PUT", "POST"]'

下载文件
ipfs get /ipns/


dns txt

dnslink=/ipns/k51qzi5uqu5dktqjw8varl8cf6cbz9agjzu1aiimnwhuj650dadx3cvv9s0pw5/