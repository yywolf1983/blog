rpm -qi portmap
rpm -qi nfs-utils

 yum -y install nfs-utils rpcbind


119.255.194.38:/media/Server on /media type nfs (rw,addr=119.255.194.38)


nfs-utils   
vi /etc/exports 配置文件
/data/lys 192.168.2.0/24(rw,no_root_squash,no_all_squash,sync)
/home/xgc *(rw,sync,no_root_squash)


/home/xgc：要共享的目录
* ：允许所有的网段访问
rw ：读写权限
sync：资料同步写入内在和硬盘
no_root_squash：nfs客户端共享目录使用者权限




        ro                      只读访问
        rw                      读写访问
        sync                    所有数据在请求时写入共享
        async                   NFS在写入数据前可以相应请求
        secure                  NFS通过1024以下的安全TCP/IP端口发送
        insecure                NFS通过1024以上的端口发送
        wdelay                  如果多个用户要写入NFS目录，则归组写入（默认）
        no_wdelay               如果多个用户要写入NFS目录，则立即写入，当使用async时，无需此设置。
        hide                    在NFS共享目录中不共享其子目录
        no_hide                 共享NFS目录的子目录
        subtree_check           如果共享/usr/bin之类的子目录时，强制NFS检查父目录的权限（默认）
        no_subtree_check        和上面相对，不检查父目录权限
        all_squash              共享文件的UID和GID映射匿名用户anonymous，适合公用目录。
        no_all_squash           保留共享文件的UID和GID（默认）
        root_squash             root用户的所有请求映射成如anonymous用户一样的权限（默认）
        no_root_squas           root用户具有根目录的完全管理访问权限
        anonuid=xxx             指定NFS服务器/etc/passwd文件中匿名用户的UID



重新挂载设置
exportfs -arv


修改
/etc/hosts.deny 和 /etc/hosts.allow  限制访问
修改后都要重启portmap daemon。不然修改无效。




/etc/init.d/portmap restart
/etc/init.d/nfs-kernel-server restart

service rpcbind start
service nfs start

客户端执行
由于nfs服务器端默认是安装了nfs客户端(nfs-common)的
mount -t nfs 192.168.1.102:/nfs/huyb /mnt/huyb
mount -t nfs 10.20.20.88:/data/fileshare /data/fileshare -o proto=tcp -o nolock


fstab
server:/shared   /shared   nfs  tcp,soft,intr,timeo=50,nfsvers=3 0 0


/etc/exports
 /home/nfs-share    192.168.1.122 *(rw,sync)

/etc/init.d/nfs start           //用service nfs start也可以
/etc/init.d/portmap start       //用service portmap stasrt也可以


showmount –a IP    显示指定NFS服务器的客户端以及服务器端在客户端的挂载点
showmount –d IP    显示指定NFS服务器在客户端的挂载点
showmount –e IP    显示指定NFS服务器上的共享目录列表（或者叫输出列表）


yum install nfs-utils portmap nfs4-acl-tools
mount -t nfs 10.61.1.31:/home/nfs /mnt/nfs

192.168.1.3:/usr/local/nfs    /usr/nfs    nfs   rw,tcp,intr   0  0

mount -t nfs -o nolock,vers=4 10.10.11.22:/data/fileshare /file
