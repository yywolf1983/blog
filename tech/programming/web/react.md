react

react native

npx nrm use taobao 切换淘宝源
npx nrm use npm 换回官方

npm install -g yarn


安装android sdk
export ANDROID_SDK_ROOT=/Users/yy/Downloads/android-home/
export ANDROID_HOME=/Users/yy/Downloads/andoird-home/

/Users/yy/Downloads/andoird-home/bin/sdkmanager --licenses --sdk_root=/Users/yy/Downloads/andoird-home

vi /Users/yy/AwesomeProject/android/local.properties
sdk.dir=/Users/yy/Downloads/andoird-home/cmdline-tools

adb kill-server

创建项目
npx react-native init AwesomeProject

配置gradle 下载
vi android/gradle/wrapper/gradle-wrapper.properties

处理调试问题
gradlew compileDebugSources --stacktrace -info

运行
cd AwesomeProject
yarn android
# 或者
yarn react-native run-android

安装打包插件
# Npm
npm install react-native-upload --save-dev
# Yarn
yarn add react-native-upload --dev

生成配置文件
npx upload-init

# 同时打包android和ios
npx upload-build --ios-export-plist path/to/xxx.plist

# 安卓默认打包release版本，可以改成debug版本
npx upload-build --ios-export-plist path/to/xxx.plist --variant=debug

# 单独打包android
npx upload-build --no-ios

# 单独打包ios
npx upload-build --no-android --ios-export-plist path/to/xxx.plist
