php


修改方法为：
不改变/usr/local/nginx/conf/fastcgi.conf配置文件里的原配置，而在

 fastcgi_param PHP_ADMIN_VALUE "open_basedir=$document_root/:/tmp/:/proc/";

之后添加

 fastcgi_param PHP_ADMIN_VALUE $basedir if_not_empty;#注意nginx要在1.1.11版本之后

$basedir变量就可以在/usr/local/nginx/conf/vhost/xxx.com.conf配置文件里的include enable-php.conf前赋值：

 set $basedir "open_basedir=/home/wwwroot/tboy.com.cn/:/tmp/:/proc/";

优点：这样既满足了thinkphp5的部署要求，又不影响其他一般站点的使用。
缺点：如果$basedir没有赋值（至少一个专属配置有赋值），nginx -t无法通过。


 location / {            
        if (!-e $request_filename){                
           rewrite ^/(.*)$ /index.php?s=/$1 last;           
         }
     }
     
     
 php 配置文件
 vi /usr/local/php/etc/php.ini