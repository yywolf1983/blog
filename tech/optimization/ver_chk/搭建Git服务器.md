adduser git

grep git-shell /etc/shells || su -c "echo `which git-shell` >> /etc/shells"
usermod -s /usr/bin/git-shell git


git init --bare sample.git
chown -R git:git *


git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell


git clone git@server:/srv/sample.git


/home/git/.ssh/authorized_keys

