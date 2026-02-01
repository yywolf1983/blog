# python

## 自定义包路径

    lib/site-packages
    mypath.pth
    d:\\pypage
        Python setup.py install --install-script= d:\\pypage  --prefix= d:\\pypage
        set PYTHONPATH= d:\\pypage\lib\site-packages
  
sys.path.append("filepath")

## 其他技巧

    python -m turtle
    python2 -m SimpleHTTPServer
    python3 -m http.server
    字符串操作
        'a {a},{0}'.format("1",a="10")
    python -m py_compile file.py
    python -O -m py_compile file.py 优化编译

    print timeit.timeit("test1()", setup="from main import test1", number=2000)

## pdb

``` py
#coding:utf-8

if __name__ == "__main__":
    a = 1
    import pdb
    pdb.set_trace()
    b = 2
    c = a + b
    print (c)
``` 

```text
python -m pdb xxxx.py

###################################
# p 打印变量
# bt  当前行
# b  行断点 直接查看断点
# cl 清除断点
# tbreak 临时断点
# disable 禁用断点
# enable  激活断点
# n  下一行
# c   执行到断点
# d  下移一层
# s  执行当前 进入函数
# w  列出所在曾
# u  上移一层
# c  执行到下一个断点
# j  跳转
# l  列出文件位置
# a  列出参数
```


## 基础语法

### 类的专有方法

    __init__  构造函数，在生成对象时调用
    __del__   析构函数，释放对象时使用
    __repr__ 打印，转换
    __setitem__按照索引赋值
    __getitem__按照索引获取值
    __len__获得长度
    __cmp__比较运算
    __call__函数调用

### 字符串操作

    'a {a},{0}'.format("1",a="10")

### 内嵌函数

    闭包
    def funX(a):
        def funY(b):
            return x+y
        return funY

    调用
    funX(1)(2)
    结果
    3

### lambda

    lambda x: x
    冒号前面是参数 冒号后面是返回值

### pickle 永久存储

    import pickle
    file = open(file,'wb')
    my_list = []
    #写入
    pickle.dump(my_list, file)
    file.close()

    #读取
    file = open(file,'rb')
    my_list = pickle.load(file)
    file.close()

### 生成器

    yield

    def gen():
        yield 1
        yield 2

    next(gen)
    next(gen)
    或
    for i in gen():
        print(i)

    a = {i:i % 2 == 0 for i in range(10) }

## 安装基础库

```text
set PYTHONPATH= d:\\pypage\lib\site-packages
Python setup.py install --install-script= d:\\pypage  --prefix= d:\\pypage
pip install -r test.txt
```

# 编译安装python

    yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel libffi-devel readline-devel tk-devel gcc

    #升级gcc到8
    yum -y install centos-release-scl
    yum -y install devtoolset-8-gcc devtoolset-8-gcc-c++ devtoolset-8-binutils
    scl enable devtoolset-8 bash

    ./configure --enable-optimizations --prefix=/data/python3

    #升级sqlite3
    LD_RUN_PATH=/usr/local/lib ./configure --enable-optimizations LDFLAGS="-L/usr/local/lib" CPPFLAGS="-I/usr/local/include" --prefix=/data/python3
    LD_RUN_PATH=/usr/local/lib make

    make
    make install


    /System/Library/Frameworks/Python.framework/Versions/

## 设置 pip
    mkdir -p ~/.pip

    windwos
    %appdata%/pip/pip.ini

    vi ~/.pip/pip.conf
    [global]
    index-url = https://mirrors.aliyun.com/pypi/simple/

    [install]
    trusted-host=mirrors.aliyun.com

    升级所有

    pip list | awk '{print $1}' | awk 'NR>2' | xargs pip install --upgrade

