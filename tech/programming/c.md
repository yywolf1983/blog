## 基础安装
sudo apt-get install libtool autoconf automake m4 make gcc g++

/etc/ld.so.conf.d/
sudo ldconfig -p


## 基础命令 

``` text
gcc -dM -E - <<<''  显示所有c宏

gcc  -E  hello.c   -o  hello.i             只预处理
gcc  -S  hello.c   -o  hello.s             只编译
gcc  -c  hello.c  -o  hello.o              预处理,编译
gcc  -o  hello hello.o

as hello.s -o hello.o
ld hello.o -o hello

gcc -DNDEBUG             预定义

cpp main.c  tmp/main.i
ccl tmp/main.i main.c  -02 -o tmp/main.s
as -o tmp/main.o  tmp/main.s
ld -o OUTPUT /lib/crt0.o hello.o -lc

objdump - display information from object files.
nm - list symbols from object files
ldd - print shared library dependencies

objdump
-h   info
-s   二进制
-d   反汇编

ldd 打印依赖库

readelf -h

gcc test.c -I src/include/ -L skalibs/lib -static -lfoo -o foo
gcc test.c -v
gcc -l opengl32 -l glu32 -l gdi32
```

## 系统相关

``` text
linux   glibc libc
mac   libSystem    /usr/lib/libSystem.dylib

windows
   UCRTBASE.DLL。 UCRT 目前已经成为 Windows 组之一
   MSVCRT.DLL

android
   libc++
   gnustl，libstdc++
   STLport

yum install gettext-devel,automake

```

## llvm

``` txt

生成LLVM中间表示文件.bc:
clang hello.c -c -o hello.bc -emit-llvm -v

用LLVM虚拟机执行
lli hello.bc
看看输出结果是不是一致。。。

转换为可读模式的LLVM中间表示:
llvm-dis < hello.bc

将LLVM中间表示转换为汇编语言文件:
llc hello.bc -o hello.s

汇编文件就可以直接使用GCC转换为可执行文件了
gcc hello.s -o hello.native

执行一下：
./hello.native

```

## 基础参数

    export LDFLAGS=-L/usr/local/lib/
    export CPATH=/usr/local/include/

    #在PATH中找到可执行文件程序的路径。
    export PATH =$PATH:$HOME/bin

    #gcc找到头文件的路径
    C_INCLUDE_PATH=/usr/include/libxml2:/MyLib
    export C_INCLUDE_PATH

    #g++找到头文件的路径
    CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/include/libxml2:/MyLib
    export CPLUS_INCLUDE_PATH

    #找到动态链接库的路径
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/MyLib
    export LD_LIBRARY_PATH

    #找到静态库的路径
    LIBRARY_PATH=$LIBRARY_PATH:/MyLib
    export LIBRARY_PATH

## 关键字

```
auto double int struct break else long switch

case enum register typedef char extern return union

const float short unsigned continue for signed void

default goto sizeof volatile do if while static
```

## 宏定义 

``` c
#ifndef COMDEF_H
    ……
#else
    #define COMDEF_H
    ……
#endif

__LINE__ 被编译的文件的行数
__FILE__ 被编译的文件的名字
__DATE__ 编译的日期（格式"Mmm dd yyyy"）
__TIME__ 编译的时间（格式"hh:mm:ss"）
__STDC__ 如果编译器接受标准C，那么值为1
```


## 指针

```
//ip 是变量的内存地址 //*ip 变量的实际值 取值 //&ip 指向指针的实际地址 对指针取址

// 指针是一种保存变量地址的变量; // 给指针赋值必须为地址，*p为所指向变量的值

//void 型指针可以存放任意类型的指针,但不能间接引用自身;
``` 


## 基础学习库

```txt
    cJSON
    crunch
        字典生成器
    fping
    tinyhttpd
        轻量型Http Server源码
    webbench
        压力测试工具
    wg-wrk
        压测工具
```

## 基础知识

```txt
堆和栈在使用时相向生长，栈向上生长，即向小地址方向生长，而堆向下增长，即向大地址方向，其间剩余部分是自由空间。

1010 & 1100 = 1000    与
1010 | 1100 = 1110    或
1010 ^ 1100 = 0110    异或
1010 << 2  = 101000  位移
1010 >> 2  = 10
~1010      = 0101    非

堆，队列优先,先进先出（FIFO—first in first out）[1]。栈，先进后出(FILO—First-In/Last-Out)。

小端序：先存储低位字节，后存储高位字节
大端序：先存储高位字节，后存储地位字节

低地址、高地址：内存地址可以对应十六进制的数值，值大的为高地址，否则为低地址；

在x86平台上这个栈是从高地址向低地址增长的

```


# 制作库

## 定义头 test.h

``` c
#ifndef MINGW_DLL_H_
#define MINGW_DLL_H_

#ifdef __cplusplu  //如果是c++
    extern " C " {
#endif

//打印点东西
int add(int b);

#ifdef __cplusplus
    }
#endif

#endif
```

## 源文件 test.c
```c
#include<stdio.h>
#include"test.h"

int add(int b)
{
        printf("this is dll\n");
        return b;
}

testc.c
#include <stdio.h>
#include "test.h"

void main()
{
    int b=add(100);
    printf("%d",b);
    return;
}
```

## Compile

``` text

 动态编译
 for linux
 gcc -fpic -shared test.c -o libtest.a  动态编译
 gcc -c -DBUILD_DLL test.c              静态编译

 gcc testc.c -L. -ltest -o test         动态调用 
 gcc testc.c test.o -o test.exe         静态调用
```

### 其他调用

```text
    --output-def,dll.def
    --out-implib,dll.a
```

# GDB

