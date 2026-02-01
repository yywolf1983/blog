使用rsync+inotify配置触发式(实时)远程同步

  yywolf1983 发表于 2013-08-06 15:57:31  删除     编辑  

安装软件:
rsync3.x
inotify-tools

条件：
需要实时同步的两台主机: 192.168.1.101 192.168.1.102
同步的网站目录: /data/www/wwwroot

# cd /usr/local/src
# wget http://www.samba.org/ftp/rsync/s ... nc-3.0.6pre1.tar.gz
# wget http://jaist.dl.sourceforge.net/ ... y-tools-3.13.tar.gz

# tar zxvf rsync-3.0.6pre1.tar.gz
# cd rsync-3.0.6pre1
# ./configure --prefix=/usr && make && make install

# tar zxvf inotify-tools-3.13.tar.gz
# cd inotify-tools-3.13
# ./configure && make && make install



# cd /usr/local/sbin   
# vi rsync.sh   //分别在两台机器上创建如下脚本，另一台改一下IP地址即可.
#!/bin/sh
src=/data/www/wwwroot/
des=/data/www/wwwroot
ip=192.168.1.101

/usr/local/bin/inotifywait -mrq --timefmt '%d/%m/%y %H:%M' --format  '%T %w%f' \
-e modify,delete,create,attrib \
${src} \
| while read  file
        do
                rsync -avz --delete --progress ${src} root@${ip}:${des} &&
                #echo "${src} was rsynced"
                #echo "-----------------------------------------------------"
        done

# chmod a+x rsync.sh
# ./rsync.sh 执行同步脚本，在相应的目录下测试相关文件.
将此脚本写入到/etc/rc.local 让系统自动加载即可.

脚本相关注解：
    －m 是保持一直监听
    －r 是递归查看目录
    －q 是打印出事件～
    －e create,move,delete,modify
    监听 创建 移动 删除 写入 事件

    rsync -aHqzt $SRC $DST

    -a 存档模式
    -H 保存硬连接
    -q 制止非错误信息
    -z 压缩文件数据在传输
    -t 维护修改时间
    -delete 删除于多余文件

当要排出同步某个目录时，为rsync添加--exculde=PATTERN参数，注意，路径是相对路径。详细查看man rsync
当要排除都某个目录的事件监控的处理时，为inotifywait添加--exclude或--excludei参数。详细查看man inotifywait

另：
/usr/local/bin/inotifywait -mrq --timefmt '%d/%m/%y %H:%M' --format  '%T %w%f' \
-e modify,delete,create,attrib \
${src} \
上面的命令返回的值类似于：
10/03/09 15:31 /wwwpic/1
这3个返回值做为参数传给read，关于此处，有人是这样写的：
inotifywait -mrq -e create,move,delete,modify $SRC | while read D E F;do
细化了返回值。



说明： 当文件系统发现指定目录下有如上的条件的时候就触发相应的指令，是一种主动告之的而非我用循环比较目录下的文件的异动，该程序

在运行时，更改目录内的文件时系统内核会发送一个信号，这个信号会触发运行rsync命令，这时会同步源目录和目标目录。
--timefmt：指定输出时的输出格式
   --format：  '%T %w%f'指定输出的格式

二.关于inotify介绍
Inotify 是文件系统事件监控机制，作为 dnotify 的有效替代。dnotify 是较早内核支持的文件监控机制。Inotify 是一种强大的、细粒度的
、异步的机制，它满足各种各样的文件监控需要，不仅限于安全和性能。

inotify 可以监视的文件系统事件包括：
IN_ACCESS，即文件被访问
IN_MODIFY，文件被 write
IN_ATTRIB，文件属性被修改，如 chmod、chown、touch 等
IN_CLOSE_WRITE，可写文件被 close
IN_CLOSE_NOWRITE，不可写文件被 close
IN_OPEN，文件被 open
IN_MOVED_FROM，文件被移走,如 mv
IN_MOVED_TO，文件被移来，如 mv、cp
IN_CREATE，创建新文件
IN_DELETE，文件被删除，如 rm
IN_DELETE_SELF，自删除，即一个可执行文件在执行时删除自己
IN_MOVE_SELF，自移动，即一个可执行文件在执行时移动自己
IN_UNMOUNT，宿主文件系统被 umount
IN_CLOSE，文件被关闭，等同于(IN_CLOSE_WRITE | IN_CLOSE_NOWRITE)
IN_MOVE，文件被移动，等同于(IN_MOVED_FROM | IN_MOVED_TO)
注：上面所说的文件也包括目录。

相关参考:
http://www.ibm.com/developerworks/cn/linux/l-ubuntu-inotify/index.html
