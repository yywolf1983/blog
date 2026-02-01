shutdown immediate;

netca
netmgr
dbca

cp /data/oracle/admin/SAM/pfile/init.ora /data/oracle/11g/dbs/initSAM.ora

环境变量
export ORACLE_BASE=/data/oracle
export ORACLE_SID=orcl
export ORACLE_HOME=$ORACLE_BASE/11g
#NLS_LANG=ZHS16GBK
export PATH=$ORACLE_HOME/bin:$PATH:



--数据库（Database, DB）

--数据库管理系统（Database Management System, DBMS）

--数据库管理员（  Database Administrator, DBA）

--数据库系统（  Database System, DBS ）



--DML语句（数据操作语言）Insert、Update、  Delete、Merge   改变数据结构

--DDL语句（数据定义语言）Create、Alter、  Drop、Truncate

--DCL语句（数据控制语言）Grant、Revoke

--事务控制语句Commit 、Rollback、Savepoint



Commit； 提交

Rollback； 回滚

-- sqlplus /nolog

-- sqlplus "sys/123456 as sysdba"

connect /as sysdba

修改临时文件大小
alter database tempfile 'F:\oracle\product\10.1.0\oradata\orcl\TEMP01.DBF' resize 2048M;

select name from v$database;



lsnrctl start  LISTENER

lsnrctl stop



启动监听

startup;

cmd-->lsnrctl start

update dcw_weibo set todo="0" where todo="1"

net manager  配置监听程序

Net Configuration Assistant   配置管理

/network/admin/tnsnames.ora



startup  启动控制文件 和数据文件

startup mount  启动控制文件

startup nomount 启动实例不启动控制文件



shutdown immediate  用户执行完成后断开

shutdown abort  强行关闭



help index    sqlplus帮助

？set   查看命令帮助



select * from dba_users where ACCOUNT_STATUS='OPEN';



Save c:\1.txt  --把SQL存到文件

Ed c:\1.txt   --编辑SQL语句

@ c:\1.txt    --运行SQL语句

Desc emp;  --描述Emp结构



col   字段重命名

spool  c:\1.txt   保存结果集合

select * from dba_users;

spool off

继续添加

spool 1.txt append



show user;



/ --执行上一条语句



-- 日期处理

-- to_date('2013-6-6 14:52:34','yyyy-MM-dd HH24:mi:ss')



select * from dba_users where username like '%SY%' and ACCOUNT_STATUS='OPEN' ;



select * from dba_users where  password is NULL and user_id=30;

select * from dba_users where  password is not NULL and user_id=30;



select * from dba_users where (username like '%SY%' and ACCOUNT_STATUS='OPEN') and username not in('SYSMAN');

select * from dba_users where (username like '%SY%' and ACCOUNT_STATUS='OPEN') or user_id=88 order by user_id desc;  --反序



Select sal+comm,ename from emp;



Select distinct account_status from dba_users;   --去除重复行



select months_between('EXPIRY_DATE') from dba_users;



select decode(user_id, 10, '财务部', 20, '研发部', 30, '销售部', '未知部门') 部门 from dba_users;   --条件查询



select

case user_id  

 when 10 then '财务部'

 when 20 then '研发部'

 when 30 then '销售部'

else '未知部门'       

 end  部门

from dba_users;



select count(*) from dba_users;



--关联查询

select username from dba_users where user_id = (select max(user_id) from dba_users where user_id=72);  

--如果子查询中返回的是空，则目标字段也更新成NULL.



--多表查询

select empno, ename, sal, emp.deptno, dname from emp, dept where emp.deptno = dept.deptno;



--笛卡尔集

Select * from emp,dept;



--左联

select empno,ename,dname from emp left outer join dept on emp.deptno = dept.deptno;



--右联

select empno,ename,dname from emp right outer join dept on emp.deptno = dept.deptno;



--满外联接（Full Outer Join）

