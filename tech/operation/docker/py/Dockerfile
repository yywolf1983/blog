FROM python:3.7

RUN echo export LANGUAGE=en_US.UTF-8 >> /etc/profile
RUN echo export LANG=en_US.UTF-8>> /etc/profile

RUN echo export LC_ALL=C.UTF-8 >> /etc/profile
RUN echo export LANG=C.UTF-8 >> /etc/profile

RUN echo source /etc/profile >> ~/.bashrc

ADD ./get-pip.py ./
RUN python -m pip install --upgrade pip

WORKDIR /root/.pip/

# COPY ./pip.conf ./
ADD ./pip.conf ./
WORKDIR /data/py

COPY requirements.txt ./
# mysql 的依赖
RUN pip3 install -r requirements.txt

