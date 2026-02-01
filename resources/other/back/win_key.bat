::# Set Key File Variable:
::# Set Key="%UserProfile%\.ssh\id_rsa"
    Set Key="bk"

::# Remove Inheritance:
    Icacls %Key% /c /t /Inheritance:d

::# Set Ownership to Owner:
    Icacls %Key% /c /t /Grant %UserName%:F

::# Remove All Users, except for Owner:
    Icacls %Key%  /c /t /Remove Administrator BUILTIN\Administrators BUILTIN Everyone System Users

::# Verify:
    Icacls %Key%

::# Remove Variable:
    set "Key="