select empno,ename,dname from emp full outer join dept on emp.deptno = dept.deptno;





 -- UNION：并集，所有的内容都查询，重复的显示一次

 -- UNION  ALL：并集，所有的内容都显示，包括重复的

 -- INTERSECT：交集：只显示重复的

 -- MINUS：差集：只显示对方没有的（跟顺序是有关系的）

SELECT  *  FROM  emp  UNION  SELECT  *  FROM  emp20  ;



-- 分页查询

select *  

from  

(select rownum no,e.* from (select * from dba_users order by user_id desc) e)

where  

no>=2 and no<=10;



-- 连续求和  sum(user_id) over(order by user_id)

select sum(user_id) over(order by user_id),user_id from dba_users where user_id<1000;



--查询某用户下所有表

select table_name from all_tables where owner='SCOTT';



--查询EMP表中所有字段（列）

select * from all_tab_columns where table_name='EMP';





-- 数据类型

--Char,nchar,varchar2,nvarchar2,number(),date,blob(binary 二进制流的大对象),clob（文件大对象）

--注意： ----------------

--1、 由于char是以固定长度的，所以它的速度会比varchar2快得多!但程序处理起来要麻烦一点，要用trim之类的函数把两边的空格去掉

--2、 Varchar2一般适用于英文和数字，Nvarchar2适用中文和其他字符，其中N表示Unicode常量，可以解决多语言字符集之间的转换问题  

--3、 Number(4,2) 指的是整数占2位，小数占2位(99.994可以。99.995不行，因为是四舍五入)

--4、 Number默认为38位





-- 一系列物理文件（数据文件，控制文件，联机日志等）的集合或与之对应的逻辑结构（表空间，段等）被称为数据库



--物理存储结构

Desc v$logfile;

Select member from v$logfile;     #查看日志文件

V$controlfile    控制文件

V$datafile;        数据文件



select * from v$tablespace; --查看表空间

select * from v$datafile;  --查看数据空间



查看表空间容量

select * from dba_data_files;

select * from dba_free_space;



--查看表空间大小

select tablespace_name,sum(bytes)/1024/1024 M  from dba_data_files group by tablespace_name;



--查看表空间以使用的大小

select tablespace_name,sum(bytes)/1024/1024 M from SYS.dba_free_space group by tablespace_name order by M  ;







参数文件



SGA （系统全局区）

    DB高速缓存区

        保持缓存池 （长期保存）

        再生缓存池 （频繁使用）

        默认缓存池

    大共享区

    共享池

        库缓存区

            共享sql区

            PL/sql区

        字典缓存区

    日志缓存区

    固定SGA



逻辑结构

    数据文件

    表空间

    段

    盘区

    块

        windows 8K





-- Oracle实时应用集群（RAC, Real Application Clusters）

-- 数据库服务名（ Database Service_Name）

-- 网络服务名（Net Service Name）

-- 监听器（Monitor）



create temporary tablespace test_temp  --创建临时表空间

create tablespace test_data            --创建数据空间

create user testserver_user identified by testserver_user  --创建表空间并指定用户



CREATE TABLESPACE data01

DATAFILE '/oracle/oradata/db/DATA01.dbf' SIZE 500M

UNIFORM SIZE 128k; --指定区尺寸为128k,如不指定，区尺寸默认为64k



SQL> create tablespace test_data datafile 'D:\oracle\yy\oradata\yytest\test_date.dbf' size 1G;



添加已有文件

create tablespace test_data datafile 'D:\oracle\yy\oradata\yytest\TEST_DATA.DBF'



1.修改状态 在线（ONLINE）、离线（OFFLINE）、只读（READ ONLY）和读写（READ WRITE）

alter tablespace temp OFFLINE;

2.查看表空间数据文件大小

select file_name,bytes from dba_data_files;

3.修改表空间数据文件的大小，添加数据文件

alter database DATAFILE 'd:\table.dbf' resize 10m;

