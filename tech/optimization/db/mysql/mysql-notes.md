

row 行
column 列
record 记录
RDBMS (Relational Database Management System)，

行格式
ROW_FORMAT=DYNAMIC 动态表 *****

DBI database interface
DBD database diiver

gcc -c -i${mysql_home}/include/mysql myclient.c

mysqld_safe
mysqld_multi  多库管理


* BUILD: 内含在各个平台、各种编译器下进行编译的脚本。
* Client: 客户端工具，如mysql, mysqladmin之类。
Dbug: 提供一些调试用的宏定义。
Extra: 提供innochecksum，resolveip等额外的小工具。
Include: 包含的头文件
Libmysql: 库文件，生产libmysqlclient.so。
Libservices: 5.5.0中新加的目录，实现了打印功能。
Man: 手册页。
Mysql-test: mysqld的测试工具一套。
* Mysys: 为跨平台计，MySQL自己实现了一套常用的数据结构和算法，如string, hash等。
Plugin: mysql以插件形式实现的部分功能。
Scripts: 提供脚本工具，如mysql_install_db等
Sql: mysql主要代码，将会生成mysqld文件。
Sql-bench: 一些评测代码。
Sql-common: 存放部分服务器端和客户端都会用到的代码。
* Storage: 存储引擎所在目录，如myisam, innodb, ndb等。
Strings: string库。
Support-files: my.cnf示例配置文件。
Tests: 测试文件所在目录。
Unittest: 单元测试。
Vio: virtual io系统，是对network io的封装。
Win: 给windows平台提供的编译环境。
Zip: zip库工具


语义分析 --》数据库读写 --》

网络协议
sql/potoclol.cc
sql/protocol.h
sql/net_serv.cc

查询分析
sql/sql_parse.cc    GNU bison 词法分析器
sql/sql_select.cc    查询分析
  mysql_select
sql/password.cc      
sql/sql_delete.cc
sql/sql_do.cc
sql/sql_help.cc
sql/sql_insert.cc
sql/sql_show.cc
sql/sql_update.cc

核心
  线程类 THD
    sql/sql_const.h 定义线程优先级。
    #define INTERRUPT_PRIOR 10
    #define CONNECT_PRIOR	9
    #define WAIT_PRIOR	8
    #define QUERY_PRIOR	6
  sql/sql_class.cc  实现线程
  sql/table.cc      表描述
  内存操作
  文件系统操作
  I/O缓存
  Strings 操作
  宏定义

核心算法
  位图 位代替算法 类似字符映射显示。
  表连接缓冲
  mysql排序
  字符集校队

网络连接
  sql/net_serv.cc
    包最大长度
    #define MAX_PACKET_LENGTH (256L*256L*256L-1)  

    错误定义
    libmariadb/include/ma_server_error.h
      #define ER_HASHCHK 1000  /* no longer in use ?! */
      #define ER_NISAMCHK 1001 /* no longer in use ? */
      #define ER_NO 1002
      #define ER_YES 1003


    连接 --》 握手 --》 认证 --》 返回结果集


线程管理
   进程 线程 锁
   线程同步
   sql/main.cc --> mysqld.cc

内存分配
  索引缓存 key buffer
  查询高速缓存 query cache
  表缓存 Table cache
  线程缓存 Thread cache
  二进制缓冲区 binlog buffer

  mysys/mf_cache.c
  mysts/mf_keycache.c

  内存分配
    mysys/my_malloc.c

  表缓存
    sql/sql_base.cc


查询解析优化
  语法分析 Lexical analysis or Scanner
  词法分析 Syntax analysis or Parser

  gnu bison

  sql/sql_yyac.cc  词法分析
  sql/lex.h        语法定义
  sql/sql_lex.cc   语法分析

安全认证
  sql/sql_acl.cc
  sql/password.c
  sql/sql_parse.cc   用户验证
  sql/parse.cc       权限认证

  sql 注入防范

引擎接口
  frm 元数据文件  sql/table.cc
  myd myisam 数据文件
  myi myisam 索引文件
  ibd innodb 索引

日志系统
  sql/log.cc
  慢查询日志 slow_log_print
  二进制日志 不记录查询语句

复制 replication (主从)
  binlog dump to slave
  index  log index
  info   io info
  sql/sql_repl.cc


set tags=~/Downloads/soft/mysql-8.0.11/tags
