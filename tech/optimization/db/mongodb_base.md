


mongodb 基础

  yywolf1983 发表于 2013-07-30 11:52:58  删除     编辑  

文件存储格式为BSON（一种JSON 的扩展)
在32位平台MongoDB不允许数据库文件（累计总和）超过2G，而64位平台没有这个限制


预留机制  下一个文件是上一个文件的2倍用0填充 最大2G
空间元素 都存储在ns中  table.1 table.2 table.3 存储信息



将启动脚本写入 rc.local 随系统启动
mongod --dbpath=/db --logpath=/log.log  --fork  
windows 下 用   --install  启动服务
mongo  进入系统

--auth   启动验证


dbpath:  数据文件存放路径，每个数据库会在其中创建一个子目录，用于防止同一个实例多次运行的mongod.lock也保存在此目录中。
logpath  错误日志文件
logappend  错误日志采用追加模式（默认是覆写模式）
bind_ip  对外服务的绑定ip，一般设置为空，及绑定在本机所有可用ip  
port  对外服务端口。Web管理端口在这个port的基础上+1000
fork  以后台Daemon形式运行服务
journal  开启日志功能，通过保存操作日志来降低单机故障的恢复时间，在1.8版本后正式加入，取代在1.7.5版本中的dur参数。
syncdelay  系统同步刷新磁盘的时间，单位为秒，默认是60秒。
directoryperdb  每个db存放在单独的目录中，建议设置该参数。与MySQL的独立表空间类似
maxConns   最大连接数
repairpath   执行repair时的临时目录。在如果没有开启journal，异常down机后重启，必须执行repair操作

vi mongodb.cnf
dbpath=/data/db/
mongod -f mongodb.cnf
mongod --config mongodb.cnf

http://localhost:27017
http://localhost:28017  查看运行信息  打开的端口 加1000 就是运行信息http端口

scons --prefix=/yy/www/mongodb install
scons --prefix=/yy/www/mongodb -full install  包含lib头

绑定登录ip
./mongod --bind_ip 192.168.1.103


use admin
db.shutdownServer()  停掉数据库

kill -2 19269   杀掉数据库
kill -9 12345   又可能损坏数据

还要解释这个吗？
--port 28018

启用验证
./mongod --auth

use admin

db.createUser({
    user:"admin",
    pwd:"admin",
    roles:[{
        role:"root",
        db:"admin"
    }]
})

db.auth("admin", "admin")

mongodb 默认打开的是 test库 要全局登录必须指定admin库
mongodb admin -u root -p

建立用户  要在admin 库中建立为所有库的权限
db.addUser("root","111")
db.auth("root","111")
1

建立管理员用户后 以后操作必须先用管理员登录

查看用户
db.system.users.find()
建立只读用户
db.addUser("root","root",true)

删除用户
use dbname
db.system.users.remove({user:"root"})
db.system.users.find()

登录后验证
db.auth('admin','admin');

./mongo -u root -p

运行状态
db.serverStatus()

数据库状态
db.stats

mongod -f  abc.cnf 读取配置文件

use admin
db.shutdownServer() 关闭服务

添加两条数据
> j = {name:"yywolf1983"}
{ "name" : "yywolf1983" }
> t = {age : "28"}
{ "age" : "28" }
> db.things.save(j);
> db.things.save(t);
> db.things.find();
{ "_id" : ObjectId("4e4120555b57c694a25d6ae8"), "name" : "yywolf1983" }
{ "_id" : ObjectId("4e41205e5b57c694a25d6ae9"), "age" : "28" }


这条不用解释了！
for(var i=1;i<10;i++)db.a.save({x:4,j:i});db.a.find();

it  继续显示未显示项目

查询
db.things.find({name:"mongo"})   条件查询
db.things.find().limit(3);  显示指定条数


游标
var cursor=db.a.find();  建立游标
next();    显示下一条
hasNext();   查询是否还有下一条

显示指定条数
> var cu=db.a.find();
> printjson(cu[4])
{ "_id" : ObjectId("4eefde75e2c37a820278e9a2"), "x" : 4, "j" : 5 }

> cu[4]
{ "_id" : ObjectId("4eefde75e2c37a820278e9a2"), "x" : 4, "j" : 5 }


插入
db.a.insert({"_id":3,"name":"yy","age":55})

更新
db.things.update({name:"mongo"},{$set:{name:"mongo_new"}});
db.a.update({_id:ObjectId("4eefdf11e2c37a820278e9a7")},{$set:{j:100}})

删除
db.things.remove({name:"mongo_new"});

bsondump: 将 bson 格式的文件转储为 json 格式的数据
mongo: 客户端命令行工具,其实也是一个 js 解释器,支持 js 语法
mongod: 数据库服务端,每个实例启动一个进程,可以 fork 为后台运行
mongodump/ mongorestore: 数据库备份和恢复工具
mongoexport/ mongoimport: 数据导出和导入工具
mongofiles: GridFS 管理工具,可实现二制文件的存取
mongos: 分片路由,如果使用了 sharding 功能,则应用程序连接的是 mongos 而不是
mongod
mongosniff: 这一工具的作用类似于 tcpdump,
不同的是他只监控 MongoDB 相关的包请
求,并且是以指定的可读性的形式输出
mongostat: 实时性能监控工具
insert:  每秒插入量
query: 每秒查询量
update: 每秒更新量
delete: 每秒删除量
locked:  锁定量
qr | qw: 客户端查询排队长度(读|写)
ar | aw: 活跃客户端量(读|写)
conn: 连接数
time:  当前时间



