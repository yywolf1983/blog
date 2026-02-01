free -m | sed -n '2p' | awk '{print $2/1024"G"}'

pass=mysql
echo $pass
ps -e -o 'pid,comm,pcpu,rsz,vsz,stime,user,uid' |  sort -nrk5 | grep ${pass}| awk '{sum += $4}; {sum2 += $5}; END { print sum/1024/1024"G   "sum2/1024/1024"G"}' 

pass=oracle
echo $pass
ps -e -o 'pid,comm,pcpu,rsz,vsz,stime,user,uid' |  sort -nrk5 | grep ${pass}| awk '{sum += $4}; {sum2 += $5}; END { print sum/1024/1024"G   "sum2/1024/1024"G"}' 

pass=java
echo $pass
ps -e -o 'pid,comm,pcpu,rsz,vsz,stime,user,uid' |  sort -nrk5 | grep ${pass}| awk '{sum += $4}; {sum2 += $5}; END { print sum/1024/1024"G   "sum2/1024/1024"G"}' 
