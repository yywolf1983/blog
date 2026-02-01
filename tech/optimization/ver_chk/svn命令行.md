svnserve -d --listen-port 800 -r /root/svnworks/

freebsd
# make NOPORTDOCS=YES -DWITH_SVNSERVE_WRAPPER install clean
# pw useradd -s /bin/sh -d /var/empty -n svn
linux
# wget http://subversion.tigris.org/downloads/subversion-1.3.2.tar.bz2
# tar -jxvf subversion-1.3.2.tar.bz2
# cd subversion-1.3.2
# ./configure --with-zlib --enable-all-static
# useradd -d /var/empty svn

# svnadmin create --fs-type fsfs 目录
# chown -R svn:svn 目录

configure: error: no suitable apr found
1.7  以后用这个解决
./get-deps.sh   


svnserve.conf文件
[general]
#"write", "read", and "none".
anon-access = none
auth-access = write
#用户密码文件
password-db = passwd
#权限设置
authz-db = authz

[sasl]
# use-sasl = true
# min-encryption = 0
# max-encryption = 256


说明：
anon-access = none #不允许匿名用户访问
auth-access = write #通过验证的用户可以读和写
password-db = /opt/svn/etc/svn-user.conf #用户保存文件
authz-db = /opt/svn/etc/svn-authz.conf #权限管理文件
realm = My First Repository #仓库名称

passwd文件

[users]
用户名 = 明文密码


authz 权限文件
#用户组
[groups]
root=root

#目录路径  svn根路径svn://127.0.0.1/
[/]

svn://127.0.0.1/works

或者
[works:/]
直接访问 svn://127.0.0.1/

因为[wroks:/]表示库works的根目录，而按上面的启动参数，是没有库的概念的。
使用类似这样的URL：svn://127.0.0.1/ 即可访问works


#可以直接使用用户名 @带表组名称


@root=rw


svnserve -d -r /svn/works


SVN_EDITOR = vi
或者
.svbversion/config
editor-cmd=vi


$ svn import /etc/svn/tmp/ file:///etc/svn/repos/ --message "init" ;导入
$ svn list --verbose file:///etc/svn/repos/ ;列表
$ svnlook info /etc/svn/repos/ ;查看信息

; apache模块

LoadModule dav_module modules/mod_dav.soLoadModule dav_svn_module
modules /mod_dav_svn.so<Location /repos>  DAV svn  SVNPath /etc /svn
/repos  ；也可以 SVNParentPath /etc/svn</Location>
;创建密码
htpasswd etc/svn/passwordfile username

;设置权限
AuthType Basic
AuthName "svn repos"
AuthUserFile /etc/svn/passwordfile
Require valid-user

;允许匿名用户
<LimitExcept GET PROPFIND OPTIONS REPORT>
  require valid-user
</LimitExcept>



；更详细的权限
；需要开启以下两个模块
LoadModule dav_svn_module modules/mod_dav_svn.so
LoadModule authz_svn_module modules/mod_authz_svn.so

<Location /repos>
DAV svn
SVNPath /etc/svn/repos
AuthType Basic
AuthName "svn repos"
AuthUserFile /etc/svn/passwd
AuthzSVNAccessFile /etc/svn/authz   ；策略文件 策略设置同authz
Satisfy Any
Require valid-user
</Location>



；mysql支持
LoadModule mysql_auth_module modules/mod_auth_mysql.so

<Location /repos>
AuthName "MySQL auth"
AuthType Basic
AuthMySQLHost localhost
AuthMySQLCryptedPasswords Off
AuthMySQLUser root
AuthMySQLDB svn
AuthMySQLUserTable users
require valid-user
</Location>

;然后在 mysql 中添加名为 svn 的数据库，并建立 users 数据表：

create database svn;
use svn;
CREATE TABLE users (
user_name CHAR(30) NOT NULL,
user_passwd CHAR(20) NOT NULL,
user_group CHAR(10),
PRIMARY KEY (user_name)
);

;插入用户信息
insert into users values('username','password','group');



Process.exe -k svnserve.exe
echo Starting svn
RunHiddenConsole.exe D:\svnwin32\bin\\svnserve.exe -d -r d:/svnwin32/svn
echo .
echo .

pause


修改 /etc/rc.d/svnserve
--root=/back/Repositories/


svn目录 hooks目录

pre-revprop-change — 修訂版本屬性修改的通知。

post-commit — 成功提交的通知。

svn propset -r 2 --revprop svn:log  "只是添加了blog目录"   修改日志




清理.svn目录
find . -name .svn | "xargs" rm -rf

svn st | awk '{if ( $1 == "?") { print $2}}' | xargs svn add

