

## 基础语法 (未整理)

sh -n 调试shell

sh -v

```
421
rwx

用户-组-其他

d 目录。
l 符号链接(指向另一个文件)。
s 套接字文件。
b 块设备文件。
c 字符设备文件。
p 命名管道文件。
- 普通文件，或者更准确地说，不属于以上几种类型的文件。

umask

read 读取输入

输入文件—标准输入 0
输出文件—标准输出 1
错误输出文件—标准错误 2

command << delimiter 把从标准输入中读入，直至遇到delimiter分界符

命令1 && 命令2

shell 支持正则匹配

awk 内置变量
ARGC 命令行参数个数
ARGV 命令行参数排列
ENVIRON 支持队列中系统环境变量的使用
FILENAME awk浏览的文件名
FNR 浏览文件的记录数
FS 设置输入域分隔符，等价于命令行 - F选项
NF 浏览记录的域个数
NR 已读的记录数
OFS 输出域分隔符
ORS 输出记录分隔符
RS 控制记录分隔符


• 实用的分类（sort）操作。
• uniq。   去重
• join。   关联合并
• cut。
• paste。
• split。

tr 替换字符串

登录成功后，系统执行两个环境设置文件，第一个是 /etc/profile ，第二个是 .profile，位
于用户根目录下。

/var/adm/messages

variable-name=version
readonly variable-name  只读变量


EDITOR=vi ; export EDITOR

$0 $1 $2 $3 ......

$# 传递到脚本的参数个数
$* 以一个单字符串显示所有向脚本传递的参数。与位置变量不同，此选项参数可超过 9个
$$ 脚本运行的当前进程ID号
$! 后台运行的最后一个进程的进程 ID号
$@ 与$#相同，但是使用时加引号，并在引号中返回每个参数
$- 显示shell使用的当前选项，与set命令功能相同
$? 显示最后命令的退出状态。 0表示没有错误，其他任何值表明有错误。

GNU/linux 系统的 coreutils 软件包通
test
-d 目录       -s 文件长度大于 0、非空
-f 正规文件   -w 可写
-L 符号连接   -u 文件有suid位设置
-r 可读       -x 可执行


常见字符串测试

-z string       字符串string 为空串(长度为0)时返回真
-n string       字符串string 为非空串时返回真
str1 = str2     字符串str1 和字符串str2 相等时返回真
str1 == str2    同 =
str1 != str2    字符串str1 和字符串str2 不相等时返回真
str1 < str2     按字典顺序排序，字符串str1 在字符串str2 之前
str1 > str2     按字典顺序排序，字符串str1 在字符串str2 之后
举例: name="zqf"; [ $name = "zqf" ];echo $? // 打印 0 表示变量name 的值和字符串"zqf"相等

常见数值测试

int1 -eq int2   如果int1 等于int2，则返回真
int1 -ne int2   如果int1 不等于int2，则返回真
int1 -lt int2   如果int1 小于int2，则返回真
int1 -le int2   如果int1 小于等于int2，则返回真
int1 -gt int2   如果int1 大于int2，则返回真
int1 -ge int2   如果int1 大于等于int2，则返回真


expr 计算器


if 条件1
then 命令1
elif 条件2
then 命令2
else 命令3
fi

case 值 in
模式1 }
命令1
;;
模式2）
命令2
;;
esac

${WHEN:="abcs"}  如果没有定义则等于


for loop in 1 2 3 4 5 6
do
echo $loop
done

for i in {001..999};
do
   echo $i ;
done

为真停止
until 条件
命令1
. . .
done

while 命令
do
命令1
命令2
. . .
done

使用break和continue控制循环

shift   向右偏移

while getopts afkge OPT
do
  case $OPT in


  1    SIGHUP 挂起或父进程被杀死
  2    SIGINT 来自键盘的中断信号，通常是 < C T R L - C >
  3    SIGQUIT 从键盘退出
  9    SIGKILL 无条件终止
  11   SIGSEGV 段（内存）冲突
  15   SIGTERM 软件终止（缺省杀进程信号）
```

