# 围棋打谱应用

## 项目概述

这是一个基于 Android 的围棋打谱应用程序，支持标准 SGF 格式的解析、保存和多分支管理。项目使用 Java 和 Kotlin 混合开发，提供了完整的围棋规则实现和用户界面。

本项目的 SGF 处理算法基于 Sabaki 风格的实现，采用词法分析和语法分析相结合的方式，支持完整的 SGF 标准（FF[4]）。

## 需求说明

### 功能需求
1. **围棋规则支持**
   - 实现完整的围棋规则，包括落子、提子、打劫规则、自杀检测
   - 支持标准 19x19 棋盘，兼容 13x13 和 9x9 棋盘
   - 支持虚手操作
   - 支持 1-9 子的让子设置

2. **SGF 文件支持**
   - 支持标准 SGF 格式（FF[4]）的解析和生成
   - 支持 SGF 文件的加载和保存操作
   - 支持游戏信息的处理（黑方、白方、结果、日期等）
   - 支持多分支管理，包括第一手分支和后续分支

3. **用户界面**
   - 不可移动的带坐标棋盘
   - 显示棋盘线条、星位点、棋子、标记和注释
   - 工具栏：包含新游戏、加载、保存、设置等按钮
   - 导航栏：包含到起始、上一步、下一步、虚手等按钮
   - 功能栏：包含注释、标记、悔棋、重做等按钮
   - 信息栏：显示游戏信息、注释等内容

4. **多分支管理**
   - 支持游戏分支的创建和保存
   - 支持分支切换和管理
   - 支持第一手分支和后续分支
   - 支持分支注释和标记

### 技术需求
1. **开发环境**
   - Android Studio
   - Java 8+
   - Kotlin
   - Gradle 6.8.3+

2. **构建系统**
   - 使用 Gradle 构建系统
   - 支持国内镜像源加速依赖下载
   - 提供构建脚本简化构建过程

3. **测试要求**
   - 提供完整的单元测试
   - 测试覆盖核心功能和边缘情况
   - 确保代码质量和稳定性

### 性能需求
1. **响应速度**
   - 落子操作响应时间 < 100ms
   - SGF 文件加载时间 < 1s（普通对局）
   - 界面渲染流畅，无卡顿

2. **内存使用**
   - 应用启动内存占用 < 100MB
   - 支持大型对局（>1000手）的处理

### 兼容性需求
1. **Android 版本**
   - 支持 Android 5.0+（API Level 21+）
   - 兼容主流 Android 设备

2. **SGF 格式**
   - 兼容标准 SGF 格式（FF[4]）
   - 支持常见的 SGF 扩展和变体

### 安全需求
1. **文件操作**
   - 安全的文件 I/O 操作
   - 防止文件读写异常

2. **权限管理**
   - 合理的权限申请
   - 保护用户数据安全

## 核心功能

### 1. 围棋规则支持
- **完整的围棋规则实现**：落子、提子、打劫规则、自杀检测
- **多棋盘尺寸**：支持标准 19x19 棋盘，兼容 13x13 和 9x9 棋盘
- **虚手操作**：支持玩家选择虚手
- **让子设置**：支持 1-9 子的让子设置，自动计算让子位置
- **坐标显示**：棋盘显示坐标，便于参考

### 2. SGF 文件支持
- **完整的 SGF 标准支持**：兼容 FF[4] 标准
- **文件操作**：支持 SGF 文件的加载和保存
- **游戏信息处理**：支持黑方、白方、结果、日期等游戏信息
- **注释和标记**：支持 SGF 中的注释、标记、箭头等元素
- **多分支管理**：支持游戏分支的创建、保存和切换

### 3. 用户界面
- **自定义棋盘视图**：不可移动的带坐标棋盘，支持棋子、标记、注释显示
- **工具栏**：新游戏、加载、保存、设置等功能按钮
- **导航栏**：到起始、上一步、下一步、虚手等导航按钮
- **功能栏**：注释、标记、悔棋、重做等功能按钮
- **信息栏**：显示游戏信息、注释等内容
- **响应式设计**：适配不同屏幕尺寸的设备

