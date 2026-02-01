Windows 远程管理(WinRM) 是WS-Management 协议的Microsoft 实现。 该协议是基于简单对象访问协议(SOAP)的防火墙友好的标准协议。

#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
#Get-ExecutionPolicy -List

### 判断并启动 pywinrm
``` Python
# Create new local Admin user for script purposes
$Password = convertto-securestring "yangyao_yy888" -asplaintext -force
New-LocalUser "yy" -Password $Password  -FullName "yywolf" -Description "运维管理用户"
Add-LocalGroupMember -Group "Administrators" -Member "yy"

$ver = get-host | findstr "Version" | %{($_ -split ": ")[1]} | %{($_ -split "\.")[0]}

echo $ver

if ([int]$ver -gt [int]3)
{
  echo "ok"
  echo "可以安装了"
  set-executionpolicy remotesigned -Force

  ### 开启winrm服务
  winrm quickconfig -Force
  winrm set winrm/config/service/auth '@{Basic="true"}'
  winrm set winrm/config/service '@{AllowUnencrypted="true"}'
  winrm enumerate winrm/config/listener
  #winrm e winrm/config/listener

  Remove-NetfirewallRule -DisplayName "winrm"
  New-NetFirewallRule -DisplayName "winrm" -Direction Inbound -LocalPort 5985 -Protocol TCP -Action Allow

  netstat -an | findstr 5985
  get-executionpolicy -List
}
else
{
  echo "no version"
  exit;
}

#这里暂停10秒 看结果
Start-Sleep –s 10

```

### 修改本地用户密码
```
$Password = Read-Host "Enter the new password" -AsSecureString
$UserAccount = Get-LocalUser -Name "administrator"
$UserAccount | Set-LocalUser -Password $Password
```

##########################

Enable-PSRemoting

#关闭防火墙
netsh advfirewall set allprofiles state off

# 禁止 winrm
Disable-PSRemoting

#Enter-Pssession -ComputerName "127.0.0.1" -port 5985 -Credential administrator
#Set-Item wsman:\localhost\Client\TrustedHosts -value 127.0.0.1 -Force

#Get-Service，别名gsv，获取服务对象。
Stop-Service WinRM
Get-Service WinRM

#powershell其他操作
```
  #Start-Service，启动服务。
  #Stop-Service，停止服务。
  #Restart-Service，重启服务。
  #Suspend-Service，挂起/暂停服务。
  #Resume-Service，继续服务。
  #Set-Service，设置服务的属性。
  #New-Service，创建新服务。
```


```
列出当前所有的Groups
Get-NetFirewallRule |Select-Object DisplayGroup -Unique

添加一条规则
New-NetFirewallRule -DisplayName "winrm" -Direction Inbound -LocalPort 5985 -Protocol TCP -Action Allow
New-NetFirewallRule -DisplayName "Block Outbound itunes.exe" -Direction Outbound -Program "C:\Program Files\apple\itunes\itunes.exe" -Action Block

启用或者禁用存在的某条规则
Set-NetfirewallRule -DisplayName "Allow Inbound OpenVPN Client Requests" -Enabled True
Set-NetfirewallRule -DisplayName "Allow Inbound OpenVPN Client Requests" -Enabled False

删除一条规则
这会永久的删除一条规则，如果你只是禁用一条规则，可以参考前面使用set-netfirewallrule的的例子。
Remove-NetfirewallRule -DisplayName "Allow Inbound OpenVPN Client Requests"

获取防火墙环境配置信息、
Get-NetFirewallProfile -name Domain

远程管理规则
任意的命令都可以通过New-CimSession命令远程使用。假设你的防火墙已经启用了我们上面列出过的组规则“Windows Firewall Remote Management“（必要的）。
$TargetComputer=New-CIMSession -Computername MYCOMPUTER
Set-NetFirewallRule -DisplayGroup "Remote Event Log Management" -Enabled True -CimSession $TargetComputer
```

### 下载文件
```
Import-Module BitsTransfer
$url="https://www.baidu.com/"
Start-BitsTransfer $url D:\in

Invoke-Item d:\in
```
