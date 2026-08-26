

cp gitea-dump-1786257249.zip gitea:/var/lib/gitea/

# open bash session in container

docker exec --user git -it gitea bash  
 
# unzip your backup file within the container

unzip gitea-dump-1610949662.zip  

# restore the app.ini  

mv app.ini /etc/gitea/app.ini

# restore the gitea data

mv data/* /var/lib/gitea

# restore the repositories itself
# 注意这里要改到用户下

mv repos/* /var/lib/gitea/git/repositories
mv repos/* /var/lib/gitea/git/repositories/用户名
# adjust file permissions

chown -R git:git /etc/gitea/app.ini /var/lib/gitea

# Regenerate Git Hooks

/usr/local/bin/gitea -c '/etc/gitea/app.ini' admin regenerate hooks
