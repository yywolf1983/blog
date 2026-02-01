
二进制安装
yum -y install make gcc-c++ cmake bison-devel ncurses-devel  readline-devel  libaio-devel perl libaio wget lrzsz vim libnuma* bzip2 xz

## 优化参照新装系统优化

wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.15-linux-glibc2.12-x86_64.tar.xz

tar xvf mysql-8.0.22-linux-glibc2.12-x86_64.tar.xz -C /data
mv /data/mysql-8.0.22-linux-glibc2.12-x86_64 /data/mysql-8.0.22/

useradd -r -s /sbin/nologin -d /data/mysql-8.0.22/ -m mysql

#排除其他可能
if [ -f /etc/my.cnf ]; then
    mv /etc/my.cnf /etc/my.cnf.`date +%Y%m%d%H%m`.bak
fi 


#建立配置文件
cat >/data/mysql-8.0.22/my_3306.cnf <<"EOF"
[client]
port    = 3306
socket    = /data/mysql-8.0.22/mysql_3306/tmp/mysql_3306.sock

[mysql]
prompt="\u@\h \R:\m:\s [\d]> "
no-auto-rehash

[mysqld]
user    = mysql
port    = 3306
admin_port=33062
mysqlx_port=33060
admin_address = 127.0.0.1
basedir    = /data/mysql-8.0.22
datadir    = /data/mysql-8.0.22/mysql_3306/data
socket    = /data/mysql-8.0.22/mysql_3306/tmp/mysql_3306.sock
pid-file = mysql_3306.pid
character-set-server = utf8mb4
skip_name_resolve = 1


#replicate-wild-ignore-table=mysql.%
replicate-wild-ignore-table=test.%
replicate-wild-ignore-table=information_schema.%

# Two-Master configure
#server-1 
#auto-increment-offset = 1
#auto-increment-increment = 2 

#server-2                          
#auto-increment-offset = 2
#auto-increment-increment = 2


# semi sync replication settings #
#plugin_dir = /usr/local/mysql/lib/mysql/plugin
#plugin_load = "validate_password.so;rpl_semi_sync_master=semisync_master.so;rpl_semi_sync_slave=semisync_slave.so"
plugin_dir = /data/mysql-8.0.22/lib/plugin #官方版本的路径
plugin_load = "rpl_semi_sync_master=semisync_master.so;rpl_semi_sync_slave=semisync_slave.so" #官方版本的路径

slave_parallel_workers = 4
slave_parallel_type = LOGICAL_CLOCK

open_files_limit = 65535
back_log = 1024
max_connections = 1024
max_connect_errors = 1000000
table_open_cache = 1024
table_definition_cache = 1024
table_open_cache_instances = 64
thread_stack = 512K
external-locking = FALSE
max_allowed_packet = 32M
sort_buffer_size = 4M
join_buffer_size = 4M
thread_cache_size = 1536
interactive_timeout = 600
#长链接不断开 默认值600
wait_timeout = 600
tmp_table_size = 32M
max_heap_table_size = 32M
slow_query_log = 1
log_timestamps = SYSTEM
slow_query_log_file = /data/mysql-8.0.22/mysql_3306/logs/slow.log
log-error = /data/mysql-8.0.22/mysql_3306/logs/error.log
long_query_time = 0.1
log_queries_not_using_indexes =1
log_throttle_queries_not_using_indexes = 60
min_examined_row_limit = 100
log_slow_admin_statements = 1
log_slow_slave_statements = 1
server-id = 3306
log-bin = /data/mysql-8.0.22/mysql_3306/logs/mysql-bin
sync_binlog = 1
binlog_cache_size = 4M
max_binlog_cache_size = 2G
max_binlog_size = 1G
binlog_expire_logs_seconds=2592000 
master_info_repository = TABLE
relay_log_info_repository = TABLE
gtid_mode = on
enforce_gtid_consistency = 1
log_slave_updates
slave-rows-search-algorithms = 'INDEX_SCAN,HASH_SCAN'
binlog_format = row
binlog_row_image=FULL
binlog_checksum = 1
relay_log_recovery = 1
relay-log-purge = 1
key_buffer_size = 32M
read_buffer_size = 8M
read_rnd_buffer_size = 4M
bulk_insert_buffer_size = 64M
myisam_sort_buffer_size = 128M
myisam_max_sort_file_size = 10G
myisam_repair_threads = 1
lock_wait_timeout = 3600
explicit_defaults_for_timestamp = 1
innodb_thread_concurrency = 0
innodb_sync_spin_loops = 100
innodb_spin_wait_delay = 30