``` text

gcc -g 添加调试信息

finish  跳出函数
until   执行到某处
b 断点
i b 显示断点信息
disable 断点失效
enable  断点生效
d 删除所有断点

r 运行
start 到起点
s 步入
n 逐行
c 继续执行
jump 5 跳转到某行

set var a="10"  设置变量
i 查看信息
  i line 查看行信息
  i li fu  查看函数定义
p 打印变量
l 列出代码
display  每次停止都显示变量值
f 查看函数信息
show listsize  查看显示代码的行数
set listsize  设置显示代码的行数

x/3uh 0x54320 表示，从内存地址0x54320读取内容，h表示以双字节为一个单位，3表示输出三个单位，u表示按无符号十进制显示。

win  窗口显示
```

## 远程调试

```
gdbserver  <host-ip>:2345 hello

gdb
:target remote <target-board-ip>:2345
转储

``` 

## 内核调试

```txt
/etc/sysctl.conf

kernel.core_pattern = /var/core/%t-%e-%p.core
kernel.core_uses_pid = 0

sysctl -p

file ddg.x86_64
```

## 反汇编

```txt
objdump -h ddg.x86_64

-h info -s 二进制 -d 反汇编

readelf

格式符号    说明
%%      %字符本身
%p      被转储进程的进程ID(PID)
%u      被转储进程的真是用户ID(UID)
%g      被转储进程的真是组(GID)
%s      引发转储的信号编号
%t      转储时间，unix时间戳(从1970年1月1日0时开始的秒数)
%h      主机名
%e      可执行文件的名称
%c      转储文件的大小上限(内核版本2.6.24以后可使用)
```

## Mac 上使用gdb

```
先要用钥匙串 创建代码签名的钥匙串
菜单上点击钥匙串访问->证书助理->创见证书 代码签名证书
然后对gdb 进行签名
codesign -s yy /usr/local/bin/gdb
更新签名
codesign -f -s yy /usr/local/bin/gdb

1.打开菜单：钥匙串访问－》证书助理－》创建证书…
2.输入证书名称，如：gdb-cert；
3.选择身份类型：自签名根证书 （Identity Type to Self Signed Root）
4.选择证书类型：代码签名 （Certificate Type to Code Signing）
5.勾选：让我覆盖这些默认签名 （select the Let me override defaults）
6.一路继续，到选择时间的时候，把时间选择的长一些，最大是20年，7300。
7.一路继续，直到选择存放证书地址，选择：系统
8.这样证书就创建好了，还要设置证书自定义信任
9.右键刚才创建的 gdb-cert 证书，选择“显示简介” （Get Info）
10.点击“信任”，会显示可以自定义的信任选项
11.“代码签名”选择“总是信任” （Code Signing to Always Trust）
12其次，将证书授予gdb，执行命令

codesign -s gdb-cert `which gdb`
  好了，以上就给gdb授予了系统信任的代码签名证书，可以正常使用gdb了。
  要让刚刚添加的证书生效需要重启taskgated服务或者重启系统
sudo killall taskgated


During startup program terminated with signal ?, Unknown signal.
vi ~/.gdbinit
set startup-with-shell off
```

# automake

## 一、Source code ->  autoscan -> configure.scan

``` sh
cp configure.scan configure.in
vi configure.in
m4_define([lxc_version_major], 1)
m4_define([lxc_version_minor], 1)
m4_define([lxc_version_micro], 0)
m4_define([lxc_version_beta], [])

m4_define([lxc_version_base], [lxc_version_major.lxc_version_minor.lxc_version_micro])
m4_define([lxc_version],
          [ifelse(lxc_version_beta, [], [lxc_version_base], [lxc_version_base.lxc_version_beta])])

AC_INIT([lxc], [lxc_version])

#注意这里和 AC_CONFIG_HEADERS 的区别
#AM_CONFIG_HEADER([config.h])

#注意这里是重点
AM_INIT_AUTOMAKE(helloworld, 1.0)
AC_CONFIG_FILES([Makefile])
```

## 二、configure.in  -> aclocal -> aclocal.m4

## 三、configure.in+aclocal.m4 -> autoconf -> configure

## 四、vi Makefile.am

```sh
AUTOMAKE_OPTIONS=foreign
bin_PROGRAMS=server client

server_SOURCES=server.c
client_SOURCES=client.c
```

## 五、 configure.in+Makefile.am -> automake  --add-missing -> makefile.in

## 六、makefile.in -> configure -> Makefile


# -- JIN --  java 调用 c

## testJin.h

``` c
/* DO NOT EDIT THIS FILE - it is machine generated */
#include <jni.h>
/* Header for class testJin */

#ifndef _Included_testJin
#define _Included_testJin
#ifdef __cplusplus
extern "C" {
#endif
/*
 * Class:     testJin
 * Method:    add
 * Signature: (I)I
 */
JNIEXPORT jint JNICALL Java_testJin_add
  (JNIEnv *, jobject, jint);

#ifdef __cplusplus
}
#endif
#endif
```

## test.c

``` c
#include<stdio.h>
#include"testJin.h"

//java调用所需
JNIEXPORT jint JNICALL Java_testJin_add(JNIEnv * env, jclass this, jint b)
{
    printf("Hello world!\n");
    return b;
}
```


## testJin.java

``` java
class testJin{

public native int add(int a);

static {
    System.loadLibrary("test");
}

    public static void main(String[] args)
    {
        testJin test2 = new testJin();
        test2.add(10);
        System.out.println();
    }
}
```

## Compile

```txt

javac testJin.java
javah testJin
gcc -shared -I%JAVA_HOME%\include -I%JAVA_HOME%\include\win32 -c test.c -o test.o
gcc -Wl,--kill-at -shared -o test.dll test.o
java testJin
del test.dll test.o testJin.class

```