alter tablespace  test_data(表空间名) add datafile 'd:\table2.dbf' size 5m;

4.修改表空间数据文件的自动扩展性

alter database datafile 'd:\table.dbf' AUTOEXTEND ON next 5m maxsize 50m;

5.移动表空间数据文件

1).设置数据文件状态为离线OFFLINE:      alter tablespace SIMPLE OFFLINE;

2).复制数据文件

3).重新指定表空间路径    alter tablespace SIMPLE RENAME DATAFILE 'E:\table2.dbf' to 'D:\table.dbf';

4).重新设置数据文件状态为离线onLINE



删除表空间

drop tablespace test_data

表空间非空，,可加上including contents子句.

drop tablespace test_data  including contents;

如果想在删除表空间的同时也删除掉对应的数据文件,加上 and datafiles

drop tablespace test_data including contents and datafiles;



删除临时表空间

 ALTER DATABASE TEMPFILE ‘d:\oracle\oradata\orcl\temp01.dbf’ DROP INCLUDING DATAFILES ;



删除表空间

alter database *** datafile ***** offline drop;



需要介质恢复时使用

recover datafile '新的数据文件路径';

用标号也可以

recover datafile 9;



--创建表

Create table student(

Sid number(10),

Sname varchar2(10)

) tablespace tt;



-- tablespace tt;  指定表空间



--查询(当前用户)默认表空间

select default_tablespace from user_users;





--创建查询建表

create table myemp as select * from emp;

create table myemp as select * from emp where deptno=10;

create table myemp as select * from emp 1=2;

select * from myemp;

drop table myemp;



Alter table student add age number(5);   --添加字段

alter table table2 rename column result to result2;  --修改字段

Alter table student drop column age;  --删除字段

Truncate table myemp --清空表 可回滚



如果发现删除错了，则可以通过 rollback 回滚。

rollback



Drop table student;  --删除表

Rename student to student1;  --重命名表



-- NOT NULL：非空约束

-- PRIMARY KEY：主键约束

-- UNIQUE：唯一约束，值不能重复（空值除外）

-- CHECK：条件约束，插入的数据必须满足某些条件

-- Foreign Key：外键

  -- pid NUMBER REFERENCES 表(pid) ON DELETE CASCADE             -- ON DELETE CASCADE 级联删除



-- 建立约束：book_pid_fk，与person中的pid为主-外键关系

-- CONSTRAINT book_pid_fk FOREIGN KEY(pid) REFERENCES 表(pid)        --参照

    CONSTRAINT  命名   --别名, 强制；限制；约束



-- 删除约束

ALTER TABLE book DROP CONSTRAINT 表_book_pid_fk ;

-- 启用约束

ALTER TABLE book enable CONSTRAINT 表_book_pid_fk ;

-- 禁用约束

ALTER TABLE book disable CONSTRAINT 表_book_pid_fk ;

-- 添加约束

alter table student add constraint MY_CONSTRAINT_1 unique(tel);

--条件约束

alter table 表 add constraint 字段 check(tel="1" or tel="2");

--查看constraint

select constraint_name, constraint_type from user_constraints



--  视图      封装的select语句

CREATE VIEW 视图名字(字段) AS 子查询



-- 只读视图

  CREATE OR REPLACE VIEW empv20 (empno,ename,sal,deptno)

AS SELECT empno,ename,sal,deptno FROM emp WHERE deptno=20

WITH READ ONLY;



with check option；  限制条件



Select text from user_views;  --查看视图



select * from  user_indexes --查询现有的索引  

select * from  user_ind_columns --可获知索引建立在那些字段上



系统数据字典表

user_views

dba_views

all_views





-- 创建索引

create index abc on student(sid,sname);

--对常常查询的大于5M的表有好处

drop index abc



declare  --可以没有

 --声明

        x varchar2(10);

 cou NUMBER ;

