

$PSVersionTable

$profile

test-path $profile

生成默认配置文件
new-item -path $profile -itemtype file -force

跳转到管理员
Start-Process powershell -Verb runAs 

## 背景及透明设置

"profiles": 
{
    "defaults": {
        "name" : "Powershell",
            "source" : "Windows.Terminal.PowershellCore",
            "colorScheme" : "One Half Dark",
            "cursorColor" : "#FFFFFF",
            "backgroundImage":"F:\\download\\127.png",
            "backgroundImageOpacity": 0.1,
                "backgroundImageStretchMode": "fill",
            "useAcrylic" : false
    },
}

## 添加插件 starship
echo $PROFILE
open $PROFILE

# Invoke-Expression (&starship init powershell)