> 使用SysBench  性能测试工具
> mysqlslap
>
> innobackupex mysql 热备份工具
>
> mysqldumpslow

#### docker 运行mysql
> docker run --name first-mysql -p 3306:3306 -e MYSQL\_ROOT\_PASSWORD=123456 -d mariadb

#### > show processlist

    mysqladmin -uroot -pyangyao ping
    mysqladmin -uroot -pyangyao status  
    mysqladmin -uroot -pyangyao processlist


#### mysql忘记密码

    /usr/local/mysql/bin/mysqld_safe --skip-grant-tables&
    [root@localhost /]#/usr/local/mysql/bin/mysql  //进入mysql
    mysql> use mysql   //切换到mysql database

#### 更新密码
    use mysql
    UPDATE user SET password=password('123456') WHERE user='root';

    SET PASSWORD = PASSWORD('123456');
    ALTER USER 'root'@'%' PASSWORD EXPIRE NEVER;

    flush privileges;

    #mysqladmin -uroot -p'oldpass' password newpass



#### > mysql_config_editor   加密登陆密码

#### mac 安装 mariadb
    brew install mariadb
    brew services start mariadb


> /usr/local/mysql/bin/mysqld_safe --defaults-file=/usr/local/mysql/my.cnf &

#### mysql 备份
cd /data/back
pw='xxxxxxx'
mysql -e "show databases;" -h127.0.0.1  -uroot -p${pw}| grep -Ev "Database|information_schema|mysql|performance_schema" | xargs mysqldump -h127.0.0.1  -uroot -p${pw}  --databases | gzip > dump_$(date +%Y%m%d).sql.gz


01 01 * * * /usr/bin/sh /data/back/mysql_back.sh 2>&1 > /dev/null &

#### 备份相关
    数据导出到另一个库
    shell> mysqladmin -h hostname -P port -u user -p passwd create db_name
    shell> mysqldump --opt db_name | mysql -h hostname -P port -u user -p
    mysqldump --database sampdb | ssh ip.net mysql
    mysqldump --database sampdb | mysql --compress

    备份数据库
    mysqldump -d phptest > a.sql

    mysqldump -h 127.0.0.1 -u用户名 -p密码 --all-databases
    #mysqldump -uroot -p --skip-lock-tables  --database mydb>ss.sql  导出
    #导出单个表
    mysqldump -uroot -p mydb abc>ss.sql
    导出数据不导出结构
    mysqldump　-t　数据库名　-uroot　-p　>　xxx.sql　
    导出结构不导出数据
    mysqldump　--opt　-d　数据库名　-u　root　-p　>　xxx.sql
    select * from driver into outfile "a.txt"; 执行结果导出


    source 导入
    \. "filename"
    mysql -uroot -p < back.sql

    有了数据库结构之后
    mysqlimport --user=name --password=pwd

    插入格式数据 非sql格式
    LOAD DATA INFILE '/tmp/test_outfile.txt' INTO TABLE test_outfile


#### windows mysql 注入服务
> mysqld --install MySQL --defaults-file="my.ini"

#### 从 binglog 恢复

> mysqlbinlog -d ops mysql-bin.000002 >002bin.sql
> 在恢复全备数据之前必须将该binlog文件移出，否则恢复过程中，会继续写入语句到binlog，最终导致增量恢复数据部分变得比较混乱


### 动态修改参数
system gdb -p $(pidof mysqld) -ex "set opt_log_slave_updates=1" -batch
### 添加多重选项
system gdb -p $(pidof mysqld) -ex 'call rpl_filter->add_do_db(strdup("hehehe"))' -batch


### 核心组件
进程，网络，文件，内存，安全，客户端
### 工具
备份，复原，监控，
### 查询管理器
> 查询解析器（Query parser）：用于检查查询是否合法
>
> 查询重写器（Query rewriter）：用于预优化查询
>
> 查询优化器（Query optimizer）：用于优化查询
>
> 查询执行器（Query executor）：用于编译和执行查询
### 数据管理
> 事务管理器（Transaction manager）：用于处理事务
>
> 缓存管理器（Cache manager）：数据被使用之前置于内存，或者数据写入磁盘之前置于内存
>
> 数据访问管理器（Data access manager）：访问磁盘中的数据


>   引擎
    数据类型
    索引  
    视图
    存储过程
    触发器
    事务
    分区
    SQL mode


> 分库又叫垂直分区，这种方式实现起来比较简单，重要的是对业务要细化，分库时候要想清楚各个模块业务之间的交互情况，避免将来写程序时出现过多的跨库操作。

> 分表又叫水平分区，这种方式实现起来就比垂直分区复杂些，但是它能解决垂直分区所不能解决的问题，即单张表的访问及写入很频繁，这时候就可以根据一定的业务规则（PS:如互联网BBS论坛的会员等级概念：根据会员等级来分表）来分表，这样就能减轻单表压力，并且还能解决各个模块的之间的频繁交互问题。

