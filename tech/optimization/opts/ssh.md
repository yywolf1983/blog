
ssh 验证设置

GIT_SSH="C:\Program Files\PuTTY\plink.exe"

ssh-add -K ~/.ssh/id_rsa

~. Disconnect.  

echo ${SSH_CLIENT}

#Denyhosts SHELL SCRIPT
#防止暴力破解
 ```
cat /var/log/secure|awk '/Failed/{print $(NF-3)}'|sort|uniq -c|awk '{print $2"="$1;}' >Denyhosts.txt
DEFINE="10"
for i in `cat Denyhosts.txt`
do
        IP=`echo $i|awk -F= '{print $1}'`
        NUM=`echo $i|awk -F= '{print $2}'`
        if [ $NUM -gt $DEFINE ]
        then
                grep $IP /etc/hosts.deny >/dev/null
                if [ $? -gt 0 ];
                then
                echo "sshd:$IP" >> /etc/hosts.deny
                fi
        fi
done
```

修改密码
ssh-keygen -f ~/.ssh/id_rsa -p

    ssh-keygen -t rsa -b 4096  -L -f mysql    

    openssl genrsa -des3 -out privkey.pem 2048   手动生成私钥  -des3 为密码格式

    ssh-keygen -e -f ~/.ssh/id_dsa > abc   生成成 IETF SECSH 格式公钥
    ssh-keygen -i -f ~/.ssh/abc  将 IETF SECSH 转换成 ssh 格式公钥

    ssh-keygen -y -f id_rsa 直接生成ssh 公钥

    ssh-keygen -l -f ~/.ssh/id_rsa.pub   查看key指纹
    ssh-keygen -l -v -E md5  -f ~/.ssh/id_rsa.pub  md5指纹


    生成私钥：openssl genrsa -out test.key 1024

    生成公钥：openssl rsa -in test.key -pubout -out test_pub.key

    用公钥加密：openssl rsautl -encrypt -pubin -inkey test_pub.key -in aaa.txt -out en.txt

    用私钥解密：openssl rsautl -decrypt -inkey test.key -in en.txt -out de.txt


# Setup SSH agent??
eval "$(ssh-agent -s)"
ssh-add -K ~/.ssh/id_rsa


1，只允许某个IP登录，拒绝其他所有IP
在 /etc/hosts.allow 写:
sshd: 1.2.3.4
在 /etc/hosts.deny 写:
sshd: ALL
用 iptables 也行:
iptables -I INPUT -p tcp --dport 22 -j DROP
iptables -I INPUT -p tcp --dport 22 -s 1.2.3.4 -j ACCEPT

2，禁止某个用户通过ssh登录
在/etc/ssh/sshd_conf添加
AllowUsers 用户名
或者
AllowGroups 组名
或者
DenyUsers 用户名

3，设定登录黑名单
vi /etc/pam.d/sshd
增加
auth required /lib/security/pam_listfile.so item=user sense=deny file=/etc/sshd_user_deny_list onerr=succeed
所有/etc/sshd_user_deny_list里面的用户被拒绝ssh登录
config

~/.ssh/config

Host    别名
HostName        主机名
Port            端口
User            用户名
IdentityFile    密钥文件的路径

ssh config

~/.ssh/config
Host *
#防止自动断开
ServerAliveInterval 30
user root


#自动穿过代理机
Host tb185                                                                      
ProxyCommand ssh tb95 nc 10.172.195.185 %p 2>/dev/null                          
Port 2001

#W18 是跳板
Host      ll118
hostname  127.0.0.1
ProxyCommand ssh W18 nc %h %p 2>/dev/null
Port      2222


http://doc.licess.org/openssh/sshd_config.html

# 1. 关于 SSH Server 的整体设定，包含使用的 port 啦，以及使用的密码演算方式
Port 22          # SSH 预设使用 22 这个 port，您也可以使用多的 port ！
            　 # 亦即重复使用 port 这个设定项目即可！
Protocol 2,1      　 # 选择的 SSH 协议版本，可以是 1 也可以是 2 ，
            　 # 如果要同时支持两者，就必须要使用 2,1 这个分隔了！
