
免费证书

https://letsencrypt.org/

git clone https://github.com/certbot/certbot.git

cd letsencrypt


pip install certbot



wget https://dl.eff.org/certbot-auto --no-check-certificate
chmod +x ./certbot-auto
./certbot-auto -n


letsencrypt  支持配通符了需要dns 支持
/root/letsencrypt/letsencrypt-auto certonly --standalone --email xxx@xxx.cn  -d ios.xxx.net

/data/certbot/letsencrypt-auto certonly --preferred-challenges dns --manual --email yywolf1983@gmail.com  -d *.nones.top -d nones.top --server https://acme-v02.api.letsencrypt.org/directory

/data/certbot/letsencrypt-auto certonly --preferred-challenges dns --manual --email yywolf1983@gmail.com  -d *.d7home.com -d d7home.com --server https://acme-v02.api.letsencrypt.org/directory



/data/certbot/letsencrypt-auto certonly --standalone --email  yywolf1983@gmail.com  -d www.d7home.com -d d7home.com


参数如下
--preferred-challenges dns: 认证方式选择DNS, 泛域名支持DNS
--manual: 手动模式, 这里为了简单就使用手动认证了, 下面会说自动模式的使用.
-d *.bysir.cn: 就是要申请的泛域名了
--server https://acme-v02.api.letsencrypt.org/directory: 泛域名证书是新功能, 如果要使用就得加上这个参数


./certbot-auto certonly  -d ***_*.example.com --manual --preferred-challenges dns --dry-run  --manual-auth-hook "~/au/au.sh php aly add" --manual-cleanup-hook "~/au/au.sh python aly clean"

更新所有证书
./certbot-auto renew  --manual --preferred-challenges dns --deploy-hook  "/data/nginx/sbin/nginx -s reload" --dry-run --manual-auth-hook "~/au/au.sh python aly add" --manual-cleanup-hook "~/au/au.sh python aly clean"


0 0 1 * * root /data/mypy/bin/certbot renew  --manual --preferred-challenges dns --deploy-hook  "/data/nginx/sbin/nginx -s reload" --manual-auth-hook "/root/au/au.sh python aly add" --manual-cleanup-hook "/root/au/au.sh python aly clean"


listen 443 ssl;

ssl on;
ssl_certificate /etc/letsencrypt/live/laojiang.me/fullchain.pem;
ssl_certificate_key /etc/letsencrypt/live/laojiang.me/privkey.pem;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_prefer_server_ciphers on;


每月更新证书
/data/certbot/letsencrypt-auto renew --dry-run --server https://acme-v02.api.letsencrypt.org/directory

删除
/data/certbot/letsencrypt-auto delete

模拟更新
./certbot-auto renew –dry-run

更新
./certbot-auto renew

查看信息
./certbot-auto certificates
