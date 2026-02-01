1.参数说明
复制代码

ETHEREUM选项:
  --config value                        TOML 配置文件
  --datadir "/home/user4/.ethereum"  数据库和keystore密钥的数据目录
  --keystore                            keystore存放目录(默认在datadir内)
  --nousb                               禁用监控和管理USB硬件钱包
  --networkid value                     网络标识符(整型, 1=Frontier, 2=Morden (弃用), 3=Ropsten, 4=Rinkeby) (默认: 1)
  --testnet                             Ropsten网络:预配置的POW(proof-of-work)测试网络
  --rinkeby                             RRinkeby网络: 预配置的POA(proof-of-authority)测试网络
  --syncmode "fast"                     同步模式 ("fast", "full", or "light")
  --gcmode value                        区块链垃圾收集模式 ("full", "archive") (default: "full")
  --ethstats value                      上报ethstats service  URL (nodename:secret@host:port)
  --identity value                      自定义节点名
  --lightserv value                     允许LES请求时间最大百分比(0 – 90)(默认值:0)
  --lightpeers value                    最大LES client peers数量(默认值:100)
  --lightkdf                            在KDF强度消费时降低key-derivation RAM&CPU使用
  --whitelist value                     使用逗号分隔的块编号到hash的映射来执行(<number>=<hash>)

开发链选项:
  --dev               使用POA共识网络，默认预分配一个开发者账户并且会自动开启挖矿
  --dev.period value  开发者模式下挖矿周期 (0 = 仅在交易pending时进行挖矿) (默认: 0)

ETHASH选项:
  --ethash.cachedir                         ethash验证缓存目录(默认 = datadir目录内)
  --ethash.cachesinmem value                在内存保存的最近的ethash缓存个数  (每个缓存16MB ) (默认: 2)
  --ethash.cachesondisk value               在磁盘保存的最近的ethash缓存个数 (每个缓存16MB) (默认: 3)
  --ethash.dagdir "/home/user4/.ethash"  存ethash DAGs目录 (default = inside home folder)
  --ethash.dagsinmem value                  在内存保存的最近的ethash DAGs 个数 (每个1GB以上) (默认: 1)
  --ethash.dagsondisk value                 在磁盘保存的最近的ethash DAGs 个数 (每个1GB以上) (默认: 2)

交易池选项:
  --txpool.locals value        将逗号分隔的帐户视为局部变量(没有刷新，包含优先级)
  --txpool.nolocals            为本地提交交易禁用价格豁免
  --txpool.journal value       本地交易的磁盘日志：用于节点重启 (默认: "transactions.rlp")
  --txpool.rejournal value     重新生成本地交易日志的时间间隔 (默认: 1小时)
  --txpool.pricelimit value    加入交易池的最小的gas价格限制(默认: 1)
  --txpool.pricebump value     价格波动百分比（相对之前已有交易） (默认: 10)
  --txpool.accountslots value  每个帐户保证可执行的最少交易槽数量  (默认: 16)
  --txpool.globalslots value   所有帐户可执行的最大交易槽数量 (默认: 4096)
  --txpool.accountqueue value  每个帐户允许的最多非可执行交易槽数量 (默认: 64)
  --txpool.globalqueue value   所有帐户非可执行交易最大槽数量  (默认: 1024)
  --txpool.lifetime value      非可执行交易最大入队时间(默认: 3小时)

性能调优选项:
  --cache value            分配给内部缓存的内存的兆字节 (默认值为: 1024)
  --cache.database value   用于数据库io的缓存内存预留百分比 (default: 50)
  --cache.trie value       用于trie缓存的缓存内存预留百分比 (default: 25)
  --cache.gc value         用于trie修剪的缓存内存预留百分比 (default: 25)
  --trie-cache-gens value  需要保存在内存中的trie节点代数 (default: 120)

帐户选项:
  --unlock value    需解锁账户用逗号分隔
  --password value  用于非交互式密码输入的密码文件

API和控制台选项:
  --rpc                  启用HTTP-RPC服务器
  --rpcaddr value        HTTP-RPC服务器接口地址(默认值:"localhost")
  --rpcport value        HTTP-RPC服务器监听端口(默认值:8545)
  --rpcapi value         基于HTTP-RPC接口提供的API
  --ws                   启用WS-RPC服务器
  --wsaddr value         WWS-RPC服务器监听接口地址(default: "localhost")
  --wsport value         WS-RPC服务器监听端口(默认值:8546)
  --wsapi value          基于WS-RPC的接口提供的API
  --wsorigins value      websockets请求允许的源
  --ipcdisable           禁用IPC-RPC服务器（默认是打开的）
  --ipcpath              包含在datadir里的IPC socket/pipe文件名(转义过的显式路径)
  --rpccorsdomain value  允许跨域请求的逗号分隔域名列表(浏览器强制)
  --rpcvhosts value      接受请求的虚拟主机名的逗号分隔列表(服务器强制的)。接受“*”通配符.(default: "localhost")
  --jspath loadScript    JavaScript加载脚本的根路径 (default: ".")
  --exec value           执行JavaScript语句(需要结合console/attach命令一起使用)
  --preload value        预加载到控制台的逗号分隔的JavaScript文件列表