``` mysql
1. CREATE TABLE users (  
2.        uid INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,  
3.        name VARCHAR(30) NOT NULL DEFAULT '',  
4.        email VARCHAR(30) NOT NULL DEFAULT ''  
5. )  
6. PARTITION BY RANGE (uid) (  
7.        PARTITION p0 VALUES LESS THAN (3000000)  
8.        DATA DIRECTORY = '/data0/data'  
9.        INDEX DIRECTORY = '/data1/idx',  
10.  
11.        PARTITION p1 VALUES LESS THAN (6000000)  
12.        DATA DIRECTORY = '/data2/data'  
13.        INDEX DIRECTORY = '/data3/idx',  
14.  
15.        PARTITION p2 VALUES LESS THAN (9000000)  
16.        DATA DIRECTORY = '/data4/data'  
17.        INDEX DIRECTORY = '/data5/idx',  
18.  
19.        PARTITION p3 VALUES LESS THAN MAXVALUE     DATA DIRECTORY = '/data6/data'  
20.        INDEX DIRECTORY = '/data7/idx'  
21. );  
```
## mysql 数据类型 及 常用函数

    TINYINT      1 字节 (-128，127) (0，255) 小整数值
    SMALLINT     2 字节 (-32 768，32 767) (0，65 535) 大整数值
    MEDIUMINT    3 字节 (-8 388 608，8 388 607) (0，16 777 215) 大整数值
    INT或INTEGER 4 字节 (-2 147 483 648，2 147 483 647) (0，4 294 967 295) 大整数值
    BIGINT       8 字节 (-9 233 372 036 854 775 808，9 223 372 036 854 775 807) (0，18 446 744 073 709 551 615) 极大整数值

    FLOAT        4 字节 23位小数 单精度
    DOUBLE       8 字节 23-53为小数 双精度
    DECIMAL 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 依赖于M和D的值 依赖于M和D的值 小数值 双精度

>>>

    CHAR         0-255字节 定长字符串
    VARCHAR      0-255字节 变长字符串
    TINYBLOB     0-255字节 不超过 255 个字符的二进制字符串
    TINYTEXT     0-255字节 短文本字符串
    BLOB         0-65,535字节 二进制形式的长文本数据
    TEXT         0-65,535字节 长文本数据
    MEDIUMBLOB   0-16,777,215字节 二进制形式的中等长度文本数据
    MEDIUMTEXT   0-16,777,215字节 中等长度文本数据
    LOGNGBLOB    0-4,294,967,295字节 二进制形式的极大文本数据
    LONGTEXT     0-4,294,967,295字节 极大文本数据

>>>
    DATE       1000-01-01/9999-12-31 YYYY-MM-DD 日期值
    TIME       -838:59:59'/'838:59:59' HH:MM:SS 时间值或持续时间
    YEAR       1901/2155 YYYY 年份值
    DATETIME   1000-01-01 00:00:00/9999-12-31 23:59:59 YYYY-MM-DD HH:MM:SS 混合日期和时间值
    TIMESTAMP  1970-01-01 00:00:00/2037 年某时 YYYYMMDD HHMMSS 混合日期和时间值，时间戳


> MySQL 还支持两种复合数据类型 ENUM 和 SET，它们扩展了 SQL 规范。虽然这些类型在技术上是字符串类型，但是可以被视为不同的数据类型。一个 ENUM 类型只允许从一个集合中取得一个值；而 SET 类型允许从一个集合中取得任意多个值。
>
    ENUM     预先设定一个值
    SET      设定的值


一. 字符串函数

    select concat(name,"age is",age) from users;

    insert(str,x,y,insert)//将字符串x位置开始y个位置替换成insert

    select  lower(str) upper(str)//转化大小写
    select * from user where upper(name)='AAA';

    left (str ,x) right(str,x)//分别返回左边和右边的x个字符
    select left ("abcdee",3),right("abcdedd",3),left("abcdedd",null);

    lpad(str,n,pad),rpad（str,n,pad）//用字符串pad对str最左边或最右边补到n位

    ltrim()
    substring(str,x,y)//返回字符串中得第x位置起，取y个字符`


二. 数值函数

    abs(x)  // 返回x的绝对值
    ceil(x)  //返回大于x的最小整数
    floor（x）//返回小于x的最大整数
    mod（x，y） 返回x/y的膜
    rand（）  //0-1之间随机数
    round（x，y）//返回参数x的四舍五入的有y位小数的值
    truncate（x，y） //返回数字x截断y位小数的结果


三. 日期函数

    用php的时间戳来完成
    select  curdate()
            curtime()
            now()
            unix_timestamp(now（）)
            unix_timestamp(date)//unix时间戳
            from_unixtime()   //与unix时间戳相互转换
            week()
            year()
            hour()
            minute()
                 ……

    select  now()
    select  unix_timestamp(now())
    select  from_unixtiom(1293433835);
    select  from_unixtime()
    select  week(now())
    select  minute/hour(curtime())
    select  data_format(now(),"%Y-%m-%d %H%i%s")


