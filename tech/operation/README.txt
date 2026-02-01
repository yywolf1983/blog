XXL

金丝雀发布(灰度)
蓝绿
滚动

重点监控接口 
报警方案（邮件，短信，消息。）
运维架构 
   服务启动（开机自启，快速伸缩部署。）
   单点故障，运维承载
容器化


gitlab pipeline


docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma


cloudflare tunnel ssh 
Host pi.danishshakeel.me
  ProxyCommand /opt/homebrew/bin/cloudflared access ssh --hostname %h