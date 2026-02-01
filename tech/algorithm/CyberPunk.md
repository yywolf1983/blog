# block

## 名人堂

Richard Matthew Stallman      GNU
Dennis MacAlistair Ritchie    C之父

Philip R. Zimmermann          GPG
Guido van Rossum              Python
Ryan Dahl                     Node.js

Nick Szabo                    数位货币
Gavin Wood                    ETH CTO  波卡
Satoshi Nakamoto              BTC

## ipfs-core

    kademlia      身份验证
    NAT webRTC    网络传输
    DHT           分布hash routing
    BitTorrent    BitSwap
    Merkle-DAG    数据对象
    Git           版本控制
    SFS，IPNS     命名绑定

## BTC core

    ECC
    Merkle
    P2P
    PoW
    LevelDB


## Bell Labs

    晶体管、
    激光器、
    太阳能电池、
    发光二极管、
    数字交换机、
    通信卫星、
    电子数字计算机、
    C语言、
    UNIX操作系统、
    蜂窝移动通信、
    长途电视传送、
    仿真语言、
    有声电影、
    立体声录音、
    通信网

### 胶片

   卤化银是卤素（氟、氯、溴、碘等）与银元素形成的盐（氟化银、氯化银、溴化银、碘化银等），这些盐具有相似的化学性质。 

### CryptoPunks

白皮书
eth btc

ERC20 token规范
ERC721  唯一性，不可分割
ERC1155
ERC3525
ERC9980

EIP-1154 预言机


词根词缀
多重签名
Dpos

智能合约(代码即法律)

pow 工作量证明  BTC
pos  参与证明     ETH2.0
poh 历史证明      solana

ERC-20,ERC-721,ERC-1155
defi 金融 dex 
nft 非同质化代币
gamefi 游戏
DAO 去中心化自治组织
     代码即法律
合作 共赢

BIP39 助记次
BIP32 分层
BIP44 数字编码

CEX
DEX
coin
token
稳定币


multisig P2SH

eth bsc Solana wax 
cardano
walletconnect
p2p ECC hash
paxos

Zero-Trust Network Access, ZTNA
schnorr 多签

DAT 算法
Merkle Tree（默克尔树）

ECDH bip151

主链 测链
波卡异构多链？

## btc 钱包

生成一个私钥在本质上在1到2^256之间选一个数字
实际过程需要比较下是否小于n-1（n = 1.158 * 10^77, 略小于2^256），我们就有了一个合适的私钥。否则，我们就用另一个随机数再重复一次。这样得到的私钥就可以根据上面的方法进一步生成公钥及地址。

BIP32

首先使用额外的 256 位熵扩展私钥和公钥。 这个扩展称为链码，由 32 个字节组成。 
我们将扩展私钥表示为 (k, c)，其中 k 是普通私钥，c 是链码。 扩展公钥表示为 (K, c)，其中 K = point(k)，c 是链码。 

BIP44 
    BIP43
        BIP32
    确定性钱包的多账户层次结构
    m / purpose' / coin_type' / account' / change / address_index

BIP39
先生成一个128位随机数，再加上对随机数做的校验4位，得到132位的一个数，然后按每11位做切分，这样就有了12个二进制数，然后用每个数去查BIP39定义的单词表，这样就得到12个助记词

助记词推导出种子
这个过程使用密钥拉伸（Key stretching）函数，被用来增强弱密钥的安全性，PBKDF2是常用的密钥拉伸算法中的一种。
PBKDF2基本原理是通过一个为随机函数(例如 HMAC 函数)，把助记词明文和盐值作为输入参数，然后重复进行运算最终产生生成一个更长的（512 位）密钥种子。这个种子再构建一个确定性钱包并派生出它的密钥。

密钥拉伸函数需要两个参数：助记词和盐。盐可以提高暴力破解的难度。 盐由常量字符串 "mnemonic" 及一个可选的密码组成，注意使用不同密码，则拉伸函数在使用同一个助记词的情况下会产生一个不同的种子

*** 重点 
    https://en.bitcoin.it/wiki/Secp256k1
    HMAC-sha256