四. 流程控制函数

    create  table  salary（id int,salary decimal(9,2)）;
    insert into salary  values(1,1000);
    *****
    if(value,t  f)
    select  if(salary) >3000,  'height','low')from  salary;
    ifnull(value1,value2)
    select  id,salary,ifnull(salary,0)  from  salary
    case when[value1]  then[result1]...else[default] end
    case when ...then
    select case when salary<=300  then 'low'  else 'high'  end  from salary;

    DELIMITER
    CREATE PROCEDURE p()
    BEGIN
      DECLARE v INT DEFAULT 1;
      CASE v
        WHEN 2 THEN SELECT v;
        WHEN 3 THEN SELECT 0;
        ELSE BEGIN END;
      END CASE;
    END;


五. 其他函数

    database（）
    version()   //查看数据库当前版本
    user()   //查看当前用户
    inet_aton(ip)  //返回ip地址的网络自解序
    inet_ntoa()  //返回网络自解序代表的ip地址
    password()  //将字符串加密，给mysql系统用户用的
    select  password ('123456');
    md5()   //给网站用户加密
    select * from mysql.user \G;//从mysql库中user表查看
    base command

    mysqld-nt.exe --install 服务名 --defaults-file=dmy.ini
    httpd.exe -k install -n 服务名

## 避免输入用户名密码
    [client]
    host = your_mysql_server
    user = your_username
    password = your_password
    database = your_database_name
    mysql -u 你的mysql用户名 -p -S /var/lib/mysql/mysql.sock

> 在select 语句中可以使用group by 子句将行划分成较小的组，然后，使用聚组函数返回每一个组的汇总信息，另外，可以使用having子句限制返回的结果集。
select  count(url),ip from logs   group by  ip  having count(ip)>100 order by count(ip)  

#### 查看重复数据
> select *,count(distinct name) from cs_id group by id HAVING COUNT( * ) >0

> show processlist
>
> kill 2222

查看innodb 锁
SELECT * FROM information_schema.INNODB_TRX;
SELECT * FROM information_schema.INNODB_LOCKs;


#### 慢查询日志开启
    set global slow_query_log=on
    show variables like "%slow%";
    可用mysql提供的mysqldumpslow，使用很简单，参数可–help查看
    查看连接数
    mysqladmin -uroot -proot processlist


#### show processlist;
    show grants for user_name@localhost;
    解释：显示一个用户的权限，显示结果类似于grant 命令
    show index from table_name;或show keys;
    解释：显示表的索引
    show status;
    解释：显示一些系统特定资源的信息，例如，正在运行的线程数量
    show variables;
    解释：显示系统变量的名称和值
    show privileges;
    解释：显示服务器所支持的不同权限
    show create database database_name;
    解释：显示创建指定数据库的SQL语句
    show create table table_name;
    解释：显示创建指定数据表的SQL语句
    show engies;
    解释：显示安装以后可用的存储引擎和默认引擎。
    show innodb status;
    解释：显示innoDB存储引擎的状态
    show logs;
    解释：显示BDB存储引擎的日志
    show warnings;
    解释：显示最后一个执行的语句所产生的错误、警告和通知
    show errors;
    解释：只显示最后一个执行语句所产生的错误


##  查看那些表锁到了
    --
    show OPEN TABLES where In_use > 0;
    -- 查看进程号
    show processlist;
    --删除进程
     kill 1085850；

> 这些历史文件包括~/.bash_history、~/.mysql_history等


## mysql支持数据分区

    内置帮助
    ? contents;
    ? date types;
    ? int;
    ? show;


> SELECT * FROM tbl_name ORDER BY RAND(); 取随机

## 赋值
    #列出现有行行号
    set @rowNo = 0;
    SELECT *, (@rowNo := @rowNo + 1) as mysqlnum FROM dcw_blog where classid=3;
    set @rowNo = 0;


### 分析select 分析
    explain select * from user;

### 探测执行瓶颈 慢查询
    set profiling=1;   开启探测
    执行语句 查询语句
    show profiles;    显示探测结果
    show profile cpu,block io for query 1;  查看详细信息  最后的 1 是id号

    show indexs

### 检查
    check table user   检测表
    CHECKSUM TABLE  效验和
    analyze table user;  分析关键字分布

    optimize table user; 重新整理表碎片



针对myisamchk 修复
myisamchk -r tablename
myisamchk -o tablename

表超过4G
alter table weblogentry MAX_ROWS=1000000000 AVG_ROW_LENGTH=15000;
myisamchk － dv tablename





权限 用户
create user 'yy'@'%' Identified by 'password';
-- 付给所有权限 包括 grant
grant all privileges on *.* to 'yy1'@'%' WITH GRANT OPTION;
flush privileges;

show grants for 'zhangsan';

回收权限
revoke all on * from user;

查看权限
show grants for 'yy'@'%'

权限列表
select,insert,update,delete

select  now(),user(),version();


show grants for 'test';
REVOKE all ON *.* from 'test'@'%';
grant all privileges on gzy_axzl.* to test;
FLUSH PRIVILEGES ;

查看当前库
select database();

要在删除表时，同时取消其他用户在此表上的相应权限。

show status;
show processlist  查看线程

show engines;  查看库信息 引擎信息

