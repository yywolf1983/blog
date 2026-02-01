NODE_HOME
NODE_PATH

export NODE_HOME=/data/soft/node-v14.15.4-linux-x64/
export NODE_PATH=/data/soft/node-v14.15.4-linux-x64/bin/
-g 全局安装
从指定服务器下载
    npm install -gd express --registry=http://registry.npm.taobao.org
设置下载服务器
    npm config set registry http://registry.npm.taobao.org
    npm config set registry http://registry.cnpmjs.org



webpack 

 npm install -g cnpm --registry=https://registry.npm.taobao.org
 npm install -g @vue/cli
 vue init webpack nones

npm i element-ui -S
npm i vue-router 
npm i vue-resource

npm run serve


npm install nrm

nrm ls
nrm use npm
nrm add company http://npm.company.com/
nrm del company

nrm test
nrm test npm


## node n

npm install -g n

n v16.4.0
n latest
n lts

n ls
n ls-remote

n 切换版本