## 设置虚拟环境


    python3 -m venv /data/mypy

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
    python3 -m pip install --upgrade pip

    alias mypy='source /data/mypy/bin/activate'

    这样就可以打包了
    export PYTHONHOME=/data/mypy

    升级环境
    python3 -m venv /data/mypy

    pip install bottle -i http://mirrors.aliyun.com/pypi/simple/

    阿里云 http://mirrors.aliyun.com/pypi/simple/
    中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
    豆瓣(douban) http://pypi.douban.com/simple/
    清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
    中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

## mac 卸载 python

    sudo rm -rf /Library/Frameworks/Python.framework/Versions/2.7
    sudo rm -rf "/Applications/Python 2.7"
    ls -l /usr/local/bin | grep '/Library/Frameworks/Python.framework/Versions/2.7'  

## modules
    
    dir 查看模块内所有函数
    
    jupyter-lab
        jupyter notebook
        jupyter lab
    ctypes
        C语言接口
    base64
    django
    gevent
    HTMLParser
    logging
    pycurl
    pyinstaller
        -F, –onefile 打包成一个exe文件。
        -D, –onedir 创建一个目录，包含exe文件，但会依赖很多文件（默认选项）。
        -c, –console, –nowindowed 使用控制台，无界面(默认)
        -w, –windowed, –noconsole 使用窗口，无控制台
    APScheduler
        任务调度模块
    gunicorn
    virtualenv

    wxpython
    pip install libtiff

    distutils 安装包管理
    setuptools 增强distutils
    ez_setup.py
    pip 代替 ez
    wheel 代替 egg
    cx_freeze 打包工具 支持3.0

    python -m turtle

    pip install viztracer   多线程调试
    
    pillow   Python Imaging Library

    截屏软件 ./webkit2png.py -x 1024 768 -g 1024 0 http://bluehua.org -o test.png

    YAPF python代码格式化工具
    pysnooper #python 调试

    Celery 分布式任务队列
    PyMySQL  mysql 驱动
    StringIO
    
    ClusterShell 集群shell管理工具
    APScheduler python 任务调度模块
    gunicorn 

    kivy  图界面形库
    buildozer  打包工具
    python-for-android  还用解释

    ZbarLight  二维码识别库
    yum install libcurl-devel
    pip install


## 内置修饰

``` py
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print 'call %s to %s' % (self.calls, self.func.__name__)
        self.func(*args)

    print "hello"

    def b(self, *args):
        print args

@tracer
def spam(a, b, c): # Wrap spam in a decorator object
    print a, b, c

spam(1, 2, 3) # Really calls the tracer wrapper object
spam('a', 'b', 'c') # Invokes __call__ in class
spam(4, 5, 6) # __call__ adds logic and runs original object


"""
    输出结果
    hello
    call 1 to spam
    1 2 3
    call 2 to spam
    a b c
    call 3 to spam
    4 5 6
"""
```


## 编译py

``` text
python -m py_compile file.py

python -m py_compile /root/src/{file1,file2}.py
编译成pyc文件。
也可以写份脚本来做这事：
import py_compile
py_compile.compile('pyfile') //path是包括.py文件名的路径

import compileall
compileall.compile_dir('dirpath')
递归编译目录的方法 tmp为输出的目录， xxxx为需要递归pyc的目录

uncompyle2 -ro /home/tmp /home/xxxxx



反编译
https://github.com/Mysterie/uncompyle2

在命令行输入 uncompyle2 -h 如果有现实使用方法，就表示已经安装成功

Examples:
  uncompyle2      foo.pyc bar.pyc       # decompile foo.pyc, bar.pyc to stdout
  uncompyle2 -o . foo.pyc bar.pyc       # decompile to ./foo.pyc_dis and ./bar.pyc_dis
  uncompyle2 -o /tmp /usr/lib/python1.5 # decompile whole library

其实加密很简单的,修改Python虚拟机的代码,针对编译出pyc的部分修改下虚拟码,或者对调几个.别人死都解不出来的.这个方法是来自于(云风大侠的书<我的编程感悟>中的)
缺点也很显而易见,执行时必须使用自己的修改的Python虚拟机.

```
