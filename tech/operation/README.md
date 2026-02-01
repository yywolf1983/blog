# 运维相关

运维技术文档和脚本集合。

## 目录结构

### Ansible
- [base/](../viewer.html?file=tech/operation/ansible/base/tasks/main.yml)：Ansible基础配置
  - [tasks/](../viewer.html?file=tech/operation/ansible/base/tasks/main.yml)：任务文件
  - [templates/](../viewer.html?file=tech/operation/ansible/base/templates/add_jdk.sh.j2)：模板文件
  - [vars/](../viewer.html?file=tech/operation/ansible/base/vars/main.yml)：变量文件
- [docker/](../viewer.html?file=tech/operation/ansible/docker/tasks/main.yml)：Docker相关Ansible配置
- [docker_nginx/](../viewer.html?file=tech/operation/ansible/docker_nginx/tasks/main.yml)：Docker Nginx配置
- [mysql/](../viewer.html?file=tech/operation/ansible/mysql/tasks/main.yml)：MySQL相关Ansible配置
- [nginx/](../viewer.html?file=tech/operation/ansible/nginx/tasks/main.yml)：Nginx相关Ansible配置
- [nginx_conf/](../viewer.html?file=tech/operation/ansible/nginx_conf/tasks/main.yml)：Nginx配置管理
- [passwd/](../viewer.html?file=tech/operation/ansible/passwd/tasks/main.yml)：密码管理
- [prometheus/](../viewer.html?file=tech/operation/ansible/prometheus/tasks/main.yml)：Prometheus监控配置
- [python3/](../viewer.html?file=tech/operation/ansible/python3/tasks/main.yml)：Python3相关配置
- [rabbitmq.base/](../viewer.html?file=tech/operation/ansible/rabbitmq.base/tasks/main.yml)：RabbitMQ基础配置
- [redis/](../viewer.html?file=tech/operation/ansible/redis/tasks/main.yml)：Redis相关配置
- [rocket/](../viewer.html?file=tech/operation/ansible/rocket/rocket.yml)：Rocket Chat配置
- [sh/](../viewer.html?file=tech/operation/ansible/sh/ipck.sh)：Shell脚本
- [base.yml](../viewer.html?file=tech/operation/ansible/base.yml)：基础配置Playbook
- [docker.yml](../viewer.html?file=tech/operation/ansible/docker.yml)：Docker配置Playbook
- [docker_nginx.yml](../viewer.html?file=tech/operation/ansible/docker_nginx.yml)：Docker Nginx配置Playbook
- [ipch.yml](../viewer.html?file=tech/operation/ansible/ipch.yml)：IP配置Playbook
- [mysql.yml](../viewer.html?file=tech/operation/ansible/mysql.yml)：MySQL配置Playbook
- [nginx.yml](../viewer.html?file=tech/operation/ansible/nginx.yml)：Nginx配置Playbook
- [nginx_conf.yml](../viewer.html?file=tech/operation/ansible/nginx_conf.yml)：Nginx配置管理Playbook
- [passwd.yml](../viewer.html?file=tech/operation/ansible/passwd.yml)：密码管理Playbook
- [prometheus.yml](../viewer.html?file=tech/operation/ansible/prometheus.yml)：Prometheus配置Playbook
- [python3.yml](../viewer.html?file=tech/operation/ansible/python3.yml)：Python3配置Playbook
- [rabbitmq.yml](../viewer.html?file=tech/operation/ansible/rabbitmq.yml)：RabbitMQ配置Playbook
- [redis.yml](../viewer.html?file=tech/operation/ansible/redis.yml)：Redis配置Playbook
- [test.yml](../viewer.html?file=tech/operation/ansible/test.yml)：测试Playbook

### Docker
- [ceph/](../viewer.html?file=tech/operation/docker/ceph/docker-compose.yml)：Ceph Docker配置
- [docker-elk/](../viewer.html?file=tech/operation/docker/docker-elk/README.md)：ELK Stack Docker配置
  - [elasticsearch/](../viewer.html?file=tech/operation/docker/docker-elk/elasticsearch/Dockerfile)：Elasticsearch配置
  - [kibana/](../viewer.html?file=tech/operation/docker/docker-elk/kibana/Dockerfile)：Kibana配置
  - [logstash/](../viewer.html?file=tech/operation/docker/docker-elk/logstash/Dockerfile)：Logstash配置
  - [extensions/](../viewer.html?file=tech/operation/docker/docker-elk/extensions/README.md)：扩展配置
