for i in $(cat ~/.ssh/config  | grep  "host .*$" | awk '{print $2}')
do 
  echo $i
  /usr/bin/expect -c "
      spawn /usr/bin/ssh $i
      expect {
      \"(yes/no)?\" {send \"yes\r\"; exp_continue;}
      \"~]#\" {send \"exit\r\";}
      }
     expect eof"
done
