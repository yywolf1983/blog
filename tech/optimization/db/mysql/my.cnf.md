
#多实例集中配置
[mysqld_multi]
mysqld		=	/usr/mysql/mysql-5.7.18/bin/mysqld_safe
mysqladmin	=	/usr/mysql/mysql-5.7.18/bin/mysqladmin
log		   =	/usr/mysql/mysql-5.7.18/logs/mysqld_multi.log
user		=	mysql
password	=	mysql

#查看实例
mysqld_multi --defaults-extra-file=my.cnf report
mysqld_multi --defaults-extra-file=my.cnf stop 3320,3321,3322,3323


[client]
default-character-set = utf8
#被如下替换
character_set_server = utf8
port = 3309
socket = /home/mysql/mysql/tmp/mysql.sock

[mysqld]
!include /home/mysql/mysql/etc/mysqld.cnf #包含的配置文件 ，把用户名，密码文件单独存放
port = 3309

autocommit = 1  #开启自动提交

#不同步的数据
replicate-ignore-db = mysq
replicate-ignore-db = tes
replicate-ignore-db = information_schem
user    = mysq
port    = 330
socket = /home/mysql/mysql/tmp/mysql.sock
pid-file = /longxibendi/mysql/mysql/var/mysql.pid
basedir = /home/mysql/mysql/
datadir = /longxibendi/mysql/mysql/var/
# tmp dir settings
tmpdir = /home/mysql/mysql/tmp/
slave-load-tmpdir = /home/mysql/mysql/tmp/
#当slave 执行 load data infile 时用
#language = /home/mysql/mysql/share/mysql/english/
character-sets-dir = /home/mysql/mysql/share/mysql/charsets/
# skip options
skip-name-resolve #禁止dns连接，必须使用ip不能使用主机名  
skip-symbolic-links #不能使用连接文件
skip-external-locking #不使用系统锁定，要使用myisamchk,必须关闭服务器
skip-locking  #避免MySQL的外部锁定，减少出错几率，增强稳定性。
skip-slave-start #启动mysql,不启动复制
#sysdate-is-now

#忽略错
slave-skip-errors = 1032,1062,126,1114,1146,1048,139

#忽略大小写
lower_case_table_names=1

# res settings
back_log = 50
#接受队列，对于没建立tcp连接的请求队列放入缓存中，队列大小为back_log，受限制与OS参数。对于Linux系统推荐设置为小于512的整数。
max_connections = 1000 #最大并发连接数 ，增大该值需要相应增加允许打开的文件描述符数
max_connect_errors = 10000 #如果某个用户发起的连接error超过该数值，则该用户的下次连接将被阻塞，直到管理员执行flush hosts ; 命令；防止黑客
#open_files_limit = 10240
connect-timeout = 10 #连接超时之前的最大秒数,在Linux平台上，该超时也用作等待服务器首次回应的时间
wait-timeout = 28800 #等待关闭连接的时间
interactive-timeout = 28800 #关闭连接之前，允许interactive_timeout（取代了wait_timeout）秒的不活动时间。客户端的会话wait_timeout变量被设为会话interactive_timeout变量的值。
slave-net-timeout = 600 #从服务器也能够处理网络连接中断。但是，只有从服务器超过slave_net_timeout秒没有从主服务器收到数据才通知网络中断
net_read_timeout = 30 #从服务器读取信息的超时
net_write_timeout = 60 #从服务器写入信息的超时
net_retry_count = 10 #如果某个通信端口的读操作中断了，在放弃前重试多次
net_buffer_length = 16384 #包消息缓冲区初始化为net_buffer_length字节，但需要时可以增长到max_allowed_packet字节
max_allowed_packet = 64M #网络传输缓冲区最大长度
#table_cache = 512    #所有线程打开的表的数目。增大该值可以增加mysqld需要的文件描述符的数量
thread_stack = 192K #每个线程的堆栈大小
thread_cache_size = 200 #线程缓存
thread_concurrency = 8  #同时运行的线程的数据 此处最好为CPU个数两倍。
# qcache settings
#如果查询重复值不大 建议缩小或禁止查询缓
query_cache_size = 256M #查询缓存大小
query_cache_limit = 2M #不缓存查询大于该值的结果
query_cache_min_res_unit = 2K #查询缓存分配的最小块大小
# default settings
# time zone
default-time-zone = system #服务器时区
character-set-server = utf8 #server级别字符集
default-storage-engine = InnoDB #默认存储

