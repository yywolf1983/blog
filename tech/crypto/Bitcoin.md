## btc

UTXO 未花费交易输出

hash

数字签名

双花问题
timestamp server
block timestamp

POW HashCash
最长链原则 6次确认
51%攻击 ( 女巫攻击 )

### P2SH (Pay-to-Script-Hash)


### 私钥 

256位随机数字
n=1.158 * 10^77，略小于2^256
dumpprivkey命令会把私钥以Base58校验和编码格式显示，这种私钥格式被称为（WIF，Wallet Import Format）

### 公钥

通过椭圆曲线算法可以从私钥计算得到公钥
secp256k1

由公钥生成比特币地址时使用的算法是Secure Hash Algorithm (SHA)和the RACE Integrity Primitives Evaluation Message Digest (RIPEMD)，特别是SHA256和RIPEMD160。

K是公钥，A是生成的比特币地址
A = RIPEMD160(SHA256(K))
得到一个长度为160比特（20字节）的数字
通常用户见到的比特币地址是经过“Base58Check”编码的

K->sha256->RIPEMD160->Base58Check->钱包地址

RIPEMD160 一种hash算法

### bip32

root seed (128->256)位 -> HMAC-SHA512 -> master key(left 256) +  master Chain code (right 256)

母私钥 + 母链码 + 索引号 -> HMAC-SHA512 -> left 256 + right 256

左半部分256位散列以及索引码被加载在母私钥上来衍生子私钥

### bip44
m / purpose' / coin_type' / account' / change / address_index

目前有三种货币被定义：Bitcoin is m/44'/0'、Bitcoin Testnet is m/44'/1'，以及Litecoin is m/44'/2'。

### bip39

要通过助记词创建一个二进制种子，我们使用助记符作为密码（UTF-8 NFKD）和字符串“mnemonic”+ passphrase 作为盐（再次以UTF-8 NFKD）来调用PBKDF2函数。迭代计数设置为2048，HMAC-SHA512用作伪随机函数。派生密钥的长度为512位（= 64字节）。
hashlib.pbkdf2_hmac("sha512", b"asd", b"dsa1", 2048).hex() WIF-compressed 生成种子 

wif: 在生成的hex 头上加上 0x80 在进行5次 sha256循环  在用base58 编码

## 导入导出钱包 密钥管理
walletpassphrase password timeout
dumpwallet test  导出钱包密钥

importprivkey prv false 不扫描导入

sethdseed true "hdprv"

主密钥（ extended private masterkey）
搜索hdseed=1 为的哪一行，为钱包的密语种子
树状层级推导 (hierarchical deterministic) 简称 HD

获取钱包信息
getwalletinfo

获取余额
getbalance

### python 生成

生成私钥(生成的密钥受加盐和循环次数的限制而不同)
import hashlib
x = hashlib.pbkdf2_hmac("sha256", b"bittest", b"bittest", 4096).hex()
import btcwif
wif = btcwif.privToWif(x)
wif

还原成 sha256
priv1 = btcwif.wifToPriv(wif)

检查
btcwif.wifChecksum(wif)


## 编译钱包

./install_db4.sh ./
libboost1.71-all-dev
export BDB_PREFIX='/data/bitcoin/contrib/db4'

sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools

./configure BDB_LIBS="-L${BDB_PREFIX}/lib -ldb_cxx-4.8" BDB_CFLAGS="-I${BDB_PREFIX}/include" --prefix=/data/bitcoin --with-gui=qt5

## 手机钱包备份修复

https://github.com/bitcoin-wallet/bitcoin-wallet/blob/master/wallet/README.recover.md

https://github.com/bitcoinj/bitcoinj.git
gradle bitcoinj-wallettool:installDist

openssl enc -d -aes-256-cbc -md md5 -a -in bitcoin-wallet-backup-testnet-2014-11-01 > bitcoin-wallet-decrypted-backup
./wallet-tool dump --wallet=/tmp/bitcoin-wallet-decrypted-backup --dump-privkeys --password=123456