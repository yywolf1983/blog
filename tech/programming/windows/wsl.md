Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform

sudo apt remove openssh-server
sudo apt install openssh-client openssh-server

sudo vim /etc/ssh/sshd_config

sudo service ssh start             #启动SSH服务
sudo service ssh status            #检查状态
sudo systemctl enable ssh          #开机自动启动ssh命令


sed -i '/^sudo service ssh --full-restart/ d' ~/.bashrc

##使用sudo开机自启动
echo -e "%sudo\tALL=(ALL) NOPASSWD: /usr/sbin/service ssh --full-restart" | sudo tee -a /etc/sudoers

##检测ssh的状态，也是写入到bash中
cat << 'EOF' >> ~/.bashrc
sshd_status=$(service ssh status)
if [[ $sshd_status = *"is not running"* ]]; then
  sudo service ssh --full-restart
fi
EOF

sudo vi /etc/init.wsl
#!/bin/sh
# Filename: /etc/init.wsl
# Usage: sudo /etc/init.wsl [start|stop|restart]
/etc/init.d/ssh $1
/etc/init.d/cron $1


开始-运行(或者win+r)，输入：shell:startup
添加到自动启动 startubuntu.vbs
Set ws = WScript.CreateObject("WScript.Shell")
ws.run "wsl -d ubuntu -u root /usr/sbin/service ssh --full-restart", vbhide
ws.run "ubuntu run sudo /etc/init.wsl start", vbhide

要设置sudo免密 

sudo vi /etc/sudoers
yy ALL=(ALL:ALL) NOPASSWD: ALL