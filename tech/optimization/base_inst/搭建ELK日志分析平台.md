
ELK简介：
ELK是三个开源软件的缩写，分别为：Elasticsearch 、 Logstash以及Kibana , 它们都是开源软件。

Elastic Stack包含：
Elasticsearch是个开源分布式搜索引擎，提供搜集、分析、存储数据三大功能。它的特点有：分布式，零配置，自动发现，索引自动分片，索引副本机制，restful风格接口，多数据源，自动搜索负载等。

Logstash 主要是用来日志的搜集、分析、过滤日志的工具，支持大量的数据获取方式。一般工作方式为c/s架构，client端安装在需要收集日志的主机上，server端负责将收到的各节点日志进行过滤、修改等操作在一并发往elasticsearch上去。

Kibana 也是一个开源和免费的工具，Kibana可以为 Logstash 和 ElasticSearch 提供的日志分析友好的 Web 界面，可以帮助汇总、分析和搜索重要数据日志。

Beats在这里是一个轻量级日志采集器，其实Beats家族有6个成员，早期的ELK架构中使用Logstash收集、解析日志，但是Logstash对内存、cpu、io等资源消耗比较高。相比 Logstash，Beats所占系统的CPU和内存几乎可以忽略不计

ELK Stack （5.0版本之后）--> Elastic Stack == （ELK Stack + Beats）。目前Beats包含六种工具：

Packetbeat： 网络数据（收集网络流量数据）
Metricbeat： 指标 （收集系统、进程和文件系统级别的 CPU 和内存使用情况等数据）
Filebeat： 日志文件（收集文件数据）
Winlogbeat： windows事件日志（收集 Windows 事件日志数据）
Auditbeat：审计数据 （收集审计日志）
Heartbeat：运行时间监控 （收集系统运行时的数据）

关于x-pack工具：
x-pack对Elastic Stack提供了安全、警报、监控、报表、图表于一身的扩展包，是收费的，所以本文不涉及x-pack的安装
ELK官网：
https://www.elastic.co/cn/
中文指南：
https://www.gitbook.com/book/chenryn/elk-stack-guide-cn/details

--------------------------------------------------------------------------------
ELK安装准备工作
准备3台机器，这样才能完成分布式集群的实验，当然能有更多机器更好：
192.168.77.128
192.168.77.130
192.168.77.134
角色划分：
3台机器全部安装jdk1.8，因为elasticsearch是java开发的
3台全部安装elasticsearch (后续都简称为es)

主节点上需要安装kibana

配置三台机器的hosts文件内容如下：
$ vim /etc/hosts
192.168.77.128 master-node
192.168.77.130 data-node1
192.168.77.134 data-node2
然后三台机器都得关闭防火墙或清空防火墙规则。
--------------------------------------------------------------------------------
安装es
先上官方的安装文档：
https://www.elastic.co/guide/en/elastic-stack/current/installing-elastic-stack.html

--------------------------------------------------------------------------------
配置es
elasticsearch配置文件在这两个地方，有两个配置文件：
ll /etc/elasticsearch
-rw-rw---- 1 root elasticsearch 2869 2月  17 03:03 elasticsearch.yml
-rw-rw---- 1 root elasticsearch 2809 2月  17 03:03 jvm.options
-rw-rw---- 1 root elasticsearch 5091 2月  17 03:03 log4j2.properties
ll /etc/sysconfig/elasticsearch
-rw-rw---- 1 root elasticsearch 1613 2月  17 03:03 /etc/sysconfig/elasticsearch
[root@master-node ~]#
elasticsearch.yml 文件用于配置集群节点等相关信息的，elasticsearch 文件则是配置服务本身相关的配置，例如某个配置文件的路径以及java的一些路径配置什么的。
官方的配置文档：
https://www.elastic.co/guide/en/elasticsearch/reference/6.0/rpm.html

vim /etc/elasticsearch/elasticsearch.yml  # 增加或更改以下内容
cluster.name: master-node  # 集群的名称
node.name: master  # 该节点名称
node.master: true  # 意思是该节点为主节点
node.data: true  # 表示这是数据节点
network.host: 0.0.0.0  # 监听全部ip，在实际环境中应设置为一个安全的ip
http.port: 9200  # es服务的端口号
discovery.zen.ping.unicast.hosts: ["192.168.77.128", "192.168.77.130", "192.168.77.134"] # 配置自动发现


