1. 建立需要的目录
mkdir -p export/oracle/product/10.2.0/admin/bdump
mkdir -p export/oracle/product/10.2.0/admin/cdump
mkdir -p export/oracle/product/10.2.0/admin/dpdump
mkdir -p export/oracle/product/10.2.0/admin/udump
mkdir -p export/oracle/product/10.2.0/admin/adump
mkdir -p export/oracle/product/10.2.0/archive
mkdir -p export/oracle/product/10.2.0/oradata
mkdir -p export/oracle/product/10.2.0/flash_recovery_area

2. 设置环境变量，在用户环境变量里面加.
$ export ORACLE_BASE=/export/oracle
$ export ORACLE_HOME=$ORACLE_BASE/product/10.2.0/db_1
$ export ORACLE_SID=risotest


3. 建初始化参数文件
$ vi $ORACLE_HOME/dbs/initrisotest.ora        切忌此处instancename 大小写于环境变量定义不一致
#以下为建库必需参数
control_files = '/epxort/oracle/product/10.2.0/oradata/control1.ctl','/epxort/oracle/product/10.2.0/oradata/control2.ctl','/epxort/oracle/product/10.2.0/oradata/control3.ctl'
undo_management = 'AUTO'
undo_tablespace = 'UNDOTBS1'
db_name = 'risotest'
db_block_size = 8192
sga_max_size = 167M
sga_target = 167M
audit_file_dest = 'export/oracle/product/10.2.0/admin/adump'        #不设置默认$ORACLE_HOME/rdbms/adump
background_dump_dest = 'export/oracle/product/10.2.0/admin/bdump'   #不设置默认$ORACLE_HOME/rdbms/log
core_dump_dest = 'export/oracle/product/10.2.0/admin/cdump'         #不设置默认$ORACLE_HOME/rdbms/dbs
user_dump_dest = 'export/oracle/product/10.2.0/admin/udump'         #不设置默认$ORACLE_HOME/rdbms/log
db_domain = ''                                                    #不设置默认为空
open_cursors = 1500                                               #不设置默认50
processes = 250                                                   #不设置默认40,根据具体业务多少，设大小,可以改的,无所谓.
log_archive_dest_1 = 'export/oracle/product/10.2.0/admin/archive'    #不设置默认为空，归档存储在$ORACLE_HOME/rdbms/dbs/arch
log_archive_format = 'log_%t_%s_%r.arc'                           #不设置默认为%t_%s_%r.dbf
job_queue_processes = 10                                          #不设置默认为0
undo_retention = 10800                                            #不设置默认为900                                                     
#audit_sys_operations = 'TRUE'                                     #如果需要开通审计功能，设置如下参数
#audit_trail = db,extended                                         #这里注意，如果将来会转换成物理备库，这里就不能设置db，否则将来物理备库没法打开read only模式
db_recovery_file_dest = 'export/oracle/product/10.2.0/admin/flash_recovery_area' #OMF模式必需设置
db_recovery_file_dest_size = 2G                                   #OMF模式必需设置


#如果采用OMF管理数据库文件，则还需设置以下参数
db_create_file_dest = 'export/oracle/product/10.2.0/admin/oradata' #自动在该目录下建立./{db_name}/datafile 目录
db_create_online_log_dest_1 = 'export/oracle/product/10.2.0/admin/oradata' #自动在该目录下建立./{db_name}/onlinelog 目录


4. 建立密码文件,使用操作系统验证就不要下面这一行，使用口文件验证就用这一行:具体看sqlnet 中的设置
$ORACLE_HOME/bin/orapwd file=$ORACLE_HOME/dbs/orapw$ORACLE_SID password=123456 force=y


5. 建spfile后启动实例并开始建库
$ sqlplus '/as sysdba'
SQL> startup nomount pfile=$Oracle_HOME/dbs/init$ORACLE_SID.ora
SQL> create spfile from pfile; 重启用spfile再进入nomount状态,
SQL> create database risotest
user sys identified by sys
user system identified by system
logfile group 1 ('/export/oracle/product/10.2.0/oradata/redo01.log') size 50m,
group 2 ('/export/oracle/product/10.2.0/oradata/redo02.log') size 50m,
group 3 ('/export/oracle/product/10.2.0/oradata/redo03.log') size 50m
maxlogfiles 5 maxlogmembers 5 maxloghistory 1
maxdatafiles 100 maxinstances 1
character set zhs16gbk national character set al16utf16
datafile '/export/oracle/product/10.2.0/oradata/system01.dbf' size 500m reuse
extent management local
sysaux datafile '/export/oracle/product/10.2.0/oradata/sysaux01.dbf' size 250m autoextend on next 10M maxsize unlimited
default temporary tablespace temp
tempfile '/export/oracle/product/10.2.0/oradata/temp01.dbf' size 260m reuse
undo tablespace undotbs datafile '/export/oracle/product/10.2.0/oradata/undotbs01.dbf' size 60m reuse autoextend on maxsize


6. 运行数据字典脚本，其中catalog和catproc是必需的，其它可选：
SQL> spool /orahome/cat.log
SQL> @?/rdbms/admin/catalog.sql       （建数据字典视图）
SQL> @?/rdbms/admin/catproc.sql       （建存储过程包）
SQL> @?/rdbms/admin/catblock.sql   （建锁相关的几个视图）
SQL> @?/rdbms/admin/catoctk.sql       （建密码工具包dbms_crypto_toolkit）
SQL> @?/rdbms/admin/owminst.plb       （建工作空间管理相关对象，如dmbs_wm）
SQL> spool off
执行完后检查/orahome/cat.log看看有什么不可接受的错误没有。


7. 新建sqlplus属性和帮助、USERS表空间
SQL> alter user sys identified by 123;
SQL> alter user sys identified by 123;
SQL> connect system/iamwangnc
SQL> @?/sqlplus/admin/pupbld.sql
SQL> @?/sqlplus/admin/help/hlpbld.sql helpus.sql
SQL> connect /as sysdba
SQL> CREATE TABLESPACE USERS LOGGING DATAFILE '/export/oracle/product/10.2.0/oradata/users01.dbf' SIZE 100M REUSE AUTOEXTEND ON NEXT 10m MAXSIZE UNLIMITED EXTENT MANAGEMENT LOCAL SEGMENT SPACE MANAGEMENT AUTO;
SQL> ALTER DATABASE DEFAULT TABLESPACE USERS;
SQL> ALTER USER SYS TEMPORARY TABLESPACE TEMP;


8. 最后修改为归档模式并重启
SQL> shutdown immediate;
SQL> connect /as sysdba
SQL> startup mount
SQL> alter database archivelog;
SQL> alter database open;
重新编译所有失效过程：
SQL> execute utl_recomp.recomp_serial();


SQL> create pfile from spfile;


调整tnsnames.ora和listener.ora文件,让外部登陆.
