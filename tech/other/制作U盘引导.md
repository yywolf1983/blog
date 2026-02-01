制作U盘引导

'''
yywolf1983 发表于 2013-07-30 18:36:50 
'''

安装前需要准备几个工具：
1.U盘的容量要大于1G空间
2.VMware ESX 4的ISO
下载地址:http://www.vmware.com/products/esx/
3.syslinux
下载地址:http://kernel.org/pub/linux/utils/boot/syslinux/

准备好以上工具后可以按照下面的步骤制做：
1.将U盘格式化成FAT 32文件系统格式
2.将ESX4.1 ISO文件解压到U盘的根目录
3.在命令中运行syslinux工具，具体参数看下面
#syslinux.exe -s -m -f -a k:       <---k是U盘的盘符,具体使用参数可以看帮助
4.进入U盘isolinux目录和目录中的isolinux.cfg文件修改成syslinux目录和syslinux.cfg文件
5.完成上面的操作，将U盘移除出系统。
6.在需要安装ESX的机器上插入这个U盘，使用USB设备启动
7.屏幕画面会出现Syslinux工具的命令行，直接按回车既运行ESX 4.1 ISO的内容


启动光盘
linux 启动光盘制作

  yywolf1983 发表于 2013-07-30 18:33:41  删除     编辑  

一、制作可启动的GRUB光盘。
$ mkdir iso # 新建一个iso目录,这将作为LiveCD的镜像目录.
$ mkdir -p iso/boot/grub #在iso目录中创建boot/grub子目录
$ cp /usr/share/grub/i386-redhat/stage2_eltorito iso/boot/grub
$ mkisofs -R -b boot/grub/stage2_eltorito -no-emul-boot \
-boot-load-size 4 -boot-info-table -o teach.iso iso #制作以iso目录为镜像目录的启动光盘.
mkisofs -o 123.iso -JRAVv /path   制作iso光盘
二、制作可启动的小内核Linux光盘。
$ cp /boot/vmlinuz-2.6.15-1.2054_FC5 iso/book
$ mkisofs -R -b boot/grub/stage2_eltorito -no-emul-boot \
-boot-load-size 4 -boot-info-table -o teach.iso iso
grub> root (cd)
grub> kernel /boot/vmlinuz-2.6.15-1.2054
grub> boot
三、不用输入命令。
建立文件：/boot/grub/grub.conf
grub.conf 的文件内容可以如下所示(As your wish):
#grub.conf start *********************************
default 0
timeout 5
hiddenmenu
title MyLinux
root (cd)
kernel /boot/vmlinuz-2.6.15-1.2054 quiet
#grub.conf end *********************************
这个文件告诉grub,启动的时候默认启动第一个title, 等待时间是1秒钟,不要显示选择菜单,第一
个Title的名字是MyLinux,依次执行的命令是 root ...和kernel ..,其中quiet参数告诉kernel启动的时候不要显示信息。重新制作我们的iso文件
四、制作initrd.img
$ su #输入密码,变成root

#
mkdir initrd #创建一个initrd的目录,我们会把initrd.img挂载到这个目录
 dd if=/dev/zero of=initrd.img bs=400k count=10 #创建一个4M的initrd.img
 /sbin/mke2fs -F -m0 initrd.img # 将initrd.img初始化成ex2文件系统
 mount -o loop initrd.img initrd # 将initrd.img挂载到initrd上
 mkdir initrd/dev #在initrd目录(也就是initrd.img文件)中创建/dev目录
 mknod initrd/dev/console c 5 1 # 增加一个控制台节点
五、修改grub.conf文件
要使用initrd.img,grub.conf应该这样修改:
grub.conf 的文件内容可以如下所示(As your wish):

#
grub.conf start

**  
default 0  
timeout 1  
hiddenmenu  
title LiLiHome  
root (cd)  
kernel /boot/vmlinuz quiet root=/dev/ram1 rw   init=/linuxrc  
initrd /boot/initrd.img  
#grub.conf end   
**