然后将配置文件发送到另外两台机器上去：
[root@master-node ~]# scp /etc/elasticsearch/elasticsearch.yml data-node1:/tmp/

到两台机器上去更改该文件，修改以下几处地方：

vim /tmp/elasticsearch.yml
node.name: data-node1
node.master: false
node.data: true

cp /tmp/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml



完成以上的配置之后，到主节点上，启动es服务：
主节点启动完成之后，再启动其他节点的es服务。

通过root用户启动elasticsearch并且在后台运行
./elasticsearch -Des.insecure.allow.root=true -d

vi /etc/security/limits.conf
es soft nofile 65536
es hard nofile 65536

vi /etc/sysctl.conf
vm.max_map_count=655360
sysctl -p

centos 6 配置
bootstrap.memory_lock: false
bootstrap.system_call_filter: false

vi /etc/security/limits.d/90-nproc.conf
* soft nproc 4096

elasticsearch-head
git clone git://github.com/mobz/elasticsearch-head.git
cd elasticsearch-head

# 安装依赖 指定淘宝的npm源加速
npm install --registry=https://registry.npm.taobao.org

npm install -g phantomjs-prebuilt --unsafe-perm

# 启动server
npm run start

http://localhost:9100

修改 Elasticsearch 配置文件 config/elasticsearch.yml 处理跨域问题
http.cors.enabled: true
http.cors.allow-origin: "*"


安装插件

bin/elasticsearch-plugin install http://101.132.78.223:8000/soft/elasticsearch-analysis-ik-6.6.1.zip
bin/elasticsearch-plugin install http://101.132.78.223:8000/soft/elasticsearch-analysis-pinyin-6.6.1.zip

--------------------------------------------------------------------------------

集群的健康检查：
 curl '172.16.4.18:9200/_cluster/health?pretty'

查看集群的详细信息：
curl '172.16.4.18:9200/_cluster/state?pretty'

安装kibana
注：由于kibana是使用node.js开发的，所以进程名称为node

./bin/kibana

然后在浏览器里进行访问，如：http://172.16.4.18:5601/ ，由于我们并没有安装x-pack，所以此时是没有用户名和密码的，可以直接访问的：

到此我们的kibana就安装完成了，很简单，接下来就是安装logstash，不然kibana是没法用的。


日志显示不全问题
在kibana的management=>advance setting里设置truncate:maxHeight为0

--------------------------------------------------------------------------------
安装logstash

安装完之后，先不要启动服务，先配置logstash收集syslog日志：
[root@data-node1 ~]# vim /etc/logstash/conf.d/syslog.conf  # 加入如下内容
input {  # 定义日志源
  syslog {
    type => "system-syslog"  # 定义类型
    port => 10514    # 定义监听端口
  }
}
output {  # 定义日志输出
  stdout {
    codec => rubydebug  # 将日志输出到当前的终端上显示
  }
}
检测配置文件是否有错：
 ./logstash --path.settings /etc/logstash/ -f /etc/logstash/conf.d/syslog.conf --config.test_and_exit
命令说明：
--path.settings 用于指定logstash的配置文件所在的目录
-f 指定需要被检测的配置文件的路径
--config.test_and_exit 指定检测完之后就退出，不然就会直接启动了
配置kibana服务器的ip以及配置的监听端口：

vim /etc/rsyslog.conf
#### RULES ####
*.* @@192.168.77.130:10514

重启rsyslog，让配置生效：
systemctl restart rsyslog

指定配置文件，启动logstash：
cd /usr/share/logstash/bin
./logstash --path.settings /etc/logstash/ -f /etc/logstash/conf.d/syslog.conf -t
./logstash --path.settings /etc/logstash/ -f /etc/logstash/conf.d/syslog.conf

