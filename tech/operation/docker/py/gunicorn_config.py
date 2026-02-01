# -*- coding: utf-8 -*-
#
# @Author: yy <yy>
# @Date:   2017-03-21
# @Email:  yywolf1983@gmail.com
# @Filename: gunicorn_config.py
# @Last modified by:   yy
# @Last modified time: 2017-05-08

import multiprocessing

import os
import sys

#处理项目路径
file_list_path = os.path.abspath(__file__).split("/")
fun_path =  "/".join(file_list_path)+"/"

NONES_PATH = "/data/py/flask_project_martin_3_duichong"

bind = '0.0.0.0:8095'
workers = multiprocessing.cpu_count() * 1 + 1
#worker_class = 'gevent' #这里可以使用 gevent,rync 等
worker_connections = 200
graceful_timeout = 30
timeout = 600
keepalive = 2
daemon = False
chdir = NONES_PATH
backlog = 1024
reload = True

errorlog = NONES_PATH+'/logs/gunicorn.error.log'
loglevel = 'info'
accesslog = NONES_PATH+'/logs/gunicorn.access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'


#gunicorn -c gunicorn_config.py mysite.wsgi:application

#Flask run:app
#app = Flask(__name__)
