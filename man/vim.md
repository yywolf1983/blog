
## vim命令图解

![vim](/vim/vi2.png)

# vim基础操作
```text
F6 文件列表
shift+c 设置当前目录为工作目录

! 插入注释

C+F12 建立 tag
F8 Tagbar
F5 粘贴模式

F9 查看md 文件

% 当前完整的文件名
%:h 文件名的头部，即文件目录.例如../path/test.c就会为../path
%:t 文件名的尾部.例如../path/test.c就会为test.c

:qall -- 关闭所有窗口，退出vim。

\ n 新建tab
\ p 下一个tab
\ c 关闭tab
\ e 打开文件

:sp 水平分割
:vs 垂直分割

打开远程
:e scp://sk@test/info.txt

Ctrl + W  窗口间移动
Ctrl + w + r  交换窗口
Ctrl + w + x

Ctrl+ ]跳到光标所在函数或者结构体的定义处
Ctrl+ T返回查找或跳转

mks! 保存sesion

:vimgrep 随机 **/**.cpp **/*.h
:grep 
:copen   :cw
:ccolse  :ccl
\ s 搜索

列出缓冲区
:buffers，:files和:ls
:buffer number 或者 :buffer filename
:bdelete 3 或 :3 bdelete 也可以使用:1,3 bdelete
:badd 增加缓冲区
:bnext
:bp
:bm 到修改过的缓冲区
:ba  编辑所有缓冲区
```
