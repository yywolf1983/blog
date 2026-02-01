彻底清理oracle
sqlplus /nolog
SQL> connect / as sysdba
SQL> shutdown [immediate]
SQL> exit
3.停止Listener
[oracle@ora920 oracle]$ lsnrctl stop

rm -rf /data/oracle/

rm /usr/bin/dbhome
rm /usr/bin/oraenv
rm /usr/bin/coraenv

rm /etc/oratab
rm /etc/oraInst.loc


Administration Assistant for Windows     ORACLE mmc
Database Configuration Assistant     数据库管理
Database Upgrade Assistant       升级向导
Locale Builder                 本地化
Microsoft ODBC 管理员          ODBC
Net Configuration Assistant    监听器配置
Net Manager                    网络管理
Oracle Counters for Windows Performance Monitor  性能工具


Database Control - yy   数据库控制台
