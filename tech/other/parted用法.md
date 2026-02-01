随着单块硬盘容量的增大和硬盘价格的下降，2TB的磁盘使用将很快会普及，由于传统的MBR方式存储分区表的方 式缺陷，将可能导致很多分区工具不能正确地读取大于2TB容量的硬盘而无法正常分区大容量硬盘。其实linux在很早就已经有相关的工具来化解这个困境 了，那就是parted。
parted是类似fdisk的命令行分区软件，假设我们在linux系统中有一块未分区的硬盘挂载为/dev/hdd，下面以实例的方式来讲解如何使用 parted：
注意：parted的操作都是实时的，也就是说你执行了一个分区的命令，他就实实在在地分区了，而不是像fdisk那样，需要执行w命令写入所做的修改， 所以进行parted的测试千万注意不能在生产环境中！！
标记：#开始表示在shell的root下输入的命令，(parted)表示在parted中输入的命令，其他为自动打印的信息

mklabel gpt
mkpart extended 0% 100%


1、首先类似fdisk一样，先选择要分区的硬盘，此处为/dev/hdd：
# parted /dev/hdd
GNU Parted 1.8.1
Using /dev/hdd
Welcome to GNU Parted! Type 'help' to view a list of commands.


2、现在我们已经选择了/dev/hdd作为我们操作的磁盘，接下来需要创建一个分区表(在parted中可以 使用help命令打印帮助信息)：
(parted) mklabel
Warning: The existing disk label on /dev/hdd will be destroyed and all data on this disk will be lost. Do you want to continue?
Yes/No?(警告用户磁盘上的数据将会被销毁，询问是否继续，我们这里是新的磁盘，输入yes后回车) yes
New disk label type? [msdos]? (默认为msdos形式的分区，我们要正确分区大于2TB的磁盘，应该使用gpt方式的分区表，输入gpt后回车)gpt


3、创建好分区表以后，接下来就可以进行分区操作了，执行mkpart命令，分别输入分区名称，文件系统和分区 的起止位置
(parted) mkpart
Partition name? []? dp1
File system type? [ext2]? ext3
Start? 0
End? 500GB


4、分好区后可以使用print命令打印分区信息，下面是一个print的样例
(parted) print
Model: VBOX HARDDISK (ide)
Disk /dev/hdd: 2199GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Number Start End Size File system Name Flags
1 17.4kB 500GB 500GB dp1


5、如果分区错了，可以使用rm命令删除分区，比如我们要删除上面的分区，然后打印删除后的结果
(parted)rm 1 #rm后面使用分区的号码
(parted) print
Model: VBOX HARDDISK (ide)
Disk /dev/hdd: 2199GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Number Start End Size File system Name Flags


6、按照上面的方法把整个硬盘都分好区，下面是一个分完后的样例
(parted) mkpart
Partition name? []? dp1
File system type? [ext2]? ext3
Start? 0
End? 500GB
(parted) mkpart
Partition name? []? dp2
File system type? [ext2]? ext3
Start? 500GB
End? 2199GB
(parted) print
Model: VBOX HARDDISK (ide)
Disk /dev/hdd: 2199GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Number Start End Size File system Name Flags
1 17.4kB 500GB 500GB dp1
2 500GB 2199GB 1699GB dp2


7、由于parted内建的mkfs还不够完善，所以完成以后我们可以使用quit命令退出parted并使用 系统的mkfs命令对分区进行格式化了，此时如果使用fdisk -l命令打印分区表会出现警告信息，这是正常的
#fdisk -l
WARNING: GPT (GUID Partition Table) detected on '/dev/hdd'! The util fdisk doesn't support GPT. Use GNU Parted.
Disk /dev/hdd: 2199.0 GB, 2199022206976 bytes
255 heads, 63 sectors/track, 267349 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Device Boot Start End Blocks Id System
/dev/hdd1 1 267350 2147482623+ ee EFI GPT #mkfs.ext3 /dev/hdd1
#mkfs.ext3 /dev/hdd2
#mkdir /dp1 /dp2
#mount /dev/hdd1 /dp1
#mount /dev/hdd2 /dp2
