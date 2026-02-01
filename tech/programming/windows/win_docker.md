
启用wsl
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

启用虚拟平台
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart


wsl --list --online

wsl --install -d Debian

卸载
wslconfig.exe /u Debian

sudo dpkg-reconfigure locales



wsl --set-default-version 2

wsl -l -v


改变docker目录
wsl --export docker-desktop-data "F:\Docker\docker-desktop-data.tar"

wsl --unregister docker-desktop-data

wsl --import docker-desktop-data "F:\Docker\wsl\data" "F:\Docker\docker-desktop-data.tar" --version 2