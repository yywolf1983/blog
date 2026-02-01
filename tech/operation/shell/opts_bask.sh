jenkins_home=/mnt/jenkins
back_home=/data/ubuntu/jenkins.back
today=`date '+%Y%m%d'`

mkdir -p $back_home
cd $jenkins_home
file_list=`find ./jobs -maxdepth 1 -mindepth 1 -type d | grep -v builds`

for i in $file_list
do
    mkdir -p $back_home/$i
    cp -f $i/config.xml $back_home/$i
    echo $i
done

tar zcPf $back_home/jenkins$today.tar.gz $back_home/jobs

tar zcPf $back_home/portainer$today.tar.gz /data/docker/portainer_data

tar zcPf $back_home/prometheus.$today.tar.gz /mnt/prometheus/{alertmanager,blackbox,prometheus,ssl}

tar zcPf $back_home/ssh.$today.tar.gz /data/ubuntu/.ssh

su - ubuntu -c "sh  /data/ubuntu/k8back/bin/k8back.sh mfi mfi-test"

tar zcPf $back_home/k8s.$today.tar.gz /data/ubuntu/k8back/data/

#rsync -e  "ssh -i /data/ubuntu/.ssh/id_rsa" --delete -avz /data/cephfs/gitback root@heco:/data/gitback

rm -rf /data/ubuntu/k8back/data/backup


find $back_home -name "*.tar.gz" -mtime +60 -exec rm -f {} \;
find /data/cephfs/gitback -name "*.tar" -mtime +60 -exec rm -f {} \;

