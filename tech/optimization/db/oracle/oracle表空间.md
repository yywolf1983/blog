--1、查看表在那个表空间
select tablespace_name,table_name from user_talbes where table_name='test';
--2、获取用户的默认表空间
select   username,   DEFAULT_TABLESPACE     from   dba_users where username='MXH';
--3、查看表空间所有的文件
select * from dba_data_files where tablespace_name='USERS';
--4、查看表空间使用情况：
SELECT tbs 表空间名,
sum(totalM) 总共大小M,
sum(usedM) 已使用空间M,
sum(remainedM) 剩余空间M,
sum(usedM)/sum(totalM)*100 已使用百分比,
sum(remainedM)/sum(totalM)*100 剩余百分比
FROM(
SELECT b.file_id ID,
b.tablespace_name tbs,
b.file_name name,
b.bytes/1024/1024 totalM,
(b.bytes-sum(nvl(a.bytes,0)))/1024/1024 usedM,
sum(nvl(a.bytes,0)/1024/1024) remainedM,
sum(nvl(a.bytes,0)/(b.bytes)*100),
(100 - (sum(nvl(a.bytes,0))/(b.bytes)*100))
FROM dba_free_space a,dba_data_files b
WHERE a.file_id = b.file_id
GROUP BY b.tablespace_name,b.file_name,b.file_id,b.bytes
ORDER BY b.tablespace_name
)
GROUP BY tbs
--5、扩展表空间
alterdatabase datafile 'D:\ORACLE\PRODUCT\ORADATA\TEST\USERS01.DBF' resize 50m;
--自动增长
alterdatabase datafile 'D:\ORACLE\PRODUCT\ORADATA\TEST\USERS01.DBF' autoextend onnext 50m maxsize 500m;
--增加数据文件
alter tablespace USERS add datafile 'd:\users02.dbf' size 5m; 