alter table tb_name engine=innodb;(版本5.0后都可以用engine参数)
或
alter table tb_name type=innodb;(低版本中用type参数)


mysqlshow --外部命令 和 内部命令 show 相似

#mysql -u root -p mydb select uuid();
#+--------------------------------------+
#| uuid()                               |
#+--------------------------------------+
#| 54b4c01f-dce0-102a-a4e0-462c07a00c5e |
#+--------------------------------------+
#engine=memory  存储引擎 内存表

show databases;

#建立索引
CREATE INDEX id_abc USING BTREE ON abc (uid);
-- BTREE 索引类型
DROP INDEX id_abc ON abc; #删除索引
#视图
CREATE VIEW abc AS SELECT username FROM abc;
ALTER VIEW vabc as select username,uid from abc;
drop view vabc;
ALTER TABLE name RENAME TO abc; #更改表名
#alter database add/delete/change(更变) 修改
#alter table name add 修改表
ALTER TABLE abc DROP COLUMN massage; #删除列
alter table abc add massage text NOT NULL; #添加列
ALTER TABLE abc MODIFY username char(20) NOT NULL, CHANGE massage massage2 CHAR(20); #更变列
ALTER TABLE abc CHANGE massage2 massage text;
show full fields from abc; #查看表详细结构及注释
-- 修改数据库名称
rename table t1 to tmp, t2 to t1 , tmp to t2;

-- 查看字符集 查看支持字符集！
show variables like 'character\_set\_%';  
show variables like 'collation_%';
show CHARACTER set

-- 查看警告信息
show warnings;

#show create table 'abc' 查看表如何建立！
select   count(其中任意一列名)   from   表    获取表内数据条数
select   count(id)   as   num   from   test

#建立表 插入数据：
#if not exists 防止重复插入
create table if not exists user
(
userid integer not null auto_increment primary key,
username varchar(12) not null
) type=innodb;

insert into user (userid,username) values ("","abc"),("","abc2"),("","abc3");

从查询插入
#insert into tbl_name select .......;

#防止重复插入
INSERT INTO clients
(client_id, client_name, client_type)
SELECT 10345, 'IBM', 'advertising'
FROM dual
WHERE not exists (select * from clients
where clients.client_id = 10345);


查看表个数
SELECT count(TABLE_NAME) FROM information_schema.TABLES WHERE TABLE_SCHEMA='gk';

#password表： 外键关联
create table password
(
userid integer not null,
password varchar(12) not null,
index (userid),
foreign key (userid) references user (userid)
on delete cascade
on update cascade
) type=innodb;

delete from user where userid="2";
select * from user;
select * from password;

delete from password where userid="3";
select * from user;
select * from password;

因外间约束删除失败
SET FOREIGN_KEY_CHECKS = 0;
删除完成后设置
SET FOREIGN_KEY_CHECKS = 1;

#外键说明：
#只有InnoDB类型的表才可以使用外键
#把id列 设为外键 参照外表outTable的id列 当外键的值删除 本表中对应的列筛除 当外键的值改变 本表中对应的列值改变。
#事件触发限制: on delete和on update , 可设参数cascade(跟随外键改动), restrict(限制外表中的外键改动),set #Null(设空值）,set Default（设默认值）,[默认]no action

#查看表结构
DESCRIBE abc;
show columns from user like 'user'
show create DATABASE mysql;
show create TABLE test.mytal;

#锁定 解锁
#FLUSH TABLES WITH READ LOCK; 锁定数据库以便/备份
unlock tables;
#LOCK TABLES和UNLOCK TABLES语句
锁表查询。
lock tables tablename write select * from abc;

#SHOW TABLE STATUS 库中表信息
#check table abc 检查表
#repair table abc 修复表
truncate table abc;  #清空表
alter table abc auto_increment = 0; #自增长id清零

#模糊查询
#like _ 单个匹配 % 多个匹配
select * from abc where massage like '_444';
select * from abc where massage like '%444';

#反排序 分业 order by  desc
select tid,username from abc order by uid desc limit 3,3; //检索3-3行 limit 5 检索前五行

UPDATE abc SET username='2222' and massage='222222' WHERE username='1111'; #更改数据
select '子查询没搞定';
select uid from abc where exists ( select username from abc where username='2222' );   #外至内
select uid from abc where in ( select username from abc where username='2222');   #内至外
#合并查询 union all 包括重复值
select uid from abc union select username from abc where username='2222';
#联合多表查询
#SELECT  t1.name, t2.salary FROM employee t1, info t2 WHERE  t1.name =  t2.name LIMIT 5
SELECT COUNT(*) from abc;  #查询数据条数
#system clear
#backup table abc to file
#触发器 只能在其他库中插入
before 之前
after  之后
mysql> DELIMITER ||
mysql> CREATE TRIGGER 触发器名 BEFORE|AFTER 触发事件
    -> ON 表名 FOR EACH ROW
    -> BEGIN
    -> select old.id
    -> select new.id
    -> INSERT INTO logs VALUES(NOW());
    -> INSERT INTO logs VALUES(NOW());
    -> END
    -> ||
