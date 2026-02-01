部署一个完整的 Trojan 服务端，包括 **WebSocket 和 TLS** 功能，在 Linux 上实现。

这里我将为您提供一个详细的**分步指南和脚本模板**。这个脚本会自动化大部分步骤，但你需要手动输入一些信息，比如你的域名和密码。

### 准备工作

在开始之前，请确保你已经准备好以下东西：

  * **一台 Linux VPS**：操作系统推荐 **Debian 11** 或 **CentOS 7/8**。
  * **一个域名**：将域名解析到你的 VPS 的 **IP 地址**。
  * **SSH 客户端**：用来连接你的 VPS。

-----

### 第一步：连接服务器并更新系统

首先，使用 SSH 登录到你的 VPS。然后，更新系统以确保所有软件包都是最新的。

**对于 Debian/Ubuntu 系统：**

```bash
sudo apt update && sudo apt upgrade -y
```

**对于 CentOS 系统：**

```bash
sudo yum update -y
```

-----

### 第二步：安装 Nginx 和 Certbot

Trojan-Go 依赖 Nginx 来处理 WebSocket 和 TLS 流量。Certbot 则是用来自动申请和续订 SSL 证书。

**对于 Debian/Ubuntu 系统：**

```bash
sudo apt install -y nginx certbot
```

**对于 CentOS 系统：**

```bash
sudo yum install -y epel-release
sudo yum install -y nginx
sudo yum install -y certbot
```

-----

### 第三步：生成 SSL 证书

我们需要为你的域名申请一个有效的 SSL 证书。

```bash
sudo certbot certonly --standalone --agree-tos --no-eff-email -d your_domain.com
```

  * **请将 `your_domain.com` 替换为你的真实域名。**
  * **`--agree-tos`**：同意服务条款。
  * **`--no-eff-email`**：不发送邮件。

如果成功，你的证书和密钥将保存在 `/etc/letsencrypt/live/your_domain.com/` 目录下。

-----

### 第四步：部署 Trojan-Go

Trojan-Go 是一个更活跃的 Trojan 衍生项目，功能更强大，支持 WebSocket。

#### 1\. 下载并安装 Trojan-Go

```bash
# 下载最新版本（请从 GitHub 页面获取最新版本号）
cd /usr/local/
wget https://github.com/p4gefau1t/trojan-go/releases/download/v0.10.6/trojan-go-linux-amd64.tar.gz

# 解压文件
tar -xvf trojan-go-linux-amd64.tar.gz
rm trojan-go-linux-amd64.tar.gz

# 将 trojan-go 可执行文件移动到 /usr/bin 目录
mv trojan-go /usr/bin/
```

#### 2\. 配置 Trojan-Go

创建一个配置文件 `/usr/local/etc/trojan-go/config.json`。

```bash
sudo mkdir -p /usr/local/etc/trojan-go
sudo nano /usr/local/etc/trojan-go/config.json
```

将以下内容粘贴到文件中，并修改 `your_domain.com` 和 `your_password`。

```json
{
  "run_type": "server",
  "local_addr": "0.0.0.0",
  "local_port": 443,
  "remote_addr": "127.0.0.1",
  "remote_port": 80,
  "password": [
    "your_password"
  ],
  "ssl": {
    "cert": "/etc/letsencrypt/live/your_domain.com/fullchain.pem",
    "key": "/etc/letsencrypt/live/your_domain.com/privkey.pem",
    "fallback_addr": "127.0.0.1",
    "fallback_port": 80
  },
  "websocket": {
    "enabled": true,
    "path": "/trojan-ws",
    "host": "your_domain.com"
  }
}
```

  * **`password`**：设置你的 Trojan 密码，可以添加多个。
  * **`ssl.cert` 和 `ssl.key`**：指向你刚才申请的 SSL 证书路径。
  * **`websocket.path`**：WebSocket 的路径，可以自定义。

-----

### 第五步：配置 Nginx

Trojan-Go 监听 443 端口，并将流量转发给 Nginx 的 80 端口。Nginx 负责伪装成一个正常的网站。

1.  **创建 Nginx 配置文件：**

    ```bash
    sudo nano /etc/nginx/sites-available/your_domain.com
    ```

    粘贴以下内容：

    ```nginx
    server {
        listen 80;
        listen [::]:80;
        server_name your_domain.com;
        return 301 https://$server_name$request_uri;
    }

    server {
        listen 443 ssl;
        listen [::]:443 ssl;
        server_name your_domain.com;
        ssl_certificate /etc/letsencrypt/live/your_domain.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/your_domain.com/privkey.pem;
        ssl_session_timeout 1d;
        ssl_session_cache shared:SSL:10m;
        ssl_session_tickets off;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384';
        ssl_prefer_server_ciphers off;
        
        # 将 trojan 的 WebSocket 流量转发到 trojan-go
        location /trojan-ws {
            proxy_pass http://127.0.0.1:80;
            proxy_redirect off;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $http_host;
        }

        # 伪装一个正常网站
        location / {
            root /var/www/html;
            index index.html index.htm;
        }
    }
    ```

      * 请将 `your_domain.com` 替换为你的真实域名。
      * `location /trojan-ws` 这里的路径要与 Trojan-Go 配置文件中的 `websocket.path` 一致。

2.  **启用 Nginx 配置文件并重启：**

    ```bash
    sudo ln -s /etc/nginx/sites-available/your_domain.com /etc/nginx/sites-enabled/
    sudo nginx -t && sudo systemctl restart nginx
    ```

-----

### 第六步：设置 Trojan-Go 为系统服务

为了让 Trojan-Go 在后台运行，并能在系统重启后自动启动，我们需要把它配置成一个系统服务。

```bash
sudo nano /etc/systemd/system/trojan-go.service
```

粘贴以下内容：

```ini
[Unit]
Description=Trojan-Go Service
After=network.target nss-lookup.target

[Service]
Type=simple
ExecStart=/usr/bin/trojan-go -config /usr/local/etc/trojan-go/config.json
Restart=on-failure
RestartSec=10s

[Install]
WantedBy=multi-user.target
```

保存并关闭文件。然后，重新加载 systemd 并启动服务。

```bash
sudo systemctl daemon-reload
sudo systemctl start trojan-go
sudo systemctl enable trojan-go
```

你可以使用 `sudo systemctl status trojan-go` 来检查服务是否正在运行。

-----

### 第七步：配置防火墙

如果你的服务器有防火墙，你需要开放 80 和 443 端口。

**对于 UFW (Debian/Ubuntu)：**

```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

**对于 Firewalld (CentOS)：**

```bash
sudo firewall-cmd --permanent --zone=public --add-service=http
sudo firewall-cmd --permanent --zone=public --add-service=https
sudo firewall-cmd --reload
```

-----

### 总结

现在，你的 Trojan-Go 服务端已经成功部署。你可以用以下信息来配置客户端：

  * **协议**：Trojan
  * **地址**：`your_domain.com`
  * **端口**：443
  * **密码**：`your_password`
  * **TLS**：启用
  * **WebSocket**：启用
  * **WebSocket 路径**：`/trojan-ws`

如果你在部署过程中遇到任何问题，请随时告诉我。

sudo systemctl list-timers | grep certbot