# tmp & heap
tmp_table_size = 512M #临时表大小，如果超过该值，则结果放到磁盘中
max_heap_table_size = 512M #该变量设置MEMORY (HEAP)表可以增长到的最大空间大小
log-bin = mysql-bin #这些路径相对于datadir 二进制日
log-bin-index = mysql-bin.index    #二进制日志索
binlog-do-db = db_name     
binlog-ignore-db = db_name   #忽略某个数据库的二进制记
relayrelay-log = relay-log      #slave 日
relayrelay_log_index = relay-log.index

# max binlog keeps days
expire_logs_days = 30 #超过30天的binlog删除
binlog_cache_size = 1M #session级别

max_binlog_size = 1G   #二进制日志存储上
max_relay_log_size = 1G

# warning & error log
log-warnings = 1
log-error = /home/mysql/mysql/log/mysql.err
log_output = FILE #参数log_output指定了慢查询输出的格式，默认为FILE，你可以将它设为TABLE，然后就可以查询mysql架构下的slow_log表了
log_output = FILE #参数log_output指定了慢查询输出的格式，默认为FILE，你可以将它设为TABLE，然后就可以查询mysql架构下的slow_log表了



show variables like 'long_query_time';
show variables like 'log_slow%';
show variables like 'slow_query_log';
show variables like '%slow_query%';
show variables like 'log_queries_not_%';
# slow query log
slow_query_log = on
long_query_time = 1 #慢查询时间 超过1秒则为慢查询 0.1可以这样设置 0记录所有
slow_query_log_file = /home/mysql/mysql/log/slow.log
log_queries_not_using_indexes=on  #索引慢查询
#log-queries-not-using-indexes
#log-slow-slave-statements
general_log = 1
general_log_file = /home/mysql/mysql/log/mysql.log
# if use auto-ex, set to 0
relay-log-purge = 1 #当不用中继日志时，删除他们。这个操作有SQL线程完成

# replication
replicate-wild-ignore-table = mysql.% #复制时忽略数据库及表
replicate-wild-ignore-table = test.% #复制时忽略数据库及表
table_open_cache=1024;      这个数值是偏小的，如果max_connections较大，则容易引起性能问题。
# slave_skip_errors=all
key_buffer_size = 256M #myisam索引buffer,只有key没有data
sort_buffer_size = 2M #排序buffer大小；线程级别
read_buffer_size = 2M #以全表扫描(Sequential Scan)方式扫描数据的buffer大小 ；线程级别
join_buffer_size = 8M # join buffer 大小;线程级别
read_rnd_buffer_size = 8M #MyISAM以索引扫描(Random Scan)方式扫描数据的buffer大小 ；线程级别
bulk_insert_buffer_size = 64M #MyISAM 用在块插入优化中的树缓冲区的大小。注释：这是一个per thread的限制
myisam_sort_buffer_size = 64M #MyISAM 设置恢复表之时使用的缓冲区的尺寸,当在REPAIR TABLE或用CREATE INDEX创建索引或ALTER TABLE过程中排序 MyISAM索引分配的缓冲区
myisam_max_sort_file_size = 10G #MyISAM 如果临时文件会变得超过索引，不要使用快速排序索引方法来创建一个索引。注释：这个参数以字节的形式给出.重建MyISAM索引(在REPAIR TABLE、ALTER TABLE或LOAD DATA INFILE过程中)时，允许MySQL使用的临时文件的最大空间大小。如果文件的大小超过该值，则使用键值缓存创建索引，要慢得多。该值的单位为字节
myisam_repair_threads = 1 #如果该值大于1，在Repair by sorting过程中并行创建MyISAM表索引(每个索引在自己的线程内)
myisam_recover = 64K#允许的GROUP_CONCAT()函数结果的最大长度

# 设定默认的事务隔离级别.可用的级别如下
# READ-UNCOMMITTED, READ-COMMITTED, REPEATABLE-READ, SERIALIZABL
# 1.READ UNCOMMITTED-读未提交2.READ COMMITTE-读已提交3.REPEATABLE READ -可重复读4.SERIALIZABLE -串
transaction_isolation = REPEATABLE-READ

