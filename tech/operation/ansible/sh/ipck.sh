eht=`ip add | grep BROADCAST,MULTICAST,UP | grep -vE 'veth|br-|docker' | awk -F":" '{print $2}'`

for i in $eht
do
  echo $i
  ip add show $i | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}'
done
