FROM centos
MAINTAINER yywolf <yywolf1983>
RUN source /myenv/bin/activate
ADD pip.txt pip.txt
RUN yum -y install python-devel sqlite-devel openssl-devel curl-devel
RUN pip install -U pip.txt
