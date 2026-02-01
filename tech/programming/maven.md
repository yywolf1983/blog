maven

export M2_HOME=/Users/yy/Downloads/apache-maven-3.5.0
export M2=$M2_HOME/bin
export MAVEN_OPTS="-Xms256m -Xmx512m"
export PATH=$M2:$PATH

修改nexus3的运行用户为root
[root@localhost ~]# vim bin/nexus.rc
里面内容修改为：run_as_user="root"

NEXUS OSS [ OSS = Open Source Software，开源软件——免费]
NEXUS PROFESSIONAL -FREE TRIAL [ 专业版本——免费体验－－收费]。

pom.xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
   http://maven.apache.org/xsd/maven-4.0.0.xsd">
   <modelVersion>4.0.0</modelVersion>

   <groupId>com.companyname.project-group</groupId>
   <artifactId>project</artifactId>
   <version>1.0</version>

</project>



在maven的settings.xml 文件里配置mirrors的子节点，添加如下mirror
    <mirror>
        <id>nexus-aliyun</id>
        <mirrorOf>*</mirrorOf>
        <name>Nexus aliyun</name>
        <url>http://maven.aliyun.com/nexus/content/groups/public</url>
    </mirror>

<localRepository>/Users/yy/Downloads/mvn/.m2</localRepository>


基础
mvn help:system

清理
mvn post-clean

编译
mvn compile

构建包
mvn package
mvn test
mvn clean


Maven执行install时GPG Passphrase的解决办法
mvn install -Dgpg.skip

mvn jetty:run

生成 eclipse 项目
 mvn eclipse:eclipse

本地库搭建
下载Nexus Repository OSS
下载地址： http://www.sonatype.com/download-oss-sonatype
默认账号admin，密码admin123

./nexus run   控制台启动
./nesus start 后台启动
在ubuntu打开浏览器，输入http://localhost:8081/

设为服务
NEXUS_HOME="/home/{user}/nexus-3.0.1-01"
bin/nexus.rc
run_as_user="nexus"
ln -s $NEXUS_HOME/bin/nexus /etc/init.d/nexus
cd /etc/init.d
update-rc.d nexus defaults
service nexus start

pom 中 设置私仓
<repositories>  
      <!-- 配置nexus远程仓库 -->  
      <repository>  
         <id>nexus</id>  
         <name>Nexus Snapshot Repository</name>  
         <url>http://127.0.0.1:8088/nexus/content/groups/public/</url>  
         <releases>  
            <enabled>true</enabled>  
         </releases>  
         <snapshots>  
           <enabled>false</enabled>  
         </snapshots>  
      </repository>  
   </repositories>  
   <!-- 配置从哪个仓库中下载构件，即jar包 -->  
   <pluginRepositories>  
       <pluginRepository>  
         <id>nexus</id>  
         <name>Nexus Snapshot Repository</name>  
         <url>http://127.0.0.1:8088/nexus/content/groups/public/</url>  
         <releases>  
           <enabled>true</enabled>  
         </releases>  
         <snapshots>  
           <enabled>false</enabled>  
         </snapshots>  
      </pluginRepository>  
    </pluginRepositories>  



版本设置相关
你可以在pom.xml中加入下面的东西即可
<properties>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
</properties>
或者你直接在pom.xml中配置Maven的编译插件也是可以的，类似下面这样<build>
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.7.0</version>
    <configuration>
       <source>1.8</source>
       <target>1.8</target>
    </configuration>
</plugin>

mav war包插件
<plugin>
<groupId>org.apache.maven.plugins</groupId>
<artifactId>maven-war-plugin</artifactId>
<version>3.2.0</version>
</plugin>



settings.xml
<!-- 私仓 -->
<mirror>
        <id>nexus-aliyun</id>
        <mirrorOf>central</mirrorOf>
        <name>Nexus aliyun</name>
        <url>http://maven.aliyun.com/nexus/content/groups/public</url>
</mirror>

<!--   私库设置   -->
<server>
        <id>sinafenqi-release</id>
        <username>admin</username>
        <password>admin123</password>
    </server>
    <server>
        <id>sinafenqi-snapshots</id>
        <username>admin</username>
        <password>admin123</password>
    </server>


<profiles>
    <profile>
        <id>nexu</id>
        <repositories>
            <repository>
                <id>sinafenqi-release</id>
                <name>sinafenqi-release</name>
                <snapshots>
                    <enabled>false</enabled>
                </snapshots>
                <releases>
                    <enabled>true</enabled>
                </releases>
                <url>http://47.96.164.18:8081/repository/maven-releases</url>
            </repository>
            <repository>
                <id>sinafenqi-snapshots</id>
                <name>sinafenqi-snapshots</name>
                <url>http://47.96.164.18:8081/repository/maven-snapshots</url>
                 <snapshots>
                    <enabled>true</enabled>
                </snapshots>
                <releases>
                    <enabled>false</enabled>
                </releases>
            </repository>
        </repositories>
    </profile>
</profiles>



## nexus3.yml

version: '3'
services:
  nexus3:
    image: sonatype/nexus3
    container_name: nexus3
    restart: always
    ports:
      - 8081:8081
    volumes:
      - /data/docker/nexus-data:/nexus-data

cat /data/docker/nexus-data/admin.password

sudo chown -R 200 /data/docker/nexus-data/
