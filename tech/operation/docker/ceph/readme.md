
## TODO

1. 各服务器主从手动切换

## 基础概念
PG 是指定存储池存储对象的目录有多少个，
PGP 是存储池 PG 的 OSD 分布组合个数。
PG 的增加会引起 PG 内的数据进行分裂，分裂到相同的 OSD 上新生成的 PG 当中。
PGP 的增加会引起部分 PG 的分布进行变化，但是不会引起 PG 内对象的变动。

## 基础命令
sudo seq 200 | xargs -i sudo dd if=/dev/zero of={}.dat bs=1M count=200

clush -b -w devops,arche-prod-end-01,arche-prod-end-02 "mkdir -p /mnt/ceph_data"

重新安装要清空缓存

列出存储池
ceph osd lspools 

建立存储池
ceph osd pool create pool-name

ceph osd pool delete
ceph osd pool get cephfs_data min_size 最小副本数量 size 副本数量
ceph osd pool rename

查看统计
rados df

设置配额
ceph osd pool set-quota data max_objects 10000

自动清理内存
ceph config set osd osd_memory_target_autotune true

用户管理
ceph auth list
ceph auth del 


启动test1
docker-compose up -d
要开通6789 端口

uuidgen 生成uuid

command="rm -rf /mnt/ceph_data/osd/*"

## 清理战场

ceph_host="devops,test,arche-prod-end-01,metates"
ansible -u root $ceph_host -m shell -a "docker-compose down"

command="rm -rf /data/cephfs/*"
ansible -u root $ceph_host -m shell -a "$command"

ansible -u root $ceph_host -m shell -a "docker-compose restart"

ssh -F /data/ubuntu/.ssh/config -i /data/ubuntu/.ssh/id_rsa root@arche-prod-end-01 

### 备份整个mon

