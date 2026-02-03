# 保存当前目录
Push-Location

try {
    Get-ChildItem -Directory | ForEach-Object {
        $repoPath = $_.FullName
        if (Test-Path "$repoPath\.git") {
            Write-Host "`n检查仓库: $($_.Name)" -ForegroundColor Cyan
            
            # 进入仓库目录
            Set-Location $repoPath
            
            # 检查是否有更新
            $pullOutput = git pull --dry-run 2>&1
            if ($pullOutput -like '*Already up to date.*' -or $pullOutput -like '*已经是最新的。*') {
                Write-Host '没有发现更新' -ForegroundColor Green
            } else {
                Write-Host '正在拉取更新...' -ForegroundColor Yellow
                git pull
            }
            
            # 检查未提交的更改
            $statusOutput = git status --porcelain
            if ($statusOutput) {
                Write-Host "******* 未提交的更改 ($($repoPath)) ​*******" -ForegroundColor Red
                $statusOutput | ForEach-Object { 
                    $line = $_.Trim()
                    if ($line.Length -gt 3) {
                        $line.Substring(3)  # 提取文件名部分
                    }
                }
            } else {
                Write-Host '没有未提交的更改' -ForegroundColor Green
            }
            
            # 返回原始目录
            Set-Location $repoPath
        }
    }
}
catch {
    Write-Host "发生错误: $_" -ForegroundColor Red
}
finally {
    # 恢复原始目录
    Pop-Location
    Write-Host "`n所有仓库检查完成" -ForegroundColor Cyan
    pause
}