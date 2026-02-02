
kubectl apply -f secret.yml

cd image/percona-xtrabackup
sudo docker build . -t percona-xtrabackup:8.0


kubectl create configmap mysql-user --from-file=create-mysql-account.sh
kubectl label nodes m2 mysql=master
kubectl label nodes m3 mysql=slave
kubectl apply -f master-slave.yaml
或者
kubectl apply -f innodb-cluster.yaml


#万丈深坑在此处
mysql -uroot -pmysql_pass -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';"
mysql -uroot -pmysql_pass -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';"
mysql -uroot -pmysql_pass -e "CREATE USER 'root'@'localhost' IDENTIFIED BY 'mysql_pass';"
mysql -uroot -pmysql_pass -e "CREATE USER 'root'@'%' IDENTIFIED BY 'mysql_pass';"