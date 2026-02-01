
正向代理对server 透明
反响代理对client 透明

nginx采用了异步非阻塞的方式来处理请求
 在24G内存的机器上，处理的并发请求数达到过200万。
当然，这里说的是最大连接数，对于HTTP请求本地资源来说，能够支持的最大并发数量是
worker_connections * worker_processes，而如果是HTTP作为反向代理来说，
最大并发数量应该是worker_connections * worker_processes/2。
因为作为反向代理服务器，每个并发会建立与客户端的连接和与后端服务的连接，会占用两个连接。

# 使用的用户和组
user  www www;
# 指定工作衍生进程数
worker_processes  2;
# 指定 pid 存放的路径
pid /var/run/nginx.pid;
# 分别给每个进程绑定一个cpu
worker_cpu_affinity 0001 0010;
#这个指令是指当一个nginx进程打开的最多文件描述符数目，理论值应该是最多打开文件数（ulimit -n）与nginx进程数相除，但是nginx分配请求并不是那么均匀，所以最好与ulimit -n的值保持一致。
worker_rlimit_nofile 102400;
#每个进程连接数
worker_connections 102400

# kill -HUP cat /var/log/nginx.pid  linux下可重新加载
#USR1 重新打开日志文件
#USR2 平滑升级可执行程序。
#WINCH 从容关闭工作进程
time set

工作模式

events {
# 允许的连接数
connections   2000;
#单个进程最大连接数（最大连接数=连接数*进程数）
worker_connections 65535;
#参考事件模型，use [ kqueue | rtsig | epoll | /dev/poll | select | poll ]; epoll模型是Linux 2.6以上版本内核中的高性能网络I/O模型，如果跑在FreeBSD上面，就用kqueue模型。
# 具体内容查看 http://wiki.codemongers.com/事件模型
# use kqueue;
use epoll;  #内核大于 2.6 #事件模型
}

log config

http {
include       conf/mime.types;
default_type  application/octet-stream; #默认文件类型

# 可以在下方直接使用 [ debug | info | notice | warn | error | crit ]  参数
error_log  /var/log/nginx.error_log  info;

#关闭日志
#error_log /dev/null crit;

log_format main  '$remote_addr - $remote_user [$time_local]  '
'"$request" $status $bytes_sent '
'"$http_referer" "$http_user_agent" '
'"$gzip_ratio"';

access_log logs/nginx-access.log gzip buffer=32k;
}


base

server_names_hash_bucket_size 128; #服务器名字的hash表大小
client_header_buffer_size 32k; #上传文件大小限制
large_client_header_buffers 4 64k; #设定请求缓
client_max_body_size 8m; #上传限制
client_body_timeout 1200;
client_body_buffer_size 1024k;
client_header_timeout  3m;
send_timeout           3m;
sendfile on; #开启高效文件传输模式，sendfile指令指定nginx是否调用sendfile函数来输出文件，对于普通应用设为 on，如果用来进行下载等应用磁盘IO重负载应用，可设置为off，以平衡磁盘与网络I/O处理速度，降低系统的负载。注意：如果图片显示不正常把这个改 成off。
tcp_nopush on; #防止网络阻塞
tcp_nodelay on; #防止网络阻塞

keepalive_timeout 60;   #负载超时时间

fastcgi_connect_timeout 60;
fastcgi_send_timeout 180;
fastcgi_read_timeout 180;
fastcgi_buffer_size 128k;
fastcgi_buffers 4 256k;
fastcgi_busy_buffers_size 256k;
fastcgi_temp_file_write_size 256k;
fastcgi_intercept_errors on;

#打开文件缓存 20秒后删除
open_file_cache max=102400 inactive=20s
#这个是指多长时间检查一次缓存的有效信息。
open_file_cache_valid 30s;
#open_file_cache指令中的inactive参数时间内文件的最少使用次数,不超过则删除
open_file_cache_min_uses 1;

