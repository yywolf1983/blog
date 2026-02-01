1、安装好docker docker-compose

2、下载node 
wget https://github.com/prometheus/node_exporter/releases/download/v1.2.0/node_exporter-1.2.0.linux-amd64.tar.gz

3、启动node

hostgroup="lianghua"

#这里先要生成证书 参见 node_exporter 添加证书
ansible aws -m copy -a "src=/mnt/prometheus/ssl dest=/data/docker/ssl"

ansible ${hostgroup} -m shell -a "mkdir -p /data/docker/prometheus/"
ansible ${hostgroup} -m copy -a "src=node_exporter dest=/data/docker/prometheus/node_exporter"
ansible ${hostgroup} -m shell -a "chmod 755 /data/docker/prometheus/node_exporter"

ansible ${hostgroup} -m copy -a "src=node.yml dest=node.yml"

修改主机名
ansible ${hostgroup} -m copy -a "src=hostname.sh dest=hostname.sh"
ansible ${hostgroup} -m shell -a "bash hostname.sh"

ansible ${hostgroup} -m shell -a "docker-compose -f node.yml up -d"

http://47.108.235.230:9101/

4、启动prometheus
mkdir -p /data/docker/prometheus/prometheus
mkdir -p /data/docker/prometheus/grafana_data
mkdir -p /data/docker/prometheus/alertmanager
mkdir -p /data/docker/prometheus/alertmanager_data/templates
chown 1000.1000 /data/docker/prometheus/ -R

cp prometheus_config.yml /data/docker/prometheus/prometheus
cp alert.rules /data/docker/prometheus/prometheus

#要修改prometheus_config.yml 的报警配置
cp alertmanager_config.yml /data/docker/prometheus/alertmanager
cp wechat.tmpl /data/docker/prometheus/alertmanager_data/templates


prometheus 主要程序
docker-compose -f prometheus.yml up -d


http://47.108.235.230:9090/targets

5、设置grafana
http://47.108.235.230:3000
admin/admin

data source
http://localhost:9090
导入 dashboard

curl https://api.d7home.com/getip


## prometheus 集群模式（FEDERATION）

federate
scrape_configs:
  - job_name: 'federate'
    scrape_interval: 15s

    honor_labels: true
    metrics_path: '/federate'

    params:
      'match[]':
        - '{job="prometheus"}'
        - '{__name__=~"job:.*"}'

    static_configs:
      - targets:
        - 'source-prometheus-1:9090'
        - 'source-prometheus-2:9090'
        - 'source-prometheus-3:9090'


## node_exporter 添加证书

cadvisor 和 Blackbox 可以用反向代理做https

./cadvisor --http_auth_file test.htpasswd --http_auth_realm localhost

openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 -keyout prometheus.key -out prometheus.crt -subj "/C=CN/ST=Beijing/L=Beijing/O=*/CN=*" -addext "subjectAltName = DNS:prometheus"


htpasswd -nBC 12 '' | tr -d ':\n'

添加配置
echo > web.config.yml << EOF
tls_server_config:
  cert_file: /ssl/prometheus.crt
  key_file: /ssl/prometheus.key

basic_auth_users:
  prometheus: $2y$12$bmK43Gu7VYDfHwkQLwBlyO2cx/9XFlG4Pppro6NiVx7fwx5Wx4q6S%

EOF


ansible ${hostgroup} -m copy -a "src=ssl dest=/data/docker/ssl"
ansible ${hostgroup} -m copy -a "src=web.config.yml dest=/data/docker/ssl"