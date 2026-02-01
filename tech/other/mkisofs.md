
mkisofs

apt-get install genisoimage isolinux
yum install squashfs-tools
yum install libuuid-devel
https://www.kernel.org/pub/linux/utils/boot/syslinux/

yum install  ncurses-devel
yum install  glibc-static -y
busybox
make menuconfig  添加静态编译

make && make install && cd ./_install

mkdir proc sys etc dev
cd dev
mknod console c 5 1 (创建一个控制台字符设备文件)
mknod null c 1 3    (创建一个0设备文件)
cd ../etc
vim fstab
proc  /proc proc  defaults  0 0
sysfs /sys sysfs defaults  0 0
mkdir init.d
vim init.d/rcS
#!/bin/sh
Mount -a
chmod +x init.d/rcS
vim inittab

::sysinit:/etc/init.d/rcS
console::respawn:-/bin/sh
::ctrlaltdel:/sbin/reboot
::shutdown:/bin/umount –a -r
cd ..
rm linuxrc
ln –sv bin/busybox init





isolinux/
  ->isolinux.bin
  ->isolinux.cfg
  ->ldlinux.c32 -> /usr/lib/syslinux/modules/bios/ldlinux.c32
  ->vmlinuz-3.19-lfs-7.7-systemd


mksquashfs LFS LFS.squashfs

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
isolinux.cfg
------------
default linux64
prompt 1
timeout 600
#display boot.msg
#F1 F1.txt
#F2 F2.txt
#F3 F3.txt
#F4 F4.txt
#F5 F5.txt
#F6 F6.txt
#F7 F7.txt
#F8 F8.txt
#F9 F9.txt
#F10 F10.txt

label linux64
  kernel vmlinuz-3.19-lfs-7.7-systemd
  append root=/dev/ram0 init=/init dokeymap looptype=squashfs  loop=/image.squashfs  cdroot initrd=initramfs.cpio.gz /vga=791
  #这里不需要 looptype=squashfs  loop=/image.squashfs

label LFS
  #menu label ^Live USB Persistence
  linux /live/vmlinuz
  initrd /live/initrd.img
  append boot=live noconfig=sudo username=root hostname=kali persistence

%%%%%%%%%%%%%%%%%%%%%%%%%%%
gentoo livecd 实现原理

在 initrd 启动是创建/mnt/livecd
并挂载 /dev/loop0 到 /mnt/livecd
将其他链接到 /mnt/livecd

/etc/initrd.script
CDROOT_MARKER='/livecd'

ln -s /usr /livecd/usr

~~~~~~~~~~~~~~~~~~~~~~~~~~~

mkdir sub
cp hello sub/init
cd sub
find . | cpio -o -v -H newc | gzip > ../initramfs_data.cpio.gz
find . -print | cpio -o -v -H newc |gzip -9 -c - > ../gentoo.igz.new
cd ..
rm -rf sub


zcat initramfs_data.cpio.gz | cpio -i -d -H newc --no-absolute-filenames


gzip -cd initrd.img > initrd.ext2
mount -o loop initrd.ext2 /mnt/

umount /mnt/
gzip -c9 initrd.ext2 > initrd.img
---------------------------

mkisofs -o output.iso \
   -b isolinux/isolinux.bin -c isolinux/boot.cat \
   -no-emul-boot -boot-load-size 4 -boot-info-table \
   CD_root

boot.cat auto crente

genisoimage  -r -V "yy LFS" -cache-inodes -J -l  -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -o yy_LFS.iso  /LFS

mkisofs(make iso file system)

功能说明：建立ISO 9660映像文件。

语  法：mkisofs [-adDfhJlLNrRTvz][-print-size][-quiet][-A <应用程序ID>][-abstract < 摘要文件>][-b <开机映像文件>][-biblio <ISBN文件>][-c <开机文件名称>] [-C <盘区编号，磁区编号>][-copyright <版权信息文件>][-hide <目录或文件名>] [-hide-joliet <文件或目录名>][-log-file <记录文件>][-m <目录或文件名>] [-M <开机映像文件>][-o <映像文件>][-p <数据处理人>][-P <光盘发行人>] [-sysid <系统ID >][-V <光盘ID >][-volset <卷册集ID>][-volset-size <光盘总数>][-volset-seqno <卷册序号>][-x <目录>][目录或文件]

补充说明：mkisofs可将指定的目录与文件做成ISO 9660格式的映像文件，以供刻录光盘。

参  数：
  -a或--all   mkisofs通常不处理备份文件。使用此参数可以把备份文件加到映像文件中。
  -A<应用程序ID>或-appid<应用程序ID>   指定光盘的应用程序ID。
  -abstract<摘要文件>   指定摘要文件的文件名。
  -b<开机映像文件>或-eltorito-boot<开机映像文件>   指定在制作可开机光盘时所需的开机映像文件。
  -biblio<ISBN文件>   指定ISBN文件的文件名，ISBN文件位于光盘根目录下，记录光盘的ISBN。
  -c<开机文件名称>   制作可开机光盘时，mkisofs会将开机映像文件中的全-eltorito-catalog<开机文件名称>全部内容作成一个文件。
  -C<盘区编号，盘区编号>   将许多节区合成一个映像文件时，必须使用此参数。
  -copyright<版权信息文件>   指定版权信息文件的文件名。
  -d或-omit-period   省略文件后的句号。
  -D或-disable-deep-relocation   ISO 9660最多只能处理8层的目录，超过8层的部分，RRIP会自动将它们设置成ISO 9660兼容的格式。使用-D参数可关闭此功能。
  -f或-follow-links   忽略符号连接。
  -h   显示帮助。
  -hide<目录或文件名>   使指定的目录或文件在ISO 9660或Rock RidgeExtensions的系统中隐藏。
  -hide-joliet<目录或文件名>   使指定的目录或文件在Joliet系统中隐藏。
  -J或-joliet   使用Joliet格式的目录与文件名称。
  -l或-full-iso9660-filenames   使用ISO 9660 32字符长度的文件名。
  -L或-allow-leading-dots   允许文件名的第一个字符为句号。
  -log-file<记录文件>   在执行过程中若有错误信息，预设会显示在屏幕上。
  -m<目录或文件名>或-exclude<目录或文件名>   指定的目录或文件名将不会房入映像文件中。
  -M<映像文件>或-prev-session<映像文件>   与指定的映像文件合并。
  -N或-omit-version-number   省略ISO 9660文件中的版本信息。
  -o<映像文件>或-output<映像文件>   指定映像文件的名称。
  -p<数据处理人>或-preparer<数据处理人>   记录光盘的数据处理人。
  -print-size   显示预估的文件系统大小。
  -quiet   执行时不显示任何信息。
  -r或-rational-rock   使用Rock Ridge Extensions，并开放全部文件的读取权限。
  -R或-rock   使用Rock Ridge Extensions。
  -sysid<系统ID>   指定光盘的系统ID。
  -T或-translation-table   建立文件名的转换表，适用于不支持Rock Ridge Extensions的系统上。
  -v或-verbose   执行时显示详细的信息。
  -V<光盘ID>或-volid<光盘ID>   指定光盘的卷册集ID。
  -volset-size<光盘总数>   指定卷册集所包含的光盘张数。
  -volset-seqno<卷册序号>   指定光盘片在卷册集中的编号。
  -x<目录>   指定的目录将不会放入映像文件中。
  -z   建立通透性压缩文件的SUSP记录，此记录目前只在Alpha机器上的Linux有效。