server_tokens off;   #关闭nginx版本号
access_log   /var/log/nginx.access_log  main;

charset  utf-8; #默认编码
= 压缩设置 =

#gzip模块设置
gzip on; #开启gzip压缩输出
gzip_min_length 1k; #最小压缩文件大小
gzip_buffers 4 16k; #压缩缓冲区
gzip_http_version 1.0; #压缩版本（默认1.1，前端如果是squid2.5请使用1.0）
gzip_comp_level 2; #压缩等级
gzip_types text/plain application/x-javascript text/css application/xml;
#压缩类型，默认就已经包含text/html，所以下面就不用再写了，写上去也不会有问题，但是会有一个warn。
gzip_vary on;
#limit_zone crawler $binary_remote_addr 10m; #开启限制IP连接数的时候需要使用

output_buffers   1 32k;
postpone_output  1460;

autoindex 文件列表
autoindex on;      
autoindex_exact_size off;
#默认为on，显示出文件的确切大小，单位是bytes。
#改为off后，显示出文件的大概大小，单位是kB或者MB或者GB     
autoindex_localtime on;
#默认为off，显示的文件时间为GMT时间。
#改为on后，显示的文件时间为文件的服务器时间

限流模块
--with-http_stub_status_module  --with-http_realip_module

#安装header,footer支持
#./configure --add-module=../nginx-fancyindex-?.?.?
#         fancyindex on;
#         fancyindex_localtime on;
#         fancyindex_exact_size on;
          #fancyindex_header
          #fancyindex_footer
          #fancyindex_readme
          #fancyindex_readme_mode top;
          #fancyindex_readme_mode pre | asis | top | bottom | div | iframe
 

ssl 跳转      

server {
        listen  80;
        rewrite ^(.*)$  https://$host$1 permanent;
    }

listen 443 ssl;

ssl_certificate   /usr/local/nginx/5999627_admin.xingchenborui.com.pem;
ssl_certificate_key  /usr/local/nginx/5999627_admin.xingchenborui.com.key;
ssl_session_timeout 5m;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
ssl_prefer_server_ciphers on;

#目录别名
location ^~/soft {
      alias /soft;
      limit_conn  one  5;   #限制连接数 ip  更多查阅资料
      limit_rate  100k;      #限制下载速度 每个链接

      #新的连接限制
      # $binary_remote_addr = 用二进制来储存客户端的地址，1m 可以储存 32000 个并发会话

      #下面配置不仅会限制单一IP来源的连接数，同时也会限制单一虚拟服务器的总连接数
      limit_conn_zone $binary_remote_addr zone=perip:10m;
      limit_conn_zone $server_name zone=perserver:10m;

      #指定一块已经设定的共享内存空间，以及每个给定键值的最大连接数。          
      limit_conn_zone $binary_remote_addr zone=addr:10m;

      #设置连接池名称和大小
      limit_zone  one  $binary_remote_addr  10m;

      #limie_req_zone的功能是通过 令牌桶原理来限制 用户的连接频率
      limit_req_zone  $binary_remote_addr  zone=req_one:10m rate=1r/s;

      #限制平均每秒不超过一个请求，同时允许超过频率限制的请求数不多于5个。
      #如果不希望超过的请求被延迟，可以用nodelay参数：
      limit_req zone=one burst=5 nodelay;

访问权限

        deny all; #进制权限

        #目录加密

        #auth_basic              ".........";  #提示信息
        #auth_basic_user_file d:/apm/nginxmd5; #验证密码 nginx明文加密
        # 指定 fastcgi 的主机和端口

        #auth_basic              ".........";  #提示信息
        #auth_basic_user_file d:/apm/nginxmd5; #验证密码 nginx明文加密
    }
    
cache  缓存

