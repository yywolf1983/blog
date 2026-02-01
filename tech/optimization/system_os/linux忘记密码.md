gentoo
init=/bin/bash rw
centos
.(按e)编辑kernel那行 添加 /init 1 (或/single)

centos 7
删除  ro rhgb quiet
添加 rw single init=/bin/bash
关闭  selinux
