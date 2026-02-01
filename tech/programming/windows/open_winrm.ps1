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

ipconfig | findstr IPv4

#这里暂停10秒 看结果
Start-Sleep –s 10