begin

  DBMS_OUTPUT.put_line('底工资。。。'||x) ; --||连接字符串

 --主题

exception

 --异常捕获

end;



declare

    x varchar2(10);

begin

    x:='this num';

    DBMS_OUTPUT.put_line('x='||x);

    DBMS_OUTPUT.new_line;

end;



-- oracle 默认不显示

set serveroutput on



--判断是否有数据存在

mycur%FOUND



--可以使用 ROWCOUNT对游标所操作的行数进行记录。

%ROWTYPE



--声明游标

 CURSOR mycur(id varchar2) IS 游标参数



 CURSOR mycur IS SELECT * FROM emp where empno=-1;

 OPEN mycur ;

 --游标向下一行

 FETCH mycur INTO empInfo ;

 --判断游标是否打开

 mycur%ISOPEN

 %found  游标内是否有数据

 %notfound

 %rowcount   --游标计数器



CLOSE mycur  关闭游标





LOOP  

   --循环语句;

  EXIT WHEN cou>10 ;

   --

END LOOP;



 while(判断循环的条件) loop

  循环的语句  ;

  循环条件的改变  ;

 End loop ;



 FOR 变量名称  in  变量的初始值..结束值  LOOP

  循环语句  ;

 END LOOP ;



  IF  条件  THEN

  满足条件时，执行此语句

 END IF ;

 --IF…ELSIF…ELSE



case

 when ... then ...

        ...

else

        ...

end case



 goto po1 ;

 <<po1>>



--函数

CREATE OR REPLACE FUNCTION myfun(eno emp.empno%TYPE) RETURN NUMBER

AS

 rsal NUMBER ;

BEGIN

 SELECT (sal+nvl(comm,0))*12 INTO rsal FROM emp WHERE empno=eno ;

 RETURN rsal ;

END ;



--同义词

create synonym  同义词 for 库.表

drop synonym  



create public synonym  公共同义词



user_synonyms



--序列

create sequence myseq

start with 1    --开始值

increment by 1  --递增值

order             --排序  asc或desc（即升级或降序）

nocycle;        --唯一值



dual是一个虚拟表，用来构成select的语法规则，oracle保证dual里面永远只有一条记录。

select myseq.nextval from dual;

select myseq.currval from dual;  --当前值



--使用序列

insert into auto values(myseq.nextval)



alter sequence myseq

increment by 1;  --更改递增值



dba_sequences;    --序列信息

all_sequences;

user_sequences;

--存储过程

CREATE OR REPLACE PROCEDURE myproc

AS

 i NUMBER ;

BEGIN

 i := 100 ;

 DBMS_OUTPUT.put_line('i = '||i) ;

END ;



--show errors



exec myproc;

drop procedure myproc;





--触发器

create or replace trigger tr_src_emp

after delete on emp_2

--before insert or update or delete on emp_2

--查询触发器种类及类型



for each row --行触发

begin

    delete  from emp where id=:old.id;

end tr_src_emp;



--内存表

--:old delete update

--:new insert update



--事务

 --原子性

 --一致性

 --隔离性

 --持久性



raise_application_error(-2000,'不能干什么')；  --抛出错误



超级管理员：sys/sys

普通管理员：system/system

-- 创建用户 test 密码 admin

create user test identified by admin

Drop user test;



--级联删除用户表

Drop user test cascade;



--授权访问权限

create session TO test ;

--授权角色   角色是权限的集合

GRANT CONNECT,RESOURCE TO test ;

--权限传递

Grant create session to test with admin option;





--允许向其他用户授权 级联授权

Grant select on 表 to test with Grant option;

--系统授权

Grant select on 表 to test with admin option;





--１．CONNECT, RESOURCE,  DBA

--这些预定义角色主要是为了向后兼容。其主要是用于数据库管理。oracle建议

--用户自己设计数据库管理和安全的权限规划，而不要简单的使用这些预定角色。

