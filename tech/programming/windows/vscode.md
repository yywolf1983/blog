
c 调试设置


添加变量 GIT_SSH = plink.exe
GIT_SSH with value plink.exe

#给 vscode 添加 settings-sync 插件  可以自动同步配置到gits.github.com

"program": "${workspaceFolder}/${fileBasenameNoExtension}",

使用 ssh-key 要限制 密钥权限 在windows上为本用户

插件选择 

chinese

gcc -v -E -x c - 

https://github.com/settings/tokens
 Developer settings -> Personal access tokens  ->  Generate new token  选择 gist 
 
 使用快键键shift+Alt+U（上传）或 shift+Alt+D（下载)


基础设置
{
    "git.path": "C:/Program Files/Git/bin/git.exe",
    "files.encoding": "utf8",
    "terminal.integrated.shell.windows": "C:\\Program Files\\PowerShell\\7\\pwsh.exe",
}