## 测试条件

```
分类参考
文件状态测试
-b filename 当filename 存在并且是块文件时返回真(返回0)
-c filename 当filename 存在并且是字符文件时返回真
-d pathname 当pathname 存在并且是一个目录时返回真
-e pathname 当由pathname 指定的文件或目录存在时返回真
-f filename 当filename 存在并且是正规文件时返回真
-g pathname 当由pathname 指定的文件或目录存在并且设置了SGID 位时返回真
-h filename 当filename 存在并且是符号链接文件时返回真 (或 -L filename)
-k pathname 当由pathname 指定的文件或目录存在并且设置了"粘滞"位时返回真
-p filename 当filename 存在并且是命名管道时返回真
-r pathname 当由pathname 指定的文件或目录存在并且可读时返回真
-s filename 当filename 存在并且文件大小大于0 时返回真
-S filename 当filename 存在并且是socket 时返回真
-t fd 当fd 是与终端设备相关联的文件描述符时返回真
-u pathname 当由pathname 指定的文件或目录存在并且设置了SUID 位时返回真
-w pathname 当由pathname 指定的文件或目录存在并且可写时返回真
-x pathname 当由pathname 指定的文件或目录存在并且可执行时返回真
-O pathname 当由pathname 存在并且被当前进程的有效用户id 的用户拥有时返回真(字母O 大写)
-G pathname 当由pathname 存在并且属于当前进程的有效用户id 的用户的用户组时返回真
file1 -nt file2 file1 比file2 新时返回真
file1 -ot file2 file1 比file2 旧时返回真
f1 -ef f2 files f1 and f2 are hard links to the same file
举例: if [ -b /dev/hda ] ;then echo "yes" ;else echo "no";fi // 将打印 yes
test -c /dev/hda ; echo $? // 将打印 1 表示test 命令的返回值为1，/dev/hda 不是字符设备
[ -w /etc/passwd ]; echo $? // 查看对当前用户而言，passwd 文件是否可写
测试时逻辑操作符
-a 逻辑与，操作符两边均为真，结果为真，否则为假。
-o 逻辑或，操作符两边一边为真，结果为真，否则为假。
! 逻辑否，条件为假，结果为真。
举例: [ -w result.txt -a -w score.txt ] ;echo $? // 测试两个文件是否均可写
常见字符串测试
-z string 字符串string 为空串(长度为0)时返回真
-n string 字符串string 为非空串时返回真
str1 = str2 字符串str1 和字符串str2 相等时返回真
str1 == str2 同 =
str1 != str2 字符串str1 和字符串str2 不相等时返回真
str1 < str2 按字典顺序排序，字符串str1 在字符串str2 之前
str1 > str2 按字典顺序排序，字符串str1 在字符串str2 之后
举例: name="zqf"; [ $name = "zqf" ];echo $? // 打印 0 表示变量name 的值和字符串"zqf"相等
常见数值测试
int1 -eq int2 如果int1 等于int2，则返回真
int1 -ne int2 如果int1 不等于int2，则返回真
int1 -lt int2 如果int1 小于int2，则返回真
int1 -le int2 如果int1 小于等于int2，则返回真
int1 -gt int2 如果int1 大于int2，则返回真
int1 -ge int2 如果int1 大于等于int2，则返回真
在 (()) 中的测试：
< 小于(在双括号里使用) (("$a" < "$b"))
<= 小于等于 (在双括号里使用) (("$a" <= "$b"))
> 大于 (在双括号里使用) (("$a" > "$b"))
>= 大于等于(在双括号里使用) (("$a" >= "$b"))
举例: x=1 ; [ $x -eq 1 ] ; echo $? // 将打印 0 表示变量x 的值等于数字1 x=a ; [ $x -eq "1" ] // shell 打印错误信息 [: a: integer expression expected
test ， [] , [[]]
因为 shell 和我们通常编程语言不同，更多的情况是和它交互，总是调用别人。 所以有些本属于程序语言本身的概念在 shell 中会难以理解。"基本功" 不好， 更容易 "犯困" 了，我就是一个 :-) 。
以 bash 为例 (其他兼容 shell 差不多)：
test 和 [ 是 bash 的内部命令，GNU/linux 系统的 coreutils 软件包通 常也带 /usr/bin/test 和 /usr/bin/[ 命令。如果我们不用绝对路径指 明，通常我们用的都是 bash 自带的命令。
[[ 是 bash 程序语言的关键字！
$ ls -l /usr/bin/[ /usr/bin/test
-rwxr-xr-x 1 root root 37400 9月 18 15:25 /usr/bin/[
-rwxr-xr-x 1 root root 33920 9月 18 15:25 /usr/bin/test
$ type [ [[ test
[ is a shell builtin
[[ is a shell keyword
test is a shell builtin
绝大多数情况下，这个三个功能通用。但是命令和关键字总是有区别的。命令和 关键字的差别有多大呢？
如果是命令，它就和参数组合为一体被 shell 解释，那样比如 ">" "<" 就被 shell 解释为重定向符号了。关键字却不这样。
在 [[ 中使用 && 和 ||
[ 中使用 -a 和 -o 表示逻辑与和逻辑或。
[[ 中可以使用通配符
arch=i486
[[ $arch = i*86 ]] && echo "arch is x86!"
[[ 中匹配字符串或通配符，不需要引号
    [[ $arch_com = i386 || $ARCH = i*86 ]] &&
    cat >> $TFS_REPO <<EOF
[tfs-i386]
name=GTES11.3 prelim1
baseurl=${BASEURL}i386/
enabled=1
EOF
```

