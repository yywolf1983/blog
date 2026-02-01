Custom keys

vim key

python
\g goto function
\d goto define
K  __doc__
\n  Usages

\me open buf
\mc  close but
\->
\<-
:b"num"

"?p  #"+p
"?y  #"+y

:reg 查看缓冲区
:ls 列出缓冲区
:buffers
:bdelete #3 删除缓冲区
:buffer 2

q:  历史命令

去掉utf-8 BOM
:set nobomb


保留utf-8 BOM
:set bomb

# 查找相关单词

c
\fs find
\fg find define
\fd find this call
\fc find call this
\ft find string
\ff find file
\fi find include
\l close list

 Ctrl+o back
 Ctrl+i  goto

<f5> NERDTree
\nc  NERDTreeColse


vim key


sudo ./configure --enable-pythoninterp=yes

自动完成 (auto-completion)
vim本身有自动完成功能（这里不是说ctag，而是vim内建的）
CTRL-p -> 向后搜索自动完成 (search backward)
CTRL-n -> 向前搜索自动完成 (search forward)
CTRL-x+CTRL-o -> 代码自动补全 (code completion)

 *:sor* *:sort*  排序

set guifont=*


browse e

Shift+4 行尾
Shift+6 行首

:X  加密
:set key=     取消密码

每行的行首都添加一个字符串：%s/^/要插入的字符串
每行的行尾都添加一个字符串：%s/$/要插入的字符串

删除空格行：:g/^$/d
删除行首空格：:%s/^\s*//g
删除行尾空格：:%s/\s*$//g

ex 相当于 vi -E
打开多个文件
n 下一个文件
e 打开指定文件
b 打开指定编号的文件
e# 回到上一个编辑的文件
o 添加一个文件
bd 关闭文件
I 首行插入
函数列表
taglist.vim（插件） 列表插件。
let Tlist_Use_Right_Window = 1（写入配置文件.vimrc中） 如果希望列表在右侧显示，则加入这个配置，默认是左侧。
:Tlist（正常模式下使用命令） 显示函数列表。
d（在taglist窗口下使用） 从列表中删除文件。
+（在taglist窗口下使用） 展开文件。
-（在taglist窗口下使用） 折叠文件。
=（在taglist窗口下使用） 折叠所有文件。
x（在taglist窗口下使用） 显示或隐藏正常窗口。
文件列表
NERD_tree.vim（插件） 横向拆分窗口（多行窗口）。
let NERDTreeWinPos = 'right'（写入配置文件.vimrc中） 如果希望文件树在右侧显示，则加入这个配置，默认是左侧。
:NERDTree（正常模式下使用命令） 显示文件列表。
函数跳转
ctags（软件，需要另外安装） 生成多种语言tag文件的软件。
Ctags –R *.c（在shell下使用命令） 生成当前路径所有.c文件的tag，-R代表递归。
:ta 标记 或 [g] ctrl-] 列举标签（多个标签）或者跳转到标签（单个标签）。
ctrl-t 返回上一级。
:tags 列出标签栈。
:set ts=4
:set expandtab
:%retab!

空格替换为TAB：
:set ts=4
:set noexpandtab
:%retab!
d 删除文被 可以配配合跳转
w 向后跳一个单词
b 向前跳一个单词
$ 行尾
^ 行首
f o 查找 向后向前
J 合并行
crtl+g 当前行信息
crtl+u 向下翻页
crtl+d 先上翻页
vim分屏
new 新建一个窗口
split 水平分屏
vsplit 垂直分屏
ctrl+w 窗口间切换
    w切换窗口 n 新建 s 分割 v 垂直分割 o 关闭其他 c 关闭
:w !sudo tee % 普通用户保存root文件
多行添加 多行注释
Ctrl + v
选择首行 I 在首行插入
输入要插入的字符 按esc完成
% 括号配对
:close 关闭窗口
num ctrl+w - or + 更改窗口大小
:only 打开一个
:wqall 这个命令应该理解了
:%s/old/new/gc 全部替换
:%s/old/new/gw
:2,25s/old/new/g 替换2-25行
:5,$s/old/new/g 第五行至结尾
:%s/^/hello/g 正则
:%s/old/new/gi 向前
:v/string/d 删除不包含字符串的行
:g/string/d 删除包含字符串的行
1,10 w outfile 领存至一个文件
:1,10 w >> outfile       输出到一个文件
:23r infile 插入到文件
:s/name/name1/ 替换命令
:s/exec/startup/10
:mksession! test.vim
TOhtml
ctrl+r" 将缓冲区复制到命令行
ctrl+r+ 将系统缓冲区复制到命令行
j k 上下
h l 左右
e 打开 q 退出 w 保存 sav 另存
u 撤销 vz 选中 ctrl+r 重做 close 关闭
kx 设定标记
'x 跳转到标记
marks 查看标记
mX 后跟大写为文件标记
vertical diffsplit 与另一个文件比较
:diffupdate 消除差异 同步
vimwiki
 fplugin/vimwiki.vim
   VWS lvimgrep <args>
   VWS vimgrep <args>
