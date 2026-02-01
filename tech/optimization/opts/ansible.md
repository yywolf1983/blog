roles 角色
  tasks 运行任务列表
  handlers 运行任务后的触发动作
  vars variables 定义的变量
      group_vars
      host_vars
  defaults   存放默认的变量
  files 文件包
  templates  模板文档



hosts="metafinance_front" #这里别用下横杠

for name in $hosts
do
  echo $name
  ansible $name -m hostname -a "name=$name"
done



echo "export ANSIBLE_HOSTS=~/ansible_hosts" >> ~/.bashrc

echo "127.0.0.1" > ~/ansible_hosts

pip install ansible

mkdir -p /etc/ansible

vim /etc/ansible/ansible.cfg
or 
cat << EOF > ~/.ansible.cfg
[defaults]
remote_port = 22
private_key_file = ~/.ssh/id_rsa 
log_path = ~/ansible.log
inventory = ~/ansible_hosts

[colors]
EOF

cat << EOF > ~/ansible_hosts
[storm_cluster]
192.168.99.227
192.168.99.251

[test]
192.168.200.13[6:7]

[k8s]
 m1 ansible_ssh_host=192.168.3.93
 m2 ansible_ssh_host=192.168.3.94
 m3 ansible_ssh_host=192.168.3.95
EOF

ansible all -m setup -a "filter=ansible_distribution"
ansible all -m ping
ansible all --list-hosts

copy 文件
ansible storm_cluster -m copy -a "src=/etc/ansible/ansible.cfg dest=/tmp/ansible.cfg owner=root group=root mode=0644"

# 直接将文本内容注入到远程主机的文件中
ansible web -m copy -a "content='白云深处有人家\n' dest=/tmp/b.txt"         

运行远程shell
ansible storm_cluster -m shell -a "/tmp/rocketzhang_test.sh"

下载文件
ansible web -m fetch -a 'src=/var/log/cron dest=/tmp

ansible web -a 'chdir=/tmp pwd'    # 切换目录执行命令，使用场景是编译安装时使用
ansible web -a 'creates=/tmp pwd'  # 用来判断/tmp目录是否存在，存在就不执行操作
ansible web -a 'creates=/data pwd' # 因为data不存在，所有才会执行pwd命令
ansible web -a 'removes=/tmp pwd'  # 用来判断tmp目录是否存在，存在就执行操作
ansible web -a 'removes=/data pwd' # 因为data不存在，所有才不会执行

ansible db -m file -a 'path=/lzmly2  state=directory'       #在远程机器上创建文件夹
ansible db -m file -a 'path=/root/q.txt  state=touch'       #用来在远程机器上创建文件
ansible db -m file -a 'path=/tmp/f src=/etc/fstab state=link'     #创建软连接src是源地址，path是目标地址
ansible db -m file -a 'path=/tmp/f state=absent'          #用来删除文件或者文件夹

ansible web -m yum -a 'name=wget'                 # 安装wget
ansible web -m yum -a 'name=wget state=absent'    # 卸载软件包
ansible web -m yum -a 'name="@Development Tools"' # 安装包组

ansible web -m service -a 'name=nginx state=started enabled=yes' # 启动nginx, 开机启动nginx
ansible web -m service -a 'name=nginx state=stopped' # 关闭nginx

# 安装flask模块
ansible web -m pip -a 'name=flask' 

#执行本地文件
ansible web -m script -a '/root/m.sh' 


#计划任务
minute      # 分钟
hour       # 小时
day      　# 天
month      # 月
weekday    # 周
name     　# 任务名字
job      　# 任务
disabled    # 禁用

ansible db -m cron -a 'minute=26 job="touch /tmp/xzmly.txt" name=touchfile'          # 新建一个计划任务
ansible db -m cron -a 'name=touchfile state=absent'                         # 删除一个计划任务
ansible db -m cron -a 'minute=26 job="touch /tmp/xzmly.txt" name=touchfile disabled=yes'  # 禁用计划任务,以#表示禁用
ansible web -m cron -a 'name=synchronus minute=01 hour=01 job="/usr/sbin/ntpdate -u cn.pool.ntp.org > /dev/null 2>&1; /sbin/hwclock -w"'     　 # 每小时同步window时间

用户组

group    # 组
groups   # 附加组
home     # 家目录
name     # 用户名
password # 密码
remove   # 只有当state=absent 起作用, 删除用户家目录
shell    # 用户登录后使用的shell
system   # 创建一个系统用户
uid      # 用来指定用户的id
state 　 # 状态
ansible db -m user -a 'name=ryan uid=4000 home=/opt/wulaoshi groups=root shell=/sbin/nologin' #创建一个用户,并指定用户的id,用户的家目录,用户的附加组,用户的shell
ansible db -m user -a 'name=ryan1 state=absent' #删除用户但是不删除用户的家目录
ansible db -m user -a 'name=ryan2 state=absent remove=yes' # 删除用户并删除用户的家目录

gid      # 组的id
name    # 组名
system   # 系统组
state
ansible db -m group -a 'name=ryan3 system=yes' #创建系统组
ansible db -m group -a 'name=ryan4 state=absent' # 删除组



ansible-doc –l
service：系统服务管理
cron：计划任务管理
yum：yum软件包安装管理
user：系统用户管理
group：系统用户组管理

synchronize：使用rsync同步文件
ansible test -m synchronize -a "src=data/ dest=/tmp/data  delete=yes rsync_opts=--exclude-from=exclude.list"

