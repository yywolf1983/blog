:: Set Variable ::
set key="D:\aaa\yy\ops_base\ssh\.ssh\id"

:: Remove Inheritance ::
cmd /c icacls %key% /c /t /inheritance:d

:: Set Ownership to Owner ::
cmd /c icacls %key% /c /t /grant %username%:F

:: Remove All Users, except for Owner ::
cmd /c icacls %key%  /c /t /remove Administrator "Authenticated Users" BUILTIN\Administrators BUILTIN Everyone System Users

:: Verify ::
cmd /c icacls %key%
