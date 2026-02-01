
https://github.com/fatedier/frp/releases


cat > frps.ini << EOF
[common]
token = dWyG8tqKqLXv6Ssa
bind_port = 7000
dashboard_addr = 0.0.0.0
dashboard_port = 7500
dashboard_user = admin
dashboard_pwd = admin110

log_file = /data/frp/frps.log
log_level = info
log_max_days = 3
disable_log_color = true

EOF

## frps.service

cat > /etc/systemd/system/frps.service << EOF
[Unit]
Description=Frp Server Service
After=network.target

[Service]
Type=simple
User=nobody
Restart=on-failure
RestartSec=5s
ExecStart=/data/frp/frps -c /data/frp/frps.ini

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable frps
sudo systemctl start frps
sudo systemctl restart frps

cat > frpc.ini << EOF
[common]
server_addr = tapi.usda.one
server_port = 7000
token = dWyG8tqKqLXv6Ssa

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6222

[3389]
type = tcp
local_ip = 192.168.1.110
local_port = 3389
remote_port = 6389
EOF

## frpc.service

sudo cat > /etc/systemd/system/frpc.service << EOF
[Unit]
Description=Frp Client Service
After=network.target

[Service]
Type=simple
User=nobody
Restart=on-failure
RestartSec=5s
ExecStart=/data/frp/frpc -c /data/frp/frpc/frpc.ini
ExecReload=/data/frp/frpc reload -c /data/frp/frpc/frpc.ini
[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable frpc
sudo systemctl start frpc
sudo systemctl restart frpc