@echo off
    set var=%TIME:~3,2%
    rem 小时
    set tt=%TIME:~0,2%

    :start
        set /a var=var+5
        if %var% gtr 60 goto ttt  rem 大于分钟数
        if %tt% gtr 16 goto bey   rem 大于小时数
        set /a tt+=0
        at %tt%:%var% shutdown -s -t 0
        if %var% leq 60 GOTO start

    :ttt
        set /a tt+=1
        set var=0
        goto start

    :bey
        echo %DATE:~0,4%-%DATE:~5,2%-%DATE:~8,2% %TIME:~0,2%:%TIME:~3,2%:%TIME:~6,2%

pause

rem EQU - 等于
rem NEQ - 不等于
rem LSS - 小于
rem LEQ - 小于或等于
rem GTR - 大于
rem GEQ - 大于或等于