Ansible synchronize模块详解：
compress：开启压缩，默认为开启
archive：是否采用归档模式同步，保证源文件和目标文件属性一致
checksum：是否效验
dirs：以非递归的方式传送目录，默认是no（递归）
links：同步链接文件
recursive：是否递归yes/no
rsync_opts：使用rsync的参数
copy_links：同步的时候是否复制链接
delete：删除源中没有但目标存在的文件，使两边内容一样，以推送方为主
src：源目录及文件
dest：目标文件及目录
dest_port：目标接收的端口
rsync_path：服务的路径，指定rsync在远程服务器上执行
rsync_remote_user：设置远程用户名
–exclude=.log：忽略同步以.log结尾的文件，这个可以自定义忽略什么格式的文件，或者.txt等等都可以，但是由于这个是rsync命令的参数，所以必须和rsync_opts一起使用，比如rsync_opts=--exclude=.txt这种模式
mode：同步的模式，rsync同步的方式push、pull，默认是推送push，从本机推送给远程主机，pull表示从远程主机上拿文件
小明大强 


test.yml
---
- hosts: '{{ hosts }}'
  remote_user: root
  vars:
      http_port: 80
      max_clients: 200
  tasks:
    - name: test connection
      ping:

  tasks:
    - name: check selinux
      command: /sbin/getenforce
      register: result
      failed_when: false
  
    - name: 检查结果
      command: /sbin/setenforce 0
      ignore_errors: True
      when: result.rc == "Disabled"
     
    - name: install nload
      yum: name=nload state=present

  #tasks:
  #  - name: Copy file to client
  #    copy: src=/etc/ansible/hosts dest=/etc/ansible/hosts
  #          owner=root group=root mode=0644

  #构建多种条件
  #tasks:
  #  - include: wordpress.yml wp_user=timmy
  #  - include: wordpress.yml wp_user=alice
  #  - include: wordpress.yml wp_user=bob


  #从模版拷贝文件
  #template: src=templates/foo.j2 dest=/etc/foo.conf
  #notify:
  #   - restart apache
  # handlers: #由notify 触发
  #  - name: restart apache
  #    service: name=httpd state=restarted
  
ansible-playbook test.yml  --extra-vars hosts=tnhg


ansible-playbook --check http01.yml --extra-vars "user=`date +%Y-%m-%d`"

#### 使用时间变量
  - name: Get timestamp from the system
    shell: "date +%Y-%m-%d%H-%M-%S"
    register: tstamp

  - name: var-def
    set_fact:
      cur_date: "{{ tstamp.stdout[0:10]}}"
      cur_time: "{{ tstamp.stdout[10:]}}"
      cur_time_ns: "{{ tstamp.stdout[10:]}}"

  - name: System timestamp - date
    debug:
      msg:  "{{ cur_date }}"


多级目录

site.yml
webservers.yml
fooservers.yml
roles/
   common/
     files/
     templates/
     tasks/
     handlers/
     vars/
     defaults/
     meta/
   webservers/
     files/
     templates/
     tasks/
     handlers/
     vars/
     defaults/
     meta/


一个 playbook 如下:
---
- hosts: webservers
  roles:
     - common
     - webservers


这个 playbook 为一个角色 ‘x’ 指定了如下的行为：

    如果 roles/x/tasks/main.yml 存在, 其中列出的 tasks 将被添加到 play 中
    如果 roles/x/handlers/main.yml 存在, 其中列出的 handlers 将被添加到 play 中
    如果 roles/x/vars/main.yml 存在, 其中列出的 variables 将被添加到 play 中
    如果 roles/x/meta/main.yml 存在, 其中列出的 “角色依赖” 将被添加到 roles 列表中 (1.3 and later)
    所有 copy tasks 可以引用 roles/x/files/ 中的文件，不需要指明文件的路径。
    所有 script tasks 可以引用 roles/x/files/ 中的脚本，不需要指明文件的路径。
    所有 template tasks 可以引用 roles/x/templates/ 中的文件，不需要指明文件的路径。
    所有 include tasks 可以引用 roles/x/tasks/ 中的文件，不需要指明文件的路径。



## 常用模块
ping
ansible all -m ping

主机信息收集
ansible all -m setup -a 'filter=ansible_distribution_version'

ansible k8s -m setup | grep distribution

command
ansible all -a 'date'

cron
ansible db -m cron -a 'minute="*/10" job="/bin/echo hello" name="test cron job" state="present"'
present（添加（默认值））or absent（移除）

user
添加
ansible db -m user -a 'name="testops" password="0lwTSmqKOkL."'
删除
ansible db -m user -a 'name="testops" state="absent" remove="yes"'

copy
ansible db -m copy -a 'src=/etc/hosts dest=/tmp/ owner=root mode=640 backup=no'
添加文件内容
ansible db -m copy -a 'content="Hello ansible\n you are clever!\n" dest=/tmp/ansile.txt owner=root mode=640 backup=no'

file
ansible db -m file -a "src=/etc/fstab dest=/tmp/fstab state=link"

yum
ansible web -m yum -a 'name=httpd state=latest'

service 
ansible web -m service -a 'enabled=yes name=httpd state=started'
ansible web -a 'systemctl is-enabled httpd'

shell 复杂命令
ansible web -m shell -a "ps -ef|grep httpd"

再服务器上执行本地脚本
ansible db -m script -a '/tmp/script.sh'

mount
ansible test -m mount 'name=/mnt src=/dev/loop0 fstype=ext4 state=mounted opts=rw'

geturl
- name: download foo.conf
  get_url: url=http://example.com/path/file.conf dest=/etc/foo.conf mode=0440