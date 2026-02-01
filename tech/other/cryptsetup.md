制作加密卷

1、建立一个空文件

fallocate --length 512M vaultfile.img


2、创建一个 LUKS 卷

cryptsetup --verify-passphrase luksFormat vaultfile.img


3、打开 LUKS 卷

cryptsetup open \
    --type luks vaultfile.img myvault
ls /dev/mapper


4、建立一个文件系统

mkfs.ext4 -L myvault /dev/mapper/myvault


5、开始使用你的加密保险库

cryptsetup open \
    --type luks vaultfile.img myvault
ls /dev/mapper
myvault
mkdir /myvault
mount /dev/mapper/myvault /myvault

umount /myvault
cryptsetup close myvault