## 基础命令

```
编辑命令

Ctrl + a ：移到命令行首
Ctrl + e ：移到命令行尾
Ctrl + f ：按字符前移（右向）
Ctrl + b ：按字符后移（左向）
Alt + f ：按单词前移（右向）
Alt + b ：按单词后移（左向）
Ctrl + xx：在命令行首和光标之间移动
Ctrl + u ：从光标处删除至命令行首
Ctrl + k ：从光标处删除至命令行尾
Ctrl + w ：从光标处删除至字首
Alt + d ：从光标处删除至字尾
Ctrl + d ：删除光标处的字符
Ctrl + h ：删除光标前的字符
Ctrl + y ：粘贴至光标后
Alt + c ：从光标处更改为首字母大写的单词
Alt + u ：从光标处更改为全部大写的单词
Alt + l ：从光标处更改为全部小写的单词
Ctrl + t ：交换光标处和之前的字符
Alt + t ：交换光标处和之前的单词
Alt + Backspace：与 Ctrl + w 相同类似，分隔符有些差别 [感谢 rezilla 指正]
重新执行命令

Ctrl + r：逆向搜索命令历史
Ctrl + g：从历史搜索模式退出
Ctrl + p：历史中的上一条命令
Ctrl + n：历史中的下一条命令
Alt + .：使用上一条命令的最后一个参数
控制命令

Ctrl + l：清屏
Ctrl + o：执行当前命令，并选择上一条命令
Ctrl + s：阻止屏幕输出
Ctrl + q：允许屏幕输出
Ctrl + c：终止命令
Ctrl + z：挂起命令
Bang (!) 命令

!!：执行上一条命令
!blah：执行最近的以 blah 开头的命令，如 !ls
!blah:p：仅打印输出，而不执行
!$：上一条命令的最后一个参数，与 Alt + . 相同
!$:p：打印输出 !$ 的内容
!*：上一条命令的所有参数
!*:p：打印输出 !* 的内容
^blah：删除上一条命令中的 blah
^blah^foo：将上一条命令中的 blah 替换为 foo
^blah^foo^：将上一条命令中所有的 blah 都替换为 foo
```