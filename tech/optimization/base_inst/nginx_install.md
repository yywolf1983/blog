yum -y install gcc zlib zlib-devel pcre-devel openssl openssl-devel

cd /data/soft;tar zxvf nginx-1.18.0.tar.gz
cd /data/soft/nginx-1.18.0;./configure --prefix=/data/nginx --with-http_stub_status_module --with-http_ssl_module --with-stream 
make && make install

/data/nginx/sbin/nginx -V
/data/nginx/sbin/nginx -t

/data/nginx/sbin/nginx -s reload

TCP 转发
stream {
    upstream stream_backend {
         server 192.168.15.222:8003;
    }

     server {
        listen                8003;
        proxy_pass            stream_backend;
    }
}


cat > /etc/systemd/system/nginx.service << EOF

[Unit]
Description=The nginx HTTP and reverse proxy server
After=network.target remote-fs.target nss-lookup.target

[Install]
WantedBy=multi-user.target

[Service]
Type=forking
PIDFile=/data/nginx/logs/nginx.pid

# Nginx will fail to start if /run/nginx.pid already exists but has the wrong
# SELinux context. This might happen when running `nginx -t` from the cmdline.
# https://bugzilla.redhat.com/show_bug.cgi?id=1268621
ExecStartPre=/usr/bin/rm -f /data/nginx/logs/nginx.pid
ExecStartPre=/data/nginx/sbin/nginx -t
ExecStart=/data/nginx/sbin/nginx
ExecReload=/bin/kill -s HUP $MAINPID
KillSignal=SIGQUIT
TimeoutStopSec=5
KillMode=process
PrivateTmp=true

EOF

systemctl daemon-reload
systemctl enable nginx.service 
systemctl start nginx.service
systemctl status nginx.service