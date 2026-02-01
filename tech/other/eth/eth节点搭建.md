yum install golang
go version

yum install git
git version

yum install http://opensource.wandisco.com/centos/7/git/x86_64/wandisco-git-release-7-2.noarch.rpm
yum install git

git clone https://github.com/ethereum/go-ethereum.git
cd go-ethereum/
make all

export PATH=$PATH:/data/soft/go-ethereum/build/bin


geth version

geth init ./genesis.json --datadir /data/ethdata

geth --syncmode "fast" --datadir /data/ethdata --cache 4096 --rpc --http.corsdomain "*" --rpcport 6666 --rpcaddr 0.0.0.0   --ws --ws.addr 0.0.0.0 --ws.port 6667 --ws.origins "*"

监控同步
geth attach /data/ethdata/geth.ipc
eth.syncing   当curentBlock和highestBlock一致时，就表示区块同步成功了。
eth.blockNumber
net.peerCount
admin

windows连接
geth attach \\.\pipe\geth.ipc

迫不得已 重新同步
geth removedb --datadir /data/ethdata

#!/bin/sh
pid=`ps -ef|grep geth|grep -v grep|awk '{print $2}'`
echo $pid
kill -INT $pid

--datadir "xxxx" 指定数据目录，用来存放区块链数据，状态数据，keystore数据等。如果不加这个参数这些数据在不同的系统会放到不同的位置。这个目录占用空间是比较大的，我一般会指定一个目录，并保证这个目录所在分区有足够的磁盘空间。
--cache value 分配给内部缓存的内存MB数量，默认为 128，最后设置大一点儿，起码 1024吧，这个值设大一些可以提高数据同步效率。

--rpc                       启用HTTP-RPC服务器
--rpcaddr value             HTTP-RPC服务器接口地址(默认值:“localhost”)，默认只允许本地连接，设置为 0.0.0.0 可以接收任何地址发来的连接请求
--rpcport value             HTTP-RPC服务器监听端口(默认值:8545)，可以改为不同的端口

--ws                        启用WS-RPC服务器，几乎所有第三方节点都不启动这个服务，而要监听以太坊事件又必须启动这个服务
--wsaddr value              WS-RPC服务器监听接口地址(默认值:“localhost”)
--wsport value              WS-RPC服务器监听端口(默认值:8546)


geth attach 访问节点

# 创建账户
personal.newAccount()

# 解锁账户
personal.unlockAccount()
# 解锁账户，指定解锁具体账户
personal.unlockAccount(eth.accounts[0])

# 列出系统中的账户
eth.accounts

# 1、查看账户余额,返回值的单位是 Wei (“ ”里面是自己管理的账户地址)
eth.getBalance()
# 2、查看账户余额,返回值的单位是 Wei (“ ”里面是自己管理的账户地址)
eth.getBalance("写上账户地址")
# 3、转换为单位ether,便于阅读
web3.fromWei(eth.getBalance("写上账户地址"),'ether')
# 4、如果是在里面创建的账户可以调用内部函数拿到地址，不用每次都复制地址。
eth.getBalance(eth.accounts[0])
web3.fromWei(eth.getBalance(eth.accounts[0]),'ether')

#发起交易（发起方需要是自己管理的账户，其次需要先解锁账户），from：发起交易的地址；to:接受交易的地址
eth.sendTransaction({from:eth.accounts[0],to:"接受交易的地址",value:100000})

# 列出当前区块高度
eth.blockNumber

# 获取交易信息
eth.getTransaction()

# 获取区块信息
eth.getBlock()

# 开始挖矿
miner.start()
# 表示一直挖矿
miner.start(1)
# 查看
eth.coinbase

# 停止挖矿
miner.stop()
# 开始挖矿,当挖到一个块时就停止，
miner.start(1);admin.sleepBlocks(1);miner.stop()
 
# Wei 换算成以太币
web3.fromWei()

# 以太币换算成 Wei
web3.toWei()

# 交易油中的状态
bxpool.status


创建集群
admin.nodeInfo.enode
admin.addPeer("enode://....")


## 验证节点搭建 共识层

docker run sigp/lighthouse lighthouse --version

docker run -p 9990:9000/tcp -p 9990:9000/udp -p 127.0.0.1:5052:5052 -v $(pwd)/lighthouse:/root/.lighthouse sigp/lighthouse lighthouse --network prater beacon --http --http-address 0.0.0.0

生成钱包
docker exec -it nostalgic_darwin lighthouse --network prater account wallet create --name wally --password-file wally.pass

创建验证器
docker exec -it nostalgic_darwin lighthouse --network prater account validator create --wallet-name wally --wallet-password wally.pass --count 1

--network mainnet  使用正式网

从 staking 导入
下载钱包生成器

https://github.com/ethereum/staking-deposit-cli/releases

./deposit new-mnemonic --chain prater

monkey novel note grid tower salmon human sad clip service food suit ready story shield cattle example napkin brass second audit squeeze such urban

docker exec -it nostalgic_darwin lighthouse --network prater account validator import --directory /root/.lighthouse/prater/validator_keys

- Public key: 0x8adf6d378ba3ae8749f6c4aaa749661f8d2a9777eb223e7c8fb4c9700280720d4f4d2acee7e099b75072512287ee0503
- UUID: 203cb14e-2325-4fe2-98e7-746cd05c4505


docker exec -it nostalgic_darwin lighthouse --network prater vc

docker exec -it nostalgic_darwin lighthouse --network prater bn --checkpoint-sync-url http://127.0.0.1:5052

docker exec -it nostalgic_darwin lighthouse --network prater bn --staking --validator-monitor-auto

docker exec -it nostalgic_darwin lighthouse --network prater account wallet recover --name validators