#ListenAddress 0.0.0.0   # 监听的主机适配卡！举个例子来说，如果您有两个 IP，
            　 # 分别是 192.168.0.100 及 192.168.2.20 ，那么只想要
            　 # 开放 192.168.0.100 时，就可以写如同下面的样式：
ListenAddress 192.168.0.100          # 只监听来自 192.168.0.100 这个 IP 的SSH联机。
                   # 如果不使用设定的话，则预设所有接口均接受 SSH
PidFile /var/run/sshd.pid      # 可以放置 SSHD 这个 PID 的档案！左列为默认值
LoginGraceTime 600     # 当使用者连上 SSH server 之后，会出现输入密码的画面，
            　 # 在该画面中，在多久时间内没有成功连上 SSH server ，
            　 # 就断线！时间为秒！
Compression yes      # 是否可以使用压缩指令？当然可以啰！

# 2. 说明主机的 Private Key 放置的档案，预设使用下面的档案即可！
HostKey /etc/ssh/ssh_host_key    # SSH version 1 使用的私钥
HostKey /etc/ssh/ssh_host_rsa_key  # SSH version 2 使用的 RSA 私钥
HostKey /etc/ssh/ssh_host_dsa_key  # SSH version 2 使用的 DSA 私钥
# 2.1 关于 version 1 的一些设定！
KeyRegenerationInterval 3600　   　# 由前面联机的说明可以知道， version 1 会使用
                   # server 的 Public Key ，那么如果这个 Public
                   # Key 被偷的话，岂不完蛋？所以需要每隔一段时间
                   # 来重新建立一次！这里的时间为秒！
ServerKeyBits 768         　 # 没错！这个就是 Server key 的长度！
# 3. 关于登录文件的讯息数据放置与 daemon 的名称！
SyslogFacility AUTH        　# 当有人使用 SSH 登入系统的时候，SSH会记录资
                   # 讯，这个信息要记录在什么 daemon name 底下？
                   # 预设是以 AUTH 来设定的，即是 /var/log/secure
                   # 里面！什么？忘记了！回到 Linux 基础去翻一下
                   # 其它可用的 daemon name 为：DAEMON,USER,AUTH,
                   # LOCAL0,LOCAL1,LOCAL2,LOCAL3,LOCAL4,LOCAL5,
LogLevel INFO            # 登录记录的等级！嘿嘿！任何讯息！
                  
PermitRootLogin no     # 是否允许 root 登入！预设是允许的，但是建议设定成 no！
UserLogin no      　 # 在 SSH 底下本来就不接受 login 这个程序的登入！
StrictModes yes      # 当使用者的 host key 改变之后，Server 就不接受联机，
            　 # 可以抵挡部分的木马程序！
#RSAAuthentication yes   # 是否使用纯的 RSA 认证！？仅针对 version 1 ！
PubkeyAuthentication yes　 # 是否允许 Public Key ？当然允许啦！只有 version 2
AuthorizedKeysFile      .ssh/authorized_keys
            　 # 上面这个在设定若要使用不需要密码登入的账号时，那么那个
            　 # 账号的存放档案所在档名！
# 4.2 认证部分
RhostsAuthentication no  # 本机系统不止使用 .rhosts ，因为仅使用 .rhosts 太
            　 # 不安全了，所以这里一定要设定为 no ！
IgnoreRhosts yes    　 # 是否取消使用 ~/.ssh/.rhosts 来做为认证！当然是！
RhostsRSAAuthentication no # 这个选项是专门给 version 1 用的，使用 rhosts 档案在
            　 # /etc/hosts.equiv配合 RSA 演算方式来进行认证！不要使用
HostbasedAuthentication no # 这个项目与上面的项目类似，不过是给 version 2 使用的！
IgnoreUserKnownHosts no  # 是否忽略家目录内的 ~/.ssh/known_hosts 这个档案所记录
            　 # 的主机内容？当然不要忽略，所以这里就是 no 啦！
允许密码验证
PasswordAuthentication yes # 密码验证当然是需要的！所以这里写 yes 啰！
PermitEmptyPasswords no  # 若上面那一项如果设定为 yes 的话，这一项就最好设定
            　 # 为 no ，这个项目在是否允许以空的密码登入！当然不许！
