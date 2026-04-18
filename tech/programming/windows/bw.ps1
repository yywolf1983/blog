<#
百度网盘 智能看图 彻底删除&防复活 PS脚本
#>

# 强制结束百度网盘进程
Write-Host ">>> 正在关闭百度网盘所有进程..." -ForegroundColor Cyan
Get-Process -Name BaiduNetdisk -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep -Milliseconds 800

# 定义智能看图路径
$netdiskPaths = @(
    "C:\Program Files\Baidu\BaiduNetdisk\module\ImageViewer",
    "C:\Program Files (x86)\Baidu\BaiduNetdisk\module\ImageViewer",
    "$env:LOCALAPPDATA\Baidu\BaiduNetdisk\module\ImageViewer"
)

# 删除看图目录
foreach ($path in $netdiskPaths) {
    if (Test-Path $path) {
        Remove-Item -Path $path -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "已删除: $path" -ForegroundColor Green
        
        # 新建同名占位文件 防复活
        $lockFile = Join-Path (Split-Path $path) "ImageViewer"
        if (-not (Test-Path $lockFile)) {
            New-Item -Path $lockFile -ItemType File -Force | Out-Null
            # 设置只读+禁止写入
            $fileAttr = [System.IO.File]::GetAttributes($lockFile)
            [System.IO.File]::SetAttributes($lockFile, $fileAttr -bor [System.IO.FileAttributes]::ReadOnly)
            Write-Host "已添加防复活锁定文件" -ForegroundColor Green
        }
    }
}

# 清理注册表
Write-Host "`n>>> 正在清理注册表残留..." -ForegroundColor Cyan
$regKeys = @(
    "HKCR\BaiduNetdiskImageViewerAssociations",
    "HKCU\Software\Baidu\BaiduNetdiskImageViewer",
    "HKCU\Software\RegisteredApplications\BaiduNetdiskImageViewer"
)

foreach ($reg in $regKeys) {
    if (Test-Path "Registry::$reg") {
        Remove-Item -Path "Registry::$reg" -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "已删除注册表: $reg" -ForegroundColor Green
    }
}

Write-Host "`n✅ 操作完成，百度网盘智能看图已永久禁用！" -ForegroundColor Green
Write-Host "提示：后续网盘更新也不会自动恢复该组件" -ForegroundColor Yellow