高级查询
db.collection.find({ "field" : { $gt: value } } ); // 大于: field > value
db.collection.find({ "field" : { $lt: value } } ); // 小于: field < value
db.collection.find({ "field" : { $gte: value } } ); // 大于等于: field >= value
db.collection.find({ "field" : { $lte: value } } ); // 小于等于: field <= value
db.collection.find({ "field" : { $ne: value } } ); // 不等于: field <> value

多条件查询
db.a.find({j:{$gt:2,$lt:5,$ne:3}})

匹配所有  满足所有条件
db.users.find({age : {$all : [6, 8]}});

判断字段是否存在
db.a.find({x:{$exists:false}})  不存在
db.a.find({x:{$exists:true}})   存在

条件查询 $in 包含  $nin不包含 注意中括号
db.c2.find({age:{"$in":[null], "$exists":true}})
db.a.find({j:{$in:[6,1]}})

不显示正则匹配的值
db.c1.find({name: {$not: /^T.*/}});

取模运算  不是很明白*******************************
db.a.find({j:{$mod:[6,1]}})

查询跳过前10条 显示5条 总共多少条
db.users.find().skip(10).limit(5).count();

以年龄升序 asc
db.users.find().sort({age: 1});
以年龄降序 desc
db.users.find().sort({age: -1});

游标处理
for( var c = db.a.find(); c.hasNext(); ) { printjson(c.next()); };
for( var c = db.a.find(); c.find({j:10}); ) { printjson(c.next()); };

存储过程
db.system.js.save({_id:"addNumbers", value:function(x, y){ return x + y; }});
db.system.js.find()
db.eval('addNumbers(3, 4.2)');
db.system.js.remove({_id:"addNumbers"})

show dbs;
show tables;
use myTest   建立或打开一个库

删除一个库
use abc
db.dropDatabase();
db.abc.drop()  删除一个表

设置查看 capped collections
db.createCollection("mycoll", {capped:true, size:100000, max:100});   
db.mycoll.validate();   

操作 GridFS
mongofiles put testfile   将文件写入库
mongofiles list  查看
mongofiles get testfile   取出文件
mongofiles delete testfile   删除文件

> show collections  查看fs
fs.chunks 存储内容
fs.files  存储编号

db.fs.files.find()
db.fs.chunks.find()  查看文件实际内容

************* 跳过 MapReduce *********************



导入导出
db.students.insert({classid:1, age:14, name:'Tom'})

导出 test库中的 学生表 到 user.dat
mongoexport -d test -c students -o user.dat
导入
mongoimport -d test -c user user.dat

把指定导出到cvs
mongoexport  -d test  -c  students --csv  -f  name,age  -o  user_csv.dat
导入cvs  --headerline 不导入第一行
mongoimport -d test -c user --type csv --headerline --file user_c

