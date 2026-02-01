#!/bin/bash
#!/usr/bin/expect -f

set host www.wuranju.com
set password www.wuranju.com
set timeout 1000

host=www.wuranju.com

echo $host

 -M 10900 -fN -o "PubkeyAuthentication=yes" -o "StrictHostKeyChecking=false" -o "PasswordAuthentication=no" -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R www.wuranju.com:10022:localhost:22 ssh_dl@www.wuranju.com

#spawn  -M 10900 -fN -o "PubkeyAuthentication=yes" -o "StrictHostKeyChecking=false" -o "PasswordAuthentication=no" -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R $host:20022:localhost:22 root@$host
#  expect "*assword:*"
#  send "$password\r"
#interact
#expect eof