### 4. 分支管理
- **分支创建**：支持在任意步数创建新分支
- **分支切换**：支持在不同分支之间切换
- **分支预览**：支持显示分支预览（幽灵棋子）
- **下一手虚影展示**：支持显示下一手可能的走法预览
- **分支注释**：支持为分支添加注释
- **第一手分支**：支持创建多个第一手分支
- **分支保存**：所有分支都会被保存到 SGF 文件中，符合 SGF 规范
- **分支加载**：支持从 SGF 文件中加载所有分支
- **分支编号**：在幽灵棋子上显示分支编号，方便用户区分不同分支
- **红色边框**：为幽灵棋子添加红色边框，增强视觉效果

### 5. 开发和测试
- **完整的单元测试**：覆盖核心功能和边缘情况
- **构建脚本**：提供 build.sh 脚本简化构建过程
- **国内镜像**：配置国内镜像加速依赖下载
- **兼容性**：支持 Android 5.0+（API Level 21+）

### 6. 高级功能
- **坐标转换**：支持 SGF 坐标和棋盘坐标之间的转换
- **让子位置计算**：根据棋盘大小和让子数自动计算让子位置
- **游戏状态管理**：支持游戏状态的保存和恢复
- **错误处理**：提供友好的错误提示和处理机制

## 技术架构

### 代码结构

```
├── README.md              # 项目说明文档
├── sgf算法.md             # SGF算法详细分析文档
└── go-record-app/         # Android应用主目录
    ├── app/               # 应用模块
    │   ├── src/main/java/com/gosgf/app/  # Java源码
    │   │   ├── model/         # 核心模型
    │   │   │   └── GoBoard.java      # 棋盘逻辑实现
    │   │   ├── util/          # 工具类
    │   │   │   ├── SGFParser.java      # SGF解析器
    │   │   │   └── SGFConverter.java   # SGF转换器
    │   │   ├── view/          # 视图组件
    │   │   │   ├── BoardView.java      # 棋盘视图
    │   │   │   └── GameInfoView.java   # 游戏信息视图
    │   │   ├── GameInfoActivity.java    # 游戏信息编辑活动
    │   │   └── MainActivity.java        # 主活动
    │   ├── src/main/res/     # 资源文件
    │   │   ├── layout/       # 布局文件
    │   │   │   ├── activity_main.xml    # 主活动布局
    │   │   │   └── view_game_info.xml   # 游戏信息视图布局
    │   │   ├── values/       # 字符串、颜色等
    │   │   │   ├── arrays.xml       # 数组资源
    │   │   │   ├── colors.xml       # 颜色资源
    │   │   │   ├── strings.xml      # 字符串资源
    │   │   │   └── themes.xml       # 主题资源
    │   ├── src/test/java/com/gosgf/app/  # 测试代码
    │   │   ├── model/         # 模型测试
    │   │   │   └── GoBoardTest.java     # 棋盘逻辑测试
    │   │   └── util/          # 工具测试
    │   │       ├── SGFParserTest.java     # SGF解析测试
    │   │       └── SGFConverterTest.java  # SGF转换测试
    │   └── build.gradle       # 应用模块构建脚本
    ├── build.sh              # 构建脚本
    ├── build.gradle          # 项目构建脚本
    ├── gradle/               # Gradle包装器目录
    ├── gradle.properties     # Gradle属性配置
    ├── gradlew               # Gradle包装器脚本
    ├── gradlew.bat           # Windows Gradle包装器脚本
    └── settings.gradle       # Gradle设置脚本
```

### 依赖关系

```
GoBoard ──────┐
              │
              ▼
SGFConverter ─┼───► SGFParser
              │
              ▲
MainActivity ─┘
```

## 使用指南

### 构建和运行

#### 国内镜像源配置
为了加速依赖下载，项目已配置阿里云 Maven 镜像源：