备份恢复
mongodump -d my_db -o abc 备份  -d 指定备份库 -o 指定备份目录
mongorestore -d abc dump/*
mongorestore –drop -d abc dump/*   删除原先库 再恢复

NAMEDATE=`date +%F_%H-%M_%s`_`whoami` && echo $NAMEDATE
docker exec rocketchat-mongo-1 sh -c "mongodump -d rocketchat --gzip -o /data/$NAMEDATE" && echo "Database Dumped"

docker exec -it rocketchat-mongo-1 bash
mongorestore --gzip --drop /dump


在字段j上创建索引，1(升序);-1(降序)
db.a.ensureIndex({j:1})
db.a.ensureIndex({j:1} , {backgroud:true})   后台创建索引
db.a.getIndexes();

组合索引
db.factories.ensureIndex( { "addr.city" : 1, "addr.state" : 1 } );

唯一索引
db.t4.ensureIndex({firstname: 1, lastname: 1}, {unique: true});

强制使用索引
db.a.find({j:{$lt:3}}).explain();

db.t3.dropIndexes() 删除索引


开启  Profiling  
mongod–profile=级别
或者
db.setProfilingLevel(2);
0 – 不开启
1 – 记录慢命令  (默认为>100ms)
2 – 记录所有命令

mongod -profile=级别 –slowms=级别
相当于
db.setProfilingLevel( 1 , 10 );

查询 profiling 记录
db.system.profile.find( { millis : { $gt : 5 } } )
查看最新的  Profile  记录：
db.system.profile.find().sort({$natural:-1}).limit(1)
获得消息字段说明
ts：  该命令在何时执行
info:  本命令的详细信息
reslen: 返回结果集的大小
nscanned: 本次查询扫描的记录数
nreturned: 本次查询实际返回的结果集
millis: 该命令执行耗时，以毫秒记


集群配置  Replica Sets
--replSet rs1
mkdir -p /data/key
echo "this is rs1 super secret key" > /data/key/r0
echo "this is rs1 super secret key" > /data/key/r1
echo "this is rs1 super secret key" > /data/key/r2
chmod 600 /data/key/r*

首先建立3个是为了投票不会冲突，当服务器为偶数时可能会导致无法正常选举出主服务器
mongod --replSet rs1 --keyFile /data/key/r0 --fork --port 28010 --dbpath /data/data/r0 --logpath=/data/log/r0.log --logappend
mongod --replSet rs1 --keyFile /data/key/r1 --fork --port 28011 --dbpath /data/data/r1 --logpath=/data/log/r1.log --logappend
mongod --replSet rs1 --keyFile /data/key/r2 --fork --port 28012 --dbpath /data/data/r2 --logpath=/data/log/r2.log --logappend

--master 指定为主机器
--slave 指定为从机器
--source 指定主机器的IP地址
--slavedelay 指从复制检测的时间间隔


mongo -port 28010
> config_rs1 = {_id: 'rs1', members: [
... {_id: 0, host: 'localhost:28010', priority:1}, --成员 IP 及端口,priority=1 指 PRIMARY
... {_id: 1, host: 'localhost:28011'},
... {_id: 2, host: 'localhost:28012'}]
...
}

config_rs1={_id:'rs1',members:[{_id:0,host:'localhost:28010',priority:1}]}

rs.initiate(config_rs1); --初始化配置
rs.status()  查看集群状态
rs.add("localhost:28013")  添加节点
rs.status() 数据同步

rs.remove("localhost:28014")  减少节点


"health" : 1,
--1 表明正常; 0 表明异常
"state" : 1,
-- 1 表明是 Primary; 2 表明是 Secondary;
"stateStr" : "PRIMARY", --表明此机器是主库

rs.isMaster() 查看Replica Sets状态

Replica  Set 通过日志oplog.rs 来操作的 它存在于”local”数据库中
use local
db.oplog.rs.find()
db.system.replset.find()   主从配置信息
查看同步状态
db.printSlaveReplicationInfo()
 源数据信息
db.printReplicationInfo()

读写分离  让从库可读 分担压力
db.getMongo().setSlaveOk(); 注意大小写

主库失效 自动选举
 rs.status()  查看

物理增加借点
scp -r /data/data/r3 /data/data/r4
echo "this is rs1 super secret key" > /data/key/r4
chmod 600 /data/key/r4
mongod  --replSet  rs1  --keyFile  /data/key/r4  --fork  --port  28014  --dbpath /data/data/r4 --logpath=/data/log/r4.log --logappend --fastsync
注意 多了 --fastsync
rs.add("localhost:28014")

大集群中的配置服务器
mongod --configsvr --port 30000 --dbpath /data/shard/config --fork --logpath
/data/shard/log/config.log --directoryperdb

路由服务器
mongos --port 40000 --configdb localhost:30000 /data/shard/log/route.log --chunkSize 1


分片
启动分片服务器
mongod  --shardsvr  --port  20000  --dbpath  /data/shard/s0  --fork  --logpath=/data/shard/log/s0.log    --directoryperdb
mongod  --shardsvr  --port  20001  --dbpath  /data/shard/s1  --fork  --logpath=/data/shard/log/s1.log    --directoryperdb
启动配置服务器
mongod --configsvr --port 30000 --dbpath=/data/shard/config --fork --logpath=/data/shard/log/config.log    --directoryperdb
启动路由进程
mongos  --port  40000  --configdb  localhost:30000  --fork  --logpath=/data/shard/log/route.log    --chunkSize 1

连接到配置服务器的主库
# /Apps/mongo/bin/mongo admin --port 40000 --此操作需要连接 admin 库
MongoDB shell version: 1.8.1
connecting to: 127.0.0.1:40000/admin
> db.runCommand({ addshard:"localhost:20000" }) --添加 Shard Server
{ "shardAdded" : "shard0000", "ok" : 1 }
> db.runCommand({ addshard:"localhost:20001" })
{ "shardAdded" : "shard0001", "ok" : 1 }
> db.runCommand({ enablesharding:"test" }) --设置分片存储的数据库
{ "ok" : 1 }
> db.runCommand({ shardcollection: "test.users", key: { _id:1 }}) --设置分片的集合名称,且必须指定 Shard Key,系统会自动创建索引
{ "collectionsharded" : "test.users", "ok" : 1 }

验证分片
for(var  i  =  1;  i  <=  500000;  i++)  db.users.insert({age:i,  name:"wangwenlong",  addr:"Beijing", country:"China"})
db.user.stats();


列出所有分片
db.runCommand({ listshards: 1 })

判断是否分片
db.runCommand({ isdbgrid:1 })

查看所有分片
printShardingStatus()

对现有表分片
use admin
db.runCommand({ shardcollection: "test.users_2", key: { _id:1 }})

新增分片
db.runCommand({ addshard:"localhost:20002" })

移除分片
db.runCommand({"removeshard" : "localhost:20002"});

分片和集群组合 先分片 再集群
