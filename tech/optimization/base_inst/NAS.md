linux 挂载 NAS

  yywolf1983 发表于 2013-07-30 18:42:37  删除     编辑  

mount.cifs //[NAS IP Address]/[Folder Name] /mnt -o username=xxx,password=xxx,domain=xxx
mount -t cifs  /mnt -o username=xxx,password=xxx,domain=xxx

chkconfig netfs on

//server/share_folder /mount_point cifs rw,user=xxx,password=xxx,uid=xxxxx,gid=xxxxx 0 0

ro
mount read-only
rw
mount read-write
