# tcpdump

tcpdump -D 列出网卡

tcpdump --interface en0 监听

```text〔筆畫〕
输出包含以下信息:
    接收数据包的时间戳
    接口名称
    包流
    网络协议名称
    IP 地址和端口详细信息
    TCP 标志
    数据包中数据的序号
    确认数据
    窗口大小
    数据包长度
```

tcpdump --interface en0 -c 3  抓包次数

tcpdump --interface en0 -c 3 host 13.214.254.61 and tcp port 9000 

tcpdump --interface en0 -c 10 "(src 13.214.254.61 or src 234.231.23.234) and (port 9000 or port 80)"

-A 标志代表ASCII格式，-x表示十六进制格式。
tcpdump --interface en0 -c 1 -A
tcpdump --interface en0 -c 1 -x

tcpdump --interface en0 -c 10 -w data.pcap -v host 13.214.254.61 and tcp port 9000 

tcpdump -r data.pcap port 9000 -A