location / {
#设置Web缓存区名称为cache_one，缓存空间大小为1000MB，1天清理一次缓存，单个文件超过5m不缓存。
proxy_cache_path temp/cache  levels=1:2  keys_zone=cache_one:1000m inactive=1d max_size=5m;
proxy_temp_path temp/proxy_temp;
fastcgi_temp_path temp/fastcgi_temp;

proxy_set_header   Host             $host;                  #http host 字段
proxy_set_header   X-Real-IP        $remote_addr;
proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
#X-Forwarded-For是用于记录代理信息的，每经过一级代理(匿名代理除外)，代理服务器都会把这次请求的来源IP追加在X-Forwarded-For中
#X-Real-IP，一般只记录真实发出请求的客户端IP

client_body_temp_path      /var/nginx/client_body_temp;

proxy_connect_timeout      90;
proxy_send_timeout         90;
proxy_read_timeout         90;
proxy_send_lowat           12000;

proxy_buffer_size          4k;
proxy_buffers              4 32k;
proxy_busy_buffers_size    64k;
proxy_temp_file_write_size 64k;

proxy_temp_path            /var/nginx/proxy_temp;

}
error page

error_page  500 502 503 504 404  /404.html;

location /404.html {
    root  /spool/www;

    charset         on;
    source_charset  utf-8;
}


#Nginx Rewrite规则相关指令有if、rewrite、set、return、break等，其中rewrite是最关键的指令。
#location /static/ {
#    if (-f $request_filename) {
#    rewrite ^/static/(.*)$  /static/$1 break;
#        }
#  }

# last 完成 Rewrite 不再匹配后面的规则
# back 终止 Rewrite
# redirect  临时重定向  http状态302
# permanent  永久重定向  http状态301

# * ~         为区分大小写匹配
# * ~*         为不区分大小写匹配
# * !~和!~*     分别为区分大小写不匹配及不区分大小写不匹配


 # * -f和!-f 用来判断是否存在文件
 # * -d和!-d 用来判断是否存在目录
 # * -e 和!-e用来判断是否存在文件或目录
 # * -x 和!-x用来判断文件是否可执行


#Apache Rewrite 规则：
#RewriteRule  ^/html/tagindex/([a-zA-Z]+)/.*$ /$1/ [R=301,L]
#Nginx Rewrite 规则：
#rewrite  ^/html/tagindex/([a-zA-Z]+)/.*$ http://$host/$1/  permanent; #永久

#以上示例中，我们注意到，Nginx Rewrite 规则的置换串中增加了“http://$host”，这是在Nginx中要求的。
#另外，Apache与Nginx的Rewrite规则在变量名称方面也有区别，例如：
#Apache Rewrite 规则：
#RewriteRule  ^/user/login/$ /user/login.php?login=1&forward=http://%{HTTP_HOST}  [L]
#Nginx Rewrite 规则：
#rewrite  ^/user/login/$ /user/login.php?login=1&forward=http://$host last;     

#Apache的RewriteCond指令对应Nginx的if指令；
#Apache的RewriteRule指令对应Nginx的rewrite指令；
#Apache的[R]标记对应Nginx的redirect标记；
#Apache的[P]标记对应Nginx的last标记；
#Apache的[R,L]标记对应Nginx的redirect标记；
#Apache的[P,L]标记对应Nginx的last标记；
#Apache的[PT,L]标记对应Nginx的last标记；
#Apache的[NC]  不区分大小写
#==================================================================


访问限制

location ~* \.(txt|doc)$ {
   if (-f $request_filename) {
   root /data/www/wwwroot/linuxtone/test;
   #rewrite …..可以重定向到某个 URL
   break;
   }
}
ip限制

location / {
    deny    192.168.1.1;
    allow   192.168.1.0/24;
    allow   10.1.1.0/16;
    deny    all;
}

访问统计
#   --with-http_stub_status_module
location /Nginx{
     stub_status             on;
     #关闭访问日志!
     access_log              off;
     #rewrite  ;
     #return   403;

     #重写规则
     #rewrite ^/N$ /Nginx break;               
     }

