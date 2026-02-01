from setuptools import setup, find_packages
from setuptools.command.install_scripts import install_scripts
from distutils.core import setup, Extension
import numpy
import glob 
from os import path

import bottle

class InstallScripts(install_scripts):
    def run(self):
        print("hello")

setup(
    name="mybottle",
    version=bottle.__version__,
    author=bottle.__author__,
    long_description=bottle.__doc__,
    long_description_content_type="text/markdown",
    author_email="yywolf1983@gamil.com",
    description="Learn to Pack Python Module",
    url="http://www.d7home.com/", 
    #packages=['bottle'],
    py_modules=['bottle'],

    #安装的数据文件
    data_files=[
        ('doc', ['bottle-docs.pdf']),
        ('html', ['html/index.html']),
               ],

    # 打包的数据文件
    package_data={
               },

    # 不打包某些文件
    exclude_package_data={
               },

# 包含在分发文件中
# 如下这是一个 MANIFEST.in 的样例：
# include *.txt
# recursive-include examples *.txt *.py
# prune examples/sample?/build

# 这些配置，规定了如下几点
#  所有根目录下的以 txt 为后缀名的文件，都会分发
#  根目录下的 examples 目录 和 txt、py文件都会分发
#  路径匹配上 examples/sample?/build 不会分发

    classifiers=['Development Status :: 4 - Beta',
                   "Operating System :: OS Independent",
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
                   'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
                   'Topic :: Internet :: WWW/HTTP :: WSGI',
                   'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
                   'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
                   'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
                   'Topic :: Software Development :: Libraries :: Application Frameworks',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   ],

    # install_requires 在安装模块时会自动安装依赖包
    install_requires=['docutils>=0.3'],

    # 而 extras_require 不会，这里仅表示该模块会依赖这些包
    # 但是这些包通常不会使用到，只有当你深度使用模块时，才会用到，这里需要你手动安装
    extras_require={
        'PDF':  ["ReportLab>=1.2", "RXP"],
        'reST': ["docutils>=0.3"],
    },
    
    #限制安装环境
    python_requires='>=3.6, <=3.9',

    # 用来支持自动生成脚本，安装后会自动生成 /usr/bin/foo 的可执行文件
    # 该文件入口指向 foo/main.py 的main 函数
    entry_points={
        'console_scripts': [
            'bottle = bottle.bottle:main'
        ]
    },

    #安装到系统路径下
    # scripts=['bin/foo.sh', 'bar.py'],

    #安装测试所需依赖
    tests_require=[
        'pytest>=3.3.1',
        'pytest-cov>=2.5.1',
    ],
    setup_requires=[
        'pytest-runner>=3.0',
    ],

    #从指定链接下载以来
    dependency_links = [
        "http://packages.example.com/snapshots/foo-1.0.tar.gz",
        "http://example2.com/p/bar-1.0.tar.gz",
    ],

    #添加自定义命令
    cmdclass={
        "install_scripts": InstallScripts
    },

    #参数用于构建 C 和 C++ 扩展扩展包。
    # 每一个 Extension 实例描述了一个独立的扩展模块，
    # 扩展模块可以设置扩展包名，头文件、源文件、链接库及其路径、宏定义和编辑参数等。
    ext_modules=[
        # Extension('foo',
        #           glob(path.join(here, 'src', '*.c')),
        #           libraries = [ 'rt' ],
        #           include_dirs=[numpy.get_include()])
    ]

)


# python setup.py bdist_rpm
# python setup.py sdist
# python setup.py sdist --formats=gztar,zip
# python setup.py bdist_egg #egg 过时了
# python setup.py bdist_wininst
# python setup.py build_ext
# python setup.py bdist
# python setup.py bdist_wheel  #最新标砖

#发布上传
# register、upload:
