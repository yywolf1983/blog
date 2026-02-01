

新生代 老年代
内存堆 方法栈

垃圾回收 
字节码  class 文件结构
字节码指令 类似汇编指令

HotSpot
线程安全

top -Hp pid
jstack -l lpid > test.txt
printf "%0x" lpid
在test中查找

## 基础命令 

### javah

### jps

### jstack (Java Stack Trace)
   1、RUNNABLE，线程处于执行中
   2、BLOCKED，线程被阻塞
   3、WAITING，线程正在等待 

### jstat (Java Virtual Machine Statistics Monitoring Tool)

Option  Displays...
class   用于查看类加载情况的统计
compiler    用于查看HotSpot中即时编译器编译情况的统计
gc  用于查看JVM中堆的垃圾收集情况的统计
gccapacity  用于查看新生代、老生代及持久代的存储容量情况
gccause 用于查看垃圾收集的统计情况（这个和-gcutil选项一样），如果有发生垃圾收集，它还会显示最后一次及当前正在发生垃圾收集的原因。
gcnew   用于查看新生代垃圾收集的情况
gcnewcapacity   用于查看新生代的存储容量情况
gcold   用于查看老生代及持久代发生GC的情况
gcoldcapacity   用于查看老生代的容量
gcpermcapacity  用于查看持久代的容量
gcutil  用于查看新生代、老生代及持代垃圾收集的情况
printcompilation    HotSpot编译方法的统计

### jmap (Java Memory Map)
 打印内存信息
 配合jhat生成图像
 jmap -dump:format=b,file=heapdump.phrof pid

### jvisualvm 
    可以查看 jmap dump

### jinfo (Java Configuration Info)

### jconsole (Java Monitoring and Management Console)

#### 远程调试命令
java 
-Djava.rmi.server.hostname=10.160.13.111  #远程服务器ip，即本机ip
-Dcom.sun.management.jmxremote #允许JMX远程调用
-Dcom.sun.management.jmxremote.port=3214  #自定义jmx 端口号
-Dcom.sun.management.jmxremote.ssl=false  # 是否需要ssl 安全连接方式
-Dcom.sun.management.jmxremote.authenticate=false #是否需要秘钥
 -jar test.jar 