解析：
Active connections    //当前 Nginx 正处理的活动连接数。
server accepts handled requests //总共处理了8 个连接 , 成功创建 8 次握手,总共处理了500个请求。
Reading //nginx 读取到客户端的 Header 信息数。
Writing //nginx 返回给客户端的 Header 信息数。
Waiting //开启 keep-alive 的情况下，这个值等于 active - (reading + writing)，意思就是 Nginx 已经处理完正在等候下一次请求指令的驻留连接
php支持

kill -USR2 php-fpm   重启php   

    location ~ .*\.(php)?$ {
          root    /www/html;
          fastcgi_pass    127.0.0.1:9000;
          #fastcgi_pass  unix:/var/run/php5/php-fpm.sock;
          #file sock可以减少tcp连接开销，如果条件允许，推荐使用这种方式
          include         fastcgi_params;
          #出现文件无法读取错误时需要这句
          fastcgi_param SCRIPT_FILENAME D:/www/$fastcgi_script_name;
          fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
      }     
   }
   #include d:/apm/nginx/conf/server.conf; #针对多个主机
别名

location /pa {
        alias /var/data/phpmyadmin;
        index index.html index.php;
    }

    location ~ /pa/.+\.php.*$ {
        if ($fastcgi_script_name ~ /pa/(.+\.php.*)$) {
            set $valid_fastcgi_script_name $1;
        }
        fastcgi_pass  127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  /var/data/phpmyadmin/$valid_fastcgi_script_name;
        include  fastcgi_params;
    }
负载均衡

 upstream backend  {
      #ip_hash;  #启用可以解决session保持问题
        server    192.168.1.15:80 weight=1 max_fails=2 fail_timeout=30s;
        server    192.168.1.16:80 down;
        server    192.168.1.17:80 backup;
      #fair;
      #hash $request_uri;
      #hash_method crc32;
     }
#每个设备的状态设置为:
#1.down 表示单前的server暂时不参与负载
#2.weight 默认为1.weight越大，负载的权重就越大。
#3.max_fails ：允许请求失败的次数默认为1.当超过最大次数时，返回proxy_next_upstream 模块定义的错误

#4.fail_timeout:max_fails次失败后，暂停的时间。
#5.backup： 其它所有的非backup机器down或者忙的时候，请求backup机器。所以这台机器压力会最轻。

#不能同时使用！
#1、轮询（默认）
#每个请求按时间顺序逐一分配到不同的后端服务器，如果后端服务器down掉，能自动剔除。
#2、weight
#指定轮询几率，weight和访问比率成正比，用于后端服务器性能不均的情况。
#3、ip_hash
#每个请求按访问ip的hash结果分配，这样每个访客固定访问一个后端服务器，可以解决session的问题。
#ip_hash要求nginx一定是最前端的服务器 不然获取不到正确 后端不能再有负载不然IP不能指向后端
#为了解决ip_hash的一些问题，可以使用upstream_hash这个第三方模块

反向代理

location / {
proxy_next_upstream http_502 http_504 error timeout invalid_header;
// 如果后端服务器返回502、504或执行超时等错误，自动将请求转发到upstream另一台服务器
proxy_pass  http://backend;  #指定反向代理池
proxy_redirect off;          # 如果需要修改从被代理服务器传来的应答头中的"Location"和"Refresh"字段，可以用这个指令设置。

proxy_connect_timeout 90; #nginx跟后端服务器连接超时时间(代理连接超时)
proxy_send_timeout 90; #后端服务器数据回传时间(代理发送超时)
proxy_read_timeout 90; #连接成功后，后端服务器响应时间(代理接收超时)
proxy_buffer_size 4k; #设置代理服务器（nginx）保存用户头信息的缓冲区大小
proxy_buffers 4 32k; #proxy_buffers缓冲区，网页平均在32k以下的设置
proxy_busy_buffers_size 64k; #高负荷下缓冲大小（proxy_buffers*2）
proxy_temp_file_write_size 64k;
#设定缓存文件夹大小，大于这个值，将从upstream服务器传

}

