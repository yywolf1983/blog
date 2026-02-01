1、修改kibana 配置

elasticsearch.hosts: [ "http://47.108.235.230:9200" ]
#
elasticsearch.username: elastic
elasticsearch.password: elastic
## 将Kinbana 界面设置成中文 如果习惯英文可以删除此配置默认是英文配置
i18n.locale: "zh-CN"


2、修改 docker-compose.yml 里面的 elastic 密码
ELASTIC_PASSWORD: elastic


3、修改 Logstash 配置
xpack.monitoring.elasticsearch.hosts: [ "http://172.30.214.140:9200" ]

## X-Pack security credentials
#
xpack.monitoring.enabled: true
xpack.monitoring.elasticsearch.username: elastic
xpack.monitoring.elasticsearch.password: elastic


4、添加Logstash日志抽取配置
input {
	beats {
		port => 5044
	}

	tcp {
		port => 5000
		type => "applog"
    codec => json_lines
	}
  file {
    path => "/log/messages" #注意这里如果是docker启动要做映射
    type => "system"
    start_position => "beginning"
  }
}

## Add your filters / logstash plugins configuration here

output {
  if [type] == "applog"{
      elasticsearch {
        hosts => "47.108.235.230:9200"
        user => "elastic"
        password => "elastic"
        ecs_compatibility => disabled
            index => "%{[appName]}-%{+YYYY.MM.dd}"
      }
        stdout { codec => rubydebug }
  }
  if [type] == "system"{
        elasticsearch {
           hosts => "47.108.235.230:9200"
           user => "elastic"
           password => "elastic"
           index => "systemlog-%{+YYYY.MM.dd}"
        }
        stdout { codec => rubydebug }
    }
}
