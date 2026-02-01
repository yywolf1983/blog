


原子性(Atomicity )、一致性( Consistency )、隔离性或独立性( Isolation)和持久性(Durabilily)，简称就是ACID。

CAP 一致性(Consistency) ： 客户端知道一系列的操作都会同时发生(生效) 可用性(Availability) ： 每个操作都必须以可预期的响应结束 分区容错性(Partition tolerance) ： 即使出现单个组件无法可用,操作依然可以完成

一：数据查询语言（DQL:Data Query Language）：也称为“数据检索语句”，用以从表中获得数据，确定数据怎样在应用程序给出。 关键字：SELECT、WHERE、ORDER BY、GROUP BY、HAVING 二：数据操作语言（DML：Data Manipulation Language）：主要用于添加，修改和删除表中的行。 关键字：INSERT、UPDATE、DELETE 三：数据定义语言（DDL）：主要用于在数据库中创建新表或删除表（CREAT TABLE 或 DROP TABLE），为表加入索引等。 关键字：CREATE、DROP


DDL 数据定义
DDL is short name of Data Definition Language, which deals with database schemas and descriptions, of how the data should reside in the database.
CREATE - to create a database and its objects like (table, index, views, store procedure, function, and triggers)
ALTER - alters the structure of the existing database
DROP - delete objects from the database
TRUNCATE - remove all records from a table, including all spaces allocated for the records are removed
COMMENT - add comments to the data dictionary
RENAME - rename an object

DML 数据处理
DML is short name of Data Manipulation Language which deals with data manipulation and includes most common SQL statements such SELECT, INSERT, UPDATE, DELETE, etc., and it is used to store, modify, retrieve, delete and update data in a database.
SELECT - retrieve data from a database
INSERT - insert data into a table
UPDATE - updates existing data within a table
DELETE - Delete all records from a database table
MERGE - UPSERT operation (insert or update)
CALL - call a PL/SQL or Java subprogram
EXPLAIN PLAN - interpretation of the data access path
LOCK TABLE - concurrency Control

DCL 数据控制
DCL is short name of Data Control Language which includes commands such as GRANT and mostly concerned with rights, permissions and other controls of the database system.
GRANT - allow users access privileges to the database
REVOKE - withdraw users access privileges given by using the GRANT command

TCL 交易控制
TCL is short name of Transaction Control Language which deals with a transaction within a database.
COMMIT - commits a Transaction
ROLLBACK - rollback a transaction in case of any error occurs
SAVEPOINT - to rollback the transaction making points within groups
SET TRANSACTION - specify characteristics of the transaction
