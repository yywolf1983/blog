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