--将来的版本中这些角色可能不会作为预定义角色。

--２．DELETE_CATALOG_ROLE， EXECUTE_CATALOG_ROLE， SELECT_CATALOG_ROLE

--这些角色主要用于访问数据字典视图和包。

--３．EXP_FULL_DATABASE， IMP_FULL_DATABASE

--这两个角色用于数据导入导出工具的使用。



--对象授权

GRANT 权限（select、update、insert、delete、connect，all，create，drop）  ON schema.table TO 用户

--权限回收

REVOKE select ON scott.emp FROM test ;



--锁住一个用户

ALTER USER 用户名  ACCOUNT LOCK|UNLOCK



--密码失效

ALTER USER test PASSWORD expire ;



--查看权限

select * from user_sys_privs;



--角色就是一堆权限的集合

Create role myrole;

Grant create table to myrole;

Drop role myrole;  删除角色



--修改表空间

ALTER USER test DEFAULT TABLESPACE baobao



create user IMIS

  identified by "ttzhzx_ttdd2013"

  default tablespace ITS_DATA

  temporary tablespace ITS_TEMP

  profile DEFAULT;

-- Grant/Revoke role privileges

grant connect to IMIS;

grant dba to IMIS;



--创建表空间

CREATE TABLESPACE baobao121

DATAFILE '/opt/oracle/oradata/baobaodata/baobao.dbf' SIZE 200M

AUTOEXTEND ON NEXT 50M

EXTENT MANAGEMENT LOCAL

SEGMENT SPACE MANAGEMENT AUTO;



create temporary tablespace baobao_temp  

tempfile '/opt/oracle/oradata/baobaodata/baobao_temp.dbf' size 50M

AUTOEXTEND ON    NEXT 50M

EXTENT MANAGEMENT LOCAL;



--添加用户

create user baobao identified by baobao  

DEFAULT TABLESPACE baobao

temporary tablespace baobao_temp;



--增加权限

grant all privileges to baobao



--连接

conn baobao/baobao;

--查看用户

show user;



--外部命令

imp --导入

exp --导出



-- 表迁移办法

create table B as select * from A@dblink where ...，

insert into B select * from A@dblink where ...



--表间数据拷贝  

insert into dept1(id, name) select deptno, dname from dept;



--数据库设计规范

--字段要设计的不可再拆分

--两个表的关系，在第三张关系表中体现

--多张表中，只存关系，不存具体信息（具体开发中用的最多）

--数据库表关联越少越好，SQL语句复杂度越低越好





系统函数

select  length('字符长度')  from dual； --字符长度



--系统函数

select  length('字符长度')  from dual； --字符长度



select lengthb('字节长度ddd') from dual;  --字节长度



select trim('  ddsad  aaa ') from dual;  --去掉两端空格

select rtrim('  ddsad ') from dual;  --去掉空格

select ltrim('  ddsad ') from dual;  --去掉空格



select substr('abcdefgh',2,3) from dual; --取指定字符

select substr('abcdefgh',length('abcdefgh')-3+1,3) from dual; --右取字符串



select sysdate from dual;  --当前时间

select current_date from dual;

alter session set nls_date_format='yyyy-mon-dd hh:mi:ss'; --设置日期格式



select to_char(sysdate) from dual;

select to_date('2012-2月-14') from dual;



--聚集函数

select * from dba_users;

select count(*) from dba_users;

select max(user_id) from dba_users; --最大值

select min(user_id) from dba_users; --最小值

select sum(user_id) from dba_users; --合计

select avg(user_id) from dba_users; --平均值



select user from dual;  --查看登录用户

select sum(decode(account_status,'OPEN',1,0)) 可用用户数 from dba_users;

select user_id,nvl(password,'用户未锁') 密码为空 from dba_users;  --空值处理



卸载oracle

D:\oracle\product\11.2.0\dbhome_2\deinstall>deinstall.bat
