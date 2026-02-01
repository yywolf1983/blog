hadoop
	hdfs
		NameNode
			JobTracker
		DataNode
			TaskTracker
	MapRedue
	HBase（k/v）
		bigtable
		Hmastar
			RegionServer
	yarn
		ResourceManager（RM）
			RM是一个全局的资源管理器，负责整个系统的资源管理和分配。
		ApplicationMaster（AM）
			用户提交的每个应用程序均包含一个AM
		NodeManager（NM）
			NM是每个节点上的资源和任务管理器
	SPark
		MEM MapReduce
	zookeeper
		分布式应用程序协调服务
	Hive
		将SQL 查询转换为MapReduce 的job 在Hadoop集群上执行
		Hive Server
			元数据存储（Metastore）
	impala
		StateStore
			Impalad
	LdapServer


MapReduce 分布式数据处理模型环境
HDFS 分布式文件系统
Pig 运行在MapReduce和HDFS上的大数据检索环境
Hive 基于SQL的HDFS查询引擎，运行时被引擎翻译为MapReduce作业
HBase 使用HDFS作为底层存储，支持MapReduce计算查询
ZooKeeper 分布式高可用协调服务。
Sqoop 在数据库和HDFS之间传输数据
HDFS
    1、不适合用在低延时的访问数据上
    2、由于将文件系统的元数据存放在内存上，受限于namenode的内存容量，
    不适合存放大量的小文件
    3、不支持文件任意修改

    HDFS可以在多个文件系统上保存元数据，将持久写入本地磁盘时也写入远程文件系统.

    HAR hadoop 存盘文件

    在32位机器上有3G内存限制

    尽量考虑 nomenode 和 jobtracker 不要再同一机器上构建。


节点热备方案AvatarNode
NFS 保存节点方案 RAID5

安装 Hadoop
    安装jdk

    配置文件列表
        hadoop-env.sh 记录环境变量
        core-site.xml 常用IO设置等核心配置
        hdfs-site.xml Hadoop守护进程配置，辅助namenode和datanode等
        mapred-site.xml MapReduce守护进程配置，包括jobtracker和tasktracker
        masters namenode机器列表
        slaves datanode和tasktacker机器列表
        log4j.properties 系统日志文件配置