innodb_file_per_table = 0  #InnoDB为独立表空间模式，每个数据库的每个表都会生成一个数据空间。0关闭，1开启。
#innodb_status_file = 1
#innodb_open_files = 2048
# innodb_additional_mem_pool_size = 100M #帧缓存的控制对象需要从此处申请缓存，所以该值与innodb_buffer_pool对应  这一句已经淘汰
# 换为
innodb_use_sys_malloc = 1
innodb_buffer_pool_size = 2G #包括数据页、索引页、插入缓存、锁信息、自适应哈希所以、数据字典信息
innodb_data_home_dir = /longxibendi/mysql/mysql/var/
#innodb_data_file_path = ibdata1:1G:autoexten
innodb_data_file_path = /ibdata/ibdata1:988M;/disk2/ibdata2:50M:autoextend #表空间  一个磁盘满后在另一个磁盘存
innodb_file_io_threads = 4 #io线程数
innodb_thread_concurrency = 16 #InnoDB试着在InnoDB内保持操作系统线程的数量少于或等于这个参数给出的限制
innodb_flush_log_at_trx_commit = 1 #每次commit 日志缓存中的数据刷到磁盘中
innodb_log_buffer_size = 8M #事务日志缓存
innodb_log_file_size = 500M #事务日志大小
#innodb_log_file_size =100M
innodb_log_files_in_group = 2 #两组事务日志  为提高性能,MySQL可以以循环方式将日志文件写到多个文件。推荐设置为3。
innodb_log_group_home_dir = /longxibendi/mysql/mysql/var/#日志组
innodb_max_dirty_pages_pct = 90 #innodb主线程刷新缓存池中的数据，使脏数据比例小于90%
innodb_lock_wait_timeout = 50 #InnoDB事务在被回滚之前可以等待一个锁定的超时秒数。InnoDB在它自己的 锁定表中自动检测事务死锁并且回滚事务。InnoDB用LOCK TABLES语句注意到锁定设置。默认值是50秒
#innodb_flush_method = O_DSYNC
[mysqldump]
quick
max_allowed_packet = 64M
[mysql]
disable-auto-rehash #允许通过TAB键提示
character_set_server=utf8
connect-timeout = 3



Server接受的数据包大小
show VARIABLES like '%max_allowed_packet%';
max_allowed_packet = 20M

set global max_allowed_packet = 2*1024*1024*10 重新登录生效

连接数
show variables like '%max_connections%';
set GLOBAL max_connections = 800;


查看MySql状态及变量的方法：

swappiness=0的时候表示最大限度使用物理内存，然后才是 swap空间，swappiness＝100的时候表示积极的使用swap分区，并且把内存上的数据及时的搬运到swap空间里面。
  1.查看你的系统里面的swappiness
  $ cat /proc/sys/vm/swappiness
  不出意外的话，你应该看到是 60
  2.修改swappiness值为10
  $ sudo sysctl vm.swappiness=10
  但是这只是临时性的修改，在你重启系统后会恢复默认的60，为长治久安，还要更进一步：
  $ sudo gedit /etc/sysctl.conf
  在这个文档的最后加上这样一行:
  vm.swappiness=10
  然后保存，重启。ok，你的设置就生效了。


Mysql> show status ——显示状态信息（扩展show status like 'XXX'）
Mysql> show variables ——显示系统变量（扩展show variables like 'XXX'）
Mysql> show innodb status ——显示InnoDB存储引擎的状态
Shell> mysqladmin variables -u username -p password——显示系统变量
Shell> mysqladmin extended-status -u username -p password——显示状态信息

查看状态变量及帮助：

