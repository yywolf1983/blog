clush -b -a "yum -y install perl perl-devel perl-Time-HiRes perl-DBD-MySQL perl-Digest-MD5 rsync libev libaio"


wget  http://47.52.97.39/file/mysqlback/percona-xtrabackup-80-8.0.22-15.1.el7.x86_64.rpm
rpm -ivh percona-xtrabackup-80-8.0.22-15.1.el7.x86_64.rpm

clush -b -a "xtrabackup --version"


all_back_PATH=/data/back/allback
PORT=2378
IP=127.0.0.1
USER=root
PASSSWORD=AnvcTMagdLarwNV3CKaC
CONFIG=/data/mysql-8.0.22/my_2378.cnf
INC_PATH=/data/back/inc

rm -rf /data/back/inc

添加权限
mysql -u${USER} -p${PASSSWORD} -h${IP} -P${PORT}
GRANT BACKUP_ADMIN ON *.* TO 'root'@'%';
flush privileges;

全量备份
/usr/bin/xtrabackup --defaults-file=${CONFIG} --backup  --user=${USER}  --password=${PASSSWORD} --host=${IP} --port=${PORT}  --extra-lsndir=${all_back_PATH} --target-dir=${all_back_PATH}
压缩备份
--compress --compress-threads=4
流备份
--stream=xbstream /tmp >/backup/bak.xbstream  
流备份指定chek
--extra-lsndir=/data/back/chkpoint 
增量
--incremental-basedir=/data/back/chkpoint

流备份 解压要 qpress 支持
http://www.quicklz.com/qpress-11-linux-x64.tar

/usr/bin/xtrabackup --defaults-file=${CONFIG} --backup  --user=${USER}  --password=${PASSSWORD} --host=${IP} --port=${PORT}  --target-dir=/data/back/test --extra-lsndir=/data/back/chkpoint --compress --compress-threads=8 --stream=xbstream >/data/back/test/bak.xbstream

流增量
/usr/bin/xtrabackup --defaults-file=${CONFIG} --backup  --user=${USER}  --password=${PASSSWORD} --host=${IP} --port=${PORT} --target-dir=/data/back/test --extra-lsndir=/data/back/chkpoint --incremental-basedir=/data/back/chkpoint  --compress --compress-threads=8 --stream=xbstream >/data/back/test/bakinfo.xbstream

解压流
xbstream -x < bak.xbstream -C test

加密备份：
xtrabackup -uroot -proot123 --backup --target-dir=${all_back_PATH} --encrypt=AES256 --encrypt-threads=4 --encrypt-chunk-size=64K --encrypt-key="5QsS+fykEURHFmuLcFS81aIkCLaVJIyv"

解密：
xtrabackup --decrypt=AES256 --parallel=4 --encrypt-key="5QsS+fykEURHFmuLcFS81aIkCLaVJIyv" --target-dir=${all_back_PATH} --remove-original

全备解压缩：
xtrabackup --parallel=4 --decompress --target-dir=${all_back_PATH} --remove-original


增量备份
–incremental /data/backup1 指定增量备份存放的目标目录
–incremental-basedir=/data/backup 指定完整备份的目录

/usr/bin/xtrabackup --defaults-file=${CONFIG}  --backup  --user=${USER} --password=${PASSSWORD} --host=${IP} --port=${PORT} --incremental-dir=${INC_PATH} --incremental-basedir=${all_back_PATH} --target-dir=${INC_PATH}

还原备份
/usr/bin/xtrabackup --user=zhengda --password=goyun.org --copy-back --target-dir=/data/backup

全量还原
xtrabackup --prepare --target-dir=${all_back_PATH}
/usr/bin/xtrabackup --copy-back --datadir=/data/test/back  --target-dir=${all_back_PATH}
多线程还原
--parallel=4 


增量还原
/data/backups/base
/data/backups/inc1
/data/backups/inc2

/usr/bin/xtrabackup --prepare --apply-log-only --target-dir=${all_back_PATH}
/usr/bin/xtrabackup --prepare --apply-log-only --target-dir=${all_back_PATH} --incremental-dir=${INC_PATH}

## 还原之前操作

/usr/bin/xtrabackup --prepare --target-dir=${all_back_PATH} --incremental-dir=${INC_PATH}

根据指定目录还原
/usr/bin/xtrabackup --copy-back --datadir=/data/test/back  --redo-only --extra-lsndir=${all_back_PATH} --target-dir=${all_back_PATH}

根据配置文件还原
/usr/bin/xtrabackup --defaults-file=/data/mysql-8.0.22/my_2378.cnf --copy-back --extra-lsndir=/data/back/app2/ --target-dir=/data/back/app2/ --parallel=128

rsync -rvau --delete /data/test/back/ -e  "ssh -p 22369" 192.168.15.229:/data/mysql-8.0.22/mysql_2378/data/

chown mysql.mysql -R /data/mysql-8.0.22/

systemctl stop mysqld.service
systemctl start mysqld.service
systemctl status mysqld.service

tail -f -n 100 logs/error.log

增量备份的恢复需要有3个步骤
1、恢复完全备份
2、恢复增量备份到完全备份(开始恢复的增量备份要添加--redo-only参数，到最后一次增量备份要去掉--redo-only)
3、对整体的完全备份进行恢复，回滚未提交的数据


cat xtrabackup_info 查看信息


cat > /data/mysql_back.sh << EOF
all_back_PATH=/data/back/20201127allback
PORT=2378
IP=192.168.15.223
USER=root
PASSSWORD=AnvcTMagdLarwNV3CKaC
CONFIG=/data/mysql-8.0.18/my_2378.cnf
INC_PATH=/data/back/inc

rm -rf /data/back/inc

#增量备份
/usr/bin/xtrabackup --defaults-file=${CONFIG}  --backup  --user=${USER} --password=${PASSSWORD} --host=${IP} --port=${PORT} --incremental-dir=${INC_PATH} --incremental-basedir=${all_back_PATH} --target-dir=${INC_PATH}

#合并备份
/usr/bin/xtrabackup --prepare --apply-log-only --target-dir=${all_back_PATH} --extra-lsndir=${INC_PATH} --incremental-dir=${INC_PATH}
EOF

cat >> /var/spool/cron/root << EOF
01 00 * * * /usr/bin/sh /data/mysql_back.sh > /dev/null 2>&1
EOF