网络选项:
  --bootnodes value     用于P2P发现bootstrap的逗号分隔的enode url(为轻量级服务器设置v4+v5)
  --bootnodesv4 value   用于P2P v4发现bootstrap的逗号分隔的enode url(轻服务器, 全节点)
  --bootnodesv5 value   用于P2P v5发现bootstrap的逗号分隔的enode url(轻服务器, 轻节点)
  --port value          网卡监听端口(默认值:30303)
  --maxpeers value      最大的网络节点数量(如果设置为0，网络将被禁用)(默认值:25)
  --maxpendpeers value  最大尝试连接的数量(如果设置为0，则将使用默认值)(默认值:0)
  --nat value           NAT端口映射机制 (any|none|upnp|pmp|extip:<IP>)(default: "any")
  --nodiscover          禁用节点发现机制(手动添加节点)
  --v5disc              启用实验性的RLPx V5(Topic发现)机制
  --netrestrict value   限制对给定IP网络的网络通信(CIDR掩码)
  --nodekey value       P2P节点密钥文件
  --nodekeyhex value    十六进制的P2P节点密钥(用于测试)

矿工选项:
  --mine                         启动挖矿
  --miner.threads value          挖矿使用的CPU线程数量(默认值:0)
  --miner.notify value           逗号分隔的HTTP URL列表，用于通知新工作包
  --miner.gasprice "1000000000"  挖矿交易的最低gas价格
  --miner.gastarget value        被挖区块的目标gas的底层(default: 8000000)，即被记录的区块提供的gas要高于该值，否则不会被记录
  --miner.gaslimit value         被挖区块的目标gas的顶层(default: 8000000)，即被记录的区块提供的gas要低于该值，否则不会被记录
  --miner.etherbase value        挖矿奖励地址(默认=第一个创建的帐户)(default: "0")
  --miner.extradata value        矿工设置的额外块数据(default = client version)
  --miner.recommit value         重新创建正在挖的块的时间间隔(default: 3s)
  --miner.noverify               禁用远程密封验证

GAS价格选项:
  --gpoblocks value      用于检查gas价格的最近生成的块的个数 (default: 20)
  --gpopercentile value  建议的gas价格是一组最近的交易gas价格的该给定百分比的值(default: 60)

虚拟机选项:
  --vmdebug         记录VM及合约调试的有用信息
  --vm.evm value    外部EVM配置(默认=内置解释器)
  --vm.ewasm value  外部ewasm配置(默认=内置解释器)

日志和调试选项:
  --fakepow                 禁用proof-of-work验证
  --nocompaction            在导入后禁用db压缩
  --verbosity value         日志详细度:0=silent, 1=error, 2=warn, 3=info, 4=debug, 5=detail (default: 3)
  --vmodule value           每个模块详细度:以 <pattern>=<level>的逗号分隔列表 (比如 eth/*=6,p2p=5)
  --backtrace value         请求特定日志记录堆栈跟踪 (比如 "block.go:271")
  --debug                   带有调用站点位置(文件和行号)的日志消息
  --pprof                   启用pprof HTTP服务器
  --pprofaddr value         pprof HTTP服务器监听接口 (default: "127.0.0.1")
  --pprofport value         pprof HTTP服务器监听端口 (default: 6060)
  --memprofilerate value    按该给定频率打开memory profiling(default: 524288)
  --blockprofilerate value  按指定频率打开block profiling (default: 0)
  --cpuprofile value        将CPU profile写入指定文件
  --trace value             将execution trace写入指定文件

METRICS和状态选项:
  --metrics                          启用metrics标准收集和报告
  --metrics.influxdb                 启用metrics导出/推送到外部的InfluxDB数据库
  --metrics.influxdb.endpoint value  将metrics报告给InfluxDB数据库API端点(default: "http://localhost:8086")
  --metrics.influxdb.database value  将报告的metrics推送到的InfluxDB数据库的名称(default: "geth")
  --metrics.influxdb.username value  授权访问数据库的用户名 (default: "test")
  --metrics.influxdb.password value  授权访问数据库的密码 (default: "test")
  --metrics.influxdb.host.tag host   连接到所有测量值的InfluxDB数据库主机标记(default: "localhost")

WHISPER（实验）选项:
  --shh                       启用Whisper
  --shh.maxmessagesize value  可接受的最大的消息大小 (default: 1048576)
  --shh.pow value             可接受的最小的POW (default: 0.2)
  --shh.restrict-light        限制两个Whisper客户端之间的连接

弃用选项:
  --minerthreads value     用于挖矿的CPU线程数(已弃用,现在使用--miner.threads) (default: 0)
  --targetgaslimit value   被挖区块的目标gas底层(弃用, 现在使用--miner.gastarget) (default: 8000000)
  --gasprice "1000000000"  挖去交易的最小gas价格(弃用, 现在使用--miner.gasprice)
  --etherbase value        区块挖矿奖励的address(default = 第一个账户, 弃用, 现在使用--miner.etherbase) (default: "0")
  --extradata value        被矿工设置的区块额外数据(default = client version, 弃用, 现在使用 --miner.extradata)

其他选项:
  --override.constantinople value  手动指定constantinople分支区块，覆盖绑定设置 (default: 0)
  --help, -h                       显示帮助信息


版权:
   Copyright 2013-2018 The go-ethereum Authors

复制代码