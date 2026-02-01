

libuv 跨平台库
    linux: epoll
    freebsd: kqueue
    windows: iocp
V8 node的灵魂

git checkout v17.0.1

npm config set prefix "您想要设置的目录路径"


npm install -g node-gyp
node-gyp configure
node-gyp build

## node 17.0.1 build web3.js
export NODE_OPTIONS=--openssl-legacy-provider
node run build

shadow DOM
cordova


npm i -g n

# 升级到稳定版
sudo n stable
# 升级到最新版
sudo n lastest
# 切换使用node版本
sudo n 12.13.0
# 删除某个node版本
sudo n rm 12.13.0
# 用指定版本执行脚本
sudo n use 12.13.0  some.js