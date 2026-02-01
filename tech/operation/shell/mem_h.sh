#!/bin/bash
# 获取当前时间
now=$(date +"%Y-%m-%d %H:%M:%S")

# 列出CPU占用率最高的5个程序
echo "列出CPU占用率最高的5个程序："
top -b -n 1 | grep "PID" -A 5 | tail -n 5 | awk '{print $1, $9}'

# 列出内存占用率最高的5个程序
echo "列出内存占用率最高的5个程序："
ps aux | sort -k4nr | head -n 10 | awk '{print $2, $6/1024 "MB", $11}'
