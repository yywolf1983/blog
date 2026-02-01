

linux 控制android

### 屏幕录制

    scrcpy --record file.mp4
    scrcpy --no-display --record file.mp4  不开启屏幕录制

### 方向选择

    scrcpy --lock-video-orientation 0   # 自然朝向
    scrcpy --lock-video-orientation 1   # 90° 逆时针旋转
    scrcpy --lock-video-orientation 2   # 180°
    scrcpy --lock-video-orientation 3   # 90° 顺时针旋转
    
    scrcpy --max-size 1024   分辨率

    打开安卓设备的网络adb功能adb tcpip 5555
    将您的设备与电脑断开连接。连接到您的设备：adb connect DEVICE_IP:5555 
    运行scrcpy。 


adb kill-server    # 关闭本地5037端口上的adb服务器

scrcpy --shortcut-mod=rctrl

scrcpy -b2M -m800 --max-fps 15 -S -w
