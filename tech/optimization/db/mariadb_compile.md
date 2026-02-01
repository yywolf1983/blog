### 编译安装 mariadb


#### MaxScale 集群
------------------------

mysql_path=/data/mariadb

> yum install make cmake ncurses-devel ncurses-devel  openssl-devel gcc gcc-c++ autoconf zlib-devel bison-devel  xz-devel

[https://github.com/jemalloc]

`./autogen.sh`

> boost install
* ./bootstrap.sh
* ./b2
* ./b2 install



mysql_path=/data/mariadb

#### mariadb compile
>cmake -DCMAKE_INSTALL_PREFIX=${mysql_path} -DSYSCONFDIR=/data/mariadb/etc -DMYSQL_DATADIR=/data/mariadb/data -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DWITH_FEDERATED_STORAGE_ENGINE=1 -DEXTRA_CHARSETS=all -DDEFAULT_CHARSET=utf8mb4 -DDEFAULT_COLLATION=utf8mb4_general_ci -DWITH_EMBEDDED_SERVER=1 -DENABLED_LOCAL_INFILE=1  -DDOWNLOAD_BOOST=1 -DWITH_BOOST=/usr/local/include/boost/  -DWITH_JEMALLOC=/usr/local/include/jemalloc/ -DWITH_WSREP=ON -DWITH_INNODB_DISALLOW_WRITES=ON

cmake . -LH

>如果之前编译有错误，需要重新编译，请删除CMakeCache.txt
make && make install

* 效率更高的编译方式
```
[ "`cat /proc/cpuinfo |grep 'processor'|wc -l`" = "1" ] && make
[ "`cat /proc/cpuinfo |grep 'processor'|wc -l`" != "1" ] && make -j`cat /proc/cpuinfo |grep 'processor'|wc -l`
```

* mkdir -p ${mysql_path}/etc/
* cp ./support-files/my-small.cnf /data/mariadb/etc/my.cnf
* cp ./support-files/wsrep.cnf /data/mariadb/etc/wsrep.cnf

> 建立用户
* groupadd mysql
* useradd -s /sbin/nologin -g mysql mysql

chown mysql:mysql -R ${mysql_path}

#### 修改 my.cnf
export MYSQL_PATH=${mysql_path}
sed '/mysqld]/a\pid-file = '${MYSQL_PATH}'/data/mariadb.pid' -i ${MYSQL_PATH}/etc/my.cnf
sed '/mysqld]/a\datadir = '${MYSQL_PATH}'/data' -i ${MYSQL_PATH}/etc/my.cnf
sed '/mysqld]/a\basedir = '${MYSQL_PATH}'' -i ${MYSQL_PATH}/etc/my.cnf
sed '/mysqld]/a\user = mysql' -i ${MYSQL_PATH}/etc/my.cnf
sed '/#innodb_lock_wait_timeout = 50/a\log_error = '${MYSQL_PATH}'/data/mariadb.err' -i ${MYSQL_PATH}/etc/my.cnf
cat ${MYSQL_PATH}/etc/my.cnf |grep -v '^#' | grep -v '^$'

#### 初始化数据库
${MYSQL_PATH}/scripts/mysql_install_db --user=mysql --basedir=${MYSQL_PATH} --datadir=${MYSQL_PATH}/data

#### 启动数据库
${MYSQL_PATH}/bin/mysqld_safe  --defaults-file=${MYSQL_PATH}/etc/my.cnf &

#### 修改密码
> _mysql5.7会生成一个初始化密码，而在之前的版本首次登陆不需要登录。_
> * 注意 mysql5.7 已经生成密码
> * cat /root/.mysql_secret
> * ${MYSQL_PATH}/bin/mysqladmin -u root password 'password'

##### mysql 5.7 以上
* update mysql.user set authentication_string=password('123456') where user='root' and Host = '%';

##### mariadb
* update mysql.user set Password=password('password') where user='root' and Host='%';

alter user root@localhost identified by '123456';
flush privileges;

#### 添加环境变量
1. vi /etc/profile
2. export MYSQL_PATH=/data/mariadb
3. export PATH=$PATH:${MYSQL_PATH}/bin/

#### 远程登陆
* UPDATE user SET Host = '%' WHERE User ='root';
* FLUSH PRIVILEGES;   ``特别提示：这个很重要``

> 管理动态链接库

ldconfig


>${mysql_path}/bin/mysql -u root -pmdbpasswd -h localhost < /tmp/mysql_sec_script

> ?tar czf - /www| ssh root@ip:port tar xzf - -C /app

#### 建立用户
* GRANT USAGE ON *.* to root@'127.0.0.1' IDENTIFIED BY'123456';
* grant all privileges on *.* to root@'127.0.0.1';


### 多主集群搭建 galera

##### 官方文档
[http://galeracluster.com/documentation-webpages/index.html]
##### 编译依赖
[http://scons.org/pages/download.html]

yum install check-devel

yum install lsof which

##### 下载地址
> git clone https://github.com/codership/galera.git

scons

cp libgalera_smm.so /data/mysql/etc/

#### 所需软件
yum -y install which lsof

#### 添加配置
vi /data/mysql/etc/my.cnf

```
[mysqld]
basedir = /data/mariadb
pid-file = /data/mariadb/data/mariadb.pid

datadir = /data/mariadb/data
socket=/data/mariadb/mysql.sock
user=mysql
binlog_format=ROW
bind-address=0.0.0.0
default_storage_engine=innodb
innodb_autoinc_lock_mode=2
innodb_flush_log_at_trx_commit=0
innodb_buffer_pool_size=122M
wsrep_provider=/data/mariadb/etc/libgalera_smm.so
wsrep_provider_options="gcache.size=300M; gcache.page_size=300M"
wsrep_cluster_name="example_cluster"
wsrep_cluster_address="gcomm://"      #后启动的机器上 填写主的ip
wsrep_sst_method=rsync
wsrep_sst_auth=root:yangyao
```

> 注意这里的端口设置。 但4444 好像未影响 数据同步
> 4567 Galera Cluster is configured using `–wsrep-node-address`
> 4568 IST port is configured using `–wsrep-provider-options=”ist.recv_addr=”`
> 4444 SST port is configured using `–wsrep-sst-receive-address`

#### 启动……
> mysqld --wsrep-new-cluster --user=root &
> mysqld --defaults-file=${mysql_path}/etc/my.cnf --wsrep-new-cluster --user=mysql
> mysqld --defaults-file=${mysql_path}/etc/my.cnf --user=mysql

su - mysql -c "${mysql_path}/bin/mysqld --defaults-file=${mysql_path}/etc/my.cnf --user=mysql "

#### 查看状态
* SHOW STATUS LIKE 'wsrep%';

> * wsrep_cluster_size
> * wsrep_ready

* SHOW VARIABLES LIKE 'wsrep_cluster_address';
* SHOW VARIABLES LIKE 'wsrep%';
*
* SHOW STATUS LIKE 'wsrep_cluster_size';  


##### 手动添加机器
使用 galera 端口
> * SET GLOBAL wsrep_cluster_address='gcomm://172.17.0.4,172.17.0.5,172.17.0.6';
> * SET GLOBAL wsrep_cluster_address='dummy://192.168.2.25:3336,192.168.2.25:3337,192.168.2.25:3335';

> * SET GLOBAL wsrep_cluster_address='dummy://192.168.2.25:3306,192.168.2.25:3307,192.168.2.25:3305';

##### 设置权重
SET GLOBAL wsrep_provider_options="pc.weight=3";

##### 查看锁
FLUSH TABLES WITH READ LOCK;

#### 尚未理解
garbd --address gcomm://192.168.1.2?gmcast.listen_addr=tcp://0.0.0.0:4444 \
  --group example_cluster --donor example_donor --sst backup