Query OK, 0 rows affected (0.06 sec)
mysql> DELIMITER ;

DROP TRIGGER abc;

几种触发器例子

    DELIMITER ||
    CREATE TRIGGER new1_to_new2 AFTER INSERT
    ON mytest.new1 FOR EACH ROW
    BEGIN
    	INSERT into mytest.new2 VALUES (new.id,new.name,new.age,new.city);
    END||
    DELIMITER ;


    DELIMITER ||
    CREATE TRIGGER new1_up_new2 AFTER update
    ON mytest.new1 FOR EACH ROW
    BEGIN
    	update mytest.new2 set id=new.id,name=new.name,age=new.age,city=new.city where id = old.id;
    END||
    DELIMITER ;

    DELIMITER ||
    CREATE TRIGGER new1_del_new2 AFTER delete
    ON mytest.new1 FOR EACH ROW
    BEGIN
    	DELETE FROM new2 WHERE id = old.id;
    END||
    DELIMITER ;


#####  解决双向触发问题
``` sql
CREATE DEFINER=`baitao_admin`@`%` TRIGGER undate_coupon_user_new AFTER UPDATE ON btdb.ump_coupon_user FOR EACH ROW
begin
  -- 检查当前 环境，避免递归.
  IF @disable_trigger IS NULL THEN
    -- 设置禁用触发器标志.
    SET @disable_trigger = 1;

    UPDATE promotion_center.ump_coupon_user
		SET coupon_status = new.coupon_status,
		chl_use = new.chl_use,
		update_date = new.update_date
	WHERE
		id = old.id;

    -- 恢复禁用触发器标志.
    SET @disable_trigger = NULL;
  END IF;
END
```


#事务
START TRANSACTION或BEGIN语句可以开始一项新的事务。
COMMIT可以提交当前事务，是变更成为永久变更。
ROLLBACK可以 回滚当前事务，取消其变更。
SET [GLOBAL | SESSION] TRANSACTION ISOLATION LEVEL
{ READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SERIALIZABLE }  为事务设置隔离等级
delimiter //
create PROCEDURE abc()
begin
select * from abc;
insert into abc values('','1','xxxx','xxxxx');
select * from abc;
#COMMIT; #提交事务
ROLLBACK; #回滚
end;//
#函数
DELIMITER //
create FUNCTION f2(num1 smallint unsigned,num2 smallint unsigned)
returns float(10,2) unsigned   -- 返回值类型
begin
DECLARE x,y SMALLINT UNSIGNED DEFAULT 10;
set x = num1, y = num2;
RETURN x+y;
end//

#存储过程
create PROCEDURE
use mydb;
drop procedure abc \g
#SHOW PROCEDURE STATUS
#SHOW FUNCTION STATUS
show index from works;  查看索引
delimiter //
create PROCEDURE abc()
begin
DECLARE xid INT;  #局部变量
select * from abc;
select xid;
end;
//
#这里的更改不能实现！
delimiter //
alter PROCEDURE abc()
begin
select * from abc;
\G 竖行排列结果
insert into abc values('','1','xxxx','xxxxx');
select * from abc;
end;//
SHOW CREATE PROCEDURE abc \g
delimiter ;
call abc();
#游标
create procedure curdemo()
begin
declare done int default 0;
declare a char(16);
declare b,c int;
declare cur1 cursor for select * from abc;
declare cur2 cursor for select username from abc;
declare continue handler for sqlstate '02000' set done=1;

open cur1;
open cur2;
repeat
fetch cur1 into b,a;
fetch cur2 into c;
if not done then
if b


#多表级联 关联 查询
select
o.id id,o.oid oid,o.number number,o.seOrder seOrder,o.endprice endprice,--第一个表的字段
d.uid uid,d.oDatetime oDatetime,--第二个表的字段
p.proname proname,p.spec spec,p.material material,p.price price,--第三个表的字段
c.price1 price1,c.price2 price2,c.price3 price3,c.price4 price4,c.price5 price5 --第四个表的字段
from
orderlist o --表一
left join products p on o.pid=p.id --表二
left join orderForm d on d.id=o.oid --表三
left join classify c on p.bid=c.id --表四
--更多的表
order by o.id desc

1.INNER JOIN【以主字段为基础，匹配输出】交集】
遍历主表，每遍历一行数据，将此行数据取出进行条件判断，若副表中有满足条件的数据，则将副表中满足条件的行取出，与此时主表取出的这一行进行合并，完成一个新行的输出。若副表中有多处匹配，则输出多个新行，再进入下一次遍历；
2.LEFT JOIN【主字段全输出，不匹配虚拟】交集叠+主基不匹配NULL】
遍历主表，每遍历一行数据，将此行数据取出进行条件判断，若副表中有满足条件的数据，则将副表中满足条件的行取出，与此时主表取出的这一行进行合并，完成一个新行的输出。若副表中有多处匹配，则输出多个新行，再进入下一次遍历；[若附表中无匹配数据，则以副表的字段为模板虚拟出内容为NULL的一行数据，将其与主表数据合并]
3.RIGHT JOIN【副字段全输出，不匹配虚拟】交集叠+副基不匹配NULL】
同LEFT JOIN一样，只不过是交换了主次关系。以副表为基础遍历，来合并主表的内容。
4.FULL JOIN【并集+并集不匹配NULL】
事实上它是先执行了一次LEFT JOIN再执行一次RIGHT JOIN，最终取两次执行结果的并集。  

