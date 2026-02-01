常用命令

IntegrityError: duplicate key value violates unique constraint "eshop_groupcontentclassify_pkey"
SELECT setval('eshop_groupcontentclassify_id_seq', (SELECT MAX(id) FROM eshop_groupcontentclassify)+1);
还有一个原因就是 client_idle_limit = 300 设置时间太短

could not send startup packet: Broken pipe
cat /proc/18391/limits
echo -n 'Max open files=265535:265535' > /proc/4381/limits


/opt/PostgresPlus/9.1SS/bin/pg_ctl -D /opt/PostgresPlus/9.1SS/data/ -l /opt/PostgresPlus/9.1SS/data/logfile restart -m fast   #-m fast 强制重启

psql命令
psql -Upostgres -p5190
\l  列出库
\c cloudapi-engine
\t 列出表
\q
\h
\d+ 表结构


VACUUM 清理磁盘空间

~#pg_dump TDADB > backup.sql
~#dropdb TDADB
~#createdb TDADB
~#psql TDADB < backup.sql

createdb -Upostgres -p5190 cloudapi-engine

psql -h192.168.10.92 -Upostgres -p5190 ejabberd < pg.sql

DROP DATABASE "cloudapi-engine";

获取链接列表
SELECT   *   FROM   pg_stat_activity;

查看连接数
select count(1) from pg_stat_activity;


清理链接
for x in `ps -eF | grep -E "postgres.*idle"| awk '{print $2}'`;do kill $x; done


导出
/opt/PostgresPlus/9.0SS/bin/pg_dump -p5190 -Upostgres cloudapi-engine > cloudapi-engine
导入
/opt/PostgresPlus/9.0SS/bin/psql -Upostgres -p5190 cloudapi-engine  < cloudapi-engine_postgres_150228.sql


运维网监控
1、查看某用户的表权限
select * from information_schema.table_privileges where grantee='user_name';

2、查看usage权限表
select * from information_schema.usage_privileges where grantee='user_name';

3、查看存储过程函数相关权限表
select * from information_schema.routine_privileges where grantee='user_name';
date

3个星期前
select now() - interval '3 week';

十分钟后
select now() + '10 min';

Abbreviation    Meaning
Y       Years
M       Months (in the date part)
W       Weeks
D       Days
H       Hours
M       Minutes (in the time part)
S       Seconds
用户权限

角色
CREATE ROLE role_name;
DROP ROLE role_name;
SELECT usename FROM pg_role;
\du

登陆权限
CREATE ROLE name LOGIN

超级用户
CREATE ROLE name SUPERUSER;

创建数据库
CREATE ROLE name CREATEDB;

创建角色
CREATE ROLE name CREATEROLE;

权限继承
GRANT pgread to test;

权限列表
SELECT、INSERT、UPDATE、DELETE、RULE、REFERENCES、TRIGGER、CREATE、TEMPORARY、EXECUTE和USAGE
ALL PRIVILEGES


arwdRxt -- ALL PRIVILEGES
显示权限
\z

权限之针对表
赋予
GRANT UPDATE ON accounts TO joe;
撤销
REVOKE ALL ON accounts FROM PUBLIC;

PUBLIC 所有用户

用户
create user replica;
CREATE ROLE创建的用户默认不带LOGIN属性，而CREATE USER创建的用户默认带有LOGIN属性。
ALTER ROLE postgres WITH LOGIN;
alter user replica with password 'replica';
alter user user_namewith CONNECTION LIMIT  20;#连接数限制


postgres=# create user debug;
CREATE ROLE
postgres=# alter user debug set default_transaction_read_only = on;
ALTER ROLE
postgres=# \c - debug
连接池处理

基本ini文件配置（假设我们创建了新的ini文件/usr/local/pgsql/conf/pgbouncer.ini）
1. 添加目标数据库的连接字符串，这个表示PgBouncer将会在哪些后端数据库中建立连接，比如：
template1 = host=127.0.0.1 port=5432 dbname=template1
2. 设定PgBouncer的监听端口, port=5555，默认为6000
3. 创建用户列表文件并添加用户信息，此用户为允许客户端使用的连接用户名，比如：
A. echo "user" "password" > /usr/local/pgsql/user.txt
B. 在ini设定：auth_file = /usr/local/pgsql/user.txt
4. 创建admin用户，在配置中添加：admin_users = user，用户可以使用此用户名连接pgbouncer并查看运行状况等，注意：此用户必须为user.txt文件中已经存在的用户。
启动并测试连接/查看运行状况
1. 启动:pgbouncer -d pgbouncer.ini
2. 测试连接：psql -h 127.0.0.1 -p 6000 -U user template1
3. 通过admin用户连接pgbouncer查看配置：
psql -h 127.0.0.1 -p 6000 -U user pgbouncer
pgbouncer=# show config;
3. 通过admin用户连接pgbouncer查看运行情况：
pgbouncer=# show stats;
pgbouncer=# show lists;
pgbouncer=# show pools;
pgbouncer=# show databases;
#其余运行参数可以通过如下命令查看
pgbouncer=# show help;
4. 参数修改：如果修改了ini文件中相关参数，需要通过命令告知bouncer重新读取配置内容：
pgbouncer=# reload;

Session pooling/会话连接池
   最礼貌的方法。在客户端连接的时候，将会给他分配一个服务器连接，并且在客户端连接的全程都分配给它。在客户端中断连接的时候，这个服务器连接将会放回连接池。这种方式不能降低数据库的连接数。
Transaction pooling/事务连接池
   服务器连接只是在一个事务的过程里赋予客户端的。在 PgBouncer 注意到事务结束后，服务器就会放回连接池。
Statement pooling/语句连接池
   最激进的模式。在每个查询结束之后，服务器的连接都会立即放回连接池。在这种模式下将不允许多语句的事务，因为它们的事务语意会被破坏。
python 模块

import psycopg2
import psycopg2.extras

conn = psycopg2.connect(host='localhost', port=5190, user='postgres', password='xxxxxxx', database='xxxxxxxx')
#字典化返回数据
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute('SELECT * FROM auth_user')

item = cursor.fetchone()

print item
postgres jsonb

create table SaleOrder (OrderDetail jsonb []);

insert into SaleOrder (OrderDetail)
values (array['{"ItemName":"伺服馬達","Spec":"","Price":26000}'::jsonb,'{"ItemName":"電池","Spec":"2000mAh","Price":500}'::jsonb]);

select * from SaleOrder
test

 \timing on
mydb=# create table foo(id bigint);
mydb=# insert into foo select * from generate_series(1,10000);
mydb=# select count(*) from foo;
免密码设置

--创建密码文件 .pgpass ( on 客户端 )                               
vi /home/postgres/.pgpass                                                     
hostname:port:database:username:password                                                                             
--范例                                                               
192.168.1.25:1921:skytf:skytf:skytf                                                                                         
--权限                                                               
Chmod 600 .pgpass                 

或

export PGPASSWORD=skytf
