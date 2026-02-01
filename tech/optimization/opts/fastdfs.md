https://github.com/happyfish100/fastdfs

export DESTDIR=/data/fastdfs
./make.sh
./make.sh install

/data/fastdfs/etc/fdfs
cd /fs-src_dir/conf/
cp client.conf http.conf mime.types storage.conf tracker.conf /data/fastdfs/etc/fdfs

vim /data/fastdfs/etc/fdfs/tracker.conf
 http.server_port=8080
 port=22122
 base_path=/data/fs_data
# 0: round robin    轮询
# 1: specify group 指定组
# 2: load balance, select the max free space group to upload file  自动负载
store_lookup=2

mkdir -p /data/fs_data

启动tracker
/data/fastdfs/usr/bin/fdfs_trackerd /data/fastdfs/etc/fdfs/tracker.conf  restart

tail -f /data/fs_data/logs/trackerd.log

客户端设置
vi /data/fastdfs/etc/fdfs/client.conf
base_path=/data/fs_data
tracker_server=127.0.0.1:22122  可以有多个

/data/fastdfs/usr/bin/fdfs_monitor  /data/fastdfs/etc/fdfs/client.conf


#storage ----------------------------
vim /data/fastdfs/etc/fdfs/storage.conf
group_name=group1  (组名)
base_path=/data/fs_data (基础目录)
store_path0=/data/fs_data/fdfs_storage (存储目录)
tracker_server=172.27.0.5:22122 (tracker服务器 不能使用内网)  

mkdir -p /data/fs_data/fdfs_storage

/data/fastdfs/usr/bin/fdfs_storaged  /data/fastdfs/etc/fdfs/storage.conf restart

tail -f /data/fs_data/logs/storaged.log

/data/fastdfs/usr/bin/fdfs_monitor  /data/fastdfs/etc/fdfs/storage.conf


/data/fastdfs/usr/bin/fdfs_test   /data/fastdfs/etc/fdfs/client.conf   upload   上传文件

/data/fastdfs/usr/bin/fdfs_upload_file   /data/fastdfs/etc/fdfs/client.conf   上传文件


如果FastDFS定义store_path1，这里就是M01

# FDFS_STORAGE_STATUS：INIT      :初始化，尚未得到同步已有数据的源服务器
# FDFS_STORAGE_STATUS：WAIT_SYNC :等待同步，已得到同步已有数据的源服务器
# FDFS_STORAGE_STATUS：SYNCING   :同步中
# FDFS_STORAGE_STATUS：DELETED   :已删除，该服务器从本组中摘除
# FDFS_STORAGE_STATUS：OFFLINE   :离线
# FDFS_STORAGE_STATUS：ONLINE    :在线，尚不能提供服务
# FDFS_STORAGE_STATUS：ACTIVE    :在线，可以提供服务

删除节点
/data/fastdfs/usr/bin/fdfs_monitor  /data/fastdfs/etc/fdfs/client.conf delete group1 134.175.30.158


方式一
将 /group1/M00 映射到/data/fs_data/fdfs_storage/data
location /group1/M00 {
    alias /data/fs_data/fdfs_storage/data;
}

方式二
nginx 模块
https://github.com/happyfish100/fastdfs-nginx-module
https://github.com/happyfish100/libfastcommon

./configure --prefix=/data/nginx --add-module=../fastdfs-nginx-module-master/src

编译出错 要修改 fastdfs-nginx-module-master/src/config
ngx_module_incs="/data/fastdfs/usr/include/ /data/libfastcommon-master"

cp ../fastdfs-nginx-module-master/src/mod_fastdfs.conf /data/fastdfs/etc/fdfs/

vi /data/fastdfs/etc/fdfs/mod_fastdfs.conf
base_path=/data/fs_data
tracker_server=127.0.0.1:22122
url_have_group_name = true
store_path0=/data/fs_data/fdfs_storage

 curl http://127.0.0.1/group1/M00/00/00/rBsABVvB4nOALlipAAAMKcM_VHk9160.sh
vi nginx.conf
location /group1/M00/
{
ngx_fastdfs_module;
}