vim搜索
:vim[grep] patter **/*.php **/*.tpl 其中搜索条件 patter 可以使用 ctrl+r " 方式粘贴，因为是命令行，无法直接使用p粘贴。 **递归当前目录
:cnext (:cn) 当前页下一个结果
:cprevious (:cp) 当前页上一个结果
:clist (:cl) 打开quickfix窗口，列出所有结果，不能直接用鼠标点击打开，只能看
:copen (:cope) 打开quickfix窗口，列出所有结果，可以直接用鼠标点击打开
:ccl[ose] 关闭 quickfix 窗口。
cwindow (:cw)
ctrl + ww 切换编辑窗口和quickfix窗口，在quickfix里面和编辑窗口一样jk表示上下移动，回车选中进入编辑窗口
V 行选中
v Ctrl_v 竖向选择
Ctrl_u 向上滚屏
Ctrl_d 向下滚屏
:zt 当前行置顶
zb 当前行置底
zfap 创建折行
zf 创建折行
zo 打开折行
zc 关闭折叠
zr 打开多层
zm 折叠多层
zR 打开所有
zd 删除折行
zD 删除多行
多行缩进
< > 向前向后tab
8> 缩进8个tab
= 多行缩进
tabnew
tabe 打开标签
tabs 显示标签
tabc 关闭当前
tabo 关闭所有
tabn或gt可以移动到下一个标签页
tabp或gT将移动到上一个标签页
tabm 0 移动标签位置
tabnew [++opt选项] ［＋cmd］ 文件            建立对指定文件新的tab
标准模式下：
gt , gT 可以直接在tab之间切换。
还有很多他命令， 看官大人自己， :help table 吧。



f 当前行查找
o 另起一行插入
% 执行导入文件
p 取回删除行至于光标处
e! 重新加载文件
q! 强制退出
:help 帮助
%!xxd 转换成16进制字符
%!xxd -r 转换回来
/ 查找 n 继续查找
/jo[ha]n john or joan
/<the the,theis or then
/the> the or breathe
/free|job free or job
/<dddd> 相同的四位数
/^n{3} 找到3个空行
? 向上查找
set ignorecase 忽略查找大小写
set noic 区分大小写
/ <up> 重复过去搜索命令
* 查找当前光标处单词单词
set nohlsearch 关闭搜索高亮
:nohl 取消搜索高亮
"+p 粘贴
"+y 拷贝
y p 拷贝 粘贴
"xy 有名缓冲区 x为a-z
"xp 放回文件
yy 复制行
2yy 复制两行
的小写字母换成大写字母，就可以再原有缓冲区的内容之后追加当前内容。
:reg 查看缓冲区
:ls 列出缓冲区
:buffers
:bdelete #3 删除缓冲区
:buffer 2
hardcopy 打印
：set fileformat=unix
: set fileencoding=utf-8
或者
：set ff=dos
：wq!
ZZ 保存退出
vim中v进入可视状态，然后ctrl+v以块方式选择文本
gCtrl_g 查看文件信息
:mksession vimbook.vim 保存当前会话信息
:source vimbook.vim 读取会话信息

ctags cscope

find . -name "*.h" -o -name "*.c" -o -name "*.cc" -o -name "*.py" > cscope.files
cscope -bkq -i cscope.files
ctags -R

set tags=~/path/tags

Ctrl + ]	找到光标所在位置的标签定义的地方。
Ctrl + T	回到跳转之前的标签处。
Ctrl + O	(是字母o，不是数字0) 退回原来的地方。
[I	查找全局标识符. Vim会列出它所找出的匹配行，不仅在当前文件内查找，还会在所有的包含文件中查找。
[i	从当前文件起始位置开始查找第一处包含光标所指关键字的位置。
]i	类似上面的[i，但这里是从光标当前位置开始往下搜索。
[{	转到上一个位于第一列的”{“。（前提是 “{” 和 “}” 都在第一列。）
]}	转到下一个位于第一列的”}”。


Compile vim

cd D:\makevim\vim\vim72\src

make -f Make_ming.mak GUI=yes OLE=no USERNAME=yywolf USERDOMAIN=wuranju.com./configure --prefix=/usr/vim --enable-multibyte --enable-pythoninterp --with-features=huge --enable-cscope  --with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu/

mac


os_unix.c:830:13: error: conflicting types for 'sigaltstack'

只需要在os_unix.h中加上#include <AvailabilityMacros.h>就可以了。
