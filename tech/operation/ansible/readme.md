
mkdir -p passwd/{tasks,vars,templates,handlers}
touch passwd/{tasks/main.yml,vars/main.yml,handlers/main.yml}

rsync -avz --delete aaa/yy/ops_base/ansible/ devops:~/ansible

#从指定
ansible-playbook base.yml -e hosts=172.31.8.224 --start-at='base dir'


安装redis
port 可选
ansible-playbook redis/redis.yml -e port=9998 -e hosts=172.31.8.224

安装mysql
ansible-playbook mysql.yml -e mysql_port=9998 -e hosts=172.31.8.224
ansible-playbook mysql.yml -e mysql_port=2378 -e hosts=172.31.8.224 --start-at='in pass'

安装nginx
ansible-playbook nginx.yml -e hosts=172.31.8.224


添加nginx 配置文件 调用指定tasks
ansible-playbook nginx_conf.yml -e hosts=172.31.8.225 --start-at-task="copy web.conf"  


ansible-playbook nginx_conf.yml -e hosts=thg3

# rabbitmq
ansible-galaxy install stouts.rabbitmq
vi ~/ansible_hosts
ansible-playbook rabbitmq.yml


# RocketChat
ansible-galaxy install -p rocket/ -r rocket/rocket.yml
ansible-playbook rocket/rocket_chat.yml 

# python3
ansible-playbook python3.yml -e hosts=app2 

# docker 安装
ansible-playbook docker.yml

# prometheus 安装
ansible-playbook prometheus.yml

#修改系统密码
ansible-playbook passwd.yml

# docker_nginx 安装
ansible-playbook docker_nginx.yml

回收
rsync -avz --delete xbl:~/ansible/ aaa/yy/ops_base/ansible

下载docker证书
ansible aws -m fetch -a 'src=/etc/docker/cert.pem dest=./'
ansible aws -m fetch -a 'src=/etc/docker/key.pem dest=./'



ansible-playbook docker.yml --list-tasks
ansible-playbook docker.yml --step --start-at-task="up service"
