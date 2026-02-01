重启

# 检查配置文件语法
haproxy -c -f /etc/haproxy/haproxy.cfg

# 以daemon模式启动，以systemd管理的daemon模式启动
haproxy -D -f /etc/haproxy/haproxy.cfg [-p /var/run/haproxy.pid]
haproxy -Ds -f /etc/haproxy/haproxy.cfg [-p /var/run/haproxy.pid]

# 启动调试功能，将显示所有连接和处理信息在屏幕
haproxy -d -f /etc/haproxy/haproxy.cfg

# restart。需要使用st选项指定pid列表
haproxy -f /etc/haproxy.cfg [-p /var/run/haproxy.pid] -st `cat /var/run/haproxy.pid`

# 显示haproxy编译和启动信息
haproxy -vv

* /opt/haproxy/sbin/haproxy -f /opt/haproxy/haproxy.cfg -p /opt/haproxy/haproxy.pid -sf $(cat /opt/haproxy/haproxy.pid)
haproxy.cfg

global
        #log 127.0.0.1 local0 info
        log 127.0.0.1 local3
        maxconn 4096
        chroot /opt/haproxy
        uid 99
        gid 99
        pidfile /opt/haproxy/haproxy.pid
        daemon
        nbproc 2

defaults
        log     global
        mode    http
        option  httplog
        option  httpclose
        option  forwardfor
        retries 3                //3次连接失败就认为服务器不可用，主要通过后面的check检查
        maxconn 2000                 
        timeout client 50000     //连接超时时间   
        timeout connect 50000    //客户端连接超时时间
        timeout server 50000     //服务器端连接超时时间
        stats enable
        stats hide-version
        stats uri /admin?stats
        stats auth proxy:test


frontend picboxinc.com
        bind *:80
        acl cnhaha-cloud hdr_beg(host) -i cncloud.picboxinc.com
        acl haha-cloud hdr_beg(host) -i cloud.picboxinc.com
        acl test-cloud hdr_beg(host) -i test.picboxinc.com

        use_backend cloud_cluster  if cnhaha-cloud
        use_backend cloud_cluster  if haha-cloud
        use_backend cloud_test  if test-cloud

backend cloud_cluster
        balance roundrobin
        server  tae_001   192.168.10.91:8080 weight 1
        #server tae_002   10.173.4.129:8080 weight 5

backend cloud_test
        balance roundrobin
        server  auth_001   192.168.10.91:5194 weight 5
        server  auth_002   192.168.10.91:8080 weight 1  # is test   
