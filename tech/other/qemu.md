建立 磁盘

qemu-img create -f raw vm1.raw 8G
qemu-img create -f qcow linux.img 8G

qemu-img info linux.img

启动
qemu.exe -kernel-kqemu -L . -m 1024 -hda linux.img -cdrom E:\soft\CentOS-6.5-i386-minimal.iso -boot d
qemu-system-x86_64.exe -L . -m 1024 -hda linux.img -cdrom  D:\soft\LFS\myiso.iso -boot d
-kernel-kqemu 加快qemu速度
-m 512 为虚拟机分配512m内存
-hda linux.img 系统安装到哪里去,就安装到刚才建立的虚拟磁盘文件中
-cdrom e:\my-lab\iso\windowsxp-en.iso 为qemu的虚拟光驱中插入光盘镜像
-boot d 设置qemu的BIOS由光驱启动.
-boot c 从磁盘启动

启动网卡
-net user
 -net nic,vlan=0,macaddr=52-54-00-12-34-01 -net tap,vlan=0,ifname=tap0,script=no
注意：上面的蓝色字体是指定guest使用的网卡类型等，红色部分指定tap联网信息
-net nic,macaddr=00:00:11:33:02:02

sudo apt-get install bridge-utils
sudo apt-get install uml-utilities

### 建立网桥
sudo brctl addbr br0
sudo ip link set br0 up

### 绑定物理网卡
sudo brctl addif br0 enp3s0

### 获取IP
sudo dhclient br0

### 创建虚拟网卡
sudo tunctl -b -t tap0
sudo ip link set tap0 up
sudo brctl addif br0 tap0

转换镜像格式
qemu-img convert -c -O qcow2 vm1.raw vm1.qcow2

改编镜像大小
qemu-img resize vm2.raw +2GB

查看快照
qemu-img snapshot -l /images/vm2.qcow2
注意：只有qcow2才支持快照
打快照
qemu-img snapshot -c booting vm2.qcow2
从快照回复
qemu-img snapshot -a 1 vm2.qcow2
删除快照
qemu-img snapshot -d 2 /images/vm2.qcow



## 调试内核
qemu-system-x86_64 -m 2048M -smp 2 -kernel ./vmlinuz-5.14.10 -append "root=/dev/ram console=ttyS0 rdinit=/sbin/init mem=1024M" -initrd ./initrd.img-5.14.10 -nographic -S -s

-m  为此guest虚拟机预留的内存大小，如果不指定，默认大小是128M
-smp  表示guest虚拟机的cpu的个数
上面两个不是必须的参数选项。

-kernel 后面跟的是要调试的内核bzImage
-initrd  后面跟的是文件系统
-append 后面跟的是虚拟机的cmdline
-nographic  表示启动的是非图形界面的
-S 表示guest虚拟机一启动就会暂停
-s 表示监听tcp:1234端口等待GDB的连接

gdb ./vmlinuz-5.14.10
target remote localhost:1234
