注册windows 服务

D:\yy\nssm-2.24\win64\nssm install nginx D:\nginx-1.16.1\nginx.exe
D:\yy\nssm-2.24\win64\nssm set nginx AppDirectory D:\nginx-1.16.1
D:\yy\nssm-2.24\win64\nssm start nginx
D:\yy\nssm-2.24\win64\nssm status nginx


nssm stop nginx
nssm remove nginx confirm


call D:\tomcat9.0\bin\service.bat install tomcat9.0
D:\tomcat9.0\bin\nssm.exe set tomcat9.0 start SERVICE_DELAYED_AUTO_START
D:\tomcat9.0\bin\nssm.exe start tomcat9.0
D:\tomcat9.0\bin\nssm.exe status tomcat9.0

D:\tomcat9.0\bin\nssm.exe stop tomcat9.0
D:\tomcat9.0\bin\nssm.exe remove tomcat9.0 confirm
