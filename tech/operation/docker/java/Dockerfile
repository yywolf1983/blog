FROM openjdk:8-alpine
ENV LANG=zh_CN.UTF-8 \
    LC_ALL=zh_CN.UTF-8 \
    TZ=Asia/Shanghai
ADD *.jar /app.jar
CMD java ${JAVA_OPTS} -XX:AutoBoxCacheMax=20000 -jar /app.jar