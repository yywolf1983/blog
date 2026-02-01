cd /mnt/jenkins/workspace/arche-admin-jeecg/jeecg-cloud-module
count=`ps -ef | grep jeecg-cloud-system-start/target/jeecg-cloud-system-start | grep -v grep | awk '{print $2}'`
if [ 0 != $count ];then
kill -9 $count
fi
nohup /usr/local/jdk/jdk8/bin/java -jar jeecg-cloud-system-start/target/jeecg-cloud-system-start-3.0.jar > jeecg-cloud-system-start.log 2>&1 > /dev/null &
