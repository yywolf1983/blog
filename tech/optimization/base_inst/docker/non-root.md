id -u

grep ^$(whoami): /etc/subuid

sudo apt-get install -y dbus-user-session

/etc/sysctl.conf
kernel.unprivileged_userns_clone=1

sudo sysctl --system

sudo apt-get install -y fuse-overlayfs
sudo modprobe overlay permit_mounts_in_userns=1

slirp4netns --version

~/.local/share/docker


dockerd-rootless-setuptool.sh install

sudo apt-get install -y docker-ce-rootless-extras

systemctl --user start docker

systemctl --user enable docker

sudo loginctl enable-linger $(whoami)


## uninstall

dockerd-rootless-setuptool.sh uninstall
rootlesskit rm -rf ~/.local/share/docker

cd ~/bin

 rm -f containerd containerd-shim containerd-shim-runc-v2 ctr docker docker-init docker-proxy dockerd dockerd-rootless-setuptool.sh dockerd-rootless.sh rootlesskit rootlesskit-docker-proxy runc vpnkit


 docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /run/user/1000/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