ChallengeResponseAuthentication yes  # 挑战任何的密码认证！所以，任何 login.conf
                   # 规定的认证方式，均可适用！
#PAMAuthenticationViaKbdInt yes      # 是否启用其它的 PAM 模块！启用这个模块将会
                   # 导致 PasswordAuthentication 设定失效！

# 4.3 与 Kerberos 有关的参数设定！因为我们没有 Kerberos 主机，所以底下不用设定！
#KerberosAuthentication no
#KerberosOrLocalPasswd yes
#KerberosTicketCleanup yes
#KerberosTgtPassing no

# 4.4 底下是有关在 X-Window 底下使用的相关设定！
X11Forwarding yes
#X11DisplayOffset 10
#X11UseLocalhost yes
# 4.5 登入后的项目：
PrintMotd no              # 登入后是否显示出一些信息呢？例如上次登入的时间、地点等
            　# 等，预设是 yes ，但是，如果为了安全，可以考虑改为 no ！
PrintLastLog yes    　# 显示上次登入的信息！可以啊！预设也是 yes ！
KeepAlive yes       # 一般而言，如果设定这项目的话，那么 SSH Server 会传送
            　# KeepAlive 的讯息给 Client 端，以确保两者的联机正常！
            　# 在这个情况下，任何一端死掉后， SSH 可以立刻知道！而不会
            　# 有僵尸程序的发生！
UsePrivilegeSeparation yes # 使用者的权限设定项目！就设定为 yes 吧！
MaxStartups 10      # 同时允许几个尚未登入的联机画面？当我们连上 SSH ，
            　# 但是尚未输入密码时，这个时候就是我们所谓的联机画面啦！
            　# 在这个联机画面中，为了保护主机，所以需要设定最大值，
            　# 预设最多十个联机画面，而已经建立联机的不计算在这十个当中
# 4.6 关于使用者抵挡的设定项目：
DenyUsers *      　 # 设定受抵挡的使用者名称，如果是全部的使用者，那就是全部
            　# 挡吧！若是部分使用者，可以将该账号填入！例如下列！
DenyUsers test
DenyGroups test    　 # 与 DenyUsers 相同！仅抵挡几个群组而已！
# 5. 关于 SFTP 服务的设定项目！
Subsystem       sftp    /usr/lib/ssh/sftp-server
ssh 反向管道

建立反向管道
ssh -fN -R 10022:localhost:22 root@1.1.1.1
ssh-fCNL *:20000:localhost:10000 localhost

“-R 10022:localhost:22” 选项定义了一个反向隧道。它转发中继服务器 10022 端口的流量到本地服务器的 22 号端口。

登录到中继服务器，确认其 127.0.0.1:10022 绑定到了 sshd。

可以登录了
ssh -p 10022 root@localhost

本地端口转发：
ssh -L <local port>:<remote host>:<remote port> <SSH hostname>

从本地 3333 端口 通过 47.96.164.18 访问 远端内网 10.10.13.203
ssh -CfNg -L 3333:10.10.13.203:3306 root@47.96.164.18 -p 5272

远程端口转发：
ssh -R <local port>:<remote host>:<remote port> <SSH hostname>
       local 转发到 remote

通过47.96.164.18 的 3333 端口到本地 3333 端口  转发给10.10.13.203 3306端口
ssh -CfNg -R 3333:10.10.13.203:3306 root@47.96.164.18 -p 5272


***直接登录
在ssh打开
vi /etc/ssh/sshd_conf
GatewayPorts clientspecified
GatewayPorts yes
重启ssh

绑定反向隧道到公网地址
ssh -fN -R 1.1.1.1:10022:localhost:22 root@1.1.1.1
ssh -gNfR *:2222:192.168.2.14:22 root@1.1.1.1 -p 33001
ssh -gNfR *:2223:192.168.2.50:3389 root@1.1.1.1 -p 33001


就可以用公网地址直接登录了
ssh -p 10022 root@1.1.1.1

autossh 可以实现自动连接

autossh -M 10900 -fN -o "PubkeyAuthentication=yes" -o "StrictHostKeyChecking=false" -o "PasswordAuthentication=no" -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R 1.1.1.1:10022:localhost:22 relayserver_user@1.1.1.1

