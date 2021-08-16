


## tcp套接字

![tcp套接字](/tcp-ip/tcp套接字.png)

## tcpip定义 c语言定义

``` c
recv(m_Sock,buffer,1000,0);
先定义一个char* tempBuf型的变量，将Buffer的地址赋值，再将tempBuf强制转换成BYTE* 型就可以得到想要的:
 
#pragma pack(1)    //进入字节对齐方式

typedef struct FramHeader_t
{                      //Pcap捕获的数据帧头
    BYTE DstMAC[6];    //目的MAC地址
    BYTE SrcMAC[6];    //源MAC地址
    WORD FrameType;    //帧类型
} FramHeader_t;

typedef struct IPHeader_t
{                        //IP数据包头
    BYTE Ver_HLen;        //版本+报头长度
    BYTE TOS;            //服务类型
    WORD TotalLen;        //总长度
    WORD ID;            //标识
    WORD Flag_Segment;    //标志+片偏移
    BYTE TTL;            //生存周期
    BYTE Protocol;        //协议类型
    WORD Checksum;        //头部校验和
    DWORD SrcIP;        //源IP地址
    DWORD DstIP;        //目的IP地址
} IPHeader_t;
typedef struct ARPHeader_t
{                         //ARP数据包头
    WORD HeadwareType;    //硬件类型
    WORD ProtocolType;    //协议类型
    BYTE HLen;            //硬件地址长度
    BYTE PLen;            //协议地址长度
    WORD Operation;        //操作类型
    BYTE SrcMAC[6];        //源MAC地址
    DWORD SrcIP;        //源IP地址
    BYTE DstMAC[6];        //目的MAC地址
    DWORD DstIP;        //目的IP地址
} ARPHeader_t;

typedef struct UDPHeader_t
{                    //UDP数据包头
    WORD SrcPort;    //源端口
    WORD DstPort;    //目的端口
    WORD Len;        //总长度
    WORD Checksum;    //校验和
}UDPHeader_t;

typedef struct TCPHeader_t
{                     //TCP数据包头
    WORD SrcPort;     //源端口
    WORD DstPort;     //目的端口
    DWORD SeqNO;      //序号
    DWORD AckNO;      //确认号
    WORD Offset4_Reserved6_Flag6;    //头部长度+保留+标志
    WORD Window;      //窗口大小
    WORD Checksum;    //校验和
    WORD UrgentPointer;    //紧急指针
    DWORD Option_;    //选项+填充
}TCPHeader_t;

#pragma pack()    //恢复默认对齐方式
```

## IP数据报格式

IP数据报（datagram）的头部格式如下：

![ip数据报](/tcp-ip/ip-b.png)

```
Example Internet Datagram Header
Version：4 bits
版本字段标明建立数据报的IP版本，目前的IP版本是IPv4,IPv6正在发展中。IPv4：0100。
IHL：4 bits
IP数据报头部长度（Internet Header Length），其度量单位为4 Bytes（32 bits），因此IHL始终是4 Bytes（32 bits）的整数倍，
最长可达15 * 4 = 60个字节。IHL最小值为5（即20 Bytes），为不含填充字段和选项字段的最常见的IP数据报头格式。
Type of Service：8 bits
服务类型，有3 bits的Precedence、1 bit的Delay、1 bit的Throughout、1 bit的Relibility和2 bits的Reserved组成。
其值一般为0x00，表示Routine+Normal Delay+Normal Throughout+Normal Relibility。
Total Length：16 bits
总长度字段是指整个IP数据报的长度，以字节为单位。理论上，IP数据报最长可达2^16-1=65535 Bytes（64KB）。IP数据长度由该字段值减去IHL值计算得到。
Identification：16 bits
标识符是发送者为了接收者重组数据报的依据。当一个IP数据报比较大时，可能会被切分成多个数据包（fragments）分多次发送（此时Flags的第二位将置0，第三位置1），
接收端依据该字段进行组包。
Flags：3 bits
    The internet modules use fields in the internet header to fragment and  
    reassemble internet datagrams when necessary for transmission through "small packet" networks.
该字段用于分段控制。
第0位为预留位。
第1位表示是否分段，当值为0时，表示数据报将分段；当值为1时，表示数据报不分段（Don't Fragment）。
第2位为段是否还有后续fragment，当值为0时，表示该段是原数据报的最后一段；当值为1时，表示后面还有更多的分段（More Fragments）。
当网络设备要发送的数据报长度比所在网络的最大传输单元（MTU，Max Transfer Unit）大，并且标志位的第1位被置1，即为不分段时，
网络设备会向发送方返回一个因特网控制消息协议ICMP错误消息，并丢弃该数据报。除了最后一个分段外，其余分段的第2位均设置为1。
Fragment Offset：13 bits
段偏移字段用于指定该分段在原始数据报中的位置，以8 Bytes为度量单位。
Time to Live：8 bits
用于指定数据报允许保留在网络上的时间。计量单位为秒，在网络中每被处理一次该值就减小一次。当该值为0时，该数据报将会被销毁。
Protocol：8 bits
用于指定数据报数据区中携带的消息是由哪种高级协议建立的。ICMP为1,TCP为6，UDP为17。
Header Checksum：16 bits
    IP报头校验和。参考：《校验和的计算》
Source Address：32 bits
    源IP地址。
Destination Address：32 bits
    目的IP地址。
Options：variable
可变长可选项。
Padding：variable
4字节边界（填零）对齐。
// 定义ip报头数据结构
typedef struct _iphdr
{
    byte ver_len; // 版本4位,头长度4位,报头长度以32位为一个单位
    byte type; // 类型8位
    byte length[2]; //总长度,16位,指出报文的以字节为单位的总长度，报文长度不能超过65536个字节，否则认为报文遭到破坏
    byte id[2]; // 报文标示,用于多于一个报文16位
    byte flag_offset[2]; // 标志,3位 数据块偏移13位
    byte time; // 生存时间,8位
    byte protocol; // 协议,8位
    byte crc_val[2]; // 头校验和，16位
    byte src_addr[4]; // 源地址,32位
    byte tar_addr[4]; // 目标地址,32位
    byte options[4]; // 选项和填充,32位
}IP_HEADER;
```

