
# Android SDK 安装与配置指南

## 1. 下载 Android SDK 命令行工具
- 下载地址：[Android Command Line Tools](https://developer.android.com/studio#command-tools)
- 文件名：`commandlinetools-win-11076708_latest.zip`

## 2. 安装 SDK
1. 解压下载的 zip 文件
2. 打开命令提示符，进入解压后的目录
3. 执行以下命令安装 SDK（使用清华大学镜像源）：
   ```bash
   .\sdkmanager.bat --list --no_https --sdk_root=D:\download\android-sdk --channel=0 --proxy=http --proxy_host=mirrors.tuna.tsinghua.edu.cn --proxy_port=443
   ```

## 3. 复制命令行工具到 SDK 目录
- 将解压后的 `cmdline-tools` 目录复制到 `D:\download\android-sdk` 目录下
- 确保最终路径为：`D:\download\android-sdk\cmdline-tools\latest`

## 4. 配置环境变量
1. 右键点击「此电脑」→「属性」→「高级系统设置」→「环境变量」
2. 添加系统变量：
   - 变量名：`ANDROID_HOME`
   - 变量值：`D:\download\android-sdk`
   - 变量名：`ANDROID_SDK_ROOT`
   - 变量值：`D:\download\android-sdk`
3. 在系统变量 `Path` 中添加以下路径：
   - `D:\download\android-sdk\cmdline-tools\latest\bin`
   - `D:\download\android-sdk\emulator`
   - `D:\download\android-sdk\platform-tools`

## 5. 安装系统镜像
1. 查看已安装的镜像：
   ```bash
   sdkmanager.bat --list_installed
   ```
2. 跳过 JDK 版本检查（如果需要）：
   ```bash
   $env:SKIP_JDK_VERSION_CHECK = "true"
   ```
3. 安装系统镜像：
   ```bash
   # 安装 x86_64 架构的 Google APIs 镜像
   sdkmanager.bat "system-images;android-34;google_apis;x86_64" --sdk_root=D:\download\android-sdk
   
   # 安装 ARM64 架构的 Google APIs 镜像
   sdkmanager.bat "system-images;android-34;google_apis;arm64-v8a" --sdk_root=D:\download\android-sdk
   
   # 安装 ARM64 架构的默认镜像
   sdkmanager --install "system-images;android-34;default;arm64-v8a"
   ```

## 6. 创建和管理 AVD（Android 虚拟设备）
1. 创建 AVD：
   ```bash
   # 创建 x86_64 架构的 AVD
   avdmanager.bat create avd -n MyAVD -k "system-images;android-34;google_apis;x86_64"
   
   # 创建 ARM64 架构的 AVD
   avdmanager.bat create avd -n ARM_AVD -k "system-images;android-34;default;arm64-v8a"
   
   # 强制创建 ARM64 架构的 Google APIs AVD
   avdmanager create avd -n "ARM_AVD" -k "system-images;android-34;google_apis;arm64-v8a" --abi "arm64-v8a" --force
   ```
2. 列出所有 AVD：
   ```bash
   avdmanager.bat list avds
   ```
3. 删除 AVD：
   ```bash
   avdmanager delete avd -n MyAVD
   ```

## 7. 启动模拟器
```bash
emulator -avd ARM_AVD -skin 1080x2400 -dpi 420
```

## 8. ADB 操作
### 8.1 获取 root 权限
```bash
adb root
```

### 8.2 推送文件到设备
```bash
adb push pikafish-avx2 /data/data/top.nones.chessgame/cache/pikafish
```

### 8.3 设置文件权限
```bash
adb shell chmod 755 /data/data/top.nones.chessgame/cache/pikafish
```

### 8.4 验证文件
```bash
adb shell ls -l /data/data/top.nones.chessgame/cache/pikafish
```

### 8.5 修改文件所有者
```bash
adb shell chown u0_a192:u0_a192_cache /data/data/top.nones.chessgame/cache/pikafish
```

## 9. 常见问题解决
- **SDK 下载缓慢**：使用清华大学镜像源（如命令中所示）
- **JDK 版本问题**：设置 `SKIP_JDK_VERSION_CHECK=true` 环境变量
- **AVD 创建失败**：确保已安装对应架构的系统镜像
- **模拟器启动失败**：检查系统镜像是否正确安装，尝试使用不同的 AVD 配置