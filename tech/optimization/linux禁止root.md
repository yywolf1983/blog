# useradd -m -c "Admin User" admin
# passwd admin

# usermod -aG wheel admin    #CentOS/RHEL
# usermod -aG sudo admin     #Debian/Ubuntu

vim /etc/passwd
root:x:0:0:root:/root:/bin/bash
to
root:x:0:0:root:/root:/sbin/nologin

禁止tty设备
> mv /etc/securetty /etc/securetty.orig
> touch /etc/securetty
> chmod 600 /etc/securetty


> vim /etc/ssh/sshd_config
PermitRootLogin no

systemctl restart sshd

PAM 限制 (Pluggable Authentication Modules)
PAM，通过/lib/security/pam_listfile.so 模块，在限制特定帐户的权限方面具有很大的灵活性。
vim /etc/pam.d/login
OR
sudo vim /etc/pam.d/sshd
auth    required       pam_listfile.so \
        onerr=succeed  item=user  sense=deny  file=/etc/ssh/deniedusers


vim /etc/ssh/deniedusers
chmod 600 /etc/ssh/deniedusers

认证管理（auth），账号管理（account），会话管理（session）和密码（password）管理，