“-M 10900” 选项指定中继服务器上的监视端口，用于交换监视 SSH 会话的测试数据。中继服务器上的其它程序不能使用这个端口。
“-fN” 选项传递给 ssh 命令，让 SSH 隧道在后台运行。
“-o XXXX” 选项让 ssh：

autossh -M 10901 -fN -o "PubkeyAuthentication=yes" -o "StrictHostKeyChecking=false" -o "PasswordAuthentication=no" -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R  *:2223:192.168.2.50:3389 root@117.34.109.79 -p 33001

*/1 * * * * /usr/bin/sh /root/autossh.sh
#/usr/bin/sh
id=1
autosshpid=`ps -ef |grep -v grep  | grep "autossh -M 10905" | wc -l`
if [ "$autosshpid" -ne "$id" ]
then
        echo "auto start ssh 3389"
        /usr/local/bin/autossh -M 10905 -fN -o "PubkeyAuthentication=yes" -o "StrictHostKeyChecking=false" -o "PasswordAuthentication=no" -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R  *:2223:192.168.0.184:3389 root@60.161.128.165 -p 22369
fi
sleep 3

autosshpid2=`ps -ef |grep -v grep  | grep "autossh -M 10900" | wc -l`
if [ "$autosshpid2" -ne "$id" ]
then
        echo "auto start ssh 22"
        /usr/local/bin/autossh -M 10900 -fN -o "PubkeyAuthentication=yes" -o "StrictHostKeyChecking=false" -o "PasswordAuthentication=no" -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R  *:2222:192.168.2.25:22 root@117.34.109.79 -p 33001
fi

ps -ef | grep -v grep | grep "ssh -L" | awk '{print $2}' | xargs kill -9 ; killall -9 autossh


加上参数-b 0.0.0.0
可以在/etc /sshd_config中修改GatewayPorts no为GatewayPorts yes来打开它。


使用密钥验证，而不是密码验证。
自动接受（未知）SSH 主机密钥。
每 60 秒交换 keep-alive 消息。
没有收到任何响应时最多发送 3 条 keep-alive 消息。


ftp1@sdwl
限制sftp 用户
1. 我们需要创建一个用户组，专门用于sftp用户
$ groupadd sftp
2. 我们创建一个用户test
$ useradd -s /bin/false -d /data/sftp/ftp1 -G sftp ftp1
注意这里我们将ftp1用户的shell设置为/bin/false使他没有登陆shell的权限
3. 编辑 /etc/ssh/sshd_config
找到Subsystem这个配置项，将其修改为
Subsystem  sftp  internal-sftp
然后再到文件最尾处增加配置设定属于用户组sftp的用户都只能访问他们自己的home文件夹
Match Group sftp # 用户组
#ChrootDirectory %h
ChrootDirectory /data/sftp/%u
ForceCommand internal-sftp
AllowTcpForwarding no
保存并关闭文件
4. 修改test用户文件夹的权限，让其属于root用户
chown root /data/sftp
5. 重启sshd服务
$ service sshd restart
6. 测试用户账号
$ ssh ftp1@localhost
连接会被拒绝或者无法登陆
$ sftp test@localhost
自动登录

第一步，生成钥匙对
$ ssh-keygen -d
$ ssh-keygen -t rsa

第二步，把公钥上传到服务器上去
$ ssh-copy-id -i ~/.ssh/id_dsa.pub fwolf.com
 ssh-copy-id "-p green@125.76.226.179"

这个也可以
$ scp ~/.ssh/id_dsa.pub fwolf@fwolf.com
$ ssh fwolf@fwolf.com
$ cat fwolf_dsa.pub >> ~/.ssh/authorized_keys
$ chmod 644 authorized_keys

第三步，我们来享受一下自动登录的乐趣吧
$ ssh fwolf.com

4、解决本地登陆用户与远程登陆用户不一致
~/.ssh/config
Host *
#防止自动断开
ServerAliveInterval 30
user root



ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
ssh-keygen -t esdsa -f /etc/ssh/ssh_host_esdsa_key
ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key

vi /etc/hosts.allow 
sshd: ALL

/etc/sshd/sshd_config
PermitRootLogin yes
