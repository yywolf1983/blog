#!/bin/sh

case "$1" in
    start)
        #启动
        # echo 'starting...'
        nohup java -Xms2048m -Xmx2048m -jar $2 --spring.profiles.active=prod > /dev/null 2>&1 &
        echo 'started'
        ;;
    stop)
        #停止
        echo 'stopping...'
        ps -ef | grep "$2" | grep -v grep | grep -v check | awk '{print $2}' | xargs kill -9
        # echo 'stoped'
        ;;
    check)
        #检查并执行
        count=`ps -ef | grep "$2" | grep -v grep | grep -v check | wc -l`
        # echo "$count"
        if [ $count -lt 1 ]; then
            echo 'starting...'
            nohup java -Xms128m -Xmx4096m -jar $2 > /dev/null 2>&1 &
            echo 'started'
        else
            echo 'already running...'
        fi
        ;;
    *)
        echo 'Please use start or stop or check as first argument'
        ;;
esac