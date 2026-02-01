
vim server.properties
broker.id=0
log.dirs=/data/kafka-logs
zookeeper.connect=10.10.13.183:2181,10.10.13.184:2181,10.10.13.185:2181

host.name=10.10.13.183

添加启用删除topic配置

关闭自动创建topic
auto.create.topics.enable=false



首先要启动 zookeeper

启动kafka server
bin/kafka-server-start.sh -daemon config/server.properties &

停止kafka
bin/kafka-server-stop.sh

(非本地生产者和消费者访问Kafka，记得修改 config/server.properties中的listeners, 例如
listeners=PLAINTEXT://192.168.33.152:9092)

create a topic

bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

查看topic

bin/kafka-topics.sh --list --zookeeper localhost:2181

好像没有输出

启动生产者

bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
输入
This is a message
This is another message

启动消费者

bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
This is a message
This is another message