#transaction_isolation = REPEATABLE-READ
transaction_isolation = READ-COMMITTED
#innodb_additional_mem_pool_size = 16M
innodb_buffer_pool_size = 2867M
innodb_buffer_pool_instances = 4
innodb_buffer_pool_load_at_startup = 1
innodb_buffer_pool_dump_at_shutdown = 1
innodb_data_file_path = ibdata1:1G:autoextend
innodb_flush_log_at_trx_commit = 1
innodb_log_buffer_size = 32M
innodb_log_file_size = 2G
innodb_log_files_in_group = 3
innodb_max_undo_log_size = 4G
innodb_undo_directory = /data/mysql-8.0.22/mysql_3306/undolog
innodb_undo_tablespaces = 95

# 根据您的服务器IOPS能力适当调整
# 一般配普通SSD盘的话，可以调整到 10000 - 20000
# 配置高端PCIe SSD卡的话，则可以调整的更高，比如 50000 - 80000
innodb_io_capacity = 4000
innodb_io_capacity_max = 8000
innodb_flush_sync = 0
innodb_flush_neighbors = 0
innodb_write_io_threads = 8
innodb_read_io_threads = 8
innodb_purge_threads = 4
innodb_page_cleaners = 4
innodb_open_files = 65535
innodb_max_dirty_pages_pct = 50
innodb_flush_method = O_DIRECT
innodb_lru_scan_depth = 4000
innodb_checksum_algorithm = crc32
innodb_lock_wait_timeout = 10
innodb_rollback_on_timeout = 1
innodb_print_all_deadlocks = 1
innodb_file_per_table = 1
innodb_online_alter_log_max_size = 4G
innodb_stats_on_metadata = 0

# some var for MySQL 8
log_error_verbosity = 3
innodb_print_ddl_logs = 1
binlog_expire_logs_seconds = 2592000
#innodb_dedicated_server = 0

innodb_status_file = 1
# 注意: 开启 innodb_status_output & innodb_status_output_locks 后, 可能会导致log-error文件增长较快
innodb_status_output = 0
innodb_status_output_locks = 0

#performance_schema
performance_schema = 1
performance_schema_instrument = '%memory%=on'
performance_schema_instrument = '%lock%=on'

#innodb monitor
innodb_monitor_enable="module_innodb"
innodb_monitor_enable="module_server"
innodb_monitor_enable="module_dml"
innodb_monitor_enable="module_ddl"
innodb_monitor_enable="module_trx"
innodb_monitor_enable="module_os"
innodb_monitor_enable="module_purge"
innodb_monitor_enable="module_log"
innodb_monitor_enable="module_lock"
innodb_monitor_enable="module_buffer"
innodb_monitor_enable="module_index"
innodb_monitor_enable="module_ibuf_system"
innodb_monitor_enable="module_buffer_page"
innodb_monitor_enable="module_adaptive_hash"
#validate_password_policy=LOW

[mysqldump]
quick
max_allowed_packet = 32M

[mysqld_safe]
#malloc-lib=/usr/local/mysql/lib/jmalloc.so 
nice=-19
open-files-limit=65535

EOF

#************ 配置文件结束

wget http://58.82.201.180:9999/soft/newhost/my_2378.cnf --http-user=soft --http-passwd=sdwlsoftadmin

#修改特殊需求
sed -i 's/wait_timeout =*$/wait_timeout = 31536000/g' /data/mysql-8.0.22/my_2378.cnf


mkdir -p /data/mysql-8.0.22/{mysql_3306,mysql_3306/logs,mysql_3306/data,mysql_3306/tmp}
mkdir -p /data/mysql-8.0.22/{mysql_2378,mysql_2378/logs,mysql_2378/data,mysql_2378/tmp}
mkdir -p /data/mysql-8.0.22/{mysql_2379,mysql_2379/logs,mysql_2379/data,mysql_2379/tmp}
chown -R mysql.mysql /data/mysql-8.0.22/

#初始化数据库
# 官方推荐使用--initialize，会在错误日志中生成难以输入的临时密码，我这里使用的免密码的方式。
/data/mysql-8.0.22/bin/mysqld --defaults-file=/data/mysql-8.0.22/my_2378.cnf --initialize-insecure  --user=mysql


#启动数据库
/data/mysql-8.0.22/bin/mysqld_safe --defaults-file=/data/mysql-8.0.22/my_3306.cnf & 

cat > /etc/systemd/system/mysqld.service << EOF

[Unit]
Description=MySQL Server
Documentation=http://dev.mysql.com/doc/refman/en/using-systemd.html
After=network.target
After=syslog.target

[Install]
WantedBy=multi-user.target

[Service]
User=mysql
Group=mysql


PIDFile=/data/mysql-8.0.22/mysql_2378/data/mysql_2378.pid

# Disable service start and stop timeout logic of systemd for mysqld service.
TimeoutSec=0

# Execute pre and post scripts as root
PermissionsStartOnly=true
# Needed to create system tables
#ExecStartPre=/usr/bin/mysqld_pre_systemd

