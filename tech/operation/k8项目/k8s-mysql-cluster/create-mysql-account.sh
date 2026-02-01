MYSQL_ROOT_PASSWORD='mysql_pass'

MYSQL_SERVER_ADDRESS='127.0.0.1'

mysql -uroot -e "alter user 'root'@'localhost' IDENTIFIED BY '$MYSQL_ROOT_PASSWORD';"