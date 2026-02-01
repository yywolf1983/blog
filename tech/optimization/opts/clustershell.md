
clush


pip install clustershell

clustershell 安装

base_path="~/.local/etc/clustershell"
base_path="/etc/clustershell"

mkdir -p $base_path

cat << EOF > groups.conf

[Main]
default: local
confdir: /etc/clustershell/groups.conf.d $CFGDIR/groups.conf.d
autodir: /etc/clustershell/groups.d $CFGDIR/groups.d

[local]
map: [ -f $CFGDIR/groups ] && f=$CFGDIR/groups || f=$CFGDIR/groups.d/local.cfg; sed -n 's/^$GROUP:\(.*\)/\1/p' $f
all: [ -f $CFGDIR/groups ] && f=$CFGDIR/groups || f=$CFGDIR/groups.d/local.cfg; sed -n 's/^all:\(.*\)/\1/p' $f
list: [ -f $CFGDIR/groups ] && f=$CFGDIR/groups || f=$CFGDIR/groups.d/local.cfg; sed -n 's/^\([0-9A-Za-z_-]*\):.*/\1/p' $f

EOF

export PYTHONPATH=$PYTHONPATH:~/.local/lib
export PATH=$PATH:~/.local/bin



cat /etc/clustershell/groups
  ds: ds[001-006]
  local: local[1-5] local[7-10] local[12-14]
  haha: haha[001-005]

  all: ds[001-005] haha[001-005] local[1-5] local[7-10] local[12-14]
  all: @th @local @tb @kh


cat >  ssh_all.sh << EOF 
#!/usr/bin/expect
set time 30
spawn ssh -o StrictHostKeyChecking=no \$argv
expect {
    "(yes/no)?" {send "yes\r"}
    "*#" {send "exit\r"}
      }
expect eof
EOF

chmod +x ssh_all.sh

for i in `cat ~/.ssh/config | grep -e "Host\ "  | awk '{print $2}'`
do
  ./ssh_all.sh $i
done


#免认证
vi /etc/clustershell/clush.conf
[Main]
fanout: 64
connect_timeout: 15
command_timeout: 0
color: auto
fd_max: 8192
history_size: 100
maxrc: no
node_count: yes
verbosity: 1
ssh_options: -o StrictHostKeyChecking=no

clush -g db "uptime"

cat ~/.ssh/config
Host db_1
Hostname <SERVER>
User <USER>
Port <PORT>

Host db_2
Hostname <SERVER>
User <USER>
Port <PORT>

Host db_3
Hostname <SERVER>
User <USER>
#自动穿过代理机                                                                  
ProxyCommand ssh db_2 nc %h %p 2>/dev/null                          
Port 2001

-g 组
-a 所有
-w 主机
-b 合并

--copy
--rcopy
--dest
