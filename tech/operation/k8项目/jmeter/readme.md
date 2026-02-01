influxdb:lstest

8086 
8083 WebUI

echo '等待10s'
sleep 10
echo '创建数据库jmeter'
curl -X POST 'http://influxdb.jmeter:8086/query?q=create+database+%22jmeter%22&db=_internal'
echo '创建数据库telegraf'
curl -X POST 'http://influxdb.jmeter:8086/query?q=create+database+%22telegraf%22&db=_internal'



https://github.com/Rbillon59/jmeter-k8s-starterkit

kubectl cp -n default  jmeter-master-z9hj9:/report/report-my-scenario.jmx-2022-04-08_103226 ./jmeter