Shell> mysqld --verbose --help [|more #逐行显示]

首先，让我们看看有关请求连接的变量：

为了能适应更多数据库应用用户，MySql提供了连接（客户端）变量，以对不同性质的用户群体提供不同的解决方案，笔者就max_connections，back_log 做了一些细结，如下：

max_connections 是指MySql的最大连接数，如果服务器的并发连接请求量比较大，建议调高此值，以增加并行连接数量，当然这建立在机器能支撑的情况下，因为如果连接数越多，介于MySql会为每个连接提供连接缓冲区，就会开销越多的内存，所以要适当调整该值，不能盲目提高设值。可以过'conn%'通配符查看当前状态的连接数量，以定夺该值的大小。

back_log 是要求MySQL能有的连接数量。当主要MySQL线程在一个很短时间内得到非常多的连接请求，这就起作用，然后主线程花些时间(尽管很短)检查连接并且启动一个新线程。back_log值指出在MySQL暂时停止回答新请求之前的短时间内多少个请求可以被存在堆栈中。如果期望在一个短时间内有很多连接，你需要增加它。也就是说，如果MySql的连接数据达到max_connections时，新来的请求将会被存在堆栈中，以等待某一连接释放资源，该堆栈的数量即back_log，如果等待连接的数量超过back_log，将不被授予连接资源。另外，这值（back_log）限于您的操作系统对到来的TCP/IP连接的侦听队列的大小。你的操作系统在这个队列大小上有它自己的限制（可以检查你的OS文档找出这个变量的最大值），试图设定back_log高于你的操作系统的限制将是无效的。

优化了MySql的连接后属性后，我们需要看看缓冲区变量：

使用MySql数据库存储大量数据（或使用复杂查询）时，我们应该考虑MySql的内存配置。如果配置MySQL服务器使用太少的内存会导致性能不是最优的；如果配置了太多的内存则会导致崩溃，无法执行查询或者导致交换操作严重变慢。在现在的32位平台下，仍有可能把所有的地址空间都用完，因此需要审视。

计算内存使用的秘诀公式就能相对地解决这一部分问题。不过，如今这个公式已经很复杂了，更重要的是，通过它计算得到的值只是“理论可能”并不是真正消耗的值。事实上，有8GB内存的常规服务器经常能运行到最大的理论值（100GB甚至更高）。此外，你轻易不会使用到“超额因素”（它实际上依赖于应用以及配置）。一些应用可能需要理论内存的10%而有些仅需1%。
那么，我们可以做什么呢？

来看看那些在启动时就需要分配并且总是存在的全局缓冲吧！

全局缓冲：
key_buffer_size, innodb_buffer_pool_size, innodb_additional_mem_pool_size，innodb_log_buffer_size, query_cache_size

注：如果你大量地使用MyISAM表，那么你也可以增加操作系统的缓存空间使得MySQL也能用得着。把这些也都加到操作系统和应用程序所需的内存值之中，可能需要增加32MB甚至更多的内存给MySQL服务器代码以及各种不同的小静态缓冲。这些就是你需要考虑的在MySQL服务器启动时所需的内存。其他剩下的内存用于连接。

key_buffer_size 决定索引处理的速度，尤其是索引读的速度。一般我们设为16M，通过检查状态值Key_read_requests和Key_reads，可以知道key_buffer_size设置是否合理。比例key_reads / key_read_requests应该尽可能的低，至少是1:100，1:1000更好（上述状态值可以使用'key_read%'获得用来显示状态数据）。key_buffer_size只对MyISAM表起作用。即使你不使用MyISAM表，但是内部的临时磁盘表是MyISAM表，也要使用该值。可以使用检查状态值'created_tmp_disk_tables'得知详情。

innodb_buffer_pool_size 对于InnoDB表来说，作用就相当于key_buffer_size对于MyISAM表的作用一样。InnoDB使用该参数指定大小的内存来缓冲数据和索引。对于单独的MySQL数据库服务器，最大可以把该值设置成物理内存的80%。

innodb_additional_mem_pool_size 指定InnoDB用来存储数据字典和其他内部数据结构的内存池大小。缺省值是1M。通常不用太大，只要够用就行，应该与表结构的复杂度有关系。如果不够用，MySQL会在错误日志中写入一条警告信息。

innodb_log_buffer_size 指定InnoDB用来存储日志数据的缓存大小，如果您的表操作中包含大量并发事务（或大规模事务），并且在事务提交前要求记录日志文件，请尽量调高此项值，以提高日志效率。

query_cache_size 是MySql的查询缓冲大小。（从4.0.1开始，MySQL提供了查询缓冲机制）使用查询缓冲，MySQL将SELECT语句和查询结果存放在缓冲区中，今后对于同样的SELECT语句（区分大小写），将直接从缓冲区中读取结果。根据MySQL用户手册，使用查询缓冲最多可以达到238%的效率。通过检查状态值’Qcache_%’，可以知道query_cache_size设置是否合理：如果Qcache_lowmem_prunes的值非常大，则表明经常出现缓冲不够的情况，如果Qcache_hits的值也非常大，则表明查询缓冲使用非常频繁，此时需要增加缓冲大小；如果Qcache_hits的值不大，则表明你的查询重复率很低，这种情况下使用查询缓冲反而会影响效率，那么可以考虑不用查询缓冲。此外，在SELECT语句中加入SQL_NO_CACHE可以明确表示不使用查询缓冲。

除了全局缓冲，MySql还会为每个连接发放连接缓冲。

连接缓冲：
每个连接到MySQL服务器的线程都需要有自己的缓冲。大概需要立刻分配256K，甚至在线程空闲时，它们使用默认的线程堆栈，网络缓存等。事务开始之后，则需要增加更多的空间。运行较小的查询可能仅给指定的线程增加少量的内存消耗，然而如果对数据表做复杂的操作例如扫描、排序或者需要临时表，则需分配大约read_buffer_size，sort_buffer_size，read_rnd_buffer_size，tmp_table_size 大小的内存空间。不过它们只是在需要的时候才分配，并且在那些操作做完之后就释放了。有的是立刻分配成单独的组块。tmp_table_size 可能高达MySQL所能分配给这个操作的最大内存空间了。注意，这里需要考虑的不只有一点 —— 可能会分配多个同一种类型的缓存，例如用来处理子查询。一些特殊的查询的内存使用量可能更大——如果在MyISAM表上做成批的插入时需要分配 bulk_insert_buffer_size 大小的内存；执行 ALTER TABLE， OPTIMIZE TABLE， REPAIR TABLE 命令时需要分配 myisam_sort_buffer_size 大小的内存。

read_buffer_size 是MySql读入缓冲区大小。对表进行顺序扫描的请求将分配一个读入缓冲区，MySql会为它分配一段内存缓冲区。read_buffer_size变量控制这一缓冲区的大小。如果对表的顺序扫描请求非常频繁，并且你认为频繁扫描进行得太慢，可以通过增加该变量值以及内存缓冲区大小提高其性能。

sort_buffer_size 是MySql执行排序使用的缓冲大小。如果想要增加ORDER BY的速度，首先看是否可以让MySQL使用索引而不是额外的排序阶段。如果不能，可以尝试增加sort_buffer_size变量的大小。

read_rnd_buffer_size 是MySql的随机读缓冲区大小。当按任意顺序读取行时(例如，按照排序顺序)，将分配一个随机读缓存区。进行排序查询时，MySql会首先扫描一遍该缓冲，以避免磁盘搜索，提高查询速度，如果需要排序大量数据，可适当调高该值。但MySql会为每个客户连接发放该缓冲空间，所以应尽量适当设置该值，以避免内存开销过大。

tmp_table_size是MySql的heap （堆积）表缓冲大小。所有联合在一个DML指令内完成，并且大多数联合甚至可以不用临时表即可以完成。大多数临时表是基于内存的(HEAP)表。具有大的记录长度的临时表 (所有列的长度的和)或包含BLOB列的表存储在硬盘上。如果某个内部heap（堆积）表大小超过tmp_table_size，MySQL可以根据需要自动将内存中的heap表改为基于硬盘的MyISAM表。还可以通过设置tmp_table_size选项来增加临时表的大小。也就是说，如果调高该值，MySql同时将增加heap表的大小，可达到提高联接查询速度的效果。

当我们设置好了缓冲区大小之后，再来看看：

table_cache 所有线程打开的表的数目，增大该值可以增加mysqld需要的文件描述符的数量。每当MySQL访问一个表时，如果在表缓冲区中还有空间，该表就被打开并放入其中，这样可以更快地访问表内容。通过检查峰值时间的状态值’Open_tables’和’Opened_tables’，可以决定是否需要增加table_cache的值。如果你发现open_tables等于table_cache，并且opened_tables在不断增长，那么你就需要增加table_cache的值了（上述状态值可以使用’Open%tables’获得）。注意，不能盲目地把table_cache设置成很大的值。如果设置得太高，可能会造成文件描述符不足，从而造成性能不稳定或者连接失败。

做了以上方面的调优设置之后，MySql应该基本能满足您需求（当然是建立在调优设置适当的情况下），我们还应该了解并注意：

只有简单查询OLTP（联机事务处理）应用的内存消耗经常是使用默认缓冲的每个线程小于1MB，除非需要使用复杂的查询否则无需增加每个线程的缓冲大小。使用1MB的缓冲来对10行记录进行排序和用16MB的缓冲基本是一样快的（实际上16MB可能会更慢，不过这是其他方面的事了）。

找出MySQL服务器内存消耗的峰值。这很容易就能计算出操作系统所需的内存、文件缓存以及其他应用。在32位环境下，还需要考虑到32位的限制，限制 “mysqld” 的值大约为2.5G（实际上还要考虑到很多其他因素）。现在运行 “ps aux” 命令来查看 “VSZ” 的值（MySQL 进程分配的虚拟内存）。监视着内存变化的值，就能知道是需要增加或减少当前的内存值了。

最后来看看调优设置方法：

安装好MySql后，配制文件应该在 ./share/mysql ("./"即MySql安装目录) 目录中，配制文件有几个，有my-huge.cnf my-medium.cnf my-large.cnf my-small.cnf。win环境下即存在于MySql安装目录中的.ini文件。不同的流量的网站和不同配制的服务器环境，当然需要有不同的配制文件了。
一般的情况下，my-medium.cnf这个配制文件就能满足我们的大多需要；一般我们会把配置文件拷贝到 /etc/my.cnf ，win环境下则拷备到 my.ini 下即可，只需要修改这个配置文件就可以了。