- [java/](../viewer.html?file=tech/operation/docker/java/Dockerfile)：Java Docker配置
- [nginx/](../viewer.html?file=tech/operation/docker/nginx/nginx.conf)：Nginx Docker配置
- [prometheus/](../viewer.html?file=tech/operation/docker/prometheus/prometheus.yml)：Prometheus Docker配置
  - [grafana/](../viewer.html?file=tech/operation/docker/prometheus/grafana/Docker Dashboard for Prometheus .json)：Grafana配置
- [py/](../viewer.html?file=tech/operation/docker/py/Dockerfile)：Python Docker配置
- [ubuntu/](../viewer.html?file=tech/operation/docker/ubuntu/Dockerfile)：Ubuntu Docker配置
- [Dockerfile](../viewer.html?file=tech/operation/docker/Dockerfile)：Dockerfile示例
- [docker.sh](../viewer.html?file=tech/operation/docker/docker.sh)：Docker脚本
- [docker_log.sh](../viewer.html?file=tech/operation/docker/docker_log.sh)：Docker日志脚本
- [dockerindocker.md](../viewer.html?file=tech/operation/docker/dockerindocker.md)：Docker in Docker
- [gogs.yml](../viewer.html?file=tech/operation/docker/gogs.yml)：Gogs配置
- [my.cnf](../viewer.html?file=tech/operation/docker/my.cnf)：MySQL配置
- [mynginx.yml](../viewer.html?file=tech/operation/docker/mynginx.yml)：Nginx配置
- [mysql.yml](../viewer.html?file=tech/operation/docker/mysql.yml)：MySQL配置
- [nginx-php.conf](../viewer.html?file=tech/operation/docker/nginx-php.conf)：Nginx PHP配置
- [nginx-php.yml](../viewer.html?file=tech/operation/docker/nginx-php.yml)：Nginx PHP配置
- [openldap.yaml](../viewer.html?file=tech/operation/docker/openldap.yaml)：OpenLDAP配置
- [portainer.yml](../viewer.html?file=tech/operation/docker/portainer.yml)：Portainer配置
- [postgresql.yml](../viewer.html?file=tech/operation/docker/postgresql.yml)：PostgreSQL配置
- [readme.txt](../viewer.html?file=tech/operation/docker/readme.txt)：说明文档
- [redis.conf](../viewer.html?file=tech/operation/docker/redis.conf)：Redis配置
- [redis.yml](../viewer.html?file=tech/operation/docker/redis.yml)：Redis配置
- [rocket.chat.md](../viewer.html?file=tech/operation/docker/rocket.chat.md)：Rocket Chat文档

### 命令
- [README.md](../viewer.html?file=tech/operation/commnd/README.md)：命令文档说明
- [awk](../viewer.html?file=tech/operation/commnd/awk)：awk命令
- [base](../viewer.html?file=tech/operation/commnd/base)：基础命令
- [color](../viewer.html?file=tech/operation/commnd/color)：颜色命令
- [crontab](../viewer.html?file=tech/operation/commnd/crontab)：定时任务
- [curl](../viewer.html?file=tech/operation/commnd/curl)：curl命令
- [date](../viewer.html?file=tech/operation/commnd/date)：日期命令
- [dd](../viewer.html?file=tech/operation/commnd/dd)：dd命令
- [expect](../viewer.html?file=tech/operation/commnd/expect)：expect脚本
- [find](../viewer.html?file=tech/operation/commnd/find)：find命令
- [fstab](../viewer.html?file=tech/operation/commnd/fstab)：fstab配置
- [gpg](../viewer.html?file=tech/operation/commnd/gpg)：GPG命令
- [httpie](../viewer.html?file=tech/operation/commnd/httpie)：HTTPie命令
- [iostat](../viewer.html?file=tech/operation/commnd/iostat)：IO统计
- [ip](../viewer.html?file=tech/operation/commnd/ip)：IP命令
- [iptables](../viewer.html?file=tech/operation/commnd/iptables)：防火墙规则
- [lsof](../viewer.html?file=tech/operation/commnd/lsof)：lsof命令
- [namp](../viewer.html?file=tech/operation/commnd/namp)：网络扫描
- [nc](../viewer.html?file=tech/operation/commnd/nc)：nc命令
- [nc_namp.md](../viewer.html?file=tech/operation/commnd/nc_namp.md)：nc和namp文档
- [patch](../viewer.html?file=tech/operation/commnd/patch)：patch命令
- [perf](../viewer.html?file=tech/operation/commnd/perf)：性能分析
- [ps](../viewer.html?file=tech/operation/commnd/ps)：进程查看
- [r2](../viewer.html?file=tech/operation/commnd/r2)：r2命令
- [rsync](../viewer.html?file=tech/operation/commnd/rsync)：rsync命令
- [sar](../viewer.html?file=tech/operation/commnd/sar)：系统活动报告
- [screen](../viewer.html?file=tech/operation/commnd/screen)：screen命令
- [sed](../viewer.html?file=tech/operation/commnd/sed)：sed命令
- [sort](../viewer.html?file=tech/operation/commnd/sort)：sort命令
- [split](../viewer.html?file=tech/operation/commnd/split)：split命令
- [ss](../viewer.html?file=tech/operation/commnd/ss)：ss命令
- [sshfs](../viewer.html?file=tech/operation/commnd/sshfs)：SSH文件系统
- [strace](../viewer.html?file=tech/operation/commnd/strace)：系统跟踪
- [systemctl](../viewer.html?file=tech/operation/commnd/systemctl)：systemctl命令
- [tmux](../viewer.html?file=tech/operation/commnd/tmux)：tmux命令
- [top](../viewer.html?file=tech/operation/commnd/top)：top命令
- [ulimit](../viewer.html?file=tech/operation/commnd/ulimit)：资源限制
- [user](../viewer.html?file=tech/operation/commnd/user)：用户管理
- [uuid](../viewer.html?file=tech/operation/commnd/uuid)：UUID生成
- [vim](../viewer.html?file=tech/operation/commnd/vim)：vim命令