性能查看
flush status

LOAD DATA [LOW_PRIORITY] [LOCAL] INFILE 'file_name.txt' [REPLACE | IGNORE]  
   INTO TABLE tbl_name  
   [FIELDS  
       [TERMINATED BY '\t']  
       [OPTIONALLY] ENCLOSED BY '']  
       [ESCAPED BY '\\' ]]  
   [LINES TERMINATED BY '\n']  
   [IGNORE number LINES]  
   [(col_name,...)]  
LOAD DATA INFILE语句从一个文本文件中以很高的速度读入一个表中。如果指定LOCAL关键词，从客户主机读文件。如果LOCAL没指定，文件必须位于服务器上。


# 在[mysqld] 中輸入
#log
log-error=/usr/local/mysql/log/error.log
log=/usr/local/mysql/log/mysql.log
long_query_time=2
log-slow-queries= /usr/local/mysql/log/slowquery.log

show variables like 'log_error';

InnoDB: Error: pthread_create returned 12
skip-innodb



开启performance_schema
SHOW VARIABLES LIKE 'performance_schema'

performance_schema
performance_schema_events_waits_history_size=20
performance_schema_events_waits_history_long_size=15000

flush privileges; 刷新数据库！

MyISAM
   .myd  表数据
   .myi  索引信息
Innodb .ibd

.frm 表结构信息

主从日志
mysql-relay-bin.xxxxxn
mysql-relay-bin.index



myisam 并发低
innodb 并发高


mysql
   -H,--html”与“-X,--xml”
   --prompt=name  指定显示提示符
   --tee=name   执行指令存入文件

查看mysql 状态
mysqladmin -uroot -pyangyao ping
mysqladmin -uroot -pyangyao status  
mysqladmin -uroot -pyangyao processlist

mysqlbinlog  bin日志分析
如果需要从某个点恢复到某个点，用以下操作
定位：
--start-position 开始点
--stop-position 结束点
--start-date 开始时间
--stop-date  结束时间
现在恢复mysql-bin.000002恢复，从134点开始到386结束  
[root@localhost bin]# ./mysqlbinlog --no-defaults --start-position 134 --stop-position=386 ../var/mysql-bin.000002 | ./mysql -uroot -p

mysqladmin


安全关闭mysql
mysqladmin -u root -S /usr/local/mysql-slave/tmp/mysql.sock shutdown -p
#安全关闭 mysql
mysqladmin -uroot -pxxx shutdown -S /tmp/mysql3306.sock
kill -TERM pid

mysqladmin -uroot -r -i 1 -pxxx extended-status
-r --relative
-i --sleep

检查
mysqlcheck -uroot -prongfeng -P3306 -h192.168.2.25 mysql

mysqld --print-defaults  查看默认值

mysqlcheck
myisamchk


mysql -o mysql -e "select user,password from user" -uroot -ppassword
myisamchk
myisampack

Innodb 目录设置 不适合物理备份
innodb_data_home_dir
innodb_data_file_path
innodb_log_group_home_dir
innodb_file_per_table

行锁 表锁  页锁（少见）

show status like'table%';
show status like 'innodb_row_lock%';
show variables like '%binlog%'     查看日志信息
show variables like '%query_cache%';  查看缓存信息
show status like 'Qcache%';
show variables like 'table_cache';
show status like  'open_tables';
show variables like '%buffer%';
show status like 'innodb_log%';
show status like 'open_files';

查看打开文件数
flush tables;
show global status like 'open_%';  

互为主从  单主读写  另一主向slave写入



1.让数据库做她擅长的事情
   如md5等
   纯int  不超过 1000w
   含char 不超过 500w
2.保持表的身段苗条
   单表字段控制在20个以下
3.拒绝3B
   大SQL （BIG SQL）
   大事务（BIG Transaction）
   大批量（BIG Batch）

4.用好数据类型
tinyint(1Byte)
smallint(2B)
mediumint(3B)
int(4B)
bigint(8B)
float(4B)
double(8B)
decimal(M,D)

bad case
int(1) vs int(11)
bigint auto_increment
decimal(18,0)

5.将字符转化为数字
   例：用int存储ip
6.避免使用Null字段
   很难优化
   Null索引需要额外空间
7.少用并拆分Text/blob
数据库语言
1.DDL（Data Definition Language）数据库定义语言statements are used to define the database structure or schema.

DDL是SQL语言的四大功能之一。
用于定义数据库的三级结构，包括外模式、概念模式、内模式及其相互之间的映像，定义数据的完整性、安全控制等约束
DDL不需要commit.
CREATE
ALTER
DROP
TRUNCATE
COMMENT
RENAME

2.DML（Data Manipulation Language）数据操纵语言statements are used for managing data within schema objects.