```gradle
// build.gradle 中的配置
repositories {
    // 阿里云 Maven 镜像
    maven { url 'https://maven.aliyun.com/repository/google' }
    maven { url 'https://maven.aliyun.com/repository/gradle-plugin' }
    maven { url 'https://maven.aliyun.com/repository/central' }
    maven { url 'https://maven.aliyun.com/repository/jcenter' }
}
```

#### 构建命令

```bash
# 查看所有可用设备
./build.sh devices

# 构建项目
./build.sh build

# 安装到设备
./build.sh install

# 构建并运行
./build.sh run

# 清理构建文件
./build.sh clean

# 查看日志
./build.sh logcat

# 查看帮助信息
./build.sh help
```

#### 构建环境要求
- JDK 8+（推荐 JDK 11）
- Android SDK（API Level 30+）
- Gradle 6.8.3+
- 网络连接（首次构建需要下载依赖）

## 开发环境设置

### 必要的开发工具

1. **Android Studio**
   - 下载地址：[Android Studio 官方下载](https://developer.android.com/studio)
   - 推荐版本：最新稳定版

2. **JDK（Java Development Kit）**
   - 推荐版本：JDK 11
   - 下载地址：[Oracle JDK](https://www.oracle.com/java/technologies/downloads/) 或 [OpenJDK](https://openjdk.org/)

3. **Android SDK**
   - 通过 Android Studio 安装
   - 确保安装以下组件：
     - Android SDK Platform-Tools
     - Android SDK Build-Tools（推荐最新版本）
     - Android SDK Platform（API Level 30+）
     - Android Emulator（可选，用于模拟器测试）

### 环境变量配置

#### Windows 系统
1. **设置 JAVA_HOME**
   - 右键点击「此电脑」→「属性」→「高级系统设置」→「环境变量」
   - 在「系统变量」中点击「新建」
   - 变量名：`JAVA_HOME`
   - 变量值：JDK 安装路径（例如：`C:\Program Files\Java\jdk-11.0.16`）

2. **设置 PATH**
   - 在「系统变量」中找到「Path」变量，点击「编辑」
   - 添加 `%JAVA_HOME%\bin`
   - 添加 Android SDK 的 `platform-tools` 和 `tools` 目录路径

#### macOS/Linux 系统
1. **设置 JAVA_HOME**
   - 编辑 `~/.bashrc` 或 `~/.zshrc` 文件
   - 添加以下内容：
     ```bash
     export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-11.0.16.jdk/Contents/Home
     export PATH=$JAVA_HOME/bin:$PATH
     ```
   - 保存文件并运行 `source ~/.bashrc` 或 `source ~/.zshrc` 使配置生效

2. **设置 ANDROID_HOME**
   - 编辑 `~/.bashrc` 或 `~/.zshrc` 文件
   - 添加以下内容：
     ```bash
     export ANDROID_HOME=~/Library/Android/sdk  # macOS
     # 或
     export ANDROID_HOME=~/Android/Sdk  # Linux
     export PATH=$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools:$PATH
     ```
   - 保存文件并运行 `source ~/.bashrc` 或 `source ~/.zshrc` 使配置生效

### Gradle 配置

1. **Gradle 版本**
   - 项目使用 Gradle 8.10.1
   - Gradle 包装器已配置，无需手动安装

2. **国内镜像配置**
   - 项目已默认配置阿里云镜像源
   - 配置文件：`go-record-app/build.gradle`
   - 主要镜像源：
     ```gradle
     maven {
         url 'https://maven.aliyun.com/repository/google'
     }
     maven {
         url 'https://maven.aliyun.com/repository/gradle-plugin'
     }
     maven {
         url 'https://maven.aliyun.com/repository/central'
     }
     maven {
         url 'https://maven.aliyun.com/repository/jcenter'
     }
     ```

### 项目导入步骤

1. **克隆项目**
   ```bash
   git clone <项目仓库地址>
   cd <项目目录>
   ```

2. **在 Android Studio 中打开项目**
   - 启动 Android Studio
   - 点击「Open」或「Open an existing project」
   - 选择 `go-record-app` 目录
   - 点击「OK」

3. **Gradle 同步**
   - Android Studio 会自动开始 Gradle 同步
   - 首次同步会下载依赖，可能需要几分钟时间
   - 确保网络连接正常，以便下载依赖

4. **配置 Android SDK**
   - 如果 Android Studio 提示 SDK 缺失，点击「Install SDK」按钮
   - 按照提示完成 SDK 安装

5. **验证环境**
   - 同步完成后，点击「Build」→「Make Project」
   - 确保项目能够成功构建，无编译错误

### 构建和运行

1. **使用构建脚本**
   ```bash
   cd go-record-app
   ./build.sh build  # 构建项目
   ./build.sh install  # 安装到设备
   ./build.sh run  # 构建并运行
   ```

2. **使用 Android Studio**
   - 点击「Run」→「Run 'app'」
   - 选择运行设备（真机或模拟器）
   - 点击「OK」开始运行

3. **运行单元测试**
   ```bash
   cd go-record-app
   ./gradlew test
   ```

4. **查看测试结果**
   - 测试结果会显示在终端中
   - 详细的测试报告位于 `app/build/reports/tests/` 目录

### 常见环境问题解决

1. **Android Studio 无法启动**
   - 检查系统内存是否充足
   - 确保 JDK 已正确安装
   - 尝试以管理员权限运行

2. **Gradle 同步失败**
   - 检查网络连接
   - 确保国内镜像配置正确
   - 尝试清理 Gradle 缓存：
     ```bash
     ./build.sh clean
     ```

3. **SDK 安装失败**
   - 检查网络连接
   - 尝试使用 SDK Manager 手动安装
   - 确保磁盘空间充足

4. **模拟器启动失败**
   - 检查电脑是否支持虚拟化技术
   - 确保已启用 BIOS 中的虚拟化选项
   - 尝试使用真机测试



## 使用指南

### 基本操作

#### 创建新游戏
1. 点击工具栏中的「新游戏」按钮
2. 在弹出的对话框中设置游戏信息（黑方、白方、让子数等）
3. 点击「确定」开始新游戏

#### 落子
1. 在棋盘上点击想要落子的位置
2. 系统会自动判断落子是否合法（是否自杀、是否打劫等）
3. 合法落子会显示在棋盘上，同时会自动提掉被吃的棋子

#### 虚手
1. 点击导航栏中的「虚手」按钮
2. 系统会记录虚手并切换到对方回合

#### 悔棋和重做
1. 点击功能栏中的「悔棋」按钮可以撤销上一步操作
2. 点击功能栏中的「重做」按钮可以恢复已撤销的操作

### 文件操作

#### 加载 SGF 文件
1. 点击工具栏中的「加载」按钮
2. 在文件选择器中选择要加载的 SGF 文件
3. 点击「确定」加载文件
4. 系统会解析 SGF 文件并显示在棋盘上

#### 保存 SGF 文件
1. 点击工具栏中的「保存」按钮
2. 在文件保存对话框中选择保存位置和文件名
3. 点击「确定」保存文件
4. 系统会将当前游戏状态保存为 SGF 格式

### 分支管理

#### 创建新分支
1. 在想要创建分支的步数处，点击功能栏中的「分支」按钮
2. 选择「创建新分支」选项
3. 在弹出的对话框中输入分支名称（可选）
4. 点击「确定」创建分支
5. 继续落子，新的走法会被记录在新分支中

#### 切换分支
1. 点击功能栏中的「分支」按钮
2. 选择「分支管理」选项
3. 在分支列表中选择要切换的分支
4. 点击「确定」切换到选中的分支

#### 分支预览
- 在分支点，棋盘上会显示幽灵棋子，预览不同分支的走法
- 点击幽灵棋子可以直接切换到对应的分支

### 注释和标记

#### 添加注释
1. 点击功能栏中的「注释」按钮
2. 在弹出的对话框中输入注释内容
3. 点击「确定」保存注释
4. 注释会显示在信息栏中

#### 添加标记
1. 点击功能栏中的「标记」按钮
2. 选择要添加的标记类型（圆圈、十字、方块、三角形等）
3. 在棋盘上点击要添加标记的位置
4. 标记会显示在棋盘上

#### 添加箭头
1. 点击功能栏中的「标记」按钮
2. 选择「箭头」选项
3. 在棋盘上点击箭头的起点位置
4. 在棋盘上点击箭头的终点位置
5. 箭头会显示在棋盘上

### 导航功能

#### 到起始
- 点击导航栏中的「到起始」按钮，跳转到游戏的第一步

#### 上一步
- 点击导航栏中的「上一步」按钮，回到上一步操作

#### 下一步
- 点击导航栏中的「下一步」按钮，前进到下一步操作

#### 到结束
- 长按「下一步」按钮，跳转到游戏的最后一步

### 游戏信息编辑

1. 点击工具栏中的「设置」按钮
2. 选择「游戏信息」选项
3. 在游戏信息编辑界面中修改黑方、白方、结果、日期等信息
4. 点击「保存」按钮保存修改

### 让子设置

1. 创建新游戏时，在游戏设置对话框中设置让子数
2. 或者在游戏进行中，点击工具栏中的「设置」按钮，选择「让子设置」选项
3. 选择要设置的让子数（1-9子）
4. 点击「确定」应用让子设置
5. 系统会自动在棋盘上显示让子棋子

### 项目导入
1. 克隆项目到本地
2. 在 Android Studio 中打开项目
3. 等待 Gradle 同步完成
4. 构建项目验证环境设置

### 故障排除指南

#### 构建错误

##### Gradle 同步失败
- **症状**：Android Studio 中 Gradle 同步过程失败，显示网络错误或依赖下载失败
- **原因**：网络连接问题，或者依赖配置错误
- **解决方案**：
  - 检查网络连接是否正常
  - 确保项目已配置国内镜像源（项目已默认配置）
  - 尝试使用 `./build.sh clean` 清理构建缓存
  - 检查 `build.gradle` 文件中的依赖版本是否正确

##### 编译错误
- **症状**：代码编译过程中出现语法错误或类型错误
- **原因**：代码中的语法错误、类型不匹配或依赖缺失
- **解决方案**：
  - 检查 Android Studio 中的错误提示，修复代码中的语法错误
  - 确保所有依赖都已正确添加
  - 检查 Java 版本是否兼容（推荐使用 Java 11）

##### 签名错误
- **症状**：构建 APK 时出现签名错误
- **原因**：签名配置错误或密钥库文件缺失
- **解决方案**：
  - 检查 `build.gradle` 文件中的签名配置
  - 确保密钥库文件存在且路径正确
  - 尝试使用调试模式构建（不要求签名）

##### 版本冲突错误
- **症状**：构建过程中出现依赖版本冲突
- **原因**：不同依赖库之间的版本不兼容
- **解决方案**：
  - 使用 `./gradlew dependencies` 查看依赖树
  - 在 `build.gradle` 中添加版本冲突解决策略
  - 更新依赖库到兼容的版本

#### 运行时错误

##### SGF 解析失败
- **症状**：加载 SGF 文件时出现解析错误
- **原因**：SGF 文件格式不正确，或者文件损坏
- **解决方案**：
  - 检查 SGF 文件格式是否符合 FF[4] 标准
  - 尝试使用其他围棋软件打开该文件，验证文件是否损坏
  - 查看应用日志，了解具体的解析错误原因

##### 棋盘操作错误
- **症状**：落子操作失败，或者应用崩溃
- **原因**：落子坐标无效，或者棋盘逻辑错误
- **解决方案**：
  - 检查落子位置是否在棋盘范围内
  - 确保不是在打劫状态下落子
  - 检查是否尝试自杀（不允许自杀）
  - 查看应用日志，了解具体的错误原因

##### 内存不足
- **症状**：应用运行时出现内存不足错误，或者应用崩溃
- **原因**：SGF 文件过大，或者应用内存使用过高
- **解决方案**：
  - 尝试加载较小的 SGF 文件
  - 关闭其他后台应用，释放内存
  - 优化设备性能（如清理缓存）

##### 布局膨胀错误
- **症状**：应用启动时出现布局膨胀错误
- **原因**：布局文件中的资源引用错误，或者主题配置错误
- **解决方案**：
  - 检查布局文件中的资源引用是否正确
  - 确保 `themes.xml` 文件已正确配置
  - 检查 `colors.xml` 文件中的颜色定义是否完整

##### 安装失败
- **症状**：应用安装时出现 `INSTALL_FAILED_VERSION_DOWNGRADE` 或其他安装错误
- **原因**：设备上已存在相同包名但版本号更高的应用，或者安装过程中出现错误
- **解决方案**：
  - 卸载设备上已有的相同应用
  - 尝试使用 `./build.sh install` 重新安装
  - 检查设备存储空间是否充足

#### 性能问题

##### 渲染卡顿
- **症状**：棋盘渲染过程中出现卡顿，或者滑动不流畅
- **原因**：棋盘渲染算法效率不高，或者设备性能不足
- **解决方案**：
  - 优化设备性能（如清理缓存）
  - 减少同时显示的标记和箭头数量
  - 尝试在性能更好的设备上运行

##### 解析缓慢
- **症状**：加载大型 SGF 文件时解析过程缓慢
- **原因**：SGF 文件过大，或者解析算法效率不高
- **解决方案**：
  - 尝试加载较小的 SGF 文件
  - 优化设备性能（如清理缓存）
  - 等待解析完成，不要在解析过程中进行其他操作

##### 响应延迟
- **症状**：点击按钮或落子时出现响应延迟
- **原因**：主线程阻塞，或者设备性能不足
- **解决方案**：
  - 优化设备性能（如清理缓存）
  - 减少同时运行的后台应用
  - 尝试在性能更好的设备上运行

#### 其他问题

##### 国内镜像源配置
- **症状**：依赖下载缓慢或失败
- **原因**：未配置国内镜像源，或者镜像源配置错误
- **解决方案**：
  - 项目已默认配置阿里云镜像源
  - 检查 `build.gradle` 文件中的镜像源配置是否正确
  - 尝试使用 `./build.sh clean` 清理构建缓存后重新构建

##### Gradle 版本兼容性
- **症状**：Gradle 构建过程失败，显示版本不兼容错误
- **原因**：Gradle 版本与 Java 版本或 Android Gradle Plugin 版本不兼容
- **解决方案**：
  - 项目已默认配置兼容的 Gradle 版本（8.10.1）
  - 确保使用兼容的 Java 版本（推荐 Java 11）
  - 检查 `gradle-wrapper.properties` 文件中的 Gradle 版本配置

##### 设备兼容性
- **症状**：应用在某些设备上无法运行，或者运行异常
- **原因**：设备 Android 版本过低，或者设备硬件不兼容
- **解决方案**：
  - 确保设备 Android 版本为 5.0+（API Level 21+）
  - 尝试在其他兼容的设备上运行
  - 查看应用日志，了解具体的兼容性错误

### 日志查看

#### Android Studio 日志
1. 在 Android Studio 中，点击底部的「Logcat」选项卡
2. 选择连接的设备和应用进程
3. 查看应用运行过程中的日志信息
4. 过滤日志级别，查找错误信息

#### 命令行日志
1. 连接设备到电脑
2. 打开终端，运行 `adb logcat` 命令
3. 过滤应用包名，查看应用日志
4. 分析日志中的错误信息，定位问题原因

## 核心 API 使用

### 创建棋盘

```java
GoBoard board = new GoBoard();
```

### 落子

```java
// 正常落子
board.placeStone(3, 3);

// 虚手
board.placeStone(-1, -1);
```

### 分支管理

```java
// 获取当前分支数量
int variationCount = board.getCurrentVariationCount();

// 选择分支
board.selectVariation(0);

// 添加分支
List<GoBoard.Move> branch = new ArrayList<>();
branch.add(new GoBoard.Move(4, 4, 2));
board.addStartVariation(branch, "新分支");
```

### SGF 处理

```java
// 从 SGF 加载
board.loadFromSGF(sgfContent);

// 保存为 SGF
String sgf = board.toSGFString();
```

## 测试覆盖

### 单元测试

- **GoBoardTest**：测试棋盘逻辑和规则
  - 落子规则测试
  - 提子算法测试
  - 打劫规则测试
  - 自杀判断测试
  - 分支管理测试

- **SGFConverterTest**：测试 SGF 转换功能
  - 坐标转换测试
  - 节点转换测试
  - 树结构转换测试
  - 异常处理测试

### 功能测试

- **落子规则**：测试提子、打劫、自杀
- **分支管理**：测试分支创建、切换、保存
- **SGF 处理**：测试各种 SGF 格式的解析
- **让子功能**：测试不同让子数的处理
- **用户界面**：测试界面布局和交互
- **数据持久化**：测试数据存储和读取

## 已知问题和解决方案

### 已解决的问题

#### 无法加载 无法持续下一步
- **问题描述**：应用无法加载 SGF 文件，且无法执行下一步操作
- **原因**：
  - 初始问题：`onNext` 方法未实现，`redo` 方法也未正确实现
  - 后续问题：`SGFConverter.java` 中的 `loadFromSGF` 方法走子记录的加载逻辑存在问题，走子记录没有被正确加载到 `moveHistory` 列表中，导致 `nextMove()` 方法无法找到有效的走子记录来执行
- **解决方案**：
  - 实现了 `MainActivity.java` 中的 `onNext` 方法，使其调用 `board.redo()`
  - 修复了 `GoBoard.java` 中的 `redo` 方法，添加了 `undoStack` 来保存被撤销的移动
  - 修复了 `GoBoard.java` 中的 `undo` 方法，确保被撤销的移动能正确添加到 `undoStack`
  - 修改了 `SGFConverter.java` 文件中的 `loadFromSGF` 方法，修正了 SGF 文件的解析逻辑：
    - 正确处理 SGF 文件结构，根节点包含分支节点，每个分支节点包含多个子节点（游戏信息节点、走子节点等）
    - 遍历根节点的所有子节点（分支）
    - 对于主分支，遍历其中的所有节点并加载走子记录
    - 对于其他分支，作为变化分支处理
  - 确保了 `loadMovesFromNode` 方法正确处理子节点的遍历，递归加载所有走子记录
  - 保持了 `loadFromSGF` 方法最后调用 `board.resetToStart()` 的逻辑，确保 `currentMoveIndex` 被重置为 -1，用户可以从第一步前开始，使用 `nextMove()` 逐步浏览所有走子
- **验证结果**：
  - ✅ SGF 文件加载成功后，所有走子记录都会被正确加载到 `moveHistory` 列表中
  - ✅ 加载完成后，棋盘会停留在第一步前
  - ✅ 用户可以使用"下一步"按钮逐步浏览所有走子记录
  - ✅ 走子记录在棋盘上正确显示
  - ✅ 座子在走子过程中保持显示

## 未来计划

- **AI 分析**：集成 AI 分析功能
- **多语言支持**：添加多语言界面
- **主题支持**：添加深色主题和自定义主题
- **云存储**：支持保存到云存储
- **手势支持**：添加更多手势操作
- **动画效果**：优化落子和提子动画
- **多设备支持**：支持不同屏幕尺寸的设备
- **多 Android 版本**：支持更多 Android 版本

## 贡献指南

### 如何贡献

1. **Fork 项目**
   - 在 GitHub 上 Fork 本项目到你的个人账号

2. **克隆项目**
   ```bash
   git clone https://github.com/your-username/gosgf2.git
   cd gosgf2
   ```

3. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **开发功能**
   - 实现你的功能或修复 bug
   - 确保代码符合项目的代码风格
   - 为新功能添加单元测试

5. **提交代码**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

6. **推送代码**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **创建 Pull Request**
   - 在 GitHub 上创建 Pull Request
   - 描述你的功能或修复
   - 等待代码审查

### 代码风格要求

1. **Java 代码风格**
   - 遵循 Google Java 风格指南
   - 使用 4 个空格进行缩进
   - 行宽限制为 100 字符
   - 方法和变量使用驼峰命名法
   - 类名使用 Pascal 命名法

2. **Kotlin 代码风格**
   - 遵循 Kotlin 官方代码风格
   - 使用 4 个空格进行缩进
   - 行宽限制为 100 字符
   - 方法和变量使用驼峰命名法
   - 类名使用 Pascal 命名法

3. **XML 代码风格**
   - 使用 4 个空格进行缩进
   - 标签属性按字母顺序排列
   - 确保 XML 文件格式正确

4. **文档要求**
   - 为新功能添加 Javadoc 注释
   - 更新 README.md 中的相关内容
   - 为复杂算法添加详细注释

### 测试要求

1. **单元测试**
   - 为新功能添加单元测试
   - 确保测试覆盖核心功能和边缘情况
   - 运行 `./gradlew test` 确保所有测试通过

2. **集成测试**
   - 确保新功能与现有功能兼容
   - 测试在不同设备和 Android 版本上的运行情况

3. **性能测试**
   - 确保新功能不会影响应用性能
   - 测试大型 SGF 文件的加载速度
   - 测试棋盘渲染的流畅度

### 问题报告

1. **Bug 报告**
   - 在 GitHub Issues 中创建新的 Issue
   - 描述 Bug 的详细情况
   - 提供复现步骤
   - 附上相关日志和截图

2. **功能请求**
   - 在 GitHub Issues 中创建新的 Issue
   - 描述你希望添加的功能
   - 说明功能的使用场景
   - 提供可能的实现思路

### 代码审查

1. **审查流程**
   - 提交 Pull Request 后，项目维护者会进行代码审查
   - 审查过程中可能会要求你进行一些修改
   - 审查通过后，你的代码会被合并到主分支

2. **审查标准**
   - 代码质量：代码是否清晰、可维护
   - 功能完整性：功能是否完整、符合要求
   - 测试覆盖：是否有足够的测试覆盖
   - 性能影响：是否会影响应用性能
   - 兼容性：是否与现有功能兼容

### 行为准则

- 尊重其他贡献者
- 接受建设性批评
- 关注问题本身，不进行人身攻击
- 帮助新人，共同进步
- 保持代码库的整洁和可维护性

## 许可证

本项目采用 [WTFPL](http://www.wtfpl.net/) 许可证 - 随便你怎么做公共许可证

```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2024 gosgf2 Project Contributors

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
```

## 鸣谢

### 项目贡献者
- 感谢所有为本项目做出贡献的开发者
- 感谢社区提供的反馈和建议

### 开源库
- **Android SDK** - Google 提供的 Android 开发工具包
- **Gradle** - 优秀的构建自动化工具

### 资源和参考
- **SGF 标准** - 国际围棋联合会认可的棋盘游戏记录标准
- **Sabaki** - 优秀的围棋软件，为本项目的 SGF 处理算法提供了参考
- **阿里云 Maven 镜像** - 提供快速的依赖下载服务

### 特别鸣谢
- 感谢围棋爱好者社区的支持和鼓励
- 感谢所有测试和使用本应用的用户
- 感谢为开源项目做出贡献的所有开发者

## SGF 算法参考

本项目的 SGF 处理算法基于 Sabaki 项目的实现，并进行了适应 Android 平台的优化。详细的算法分析请参考 [sgf算法.md](./sgf算法.md) 文件。