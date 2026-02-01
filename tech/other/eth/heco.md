/root/heco-chain-1.2.1/build/bin/geth  console

ulimit -n 65535 
/data/heco/geth-linux-amd64 --datadir /data/heco/data --syncmode "fast" --cache=8096 --maxpeers 50 --http --http.addr=0.0.0.0 --http.port=8545 --http.api "web3,debug,personal,net,admin,eth" --http.corsdomain "*" --allow-insecure-unlock


./geth-linux-amd64 --datadir /data/heco/data --syncmode "full" --cache=8096 --maxpeers 50 --http --http.addr=0.0.0.0 --http.port=8545 --http.api "web3,debug,personal,net,admin,eth" --http.corsdomain "*" --allow-insecure-unlock

存活检查
curl -i -H "Content-Type: application/json" -X POST http://127.0.0.1:8545

(如果已经追上最新高度，result会返回false)

块高度
curl -H "Content-Type: application/json" -X POST --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' http://127.0.0.1:8545


查看同步大小
curl -s -H Content-Type:application/json -X POST --data '{"jsonrpc":"2.0","method":"eth_syncing","params":[],"id":1}' http://127.0.0.1:8545

gas费用
curl -H "Content-Type: application/json" -X POST --data '{"jsonrpc":"2.0","method":"eth_gasPrice","params":[],"id":73}' http://127.0.0.1:8545


curl -H "Content-Type: application/json" -X POST --data '{"jsonrpc":"2.0","method":"eth_accounts","params":[],"id":1}' http://127.0.0.1:8545


账户余额
curl -H "Content-Type: application/json" -X POST --data '{"jsonrpc":"2.0","method":"eth_getBalance","params":["0xa271429e1a5fb2dcfd14c44907ae024b951cb400", "latest"],"id":1}' http://127.0.0.1:8545

转账
curl -H Content-Type:application/json -X POST --data '{"jsonrpc":"2.0","method":"eth_sendTransaction", "params":[{"from":"0xb5ca2e8dcc6134bbdc7790d292e838e40c39ba39","to":"0xa271429e1a5fb2dcfd14c44907ae024b951cb400","gas":"0x5208","gasPrice":"0x1264c45600","value":"0xde0b6b3a7640000"}],"id":1}' http://127.0.0.1:8545

交易查询
curl -H Content-Type:application/json -X POST --data '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params":["0xe9296d312a937cdefc201a8fe80dbfa8a9c958ada9e863ddbb324804722f1de0"],"id":1}' http://127.0.0.1:8545

 转移数量
curl -H "Content-Type: application/json" -X POST --data '{"jsonrpc":"2.0","method":"eth_getTransactionCount","params":["0xb5ca2e8dcc6134bbdc7790d292e838e40c39ba39", "latest"],"id":1}' http://127.0.0.1:8545


根据高度获取信息
curl -H "Content-Type: application/json" -X POST --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["0x4fd", true],"id":1}' http://127.0.0.1:8545

查询交易数
curl -H Content-Type:application/json -X POST --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params":["0xc71d4e9e7f28ad43d9ad6cfb1824a8f3e756a01ab245bee49da843799a256f13"],"id":1}' http://127.0.0.1:8545

 根据高度查询交易
curl -H Content-Type:application/json -X POST --data '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByNumber","params":["0xe1b302"],"id":1}' http://127.0.0.1:8545

相关端口
8545
8546
30311 


bsc


https://github.com/bnb-chain/bsc/releases/download/v1.1.18/mainnet.zip

https://github.com/bnb-chain/bsc/releases/download/v1.1.18/geth_linux 


./geth_linux_bsc  --datadir data init genesis.json

https://docs.binance.org/smart-chain/developer/fullnode.html

ulimit -n 65535
./geth_linux_bsc --config ./config.toml --datadir /data/bscd/bsc/data --cache 56000 --rpc.allow-unprotected-txs --txlookuplimit 0 --syncmode light --allow-insecure-unlock --http --http.addr 0.0.0.0 --http.vhosts '*' --http.corsdomain '*' -ws --ws.addr 0.0.0.0 --ws.origins '*' --maxpeers=100 --rpc.gascap 0 --rpc.txfeecap 0