由DBMS提供，用于让用户或程序员使用，实现对数据库中数据的操作。
DML分成交互型DML和嵌入型DML两类。
依据语言的级别，DML又可分成过程性DML和非过程性DML两种。
需要commit.
SELECT
INSERT
UPDATE
DELETE
MERGE
CALL
EXPLAIN PLAN
LOCK TABLE

3.DCL（Data Control Language）数据库控制语言  授权，角色控制等
GRANT 授权
REVOKE 取消授权

4.TCL（Transaction Control Language）事务控制语言
SAVEPOINT 设置保存点
ROLLBACK  回滚
SET TRANSACTION

SQL主要分成四部分：
（1）数据定义。（SQL DDL）用于定义SQL模式、基本表、视图和索引的创建和撤消操作。
（2）数据操纵。（SQL DML）数据操纵分成数据查询和数据更新两类。数据更新又分成插入、删除、和修改三种操作。
（3）数据控制。包括对基本表和视图的授权，完整性规则的描述，事务控制等内容。
（4）嵌入式SQL的使用规定。涉及到SQL语句嵌入在宿主语言程序中使用的规则。



show variables like 'slow_query%';
show variables like 'long_query_time';

set global slow_query_log='ON';
set global long_query_time=1;



mysqldumpslow

mysqldumpslow命令
/path/mysqldumpslow -s c -t 10 /database/mysql/slow-log
这会输出记录次数最多的10条SQL语句，其中：

-s, 是表示按照何种方式排序，c、t、l、r分别是按照记录次数、时间、查询时间、返回的记录数来排序，ac、at、al、ar，表示相应的倒叙；
-t, 是top n的意思，即为返回前面多少条的数据；
-g, 后边可以写一个正则匹配模式，大小写不敏感的；
比如
/path/mysqldumpslow -s r -t 10 /database/mysql/slow-log
得到返回记录集最多的10个查询。
/path/mysqldumpslow -s t -t 10 -g “left join” /database/mysql/slow-log
得到按照时间排序的前10条里面含有左连接的查询语句。
Memory table

其中query_time表示query语句的执行时间，但是为秒，lock time是锁定的时间，
rows_sent是query语句执行返回的记录数，而rows_examined则是优化器估算的扫描行数

InnoDB、MyIsam、Memory
如它们名字所指明的，Memory表被存储在内存中，且默认使用哈希索引。
建立
CREATE TABLE test ENGINE=MEMORY;
SELECT ip,SUM(downloads) AS down FROM log_table GROUP BY ip;
SELECT COUNT(ip),AVG(down) FROM test;
DROP TABLE test;

设置内存限制
SET max_heap_table_size = 1024*1024;
/* Query OK, 0 rows affected (0.00 sec) */
CREATE TABLE t1 (id INT, UNIQUE(id)) ENGINE = MEMORY;
/* Query OK, 0 rows affected (0.01 sec) */

SET max_heap_table_size = 1024*1024*2;
/* Query OK, 0 rows affected (0.00 sec) */
CREATE TABLE t2 (id INT, UNIQUE(id)) ENGINE = MEMORY;
/* Query OK, 0 rows affected (0.00 sec) */
mysql 缓存

MySQL> select @@query_cache_type;  
+--------------------+  
| @@query_cache_type |  
+--------------------+  
| ON |  
+--------------------+  

SELECT SQL_NO_CACHE * FROM my_table WHERE …

MySQL> set query_cache_type=off;  
MySQL> set query_cache_type=on;   php100.Com
MySQL>  
MySQL> select sql_cache id, title, body from article;  
MySQL> select sql_no_cache id, title, body from article;  
MySQL> show variables like 'have_query_cache';  
+------------------+-------+  
| Variable_name | Value |  
+------------------+-------+  
| have_query_cache | YES |  
+------------------+-------+   phP100.Com
1 row in set (0.00 sec)  
  查看MySQL 查询缓存的大小

#查询全局的事务隔离级别
SELECT @@global.tx_isolation;
#查询当前会话的事务级别
SELECT @@session.tx_isolation;

四种隔离级别
未提交读,已提交读,可重复读,可串行化


MySQL> select @@global.query_cache_size;  
+---------------------------+  
| @@global.query_cache_size |  
+---------------------------+  
| 16777216 |  
+---------------------------+  
1 row in set (0.00 sec)  
MySQL> select @@query_cache_size;  
+--------------------+   phP100.Com
| @@query_cache_size |  
+--------------------+  
| 16777216 |  
+--------------------+  
1 row in set (0.00 sec)
  查看最大缓存结果，如果结果集大于该数，不缓存。

MySQL> select @@global.query_cache_limit;  
+----------------------------+  
| @@global.query_cache_limit |  
+----------------------------+  
| 1048576 |  
+----------------------------+  
1 row in set (0.00 sec)
  碎片整理

MySQL> flush query cache  
-> ;  
Query OK, 0 rows affected (0.00 sec)
  清除缓存

