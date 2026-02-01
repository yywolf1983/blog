
username="yy"
sudo echo "${username} ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/${username}

# 修改DNSsudo sed -i 's/#DNS=/DNS=8.8.8.8/' /etc/systemd/resolved.conf
sudo sed -i 's/#FallbackDNS=/FallbackDNS=223.5.5.5/' /etc/systemd/resolved.conf
sudo systemctl restart systemd-resolved.service

sudo apt-get update && sudo apt-get upgrade -y

sudo apt-get install -y vim
sudo apt install iputils-ping

ip_address="192.168.2.101/24"
netmask="255.255.255.0"
gateway="192.168.2.1"
dns_servers="223.5.5.5,8.8.8.8,8.8.4.4"

# 设置静态IP
sudo tee /etc/netplan/00-installer-config.yaml > /dev/null << EOF
# This is the network config written by 'subiquity'
network:
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: false
      addresses:
        - ${ip_address}
      nameservers:
        addresses: [${dns_servers}]
      routes:
        - to: default
          via: ${gateway}
  version: 2
EOF

sudo netplan apply

sudo hostnamectl set-hostname ks1

sudo apt-get update && sudo apt-get install -y containerd


cat << EOF > base.sh

# 设置静态IP
ip_address="192.168.2.100"
netmask="255.255.255.0"
gateway="192.168.2.1"
dns_servers="223.5.5.5 8.8.8.8 8.8.4.4"

sudo sed -i 's/dhcp/static/g' /etc/network/interfaces
sudo sed -i "\$a\address ${ip_address}" /etc/network/interfaces
sudo sed -i "\$a\netmask ${netmask}" /etc/network/interfaces
sudo sed -i "\$a\gateway ${gateway}" /etc/network/interfaces
sudo sed -i "\$a\dns-nameservers ${dns_servers}" /etc/network/interfaces
sudo service networking restart
EOF


