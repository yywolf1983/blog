
# base java

## 基础设置

### linux

```txt
vi /etc/profile
在最后加入以下几行：
export JAVA_HOME=/usr/lib/jvm/java-openjdk
export JAVA_HOME=/data/soft/jdk-16.0.2
export CLASSPATH=$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/jre/lib/rt.jar
export PATH=$JAVA_HOME/bin:$PATH
```

### windows

```txt
JAVA_HOME=F:\download\jdk-11.0.14
CLASSPATH=.;%JAVA_HOME%/lib/dt.jar;%JAVA_HOME%/lib/tools.jar;%CATALINA_HOME%/lib/servlet-api.jar
PATH=%JAVA_HOME%/bin;$PATH
TOMCAT_HOME=/usr/local/tomcat
```

```txt
java -version
```
