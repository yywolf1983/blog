option Explicit
dim strComputer,objWMIService,objShell,colProcesses
strComputer = "."
Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
Set objShell = CreateObject("Wscript.Shell")
Do
       Set colProcesses = objWMIService.ExecQuery _
               ("Select * from Win32_Process Where Name = 'php-cgi.exe'")
       '如果指定进程少于3个，就再添加一个进程
       If colProcesses.Count < 5 Then
               objShell.Run "D:\apm\RunHiddenConsole.exe D:\apm\php\php-cgi.exe -b  127.0.0.1:9000 -c D:\apm\php.ini"
       End If
       '5秒检测一次
       Wscript.Sleep 5000
Loop
