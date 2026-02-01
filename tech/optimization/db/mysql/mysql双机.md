
还有一种思路 叫延时备份。从机延时 获取主机备份。

cnf配置文件一般会有四个，可以根据命令 # ll /usr/share/mysql/*.cnf 查看；
my-small.cnf    内存少于或等于64M，只提供很少的的数据库服务；
my-medium.cnf   内存在32M--64M之间而且和其他服务一起使用，例如web；
my-large.cnf    内存有512M主要提供数据库服务；
my-huge.cnf     内存有1G到2G，主要提供数据库服务；
my-innodb-heavy-4G.cnf 内存有4G，主要提供较大负载数据库服务（一般服务器都使用这个）；
可以根据服务器配置的不同选择不同的cnf配置文件！

;双机热备
server_id = 1 ;更换id
log-bin = mysql-bin
;发送设置
binlog-do-db =foods8 ;备份库  多库多行分开
binlog-ignore-db =mysql ;不许要备份的数据库
;接收设置
master-host = localhost
master-user = root
master-password = '发送库密码'
master-port = 3306
master-connect-retry = 10 ;链接次数
replicate-do-db =foods8  ;接收库
replicate-ignore-db= mysql ;不要接收的苦

mysql 同步方法


主从前先同步数据 双库数据一直在进行主从

1.在配置中开启
vim /etc/my.cnf
server-id       = 1    master端ID号   
log-bin=/data/logbin/mysql-bin    日志路径及文件名
同步cacti，此处关闭的话，就是除不允许的，其它的库均同步。
#binlog-do-db = cacti           
binlog-ignore-db = mysql        不同步mysql库，以下同上
binlog-ignore-db = test
binlog-ignore-db = information_schema
#binlog_format=mixed

binlog-do-db=需要复制的数据库名，如果复制多个数据库，重复设置这个选项即可
binlog-ignore-db=不需要复制的数据库苦命，如果复制多个数据库，重复设置这个选项即可

slave端：
replicate-do-db=需要复制的数据库名，如果复制多个数据库，重复设置这个选项即可
replicate-ignore-db=不需要复制的数据库名，如果复制多个数据库，重复设置这个选项即可

vim /etc/my.cnf
server-id = 2      slave的ID号，此处一定要大于master端。

mysql>flush tables with read lock;
mysql>show master status\G
*************************** 1. row ***************************
File: binlog.000006
Position: 107
Binlog_Do_DB: test
Binlog_Ignore_DB: mysql
1 row in set (0.00 sec)

如果你的是MYISAM或者既有MYISAM又有INNODB的话就在主服务器上使用如下命令导出服务器的一个快照：
mysqldump -uroot -p --lock-tables --events --triggers --routines --flush-logs --master-data=2 --databases test > db.sql
试过只有INNODB的话就是用如下命令：
mysqldump -uroot -p --single-transaction --events --triggers --routines --flush-logs --master-data=2 --databases test > db.sql
这里需要注意几个参数的使用：
--single-transaction 这个参数只对innodb适用。
--databases 后面跟除mysql以后的其他所有数据库的库名，我这里只有一个test库。
--master-data 参数会记录导出快照时候的mysql二进制日志位置，一会会用到。

mysql>unlock tables;
  注：这里锁表的目的是为了生产环境中不让进新的数据，好让从服务器定位同步位置。初次同步完成后，记得解锁。

也可以
从主服务器得到一个快照版本
如果你的是MYISAM或者既有MYISAM又有INNODB的话就在主服务器上使用如下命令导出服务器的一个快照：
mysqldump -uroot -p --lock-tables --events --triggers --routines --flush-logs --master-data=2 --databases test > db.sql
试过只有INNODB的话就是用如下命令：
mysqldump -uroot -p --single-transaction --events --triggers --routines --flush-logs --master-data=2 --databases test > db.sql
这里需要注意几个参数的使用：
--single-transaction 这个参数只对innodb适用。
--databases 后面跟除mysql以后的其他所有数据库的库名，我这里只有一个test库。
--master-data 参数会记录导出快照时候的mysql二进制日志位置，一会会用到。


2.查看主服务器
MariaDB [(none)]> show master status;
+------------------+----------+--------------+------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+------------------+----------+--------------+------------------+
| mysql-bin.000006 |      106 |              |                  |
+------------------+----------+--------------+------------------+
1 row in set (0.00 sec)

3.在从服务器上指定更新


/usr/local/mysql/bin/mysql -uroot -p
#建立同步账户
mysql>grant replication slave on *.* to rsync@'192.168.2.211' identified by '123456';
mysql>flush privileges;  #更新权限

mysql>flush tables with read lock;
mysql>show master status;

备份数据

mysql>unlock tables;

mysql>change master to
     >master_host='192.168.2.67',
     >master_user='rsync',                            master端创建的用于主从同步的账户和密码
     >master_password='123456',
     >master_port='3306',                             master端设置的client端使用的端口号。
     >master_log_file='mysql-bin.000006',             master端记录的file值
     >master_log_pos=106;                       master端记录的position值

4.启动服务
mysql> start slave;

从库重启后自动同步

调试
1,查看master的状态
SHOW MASTER STATUS;
Position 不应为0

2,查看slave的状态
show slave status;
Slave_IO_Running
Slave_SQL_Running
这两个字段 应为 YES|YES.

show processlist;
会有两条记录与同步有关 state为 Has read all relay log; waiting for the slave I/O thread to update it

4,CHANGE MASTER TO
如果A 的 Slave 未启动 ,Slave_IO_Running 为No.
可能会是B的master 的信息有变化,

5,主从不能同步:
show slave status;报错:Error xxx dosn't exist
且show slave status\G:
Slave_SQL_Running: NO
Seconds_Behind_Master: NULL
解决方法:
stop slave;
set global sql_slave_skip_counter =1 ;
start slave;

restart salve;
就可以了。
如果数据库已存在 先导出导入




常用命令
stop slave;
start slave;
show master status;
show slave status;
show processlist;
SHOW GRANTS;

主库插入测试同步
mysql>use test;
mysql>create table user(id int);

强制同步
主
mysql>flush tables with read lock;
Query OK,rows affected (0.01 sec)
mysql>show master status;
从
mysql>select master_pos_wait(‘mysql-bin.0000011′,’260′);
主
mysql>unlock tables;

同步出错 忽略从主传来语句
mysql> SET GLOBAL SQL_SLAVE_SKIP_COUNTER = n;
mysql> START SLAVE;


1.FLUSH TABLES WITH READ LOCK
这个命令是全局读锁定，执行了命令之后所有库所有表都被锁定只读。一般都是用在数据库联机备份，这个时候数据库的写操作将被阻塞，读操作顺利进行。

解锁的语句也是unlock tables。

2.LOCK TABLES tbl_name [AS alias] {READ [LOCAL] | [LOW_PRIORITY] WRITE}
这个命令是表级别的锁定，可以定制锁定某一个表。例如： lock  tables test read; 不影响其他表的写操作。

解锁语句也是unlock tables。

这两个语句在执行的时候都需要注意个特点，就是 隐式提交的语句。在退出mysql终端的时候都会隐式的执行unlock tables。也就是如果要让表锁定生效就必须一直保持对话。

P.S.  MYSQL的read lock和wirte lock

read-lock:  允许其他并发的读请求，但阻塞写请求，即可以同时读，但不允许任何写。也叫共享锁

write-lock: 不允许其他并发的读和写请求，是排他的(exclusive)。也叫独占锁
