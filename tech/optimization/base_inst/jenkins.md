
bamboo Atlassian出品持续集成工具

export JAVA_HOME

yum install fontconfig

export JENKINS_HOME=/data/jenkins/jenkins_home
screen -S jenkins
java -jar jenkins.war --httpPort=8088

export JAVA_OPTS="-Xms512m -Xmx1024m -XX:PermSize=512m -XX:MaxNewSize=512m -XX:MaxPermSize=512m"


docker run \
  -u root \
  --name jenkins \
  -d \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkinsci/blueocean


docker 支持插件
docker pipeline 

http://url:8080/pluginManager/advanced
国内源
https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json
https://mirrors.cloud.tencent.com/jenkins/updates/update-center.json
https://mirrors.huaweicloud.com/jenkins/updates/update-center.json

http://mirror.esuni.jp/jenkins/updates/update-center.json

Pipeline script


java -jar -Djenkins.install.runSetupWizard=false jenkins.war


yum install fontconfig dejavu-sans-fonts

host配置

127.0.0.1 updates.jenkins-ci.org

nginx配置

rewrite ^/download/plugins/(.*)$ https://mirrors.tuna.tsinghua.edu.cn/jenkins/plugins/$1? last;


http://localhost:8080/pluginManager/advanced


cat  << EOF  > jenkins_bask.sh

jenkins_home=/data/jenkins/jenkins_home
back_home=/root/jenkins.back

mkdir -p \$back_home
cd \$jenkins_home
file_list=\`find ./jobs -maxdepth 1 -mindepth 1 -type d | grep -v builds\`

for i in \$file_list
do
    mkdir -p \$back_home/\$i
    cp -f \$i/config.xml \$back_home/\$i
    echo \$i
done

tar zcPf \$back_home/jenkins.tar.gz \$back_home/jobs

EOF


vi /mnt/jenkins/jenkins.sh
#!/bin/bash
JAVA_HOME=/usr/local/jdk/jdk8
pid=`ps -ef | grep jenkins.war | grep -v 'grep'| awk '{print $2}'| wc -l`
if [ "$1" = "start" ];then
if [ $pid -gt 0 ];then
echo 'jenkins is running...'
else
		screen -dmS jenkins1 bash -c 'source ~/.bashrc;export JENKINS_HOME=/mnt/jenkins;java -jar /mnt/jenkins/jenkins.war --httpPort=8088'
fi
elif [ "$1" = "stop" ];then
        kill -9 `ps -ef | grep -v grep | grep "jenkins.war --httpPort=$jport" | awk '{print $2}'`
        screen -X -S 12306.jenkins1 quit
        screen -wipe
echo 'jenkins is stop..'
else
echo "Please input like this:"./jenkins.sh start" or "./jenkins stop""
fi


/lib/systemd/system/jenkins.service

[Unit]
Description=Jenkins
After=network.target

[Service]
Type=forking
ExecStart=/mnt/jenkins/jenkins.sh start
ExecReload=
ExecStop=/mnt/jenkins/jenkins.sh stop
PrivateTmp=true

[Install]
WantedBy=multi-user.target




systemctl daemon-reload
systemctl start jenkins.service







#/bin/sh

if [ $2 == "" ]
then
    echo "not jenkins"
    exit
elif [ $2 == "jenkins1" ]
then
    jport=8080
    function start() {
	echo "start"
	echo "----------------"
	screen -dmS jenkins1 bash -c 'source /etc/profile;export JENKINS_HOME=/data/jenkins/jenkins_home;java -jar /data/jenkins/jenkins.war --httpPort=8080'
    }
elif [ $2 == "jenkins2" ]
then
    jport=8081
    function start() {
	echo "start"
	echo "----------------"
	screen -dmS jenkins2 bash -c 'source /etc/profile;export JENKINS_HOME=/data/jenkins2/jenkins_home;java -jar /data/jenkins2/jenkins.war --httpPort=8081'
     }
else
    echo "canshu error"
    exit
fi 

function stop() {
	echo "stop"
	echo "----------------"
        kill -9 `ps -ef | grep -v grep | grep "jenkins.war --httpPort=$jport" | awk '{print $2}'`
        screen -X -S 12306.jenkins1 quit
        screen -wipe
}

function restart() {
	echo "restart"
	echo "----------------"
	stop
	start
}

case "$1" in
	start )
		echo "****************"
		start
		echo "****************"
		;;
	stop )
		echo "****************"
		stop
		echo "****************"
		;;
	restart )
		echo "****************"
		restart
		echo "****************"
		;;
	* )
		echo "****************"
		echo "no command"
		echo "****************"
		;;
esac