nginx version 版本号

vi nginx-0.7.30/src/core/nginx.h
define NGINX_VERSION      "1.8"
define NGINX_VER          "LTWS/" NGINX_VERSION

define NGINX_VAR          "NGINX"
define NGX_OLDPID_EXT     ".oldbin"

动静分离

location ~ .*\.(gif|jpg|jpeg|png|bmp|swf|js|css)$  #处理所有页面
 {
      #对图片、JS、CSS进行缓存，使用Web缓存区cache_one
      proxy_cache cache_one;

      #对不同HTTP状态码缓存设置不同的缓存时间
      proxy_cache_valid  200 10m;
      proxy_cache_valid  304 3m;
      proxy_cache_valid  301 302 1h;
      proxy_cache_valid  any 1m;

      #设置Web缓存的Key值，
      #Nginx根据Key值md5哈希存储缓存，这里根据“域名、URI、客户端请求Header头中的If-Modified-Since信息”组合成 Key。
      proxy_cache_key $host$request_uri$http_if_modified_since;

      expires      30d;   #缓存时间

      # 防盗链设置
      valid_referers none blocked server_names *.linuxtone.org linuxtone.org http://localhost baidu.com;
      if ($invalid_referer) {
         rewrite   ^/   http://www.linuxtone.org/images/default/logo.gif;
         # return   403;
      }

 }
跨域问题

