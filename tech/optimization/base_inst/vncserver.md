
## vncserver

yum install tigervnc-server

vim /etc/sysconfig/vncservers
VNCSERVERS="1:root"
VNCSERVERARGS[1]="-geometry 1024x768 -alwaysshared -depth 24"

vncserver -kill :1
vncpasswd

vi /usr/bin/vncserver--
vncPort

sudo systemctl cat vncserver@:1.service

vi /etc/systemd/system/vncserver@:1.service
[Unit]
Description=Remote desktop service (VNC)
After=syslog.target network.target

[Service]
#Type=forking
# Clean any existing files in /tmp/.X11-unix environment
ExecStartPre=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'
ExecStart=/sbin/runuser -l yy -c "/usr/bin/vncserver %i -geometry 1280x1024"
PIDFile=/home/yy/.vnc/%H%i.pid
ExecStop=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'

[Install]
WantedBy=multi-user.target


sudo systemctl daemon-reload
sudo systemctl enable vncserver@:1.service
sudo systemctl disable vncserver@:1.service

