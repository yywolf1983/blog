
shitf ＋ 鼠标右键    再次打开 CMD

Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\folder\shell\cmd]
@="CMD快速通道"
[HKEY_CLASSES_ROOT\folder\shell\cmd\command]
@="cmd.exe /k cd %1"

AT 1:30 /every:M,T,W,Th,F,S,Su shutdown -s -t 200 AT pause

Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\*\shell\Edit with Vim\command]
@="\"d:\\work\\doc\\tools\\vim\\gvim.exe\" -p --remote-tab-silent \"%1\" \"%*\""

[HKEY_CLASSES_ROOT\*\shell\记事本\command]
@="notepad.exe %1"
[-HKEY_CLASSES_ROOT\*\shell\Edit with Vim\command]


%~dp0   当前目录
hh -decompile E:\yy\Source\js\dir htmldom.chm   反编译chm

chcp 控制台编码

浏览器做临时编辑器
data:text/html, <html contenteditable>

chrome://about/
%UserProfile%\AppData\Local\Google\Chrome