MySQL> reset query cache   phP100.Com
-> ;  
Query OK, 0 rows affected (0.00 sec
  监视MySQL 查询缓存性能：

MySQL> flush tables;  
Query OK, 0 rows affected (0.04 sec)  
查看缓存设置
show variables like '%query_cache%'
缓存性能
MySQL> show status like 'qcache%';  
+-------------------------+----------+  
| Variable_name | Value |  
+-------------------------+----------+  
| Qcache_free_blocks | 1 |  
| Qcache_free_memory | 16768408 |  
| Qcache_hits | 6 |  
| Qcache_inserts | 36 |    PhP100.Com
| Qcache_lowmem_prunes | 0 |  
| Qcache_not_cached | 86 |  
| Qcache_queries_in_cache | 0 |  
| Qcache_total_blocks | 1 |  
+-------------------------+----------+  
8 rows in set (0.06 sec)  
  看看当前缓存中有多少条信息：

MySQL> show status like 'qcache_q%';  
+-------------------------+-------+  
| Variable_name | Value |  
+-------------------------+-------+  
| Qcache_queries_in_cache | 0 |  
+-------------------------+-------+  
1 row in set (0.00 sec)  
MySQL> select sql_cache id, title, body from article;  
MySQL> show status like 'qcache_q%';  PhP100.Com
+-------------------------+-------+  
| Variable_name | Value |  
+-------------------------+-------+  
| Qcache_queries_in_cache | 1 |  
+-------------------------+-------+  
1 row in set (0.00 sec)  
MySQL> show status like 'qcache_f%';  
+--------------------+----------+  
| Variable_name | Value |  
+--------------------+----------+   PhP100.cOm
| Qcache_free_blocks | 1 |  
| Qcache_free_memory | 16766728 |  
+--------------------+----------+  
2 rows in set (0.00 sec)  
log_bin

2012-08-04 16:03:42|  分类：mysql数据库|字号订阅
mysql< show BINARY logs;
+—————–+———–+
| Log_name | File_size |
+—————–+———–+
| mysqlbin.000001 | 107 |
+—————–+———–+
1 row in set (0.00 sec)
–查看当前bin_log情况
mysql< show master logs;
+—————–+———–+
| Log_name | File_size |
+—————–+———–+
| mysqlbin.000001 | 107 |
+—————–+———–+
1 row in set (0.00 sec)
–查看当前bin_log情况
mysql< show variables like ‘%log_bin%’;
+———————————+——-+
| Variable_name | Value |
+———————————+——-+
| log_bin | ON |
| log_bin_trust_function_creators | OFF |
| sql_log_bin | ON |
+———————————+——-+
3 rows in set (0.00 sec)
–查看log_bin相关配置
mysql< flush logs;
Query OK, 0 rows affected (0.06 sec)
–切换bin_log日志
mysql< PURGE BINARY LOGS TO ‘mysqlbin.000002′;
Query OK, 0 rows affected (0.03 sec)
–删除mysqlbin.000002之前的bin_log，并修改index中相关数据
mysql< PURGE BINARY LOGS BEFORE ’2011-07-09 12:40:26′;
Query OK, 0 rows affected (0.04 sec)
–删除2011-07-09 12:40:26之前的bin_log，并修改index中相关数据
mysql< PURGE BINARY LOGS BEFORE ’2011-07-09′;
Query OK, 0 rows affected (0.00 sec)
–删除2011-07-09之前的bin_log，并修改index中相关数据
mysql< set global expire_logs_days=5;
Query OK, 0 rows affected (0.00 sec)
–设置bin_log过期日期
mysql< reset master;
Query OK, 0 rows affected (0.02 sec)
–重设bin_log日志，以前的所有日志将被删除并且重设index中的数据

-- 左联去重
SELECT new_tab_fenshu.ShoolName, COUNT(*) AS task_num,g_schooltable.Name AS name_s
FROM new_tab_fenshu
LEFT JOIN g_schooltable ON new_tab_fenshu.ShoolName = g_schooltable.Name
GROUP BY ShoolName

-- 正则
SELECT *
FROM new_tab_fenshu2
WHERE (Y2015L NOT REGEXP "^[0-9]{3}$" OR Y2015W NOT REGEXP "^[0-9]{3}$")
AND (Y2015L NOT REGEXP "^[0-9]{3}$" AND Y2015W!="")
AND (Y2015W NOT REGEXP "^[0-9]{3}$" AND Y2015L!="")
and (Y2015L NOT REGEXP "^[0-9]{3}/[0-9]{3}$" OR Y2015W NOT REGEXP "^[0-9]{3}/[0-9]{3}$")
and (Y2015L not like "%.%" and Y2015W not like "%.%")

#delete from cs_id where id>=2000;

#存储过程

delimiter $$
drop procedure if exists HelloWorld;
CREATE PROCEDURE HelloWorld(IN p_id int unsigned,out nums int unsigned)
begin
declare i integer;
set i=1;
    loop1: while i<5000 do #(select count(*) from fenshu) do
    SELECT  i;
    set i=i+1000;
end while loop1;
end $$   #重点啊！
delimiter ;

call HelloWorld(11,@nums);
select @nums

#升级数据库
#mysql_upgrade -uroot -p
