apt install libssl-dev libncurses5-dev libsqlite3-dev libreadline-dev libtk libgdm-dev libdb4o-cil-dev libpcap-dev

安装python3

mkdir /data//data


cp contrib/systemd/electrumx.service /etc/systemd/system/

docker 安装

https://github.com/lukechilds/docker-electrumx.git

docker build -t electrumx .


docker run -d --net=host -v /data/back/btc/data/:/var/lib/electrumx -e DAEMON_URL="http://username:password@52.221.21.170:8332" -e REPORT_SERVICES=tcp://3.1.119.56:50001 -e COIN=BitcoinSegwit -e SERVICES=tcp://:50001,ssl://:50002 -e SSL_CERTFILE=server.crt SSL_KEYFILE=server.key -p 50002:50002 electrumx

openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr
openssl x509 -req -days 1825 -in server.csr -signkey server.key -out server.crt

curl --user username:password -H 'content-type:text/plain;' http://52.221.21.170:8332/ --data-binary '{"jsonrpc":"1.0","id":"1","method":"getblockhash","params":[1]}'

curl --user username:password -H 'content-type:text/plain;' http://127.0.0.1:8332/ --data-binary '{"jsonrpc":"1.0","id":"1","method":"getblockhash","params":[1]}'
