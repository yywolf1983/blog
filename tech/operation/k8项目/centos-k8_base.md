ansible k8s -m shell -a "cat /sys/class/dmi/id/product_uuid"

ansible k8s -m copy -a "src=k8_bash.sh dest=~/"
ansible k8s -m shell -a "bash k8_bash.sh"

ansible k8s -m shell -a 'yum update'

ansible k8s -m yum -a 'name=kubelet state=absent'
ansible k8s -m yum -a 'name=kubeadm state=absent'
ansible k8s -m yum -a 'name=kubectl state=absent'


ansible k8s -m shell -a 'systemctl enable --now kubelet'