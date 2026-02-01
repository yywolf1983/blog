

net.ipv4.ip_forward = 1
net.ipv4.tcp_timestamps = 0
net.ipv4.tcp_tw_recycle = 0



https://openvpn.net/community-downloads/

apt install libssl-dev
apt-get install liblzo2-dev
apt-get install libpam0g-dev

openvpn xxx.ovpn

openvpn3 configs-list
openvpn3 sessions-list

openvpn3 session-start --config cy1.ovpn

openvpn3 session-manage --config my-vpn-config.conf --restart


第一种方法： 客户端进行配置
在配置文件下增加如下内容：
route-nopull # 客户端连接openvpn后 不从服务端获取路由
max-routes 1000 # 设置路由的最大条数，默认是100，这里可以根据需求修改
route 192.168.0.0 255.255.0.0 net_gateway # 使192.168.0.0/24网段，不走vpn网关
route 192.168.1.0 255.255.0.0 vpn_gateway # 使192.168.1.0/24网段，走vpn网关

第二种方法： 在服务端进行配置
服务端和客户端的配置略有不同
push "route 192.168.0.0 255.255.0.0 net_gateway" # 将引号中的路由推送到客户端
push "route 192.168.1.0 255.255.0.0 vpn_gateway" # 将引号中的路由推送到客户端
注意： 如果这里有 若配置中有redirect-gateway则需要先删除


windows
route delete 0.0.0.0
route add 0.0.0.0 mask 0.0.0.0 192.168.1.1


固定ip
client-config-dir /etc/openvpn/ccd

cat /etc/openvpn/ccd/mac

`ifconfig-push 10.8.0.2 255.255.255.0`

以上设置可配置使用mac帐号登录的客户端ip地扯为10.8.0.2


## 上网转发
iptables -t nat -A POSTROUTING -s 10.8.0.0/24  -j MASQUERADE