### 文档
- [yed/](../viewer.html?file=tech/operation/doc/yed/Kubernetes.graphml)：yEd图形文件
- [团队建设/](../viewer.html?file=tech/operation/doc/团队建设/DevOps 和 SRE.docx)：团队建设文档
- [CloudFlare批量添加.txt](../viewer.html?file=tech/operation/doc/CloudFlare批量添加.txt)：CloudFlare批量添加
- [Git分支管理实践.md](../viewer.html?file=tech/operation/doc/Git分支管理实践.md)：Git分支管理
- [WebSocket 协议.docx](../viewer.html?file=tech/operation/doc/WebSocket 协议.docx)：WebSocket协议
- [XXXXX安全服务方案.docx](../viewer.html?file=tech/operation/doc/XXXXX安全服务方案.docx)：安全服务方案
- [devops.pptx](../viewer.html?file=tech/operation/doc/devops.pptx)：DevOps演示
- [git 分支.png](../viewer.html?file=tech/operation/doc/git 分支.png)：Git分支图
- [k8s_cluster.png](../viewer.html?file=tech/operation/doc/k8s_cluster.png)：K8s集群图
- [svn缺陷.jpg](../viewer.html?file=tech/operation/doc/svn缺陷.jpg)：SVN缺陷图
- [tcpip.tcpformat.png](../viewer.html?file=tech/operation/doc/tcpip.tcpformat.png)：TCP/IP格式图
- [yw_ppt.md](../viewer.html?file=tech/operation/doc/yw_ppt.md)：运维PPT
- [区块安全.odp](../viewer.html?file=tech/operation/doc/区块安全.odp)：区块安全
- [发布流程.jpeg](../viewer.html?file=tech/operation/doc/发布流程.jpeg)：发布流程图
- [大话程序猿眼里的高并发之续篇.png](../viewer.html?file=tech/operation/doc/大话程序猿眼里的高并发之续篇.png)：高并发
- [安全运维.md](../viewer.html?file=tech/operation/doc/安全运维.md)：安全运维
- [开发维护大型项目的Java的建议.txt](../viewer.html?file=tech/operation/doc/开发维护大型项目的Java的建议.txt)：Java项目建议
- [网关设计.png](../viewer.html?file=tech/operation/doc/网关设计.png)：网关设计图
- [运维制度规范.docx](../viewer.html?file=tech/operation/doc/运维制度规范.docx)：运维制度规范
- [运维工作.txt](../viewer.html?file=tech/operation/doc/运维工作.txt)：运维工作
- [运维平台.pptx](../viewer.html?file=tech/operation/doc/运维平台.pptx)：运维平台
- [运维指标 恢复时间 恢复点.png](../viewer.html?file=tech/operation/doc/运维指标 恢复时间 恢复点.png)：运维指标
- [运维规范.png](../viewer.html?file=tech/operation/doc/运维规范.png)：运维规范
- [运维计划.pptx](../viewer.html?file=tech/operation/doc/运维计划.pptx)：运维计划

### 基础
- [base.sh](../viewer.html?file=tech/operation/base/base.sh)：基础脚本

### 其他
- [README.md](../viewer.html?file=tech/operation/README.md)：运维相关说明
- [README.txt](../viewer.html?file=tech/operation/README.txt)：说明文档
