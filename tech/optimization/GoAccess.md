yum install glib2 glib2-devel GeoIP-devel  ncurses-devel zlib zlib-develyum install gcc -y
yum -y install GeoIP-update
yum install goaccess


#修改文件/etc/goaccess.conf改成goaccess格式标准对应为
time-format %T
date-format %d/%b/%Y
log_format %h - %^ [%d:%t %^] "%r" %s %b "%R" "%u" "%^" %^ %^ %^ %T

#测试生成页面
LANG="zh_CN.UTF-8";goaccess -f /data/docker/nginx/logs/app.access.log -c -a > /data/docker/nginx/html/download/go.html