location /pub/(.+) {
    if ($http_origin ~ <允许的域（正则匹配）>) {
        #   表示允许这个域跨域调用（客户端发送请求的域名和端口）
        #   $http_origin动态获取请求客户端请求的域   不用*的原因是带cookie的请求不支持*号
        add_header 'Access-Control-Allow-Origin' "$http_origin";
        #   带cookie请求需要加上这个字段，并设置为true
        add_header 'Access-Control-Allow-Credentials' "true";
        #   表示请求头的字段 动态获取
        add_header Access-Control-Allow-Headers $http_access_control_request_headers;

        if ($request_method = "OPTIONS") {
            #   预检命令的缓存，如果不缓存每次会发送两次请求
            add_header 'Access-Control-Max-Age' 86400;
            #   请求类型
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS, DELETE';
            add_header 'Access-Control-Allow-Headers' 'reqid, nid, host, x-real-ip, x-forwarded-ip, event-type, event-id, accept, content-type';
            add_header 'Content-Length' 0;
            add_header 'Content-Type' 'text/plain, charset=utf-8';
            return 204;
        }
    }

自定义头

   location ^/get_system_live_nodes {
            add_header Content-Type application/json;
        }
设置变量

  location /test {
        set $foo hello;
        echo "foo: $foo";
    }

$ curl 'http://localhost:8080/test'
foo: hello


#### 编译安装lua
```
这里先要安装 luajit
export LUAJIT_INC=/usr/local/include/luajit-2.0
export LUAJIT_LIB=/usr/local/lib

./configure --prefix=/data/nginx --with-openssl=/data/nginx/openssl/ --add-module=../lua-nginx-module
```

location /test {
    content_by_lua '
        if ngx.var.cookie_user == nil then
            ngx.say("cookie user: missing")
        else
            ngx.say("cookie user: [", ngx.var.cookie_user, "]")
        end
    ';
}

$ curl --cookie user=agentzh 'http://localhost:8080/test'
cookie user: [agentzh]

$ curl --cookie user= 'http://localhost:8080/test'
cookie user: []

$ curl 'http://localhost:8080/test'
cookie user: missing
变量

 set $ip $http_x_forwarded_for;

     if ( $http_x_forwarded_for = '' ){
         set $ip  $remote_addr;
        }

$arg_PARAMETER 这个变量值为：GET请求中变量名PARAMETER参数的值。
$args 这个变量等于GET请求中的参数。例如，foo=123&bar=blahblah;这个变量只可以被修改
$binary_remote_addr 二进制码形式的客户端地址。
$body_bytes_sent 传送页面的字节数
$content_length 请求头中的Content-length字段。
$content_type 请求头中的Content-Type字段。
$cookie_COOKIE cookie COOKIE的值。
$document_root 当前请求在root指令中指定的值。
$document_uri 与$uri相同。
$host 请求中的主机头(Host)字段，如果请求中的主机头不可用或者空，则为处理请求的server名称(处理请求的server的server_name指令的值)。值为小写，不包含端口。
$hostname  机器名使用 gethostname系统调用的值
$http_HEADER   HTTP请求头中的内容，HEADER为HTTP请求中的内容转为小写，-变为_(破折号变为下划线)，例如：$http_user_agent(Uaer-Agent的值), $http_referer...;
$sent_http_HEADER  HTTP响应头中的内容，HEADER为HTTP响应中的内容转为小写，-变为_(破折号变为下划线)，例如： $sent_http_cache_control, $sent_http_content_type...;
$is_args 如果$args设置，值为"?"，否则为""。
$limit_rate 这个变量可以限制连接速率。
$nginx_version 当前运行的nginx版本号。
$query_string 与$args相同。
$remote_addr 客户端的IP地址。
$remote_port 客户端的端口。
$remote_user 已经经过Auth Basic Module验证的用户名。
$request_filename 当前连接请求的文件路径，由root或alias指令与URI请求生成。
$request_body 这个变量（0.7.58+）包含请求的主要信息。在使用proxy_pass或fastcgi_pass指令的location中比较有意义。
$request_body_file 客户端请求主体信息的临时文件名。
$request_completion 如果请求成功，设为"OK"；如果请求未完成或者不是一系列请求中最后一部分则设为空。
$request_method 这个变量是客户端请求的动作，通常为GET或POST。
包括0.8.20及之前的版本中，这个变量总为main request中的动作，如果当前请求是一个子请求，并不使用这个当前请求的动作。
$request_uri 这个变量等于包含一些客户端请求参数的原始URI，它无法修改，请查看$uri更改或重写URI。
$scheme 所用的协议，比如http或者是https，比如rewrite ^(.+)$ $scheme://example.com$1 redirect;
$server_addr 服务器地址，在完成一次系统调用后可以确定这个值，如果要绕开系统调用，则必须在listen中指定地址并且使用bind参数。
$server_name 服务器名称。
$server_port 请求到达服务器的端口号。
$server_protocol 请求使用的协议，通常是HTTP/1.0或HTTP/1.1。
$uri 请求中的当前URI(不带请求参数，参数位于$args)，不同于浏览器传递的$request_uri的值，它可以通过内部重定向，或者使用index指令进行修改。不包括协议和主机名，例如/foo/bar.html
down zip mod

--add-module=/path/to/mod_zip-1.x

#在页面首尾加上东西
./configure --with-http_sub_module --with-http_addition_module

location /foobar {
    alias /usr/share/nginx/html/foobar/;

    sub_filter_once off;
    #url
    sub_filter '/.theme' '/foobar/.theme';

    add_before_body /foobar/.theme/header.html;
    add_after_body /foobar/.theme/footer.html;
}


git clone https://github.com/aperezdc/ngx-fancyindex.git ngx-fancyindex

./configure --add-module=../ngx-fancyindex
fancyindex on;              # Enable fancy indexes.
fancyindex_exact_size on;   # Output human-readable file sizes.
fancyindex_header /.theme/header.html;
fancyindex_footer /.theme/footer.html;

#后段检查模块
git clone https://github.com/yaoweibin/nginx_upstream_check_module


泛域名解析
server_name  ~^(?<subdomain>.+)\.yourdomain\.com$;
root   html/$subdomain;