# Start main service
ExecStart=/data/mysql-8.0.22/bin/mysqld_safe --defaults-file=/data/mysql-8.0.22/my_2378.cnf
# Use this to switch malloc implementation
#EnvironmentFile=-/etc/sysconfig/mysql

# Sets open_files_limit
LimitNOFILE = 5000

Restart=on-failure

RestartPreventExitStatus=1

EOF

systemctl start mysqld.service
systemctl status mysqld.service
systemctl enable mysqld.service


#首次登陆
/data/mysql-8.0.22/bin/mysql --socket=/data/mysql-8.0.22/mysql_2378/tmp/mysql_2378.sock


#修改密码
# ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'UbP*tzonifjZdP$jsvYu' PASSWORD EXPIRE NEVER ;
# ALTER USER 'root'@'%' IDENTIFIED  BY 'AnvcTMagdLarwNV3CKaC' PASSWORD EXPIRE NEVER ; 
update mysql.user set Host='%' where user='root';
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'AnvcTMagdLarwNV3CKaC' PASSWORD EXPIRE NEVER ;
flush privileges;


create user 'admin'@'%' identified with mysql_native_password by 'admin@123' PASSWORD EXPIRE NEVER ;
grant all PRIVILEGES on *.* to 'admin'@'%';

alter user 'root'@'localhost' identified with mysql_native_password by '123456'
flush privileges;

cat > /data/mysql_back.sh << EOF
#mysql 备份语句
date_str=\`date +%Y%m%d\`
mkdir -p /data/back
cd /data/back
host='127.0.0.1'
user='root'
port='2378'
password='AnvcTMagdLarwNV3CKaC'

/data/mysql-8.0.22/bin/mysql -P \$port -e "show databases;" -h \$host  -u\$user -p\$password | grep -Ev "Database|sys|information_schema|mysql|performance_schema" | xargs /data/mysql-8.0.22/bin/mysqldump -P \$port --skip-opt --single-transaction --master-data  --set-gtid-purged=OFF -R -e --max_allowed_packet=1048576 --net_buffer_length=16384 -h \$host -u\$user -p\$password --databases |  gzip > \$date_str.sql.gz
EOF

cat >> /var/spool/cron/root << EOF
01 00 * * * /usr/bin/sh /data/mysql_back.sh > /dev/null 2>&1
EOF

不锁库
--skip-opt --single-transaction --master-data 


分库备份
#mysql 备份语句
date_str=`date +%Y%m%d%H`
mkdir -p /data/back/${date_str}
cd /data/back/${date_str}
host='127.0.0.1'
user='root'
port='2378'
password='AnvcTMagdLarwNV3CKaC'
for i in `/data/mysql-8.0.22/bin/mysql -P $port -e "show databases;" -h $host  -u$user -p$password | grep -Ev "Database|sys|information_schema|mysql|performance_schema"`
 do
 echo $i
/data/mysql-8.0.22/bin/mysqldump -P $port --set-gtid-purged=OFF -R -e --max_allowed_packet=1048576 --net_buffer_length=16384 -h $host -u$user -p$password --databases $i |  gzip > $i.$date_str.sql.gz
done


create user 'hpdealer'@'%' identified with mysql_native_password by 'azpfT%aptxL^$XrBI&kk' PASSWORD EXPIRE NEVER ;
grant create,insert,delete,update,select on hpdealer.* to 'hpdealer'@'%' ;
flush privileges;

grant all privileges on *.* to 'admin_m'@'127.0.0.1' with grant option;




开启 general
set global log_output=file;

设置general log的日志文件路径：
set global general_log_file='/data/mysql-8.0.22/mysql_2378/logs/general.log';

开启general log：
set global general_log=on;

关闭general log：
set global general_log=off;



#快捷启动

cat  >>/root/.bashrc <<"EOF"

#
alias mysql.3306.start="/data/mysql-8.0.22/bin/mysqld_safe --defaults-file=/data/mysql-8.0.22/mysql_3306/my_3306.cnf &"
alias mysql.3306.stop="/data/mysql-8.0.22/bin/mysqladmin -h127.0.0.1 -P 3306 -uroot -p'AnvcTMagdLarwNV3CKaC' shutdown &"
alias mysql.3306.login="/data/mysql-8.0.22/bin/mysql -h127.0.0.1 -P 3306 -uroot -p'AnvcTMagdLarwNV3CKaC'"
EOF

source  /root/.bash_profile

/data/mysql-8.0.22/bin/mysql -uroot -pAnvcTMagdLarwNV3CKaC --socket=/data/mysql-8.0.22/mysql_3306/tmp/mysql_3306.sock


cat >>/etc/ld.so.conf <<"EOF"
/data/mysql-8.0.22/lib
EOF

ldconfig 