scp -r /var/lib/ceph/mon/ceph-ceph-1/*  ceph-4:/var/lib/ceph/mon/ceph-ceph-4/
scp /etc/ceph/* ceph-4:/etc/ceph/

monmaptool --create --add devops 10.4.0.59 --fsid 6d3253f9-e70a-417e-9794-279f714eeaeb /tmp/monmap

ceph-mon -i ceph-4 --inject-monmap /tmp/monmap 
ceph-mon -i ceph-4

sudo -u ceph mkdir -p /var/lib/ceph/mon/ceph-devops
sudo -u ceph ceph-mon --mkfs -i devops --monmap /tmp/monmap --keyring /tmp/ceph.mon.keyring

chown -R ceph:ceph /var/lib/ceph/radosgw/
chown -R ceph:ceph /var/lib/ceph/mon/

## 一些基础命令
ceph osd tree
ceph osd dump 
ceph pg dump
ceph pg stat
ceph mon remove mon-id
ceph daemon osd.0 config show | less
ceph osd find osd.0
ceph osd metadata 0
ceph osd status
ceph osd perf

## osd 数据均衡分布：
ceph mgr module enable balancer
ceph balancer status
ceph balancer on
ceph balancer mode crush-compat
或者
ceph balancer mode upmap

## 查看迁移
ceph -w


## 修改权重重新分配
ceph osd df
ceph osd crush reweight osd.3 1.1

## 驱逐
ceph osd out $id
## 加入
ceph osd in $id

## 删除 osd
id=0
ceph osd stop $id
ceph osd rm $id
ceph auth del osd.$id
ceph osd crush remove osd.$id

eph osd getcrushmap -o crm
crushtool -d crm -o crm.d
ceph osd crush remove osd.1

## 1.安装 mon ********
ceph_host="test,arche-prod-end-01,devops,metates"
ansible -u root $ceph_host -m copy -a "src=ceph.yml dest=~/"

ceph_host="test"
command="docker-compose -f ceph.yml up -d ceph-mon"
ansible -u root $ceph_host -m shell -a "$command"

ceph -s

sudo vi /etc/ceph/ceph.conf
mon initial members = test,arche-prod-end-01,arche-prod-end-02
mon host = 10.4.0.83,10.4.0.231,10.4.0.183
...
//180*1024*1024*1024 = 180G
bluestore_block_size = 193273528320
osd max object name len = 256
osd max object namespace len = 64 
auth_allow_insecure_global_id_reclaim = false

禁止安全提示
ceph config set mon auth_allow_insecure_global_id_reclaim false

ceph_host="test"
ansible -u root $ceph_host -m shell -a "docker-compose restart"

rsync -avz --delete test:/data/cephfs/etc/ ./ceph/
ceph_host="metates,test,arche-prod-end-01,devops"
ansible -u root $ceph_host -m copy -a "src=ceph/ dest=/data/cephfs/etc/ owner=167 group=167"
ansible -u root $ceph_host -m shell -a "cat /data/cephfs/etc/ceph.conf"

ceph_host="arche-prod-end-01,arche-prod-end-02"
command="docker-compose -f ceph.yml up -d ceph-mon"
ansible -u root $ceph_host -m shell -a "$command"

sudo docker exec -it ceph-mon bash

## 2. 安装 mgr ********

ceph_host="test,arche-prod-end-01,devops,metates"
ansible -u root $ceph_host -m shell -a " docker-compose -f docker-compose.yml up -d ceph-mgr"

ceph mgr module ls
ceph mon enable-msgr2
ceph auth list

### 切换主从

ceph mgr fail node1

## 3. 安装 osd********

ceph_host="test,arche-prod-end-01,arche-prod-end-02"
ansible -u root $ceph_host -m shell -a "docker-compose -f docker-compose.yml up -d ceph-osd"

### 挂载设置
ceph osd pool create cephfs_data
ceph osd pool create cephfs_metadata
ceph osd pool ls
ceph osd pool set cephfs_data pg_num 64
ceph osd pool set cephfs_data pgp_num 64
mon_osd_max_split_count

### 查看 auth 信息

ceph auth list

vi  /var/lib/ceph/bootstrap-osd/ceph.keyring
vi ceph.keyring
[client.bootstrap-osd]
        key = AQAijVZi83P/GxAAdSOjzpVIkDTviWL8QWnTfA==
        caps mgr = "allow r"
        caps mon = "profile bootstrap-osd"

ceph daemon osd.0 config show | grep osd_journal

ceph-bluestore-tool show-label --path /var/lib/ceph/osd/ceph-1 | grep osd.stat_bytes
ceph-bluestore-tool set-label-key --dev /var/lib/ceph/osd/ceph-1/block --key 5 --value 4000780910592

ceph osd  metadata 0

blockdev --getsize64 /var/lib/ceph/osd/ceph-1/block

sudo rm -rf bootstrap-osd/
rsync -avz --delete test:/mnt/ceph_data/bootstrap-osd ./
sudo chown ubuntu.ubuntu bootstrap-osd  -R
ceph_host="metates,test,arche-prod-end-01,devops"
ansible -u root $ceph_host -m copy -a "src=bootstrap-osd/ceph.keyring dest=/data/cephfs/bootstrap-osd/ceph.keyring owner=167 group=167 mode=600"

ansible -u root $ceph_host -m shell -a "docker-compose restart"

## 4. 安装 mds********

ceph_host="test,arche-prod-end-01,arche-prod-end-02"
ansible -u root $ceph_host -m shell -a "docker-compose -f docker-compose.yml up -d ceph-mds"

## 附： 启动 dashboard
ceph mgr dump
ceph mgr module enable dashboard
ceph mgr module disable dashboard

ceph mgr module ls

ceph dashboard create-self-signed-cert
ceph config set mgr mgr/dashboard/ssl false
ceph config set mgr mgr/dashboard/server_addr test //迁移到其他节点
ceph config set mgr mgr/dashboard/server_port 8443

ceph mgr services #service url check
ceph dashboard ac-user-delete 

ceph dashboard ac-user-create admin -i admin.txt administrator


## 附： 物理挂载

```
获取密钥
ceph-authtool --print-key /etc/ceph/ceph.client.admin.keyring

挂载目录
sudo mount -t ceph 10.4.0.143:6789,10.4.0.231:6789,10.4.0.183:6789:/ /data/soft -o name=admin,secret=AQAgjVZiWor5NhAALgYANZs6/iy43Pe9VvKDIQ==



# 卸载目录
umount cephfs
```

## 附：add mon node

sudo vi /etc/ceph/ceph.conf

### 方法1

mkdir /var/lib/ceph/mon/ceph-admin
ceph auth list
ceph auth get mon. -o /tmp/keyring
ceph mon getmap -o /tmp/mapfile 
ceph-mon -i ceph1 --mkfs --monmap /tmp/mapfile --keyring /tmp/keyring
ceph-mon -i ceph1 --public-addr 10.4.0.231:6789  

ceph mon dump
ceph health

### 方法2

备份配置
ceph mon getmap -o /tmp/changemon
查看备份
monmaptool --print /tmp/changemon

删除mon
monmaptool --rm ns-ceph-208214 --rm ns-ceph-208215 --rm ns-ceph-208216 /tmp/changemon

添加mon
monmaptool --add arche-prod-end-02 10.4.0.183:6789  /tmp/changemon

ansible -u root $ceph_host -m copy -a "src=/mnt/ceph_data/changemon dest=/mnt/ceph_data/changemon owner=167 group=167"

倒入
ceph-mon -i devops --mkfs
ceph-mon -i arche-prod-end-01 --inject-monmap /var/lib/ceph/changemon

ansible -u root $ceph_host -m shell -a "ls -l /mnt/ceph_data/mon"

ansible -u root $ceph_host -m shell -a "chown 167.167 -R /mnt/ceph_data/mon/ceph*/store.db"