--------------------------------------------------------------------------------
配置logstash
vim /data/logstash/conf.d/syslog.conf # 更改为如下内容
input {
  file {
        path => "/data/bts-dev/*/logs/*.log"    #这是日志文件的绝对路径
        start_position=>"beginning"    #这个表示从 messages 的第一行读取，即文件开始处
        sincedb_path => "/tmp/sincedb"
#        stat_interval => 5
#        delimiter => "\n"
        codec => multiline {
            pattern => "^\d{4}-\d{2}-\d{2}"
            negate => true
            what => "previous"
        }
  }
}
output {
  elasticsearch {
    hosts => ["http://172.16.4.18:9200/"]
    index => "all-log-%{+YYYY.MM.dd}"
    #user => "elastic"
    #password => "changeme"
  }
}
同样的需要检测配置文件有没有错：
./bin/logstash -f ./config/logstash-sample.conf -t
清除缓存数据库
rm /tmp/sincedb
nohup ./bin/logstash -f ./config/logstash-sample.conf & > /dev/null

完成了logstash服务器的搭建之后，回到kibana服务器上查看日志，执行以下命令可以获取索引信息：
[root@master-node ~]# curl '192.168.77.128:9200/_cat/indices?v'

获取指定索引详细信息：
[root@master-node ~]# curl -XGET '192.168.77.128:9200/system-syslog-2018.03?pretty'

如果日后需要删除索引的话，使用以下命令可以删除指定索引：
curl -XDELETE 'localhost:9200/system-syslog-2018.03'

--------------------------------------------------------------------------------
27.10 logstash收集nginx日志
和收集syslog一样，首先需要编辑配置文件，这一步在logstash服务器上完成：
[root@data-node1 ~]# vim /etc/logstash/conf.d/nginx.conf  # 增加如下内容
input {
  file {  # 指定一个文件作为输入源
    path => "/tmp/elk_access.log"  # 指定文件的路径
    start_position => "beginning"  # 指定何时开始收集
    type => "nginx"  # 定义日志类型，可自定义
  }
}
filter {  # 配置过滤器
    grok {
        match => { "message" => "%{IPORHOST:http_host} %{IPORHOST:clientip} - %{USERNAME:remote_user} \[%{HTTPDATE:timestamp}\] \"(?:%{WORD:http_verb} %{NOTSPACE:http_request}(?: HTTP/%{NUMBER:http_version})?|%{DATA:raw_http_request})\" %{NUMBER:response} (?:%{NUMBER:bytes_read}|-) %{QS:referrer} %{QS:agent} %{QS:xforwardedfor} %{NUMBER:request_time:float}"}  # 定义日志的输出格式
    }
    geoip {
        source => "clientip"
    }
}
output {
    stdout { codec => rubydebug }
    elasticsearch {
        hosts => ["192.168.77.128:9200"]
        index => "nginx-test-%{+YYYY.MM.dd}"
  }
}


以上这就是如何使用filebeat进行日志的数据收集，可以看到配置起来比logstash要简单，而且占用资源还少。

修改用户elastic的命名：

PUT /_xpack/security/user/elastic/_password
{
  "password" : "NewPassWord"
}

用户管理
角色：角色就是用户的标签，比如用户属于管理员、属于普通员工、或者公司A的用户、公司B的用户。

4.1 查看角色
GET /_xpack/security/role
返回结果：

4.2 新增用户
POST /_xpack/security/user/usera
{
  "password" : "123456abc",
  "roles" : [ "superuser", "ucas" ]
}
4.3 用户列表
列出所有用户：

GET /_xpack/security/user
结果：

查看某一用户：
GET /_xpack/security/user/usera

4.4 禁用用户
PUT /_xpack/security/user/elastic/_disable

4.5 启用用户
PUT /_xpack/security/user/elastic/_enable

4.5 删除用户
DELETE /_xpack/security/user/usera

查看索引
curl 'localhost:9200/_cat/indices?v'

删除索引
curl -XDELETE 172.19.18.227:9200/filebeat

用nginx 做 kibana  验证

filebeat 可以吧数据传给 redis 然后用Logstash 抽取


阿里云 es
head 设置
http://172.16.4.18:9100/?auth_user=elastic&auth_password=eF0GJidyemxoENHtJo

configure.yml
http:
  cors:
    enabled: 'true'
    allow-origin: '*'
    allow-headers: 'Authorization,X-Requested-With,Content-Length,Content-Type'
