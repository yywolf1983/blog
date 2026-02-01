vim 加入右键
Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\*\shell\gvim]
@="gvim"
[HKEY_CLASSES_ROOT\*\shell\gvim\command]
@="E:\\kuaipan\\tools\\vim\\gvim.exe %1"


:e dav://machine[:port]/path                    uses cadaver
:e fetch://[user@]machine/path                  uses fetch
:e ftp://[user@]machine[[:#]port]/path          uses ftp   autodetects <.netrc>
:e http://[user@]machine/path                   uses http  uses wget
:e rcp://[user@]machine/path                    uses rcp
:e rsync://[user@]machine[:port]/path           uses rsync
:e scp://[user@]machine[[:#]port]/path          uses scp
:e sftp://[user@]machine/path                   uses sftp


vi 命令 作用
:%s/ */ /g 把一个或者多个空格替换为一个空格。
:%s/ *$// 去掉行尾的所有空格。
:%s/^/ / 在每一行头上加入一个空格。
:%s/^[0-9][0-9]* // 去掉行首的所有数字字符。


Sed
Sed是Stream EDitor的缩写，

sed ’s/^$/d’ price.txt 删除所有空行
sed ’s/^[ ]*$/d’ price.txt 删除所有只包含空格或者制表符的行
sed ’s/”//g’ price.txt 删除所有引号

编译vim

git clone https://github.com/vim/vim.git


sudo apt install libncurses5-dev libgnome2-dev libgnomeui-dev libgtk2.0-dev libatk1.0-dev libbonoboui2-dev libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev python3-dev ruby-dev lua5.1 liblua5.1-dev libperl-dev git

cd vim/src
make -f Make_ming.mak GUI=yes OLE=no USERNAME=yywolf USERDOMAIN=nones.com
./configure --with-features=huge \
--enable-multibyte \
--enable-python3interp=dynamic \
--with-python3-config-dir=/usr/lib/python3.9/config-3.9-x86_64-linux-gnu/ \
--enable-multibyte \
--enable-cscope \
--enable-gui=auto \
--enable-gtk2-check \
--enable-fontset \
--enable-largefile \
--disable-netbeans \
--enable-fail-if-missing \
--prefix=/usr/vim

make && make install

make distclean