--syncmode want "full", "snap" or "light"
--diffsync 启用差异同步

snap 模式 要去掉  --snapshot=false

wget   $(curl -s https://api.github.com/repos/bnb-chain/bsc/releases/latest |grep browser_ |grep mainnet |cut -d\" -f4)
unzip mainnet.zip

data/bsc/geth_linux_bsc attach http://127.0.0.1:8645


> eth.syncing	#查看当前区块情况

> net.peerCount	#查看当前连接节点数量，结果为false为同步完成
> eth.blockNumber #当前同步到区块高度

> eth.getBlock(15091167) 




btc

./bitcoin-24.0.1/bin/bitcoind -datadir=/data/ceph/btc/data -conf=/data/ceph/btc/bitcoin.conf -daemon

./bitcoin-22.0/bin/bitcoin-cli -rpcuser=username -rpcconnect=x.x.x.x -rpcport=8332
 -rpcpassword=password getblockchaininfo


bitcoin-24.0.1/bin/bitcoin-cli -rpccookiefile="/data/ceph/btc/data/.cookie" getblockchaininfo

gettransaction
getindexinfo

./bitcoind -datadir=/data/btctest/data -testnet -server -daemon

cat <<EOF > bitcoin.conf
server=1

rpcuser=username
rpcpassword=password

listen=1
bind=0.0.0.0
port=8333
maxconnections=64
upnp=1

dbcache=64
par=2
checkblocks=24
checklevel=0

disablewallet=1

rpcbind=0.0.0.0
rpcport=8332
rpcallowip=0.0.0.0/0
EOF


## ord

btc 配置里加上 txindex=1
查看索引同步完
bitcoin-24.0.1/bin/bitcoin-cli -rpccookiefile="/data/ceph/btc/data/.cookie" getindexinfo

https://ordinals.com/
创建钱包
ord --wallet test --bitcoin-data-dir /data/ceph/btc/data wallet create
{
  "mnemonic": "able note cradle kite change adult little load hat opinion scorpion spell",
  "passphrase": ""
}


{
  "mnemonic": "control spirit almost that balance liberty donkey lamp benefit unable yard business",
  "passphrase": ""
}

铸造铭文
ord --wallet test1 --bitcoin-data-dir /data/ceph/btc/data --data-dir /data/ceph/btc/orddata wallet inscribe pic/ord.txt --fee-rate 8

https://mempool.space/zh/

ord --wallet <name> wallet 
```text
  create
  restore "BIP39 seed"  #导入地址
  receive #生成地址
  inscribe <file> --fee-rate <fee_rate>  #创建铭文
  inscriptions #查看铭文
  send --fee-rate <fee_rate> <address> <inscription_id>
  transactions  #查看交易
  balance  #查看余额
```

--fee-rate 设置费率



xmr
./monero-x86_64-linux-gnu-v0.18.1.2/monerod --config-file monerod.conf  --detach --zmq-pub tcp://127.0.0.1:18083 --disable-dns-checkpoints --enable-dns-blocklist

 --bootstrap-daemon-login admin:admin

https://github.com/monero-project/monero.git 

docker build -t xmrd

Volume:
/home/monero/.bitmonero
/wallet
prot
18080
18083

cat << EOF > Dockerfile
# runtime stage
FROM ubuntu:20.04

add p2pool /usr/local/bin/

ENTRYPOINT ["p2pool"]
CMD ["--host","127.0.0.1","--wallet","wallet"]
EOF

docker build . -t pool

./p2pool-v2.2.1-linux-x64/p2pool --host 127.0.0.1 --wallet wallet

./xmrig -o 127.0.0.1:3333

## 监控

dashboard template : 6976

sudo docker run -it -d -p 19090:9090 \
  -e "GETH=http://52.221.21.170:8645" \
  hunterlong/gethexporter

## 官方监控
--metrics --metrics.influxdb --metrics.influxdb.endpoint "http://0.0.0.0:8086" --metrics.influxdb.username "geth" --metrics.influxdb.password "chosenpassword"

dashboard template : 13877