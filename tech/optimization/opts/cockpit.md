
yum install cockpit

systemctl enable --now cockpit.socket

9090

磁盘管理
yum install -y cockpit-storaged

集群管理
yum install -y cockpit-dashboard