## 附： 密钥创建

```text
ceph  auth get-or-create mgr.ceph-1 mon 'allow profile mgr' osd 'allow *' mds 'allow *'  -o /var/lib/ceph/mgr/ceph-ceph-1/keyring

为您的集群创建一个密钥环并生成一个监控密钥。
ceph-authtool --create-keyring /etc/ceph/ceph.mon.keyring --gen-key -n mon. --cap mon 'allow *'

生成管理员密钥环，生成client.admin用户并将用户添加到密钥环。
ceph-authtool --create-keyring /etc/ceph/ceph.client.admin.keyring --gen-key -n client.admin --cap mon 'allow *' --cap osd 'allow *' --cap mds 'allow *' --cap mgr 'allow *'

生成 bootstrap-osd 密钥环，生成client.bootstrap-osd用户并将用户添加到密钥环。
ceph-authtool --create-keyring /var/lib/ceph/bootstrap-osd/ceph.keyring --gen-key -n client.bootstrap-osd --cap mon 'profile bootstrap-osd' --cap mgr 'allow r'

将生成的密钥添加到ceph.mon.keyring
ceph-authtool /etc/ceph/ceph.mon.keyring --import-keyring /etc/ceph/ceph.client.admin.keyring
ceph-authtool /etc/ceph/ceph.mon.keyring --import-keyring /var/lib/ceph/bootstrap-osd/ceph.keyring

ceph-authtool /etc/ceph/ceph.client.admin.keyring --import-keyring /var/lib/ceph/bootstrap-osd/ceph.keyring


更改所有者ceph.mon.keyring。
sudo chown ceph:ceph /etc/ceph/ceph.mon.keyring
```


## 开启监控

ceph mgr module enable prometheus

```yml
global:
    scrape_interval: 5s

scrape_configs:
    - job_name: 'prometheus'
    static_configs:
        - targets: ['localhost:9090']
    - job_name: 'ceph'
    static_configs:
        - targets: ['localhost:9283']
    - job_name: 'node-exporter'
    static_configs:
        - targets: ['localhost:9100']
```

## 意外卸载解决办法

dmesg|grep error

modinfo ceph

## osd 问题处理

### 清理磁盘

ceph-volume lvm zap /dev/nvme2n1 --destroy

parted /dev/nvme1n1 mklabel gpt



## 初始化设备

### 创建虚拟磁盘
dd if=/dev/zeroof=/var/loop.img bs=1M count=10240
### 寻找空闲设备
losetup -f

### 挂载设备
losetup /dev/loop10 /data/cephfs/osd/ceph-2/block 

mkfs -t xfs /dev/loop4 
### 创建逻辑设备
pvcreate /dev/loop4
vgcreate cephvg /dev/loop4
lvcreate --name cephlv -l 100%FREE cephvg

### 检查LVM创建状态
lvs
vgs
pvs

### 卸载设备
losetup -d /dev/loop4
lsblk
### 开机自动挂载
grep cephvg /etc/rc.d/bkrc.local || echo "losetup -f $CEPH_DISK_FILE && vgchange -a y cephvg " >> /etc/rc.d/bkrc.local



## 设置磁盘剩余报警
ceph config get mon mon_data_avail_warn
ceph config get mon mon_data_avail_crit

ceph config set mon mon_data_avail_warn 10

ceph config get mon mon_data_size_warn
ceph config set global mon_data_size_warn 2147483648

ceph config set mon mon_data_avail_crit 1




aws elasticache modify-replication-group \
--replication-group-id ap-southeast-1 \
--auth-token FA9yRd3RWbQMQFU8 \
--auth-token-update-strategy SET \
--apply-immediately


## 可以用prometheus 监控
ceph mgr module enable prometheus


echo "AQDK2iViy85LEhAATM4/esmMnBKMmmHDmQ89rw==" | base64


ceph-secret.yaml

---

apiVersion: v1
kind: Secret
metadata:
  name: ceph-secret
  namespace: cephfs
data:
  key: QVFESzJpVml5ODVMRWhBQVRNNC9lc21NbkJLTW1tSERtUTg5cnc9PQ==

---

apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: cephfs-dev
  namespace: cephfs
provisioner: ceph.com/cephfs
parameters:
  monitors: 54.169.81.249:6789,54.255.209.0:6789,13.215.1.110:6789
  adminId: admin
  adminSecretName: ceph-secret
  adminSecretNamespace: cephfs
  claimRoot: /volumes/kubernetes/dev