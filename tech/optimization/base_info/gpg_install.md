
***   ftp://ftp.gnupg.org/gcrypt/libgpg-error
***   ftp://ftp.gnupg.org/gcrypt/libgcrypt/
***   ftp://ftp.gnupg.org/gcrypt/libassuan/
***   ftp://ftp.gnupg.org/gcrypt/libksba/
***   ftp://ftp.gnupg.org/gcrypt/npth/
***   https://www.gnupg.org/
2.0.17 所需
ftp://ftp.gnu.org/gnu/pth/

libgpg-error
./configure --prefix=/opt2--enable-static
make && make install

libgcrypt
./configure --prefix=/opt2 --with-gpg-error-prefix=/opt2/
make && make install

libassuan
./configure --prefix=/opt2 --with-gpg-error-prefix=/opt2/
make && make install

libksba
./configure --prefix=/opt2 --with-gpg-error-prefix=/opt2/
make && make install

npth
./configure --prefix=/opt2
make && make install

2.0.17所需
pth
./configure --prefix=/opt2
make && make install

gnupg
./configure --prefix=/opt2  --with-gpg-error-prefix=/opt2/  --with-libgcrypt-prefix=/opt2/ --with-libassuan-prefix=/opt2/ --with-ksba-prefix=/opt2/ --with-npth-prefix=/opt2/

取消 DISPLAY 赋值
unset DISPLAY

安装  pinentry-curses
yum install   pinentry-curses

执行 gpg
建立 $HOME/.gnupg 目录

建立  gpg-agent.conf 添加如下参数
vi .gnupg/gpg-agent.conf
pinentry-program /usr/bin/pinentry-curses


ln -s /usr/lib64/libssl.so /usr/lib/
chmod o+rw $(tty)
echo $(tty)

#test
gpg2 --version
gpg-agent --homedir /home/debug/.gnupg --use-standard-socket --daemon
gpg2 --gen-key

签名（Sign） 认证（Certify） 加密（Encrypt） 身份验证（Authenticate）

gpg --help
gpg --gen-key
gpg --full-generate-key
gpg --gen-revoke  撤销证书
gpg --list-keys
gpg --delete-key
gpg --list-sigs   签名
gpg --fingerprint  指纹


gpg --list-secret-keys --keyid-format=long

输出秘钥
gpg --armor --output public-key.txt --export [用户ID]
gpg --armor --output private-key.txt --export-secret-keys
gpg -o ssb.key -a --export-secret-subkey 私钥id! # 感叹号是必要的

上传秘钥
gpg --send-keys [用户ID] --keyserver hkp://subkeys.pgp.net
gpg --fingerprint [用户ID]  指纹
导入公钥
gpg --import [密钥文件]
查找秘钥
gpg --keyserver hkp://subkeys.pgp.net --search-keys [用户ID]
加密
gpg --recipient [用户ID] --output demo.en.txt --encrypt demo.txt
gpg -e -r username filename 同上
 -c filename 临时加密 用自己的公钥 会需要临时密码
-a 输出文本 

解密
gpg --decrypt demo.en.txt --output demo.de.txt
or
gpg demo.en.txt

签名
gpg --sign demo.txt 二进制签名
gpg --clearsign demo.txt   ASCII 签名

独立签名 签名和文件分开
gpg --detach-sign demo.txt  独立签名
gpg --armor --detach-sign demo.txt  独立ASCII 签名

签名加密
gpg --local-user [发信者ID] --recipient [接收者ID] --armor --sign --encrypt demo.txt

验证签名
gpg --verify demo.txt.asc demo.txt

清理记住的密码
echo RELOADAGENT | gpg-connect-agent


## gpg ssh

添加密钥
gpg --expert --edit-key
addkey

expire 修改日期

trust  # 绝对信任
save

删除子密钥
key 1 选择子密钥
delkey 


gpg-connect-agent killagent /bye
gpg-connect-agent /bye
export SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-ssh-socket)
gpgconf --launch gpg-agent

gpg -K --with-keygrip

gpg --export-ssh-key 1E1CE35D1C75AD8D6684AAFB0846C2A5DCB96BFD


vi ~/.gnupg/sshcontrol
echo "1E1CE35D1C75AD8D6684AAFB0846C2A5DCB96BFD" > ~/.gnupg/sshcontrol

ssh-add -L


gpg --edit-key 


gpg --list-secret-keys --keyid-format=long
gpg --armor --export 3A072E03C0FC6768

termux 处理办法
pkg install p7zip gnupg okc-agent

gpg --export-ssh-key qihuang

MAC 禁止写入钥匙串
defaults read org.gpgtools.pinentry-mac DisableKeychain
defaults write org.gpgtools.pinentry-mac DisableKeychain -bool YES  # 禁止写入钥匙串

cat > ~/.gnupg/gpg-agent.conf << EOF
#enable-ssh-support
max-cache-ttl 1800
default-cache-ttl 1800

default-cache-ttl-ssh 1800
max-cache-ttl-ssh 1800

pinentry-program  /opt/homebrew/bin/pinentry-mac
allow-preset-passphrase
EOF

log加载
debug-all
debug-level guru
log-file "log.file"
verbose
verbose
verbose

add .zshrc
killall ssh-agent gpg-agent
unset GPG_AGENT_INFO SSH_AGENT_PID cSSH_AUTH_SOCK
eval $(gpg-agent --daemon --write-env-file ~/.gpg-agent-info --enable-ssh-support)
source ~/.gpg-agent-info

echo $SSH_AUTH_SOCK
ssh-add -L

## paperkey 备份

gpg --export-secret-key 密钥 ID  |   paperkey --output  secret-key-paper.asc 

恢复
paperkey --pubring public-key.gpg --secrets secret-key-paper.asc | gpg --import
恢复到文件
paperkey --pubring  public-key.gpg --secrets  secret-key-paper.asc --output  secret-key.gpg

导出二维码
gpg --export-secret-key yy | paperkey --output-type raw | qrencode --8bit --output secret-key.qr.png

从二维码恢复
zbarcam -1 --raw -Sbinary | paperkey --pubring public-key.gpg | gpg --import
zbarimg -1 --raw -q -Sbinary secret-key.qr.png | paperkey --pubring public-key.gpg | gpg --import