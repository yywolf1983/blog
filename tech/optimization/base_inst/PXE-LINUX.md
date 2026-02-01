
yum -y install tftp tftp-server dhcp syslinux

vi /etc/xinetd.d/tftp
vi /etc/dhcp/dhcpd.conf

subnet 172.16.4.0 netmask 255.255.255.0 {
option routers                  172.16.4.1;
option subnet-mask              255.255.255.0;
filename "pxelinux.0";
next-server 172.16.4.100;   #tftp 地址
option domain-name-servers      172.162.4.1;
option time-offset              -18000; # Eastern Standard Time
range dynamic-bootp 172.16.4.100 172.16.4.200;
default-lease-time 21600;
max-lease-time 43200;
# we want the nameserver to appear at a fixed address
host ns {
next-server marvin.redhat.com;
hardware ethernet 12:34:56:78:AB:CD;
fixed-address 207.175.42.254;
}
}

service dhcpd restart
service tftp restart
/data/nginx/sbin/nginx

yum install yum-utils
repoquery -q -l syslinux

cp /usr/share/syslinux/pxelinux.0 /var/lib/tftpboot
cp /usr/share/syslinux/menu.c32 /var/lib/tftpboot
cp /iso/isolinux/vesamenu.c32 /var/lib/tftpboot

mount -o loop CentOS-7-x86_64-Minimal-1810.iso /mnt/

mkdir -p /var/lib/tftpboot/pxelinux.cfg/
cp /iso/isolinux/isolinux.cfg  /var/lib/tftpboot/pxelinux.cfg/default

vi /var/lib/tftpboot/pxelinux.cfg/default
DEFAULT vesamenu.c32
PROMPT 0
#十分之一秒
TIMEOUT 60
MENU TITLE        
label linux m
  menu label ^手动安装
  kernel vmlinuz
  #append initrd=initrd.img  inst.stage2=http://192.168.0.184/tftp/ISO/ quiet
  append initrd=initrd.img  ks=http://192.168.0.184/tftp/ks.cfg
label linux
  menu label ^Install CentOS 7
  kernel vmlinuz
  #append initrd=initrd.img  inst.stage2=http://192.168.0.184/tftp/ISO/ quiet
  append initrd=initrd.img  ks=http://192.168.0.184/tftp/ks.cfg

vi /ios/ks.cfg
#version=DEVEL
# System authorization information
auth --enableshadow --passalgo=sha512
# Use graphical install
graphical
# Run the Setup Agent on first boot
firstboot --enable
ignoredisk --only-use=sda
# Keyboard layouts
keyboard --vckeymap=cn --xlayouts='cn'
# System language
lang zh_CN.UTF-8

# Network information
network  --bootproto=dhcp --device=enp2s0 --ipv6=auto --activate
network  --hostname=localhost.localdomain

# Use network installation
url --url="http://192.168.0.184/tftp/pub/"
# rootpw "password"  #可以是明文密码
# Root password is 1234567
rootpw --iscrypted $6$/MaCTB2/td4MF8iM$grlbbScun5NNIp3F0eloSGYK0aG1iw.RERIoxR0Z547daP4LGMcL/LJfoZnEhxSD/VLM45vPlACMbkp1skah2.
# System services
services --enabled="chronyd"
# System timezone
timezone Asia/Shanghai --isUtc
# System bootloader configuration
bootloader --append=" crashkernel=auto" --location=mbr --boot-drive=sda
# Partition clearing information
clearpart --all --initlabel
# Disk partitioning information
#part swap --fstype="swap" --ondisk=sda --size=8192
part / --fstype="xfs" --ondisk=sda --grow
#part /home --fstype="xfs" --ondisk=sda --size=307200
#part /boot --fstype="xfs" --ondisk=sda --size=1024
#part /data --fstype="xfs" --ondisk=sda --size=555530

selinux --disabled

%packages
@^minimal
@core
chrony
kexec-tools

%end

%addon com_redhat_kdump --enable --reserve-mb='auto'

%end

%anaconda
pwpolicy root --minlen=7 --minquality=1 --notstrict --nochanges --notempty
pwpolicy user --minlen=6 --minquality=1 --notstrict --nochanges --emptyok
pwpolicy luks --minlen=6 --minquality=1 --notstrict --nochanges --notempty
%end

# Reboot after installation
reboot

END ks.cfg

chmod 777 /iso -R

cp /mnt/images/pxeboot/initrd.img /var/lib/tftpboot/
cp /mnt/images/pxeboot/vmlinuz /var/lib/tftpboot/


vi /etc/exports
/iso   *(ro)
service nfs start
exportfs


------------------------------

http://ipxe.org/

git clone git://git.ipxe.org/ipxe.git
  cd ipxe/src
  make

yum install mkisofs

make bin/ipxe.iso
make bin/ipxe.usb
dd if=bin/ipxe.usb of=/dev/sdX

demo.ipxe
#!ipxe
dhcp
ifstat
chain http://172.16.4.100/iso/index.html

make bin/undionly.kpxe EMBED=demo.ipxe

cp bin/undionly.kpxe /var/lib/tftpboot/

vi index.html  
#!ipxe
set base http://172.16.4.100/iso
set 210:string ${base}
set 209:string pxelinux.cfg/default
set 208:hex f1:00:74:7e
echo ${filename}
set filename ${210:string}pxelinux.0
chain ${filename} ||
echo Booting ${filename} failed, dropping to shell
shell

vi /etc/dhcp/dhcpd.conf
next-server 172.16.4.100;
 if exists user-class and option user-class = "iPXE" {
      filename "install.ipxe";
  } else {
      filename "undionly.kpxe";
  }

yum install system-config-kickstart


注意光盘要挂在copy 出来 不然repodata下文件名会出错
sudo mount -o loop ubuntu-16.10-server-amd64.iso /mnt/iso 