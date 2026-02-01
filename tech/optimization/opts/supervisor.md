
更新新的配置到supervisord   
supervisorctl update

重新启动配置中的所有程序
supervisorctl reload


environment = PATH="/disk2/dev_chatmgmt/chatenv/bin:%(ENV_PATH)s"

su - steve
cd /opt/typhone/ ./bin/supervisorctl status
./bin/supervisorctl -c etc/supervisod_core.conf
default commands (type help <topic>):
[edit]=========================
add clear fg open quit remove restart start stop update avail exit maintail pid reload reread shutdown status tail version ctl中： help //查看命令
ctl中： status //查看状态
如果修改了 /etc/supervisord.conf ,需要执行 supervisorctl reload 来重新加载配置文件，否则不会生效。。。

config Example
[program:memcached]
command = /ebs_data/opt/typhoonae/bin/memcached -u steve -m 1024
process_name = memcached
directory = /ebs_data/opt/typhoonae/bin
priority = 10
redirect_stderr = true
environment = LD_LIBRARY_PATH="/ebs_data/opt/typhoonae/parts/libevent/lib"
stdout_logfile = /ebs_data/opt/typhoonae/var/log/core/memcached.log


docker 这样设置
[supervisord]
nodaemon=ture                ; (start in foreground if true;default false)

[program:tomcat]
command=/data/tomcat-6.0/bin/catalina.sh run
environment=JAVA_HOME="/data/jdk1.8.0/",JAVA_BIN="/data/jdk1.8.0/bin"
directory=/data/tomcat-6.0
autostart = true
autorestart=true
redirect_stderr=true
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0

[program:mysql]
command=/data/mysql/bin/mysqld --basedir=/data/mysql --datadir=/data/mysql/data --plugin-dir=/data/mysql/lib/plugin --user=mysql --log-error=/data/mysql/data/3f472a550450.err --pid-file=/data/mysql/data/mariadb.pid
user=mysql
autostart = true
autorestart=true
redirect_stderr=true
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0


[program:up_nginx]
command=/usr/sbin/nginx
process_name=%(program_name)s
directory=/data/www/nginx/
username=nginx
numprocs=4                    ; 启动几个进程
autostart=true                ; 随着supervisord的启动而启动
autorestart=true              ; 自动重启。。当然要选上了
startretries=10               ; 启动失败时的最多重试次数
exitcodes=0                 ; 正常退出代码（是说退出代码是这个时就不再重启了吗？待确定）
stopsignal=KILL               ; 用来杀死进程的信号
stopwaitsecs=10               ; 发送SIGKILL前的等待时间
redirect_stderr=true          ; 重定向stderr到stdout
stdout_logfile=/data/www/nginx/logs/access.log
stdout_logfile_maxbytes=100MB
stderr_logfile=/data/www/nginx/logs/error.log
stderr_logfile_maxbytes=10MB

在nginx 中加入
daemon off；
