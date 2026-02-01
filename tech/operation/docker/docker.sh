if [ ! -n "$1" ] ;then
    echo "you have not input a word!"
    #exit
else
    echo "the word you input is $1"
fi

USER_NAME=test
MYSQL_PORT=192.168.2.25:3307
TOMCAT_PORT=192.168.2.25:8080


cat << EOF > Dockerfile
FROM base_mysql
MAINTAINER yywolf <yywolf1983>
ENV JAVA_HOME=/data/jdk1.8.0
ENV CLASSPATH=\${JAVA_HOME}/lib/dt.jar:\${JAVA_HOME}/lib/tools.jar:\${JAVA_HOME}/jre/lib/rt.jar
ENV PATH=\$PATH:\${JAVA_HOME}/bin:/data/mysql/bin/
EXPOSE 80 3306
RUN echo 'root:123456' | chpasswd
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

ENV USER_NAME=yywolf
RUN mkdir -p /data/tools/\${USER_NAME}/data
RUN mv /data/mysql/data /data/mysql_data.back
RUN ln -s /data/tools/\${USER_NAME}/data /data/mysql/data
RUN rm -rf /data/tomcat-6.0/webapps/
RUN mkdir -p /data/tools/\${USER_NAME}/web
RUN ln -s /data/tools/\${USER_NAME}/web /data/tomcat-6.0/webapps

RUN cp /data/supervisord.conf /etc/supervisord.conf
ENTRYPOINT ["/usr/bin/supervisord"]
EOF

sed -i "/USER_NAME/s/\=.*/\=${USER_NAME}/" Dockerfile

cat Dockerfile
echo "build "${USER_NAME}" Dockerfile"
docker build -t ${USER_NAME} .
echo "run docker"
docker run --name ${USER_NAME} -v /docker_data:/data/tools/:rw -p ${TOMCAT_PORT}:80 -p ${MYSQL_PORT}:3306 -d -t ${USER_NAME}
echo "tomcat dir create"
docker exec -i -t ${USER_NAME} mkdir -p /data/tools/${USER_NAME}/web
echo "mysql data re"
docker exec -i -t ${USER_NAME} mv /data/mysql_data.back /data/tools/${USER_NAME}/data


rm -f Dockerfile