svn checkout https://(项目名称).(域)/svn/(项目名称)/(DIR)
:q
svn co --depth=empty 获取单个目录
svn up filename 获取单个文件

svn add

svn propset -r 2 --revprop svn:log  "只是添加了blog目录"   修改日志
svn propset svn:ignore "*" log/  忽略目录

svn update –set-depth=exclude 文件夹  忽略文件
编辑~/.subversion/config文件，修改此文件中的global-ignores，例如，想让subversion忽略vim的交换文件文件，可以这样设置：
global-ignores = *.o *.swp


export SVN_EDITOR=/usr/bin/vim

svn blame FILENAME 查看指定文件内容

# svnadmin create --fs-type fsfs 目录
# chown -R svn:svn 目录



svn cat  查看特定文件的内容

清理工作副本：svn cleanup

有时可能会出现“工作副本已锁定”错误。若要删除锁定，并递归清理工作副本，请使用 svn update。

svn copy 副本中复制

svn delete 副本中删除

svn diff 查看文件之间的差异
svn diff -r 100:110

只看差异文件 不看差异内容
svn diff --summarize -r 100:110

svn export 在本地计算机上导出空目录树：

svn export PATH1 PATH2

svn help

svn help [SUBCOMMAND...]

svn commit -m "请在此处键入您的理由"  提交更改

svn import 导入无版本文件树

svn info 打印有关工作副本中路径的信息

svn list 查看存储库中的目录项列表：

svn log 查看提交日志信息：

合并更改：svn merge

创建新目录：svn mkdir
svn mkdir PATH
svn mkdir URL

移动文件或目录：svn move

解决冲突：svn resolved

解决冲突后，键入 svn resolved PATH...，通知工作副本该冲突已“解决”。

撤消您的更改：svn revert

使用 Subversion 时，您会发现 svn revert PATH... 等效于 Windows 中的 Ctrl Z。您可以：

  * 撤消本地工作副本中的任何本地更改，从而解决冲突状态。
  * 撤消工作副本中的条目内容及属性更改。
  * 取消任何进度安排操作，如添加文件、删除文件等。

svn status 获取文件/目录的状态

svn switch 转换工作副本：
svn switch --relocate svn://172.16.1.27/solution/sc8810/branches/GC svn://172.16.2.53/solution/sc8810/branches/GC --username xxx --password xxx

svn update 更新工作副本

列出的已更新条目以及它们的当前状态显示如下：

  * A = 已将一个文件添加到您的工作副本中。
  * U = 已更新您的工作副本中的一个文件。
  * D = 已从您的工作副本中删除一个文件。
  * R = 已替换您的工作副本中的一个文件。
  * G = 已成功合并了一个文件。
  * C = 一个文件已合并了必须手动解决的冲突


分支和标记
svn copy SRC DST -m "在此处键入您的信息"

若要彻底删除SVN版本库某一文件夹或文件,可采取这种方法(举例说明):

例:假设SVN库路径为E:\svn\project，库中的目录结构为
QA/Trunk
Software/Tags/test.exe
删除Software/Tags/目录下的test.exe文件

操作步骤为:
把SVN库dump出来
使用svndumpfilter过滤掉要删除的文件
新建一个SVN库
再将处理好的文件load到新的SVN库里
具体命令为：

>svnadmin dump E:\svn\project > aaa.dump

>svnadmin create E:\svn\project_new

>svnadmin load E:\svn\project_new < bbb.dump

完全备份
svnadmin hotcopy d:\svnroot\project1 d:\svnrootbak\project1

增量备份
svnadmin dump project1 --revision 15 --incremental > dumpfile2

把上次完全备份backuprepo，和之后的增量备份dumpfile：
svnadmin load backuprepo < dumpfile

目标对目标同步
svnsync init svn://localhost/project2 svn://localhost/project1

a同步到b
svnsync sync svn://localhost/project2

通过该方法我的确实现了彻底删除一个及多个目录的历史版本，另外在过滤时有两种方法
svndumpfilter include  project1_path < dumpfile >  abc1

这种方法就是留下project1....projectn的版本信息，其他的彻底全部干掉。

第二种方法正好相反

svndumpfilter exclude project1_path < dumpfile > abc1 I

这里一次性便可导入，直接导入abc2就OK了。



svn 重新定位  更改ip

svn switch --relocate https://192.168.0.111/svn/pic svn://192.168.0.111/pic

TortoiseSVN 比较差异文件
show log -> Ctrl+左键（选中两个版本） -> 按右键选 Compare revisions  -> 在弹出的Changed Files窗口中，全选(Ctrl+A)要导出的文件，然后点右键，选择Export selection to ... 导出这些差异文件：
