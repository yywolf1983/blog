
# mydumper

## 安装

yum install -y glib2 glib2-devel zlib-devel cmake git gcc gcc-c++

https://github.com/maxbube/mydumper

git clone https://github.com/maxbube/mydumper.git

export PATH=/data/mysql-8.0.22/bin:$PATH

cmake .
make

## 备份

./mydumper -u root -p AnvcTMagdLarwNV3CKaC -h 192.168.15.229 -P 2378 -c -t 10 -o /data/back/test/

  -B, --database              需要备份的数据库，一个数据库一条命令备份，要不就是备份所有数据库，包括mysql。
  -T, --tables-list           需要备份的表，用逗号分隔。
  -o, --outputdir             备份文件目录
  -s, --statement-size        生成插入语句的字节数
  -c, --compress              压缩输出文件
  -t, --threads               备份执行的线程数,默认4个线程
  -b, --binlogs               导出binlog
  -r, --rows                  分裂成很多行块表,表示每个线程用300000行块来分割表
  -l, --long-query-guard      设置长查询时间,默认60秒，超过该时间则会报错：There are queries in PROCESSLIST running longer than 60s, aborting dump

## 还原
./myloader  -u root -p AnvcTMagdLarwNV3CKaC -h 127.0.0.1 -P 2378 -C -t 10  -o -d /data/back/test/

  -d, --directory                   备份文件所在的目录
  -o, --overwrite-tables            如果表存在则先删除，使用该参数，需要备份时候要备份表结构，不然还原会找不到表
  -s, --source-db                   还原的数据库
  -t, --threads                     使用的线程数量，默认4
  -C, --compress-protocol           连接上使用压缩协议