## TCP报文格式

```
传输控制协议（TCP）向上与用户应用程序进程接口，向下与网络层协议IP接口。用户应用程序采用首先调用TCP（或UDP），然后将
应用程序数据递交给TCP这一方式，在IP网络上传送数据。TCP将这些数据打包分段并调用IP模块向目的主机传送每个数据段。接收方
的TCP将段中的数据放入接收缓冲区，然后将段重装（reassemble）为应用程序数据，再将这些数据发送到目的的应用程序进程。尽管
TCP和UDP都使用相同的网络层（IP），TCP却向应用层提供与UDP完全不同的服务。TCP提供一种面向连接的、可靠的字节流服务。TCP
数据包（package）的头部格式如下：
```

![tcp数据报](/tcp-ip/tcp-b.png)

```
TCP Header Format
Note that one tick mark represents one bit position.
Source Port：16 bits
源端口。
Destination Port：16 bits
目的端口。
Sequence Number：32 bits
在这个报文段中的第一个数据字节的序列号。SYN报文的序列号为初始化序列号（ISN），第一个TCP数据包的序列号为ISN+1。
SEQ为对TCP包序列号，其数值为上一次对方发过来的ACK加上本次发出去的数据量。即SEQ2 = ACK1+send。
Acknowledgment Number：32 bits
只有ACK标志为1时，确认号字段才有效。它包含目标端所期望收到源端的下一个序列号。在[SYN,ACK]报文中，ACK=ISN+1。
ACK为对上一次的响应（response）和对下一次的期待（expectation），其数值为上一次对方发过来的SEQ加上本次接收到的数据量。即ACK2 = SEQ1+recv。
Data Offset：4 bits
头部长度/4Byte，即头部长度占了多少个32 bits。没有任何选项字段的TCP头部长度为20字节；TCP头部长度最大为60（15*4）字节。
Reserved：6 bits
预留给将来使用，必须设置为0。
Control Bits：6 bits (from left to right)
URG:  Urgent Pointer field significant，紧急指针有效位。
ACK:  Acknowledgment field significant，确认序号有效位。
PSH:  Push Function，接收方应该尽快将这个报文段交给应用层。
RST:  Reset the connection，重建连接。如果主机接收到未经请求就进入的数据，接收到不符合预期的ACK，就会用它来重置。
SYN:  Synchronize sequence numbers，发起一个连接。
FIN:  No more data from sender，关闭一条连接。
Window：16 bits
用来进行流量控制的滑动窗口，单位为字节数。滑动窗口大小为接收方向发送方通知本机当前能够接收的最大数据量。发送方下次发送来的超出滑动窗口的数据将被接收方丢弃。
Checksum：16 bits
对整个TCP报文段，即TCP头部和TCP数据进行校验和计算，并由目标端进行验证。
Urgent Pointer：16 bits
它是一个偏移量，和序号字段中的值相加表示紧急数据最后一个字节的序号。只有当URG标志为1时，紧急数据才有效。
Options：variable
可能包括"窗口扩大因子"、"时间戳"等可选项。
Padding：variable
4字节边界（填零）对齐。
// 定义TCP报头
typedef struct _tcphdr
{
 byte source_port[2]; // 发送端端口号,16位
 byte dest_port[2];  // 接收端端口号,16位
 byte sequence_no[4]; // 32位，标示消息端的数据位于全体数据块的某一字节的数字
 byte ack_no[4];   // 32位，确认号,标示接收端对于发送端接收到数据块数值
 byte offset_reser_con[2]; // 数据偏移4位，预留6位，控制位6为
 byte window[2];   // 窗口16位
 byte checksum[2];  // 校验码,16位
 byte urgen_pointer[2]; // 16位，紧急数据指针
 byte options[3];  // 选祥和填充,32位
}TCP_HEADER;
```


## tcp状态转换

![tcp状态转换](/tcp-ip/tcp状态转换.png)