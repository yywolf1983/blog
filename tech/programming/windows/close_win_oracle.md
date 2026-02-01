@echo off
:start
cls
echo.
echo.
echo.
echo          ---i--- 启动oracle
echo          ---u--- 关闭oracle
echo          ---q--- exit
set /p st=
cls
if /I "%ST%"=="i" goto inst
if /I "%st%"=="u" goto unstall
if /I "%st%"=="q" goto exit

goto start

:inst
net start OracleServiceORCL
rem 远程监听器
net start OracleOraDb11g_home1TNSListener

goto start

:unstall
rem 远程监听器
net stop OracleOraDb11g_home1TNSListener
rem 基本服务
net stop OracleServiceORCL

net stop OracleVssWriterORCL
net stop OracleDBConsoleorcl
net stop OracleJobSchedulerORCL
net stop OracleMTSRecoveryService
net stop OracleOraDb11g_home1ClrAgent

sc config OracleServiceORCL start= demand
sc config OracleOraDb11g_home1TNSListener start= demand

sc config OracleVssWriterORCL start= demand
sc config OracleDBConsoleorcl start= demand
sc config OracleJobSchedulerORCL start= demand
sc config OracleMTSRecoveryService start= demand
sc config OracleOraDb11g_home1ClrAgent start= demand

rem sc config 服务名 start= demand     //手动
rem sc condig 服务名 start= auto       //自动
rem sc config 服务名 start= disabled //禁用
rem sc start 服务名
rem sc stop   服务名
goto start

:exit
@echo on
