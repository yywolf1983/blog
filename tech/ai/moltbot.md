
# MoltBot 完整配置指南

## 核心问题
在使用 MoltBot 时，可能会遇到以下访问问题：
1. `origin not allowed`
2. `control ui requires device identity`
3. `WebSocket 连接错误` 或 `requires HTTPS or localhost`

## 一、快速解决方案（推荐）

### 1.1 修改绑定模式（允许局域网访问）
默认只绑定到本机（127.0.0.1），需改为绑定到局域网接口：
```bash
moltbot config set gateway.bind lan
```

### 1.2 允许不安全认证（解决 HTTP 安全限制）
允许 HTTP 环境下的身份验证，绕过浏览器安全策略：
```bash
moltbot config set gateway.controlUi.allowInsecureAuth true
```

### 1.3 添加访问源白名单
将你访问控制界面的地址添加到允许列表中：
```bash
# 编辑配置文件 ~/.moltbot/moltbot.json
# 在 "gateway.controlUi" 部分添加：
"allowedOrigins": [
  "http://192.168.1.100:18789",  # 你的局域网IP
  "http://localhost:18789"       # 本地访问
]
```

### 1.4 重启服务
修改配置后必须重启网关服务：
```bash
moltbot gateway restart
```

## 二、通过 HTTPS 访问（最安全方案）

### 2.1 安装 Tailscale（提供 HTTPS）
```bash
# Linux
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up

# Windows/macOS：从官网下载安装包安装
# Android/iOS：在应用商店搜索安装
```

### 2.2 配置 Tailscale Serve
将 MoltBot 端口通过 HTTPS 暴露：
```bash
tailscale serve --bg 3000 http://127.0.0.1:18789
```
访问地址：`https://你的设备名.tailnet.ts.net`

## 三、访问地址格式

### 3.1 本地访问
```
http://127.0.0.1:18789
或
http://localhost:18789
```

### 3.2 局域网访问
```
http://<服务器IP>:18789/?token=<你的token>
```
通过以下命令获取包含正确 Token 的链接：
```bash
moltbot dashboard --print-url
```

### 3.3 HTTPS 访问
```
https://your-machine.tailnet.ts.net
```

## 四、安全提示
⚠️ **重要警告**：
- 将 `allowInsecureAuth` 设置为 `true` 会降低安全性
- 请仅在可信任的内网环境中使用此配置
- **绝对不要**将这些配置用于公网访问
- 定期检查防火墙规则，确保端口 18789 不向公网开放

## 五、故障排除
1. **检查配置一致性**：
   ```bash
   moltbot config get gateway.auth.token
   moltbot config get gateway.remote.token
   ```

2. **运行诊断工具**：
   ```bash
   moltbot doctor --fix
   ```

3. **检查服务状态**：
   ```bash
   moltbot gateway status
   ```

4. **清除浏览器缓存**：
   使用无痕模式访问，或清除浏览器缓存

## 六、配置示例
完整配置文件示例（`~/.moltbot/moltbot.json`）：
```json
{
  "gateway": {
    "bind": "lan",
    "port": 18789,
    "auth": {
      "token": "your_token_here"
    },
    "controlUi": {
      "allowInsecureAuth": true,
      "allowedOrigins": [
        "http://192.168.1.100:18789",
        "http://localhost:18789"
      ]
    },
    "remote": {
      "token": "your_token_here"
    }
  }
}
```

## 七、注意事项
1. 修改配置后**必须**重启服务
2. 如果通过局域网 IP 访问失败，检查防火墙是否开放 18789 端口
3. 确保客户端和服务端的 Token 配置完全一致
4. 推荐通过 HTTPS 访问，这是最安全的方式