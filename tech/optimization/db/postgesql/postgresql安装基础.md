./configure
gmake
su
gmake install
adduser postgres
mkdir /usr/local/pgsql/data
chown postgres /usr/local/pgsql/data
su - postgres
/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data
/usr/local/pgsql/bin/postgres -D /usr/local/pgsql/data >logfile 2>&1 &
/usr/local/pgsql/bin/createdb test
/usr/local/pgsql/bin/psql test


开启TCP/IP 连接
vi /var/lib/pgsql/data/postgresql.conf
tcpip_socket = true




service postgresql start
su postgresql


psql -U postgres  database
psql -h127.0.0.1 -Unetkiller netkiller


\q 退出


CREATE USER netkiller WITH PASSWORD 'chen';
drop user netkiller
ALTER USER "9812_net" PASSWORD    '123456';
CREATE DATABASE netkiller WITH OWNER = netkiller TEMPLATE = template0 ENCODING = 'UNICODE';
\l  列出库
\du 查看角色


\d  查看库 查看表


pg_dumpall -Upostgres > a.dmp  备份
psql member -f pgsql-backup.dmp


设置缺省共享内存
可以在 proc  文件系统里修改这些值（不用重起）．
echo 134217728 >/proc/sys/kernel/shmall
echo 134217728 >/proc/sys/kernel/shmmax
也可以
sysctl -w kernel.shmall=134217728
sysctl -w kernel.shmmax=134217728
还可以  /etc/sysctl.conf  
kernel.shmall = 134217728
kernel.shmmax = 134217728


postgresql.conf  设置最大链接
max_connections = 100
shared_buffers = 200   
shared_buffers = max_connections*2


查看连接数
show max_connections;




数据库性能
分组插入
begin;
insert into ……
insert into ……
insert into ……
…….
1000条insert into
…….
insert into ……
commit;


重建索引
 vacuumdb -hlocalhost -p5432 -Upostgres -a -f -z




select current_date;  当前日期
select current_time;  当前时间
select current_timestamp;   当前日期时间
select current_timestamp::timestamp (0);  不显示时区
select to_date('2003-12-2','YYYY-MM-DD')-to_date('2003-12-1','YYYY-MM-DD');    计算时差
select to_date('2003-12-6','yyyy-mm-dd')+12 ;  计算时间合


支持汉字做字段名
Create table "组"(
 "序号" Serial NOT NULL UNIQUE,
 "组名" Varchar(20) NOT NULL,
 "描述" Varchar(255),
 UNIQUE  ("组名"),
    PRIMARY KEY ("序号")
);


::   数据转换


"rate" Varchar(20) Default '0' Check (rate in ('0','1','2','3','4','5')),   约束
插入非约束字段提示出错


Create table "group"
(
  "id" Serial NOT NULL UNIQUE,
  "groupname" Varchar(20) NOT NULL,
  "description" Varchar(255),
   UNIQUE  (groupname),    唯一约束
   PRIMARY KEY ("id")   主键约束
   product_no integer REFERENCES products,   外键约束
);


\dt  查看模式
模式
CREATE SCHEMA your_schema;
DROP SCHEMA your_schema;




cat pg_hba.conf
# local    DATABASE  USER  METHOD  [OPTION]
# host     DATABASE  USER  IP-ADDRESS  IP-MASK  METHOD  [OPTION]
# hostssl  DATABASE  USER  IP-ADDRESS  IP-MASK  METHOD  [OPTION]
host    all         all         127.0.0.1         255.255.255.255   md5
local   all         all                                          trust 
