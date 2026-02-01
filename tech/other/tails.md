# tails

## mac 虚拟机 安装

QEMU

brew tap arthurk/homebrew-virt-manager
brew install virt-manager virt-viewer

brew services start libvirt

virt-manager -c "qemu:///session" --no-fork


'C:\Program Files\qemu\qemu-img.exe' create -f qcow linux.img 8G

cd 'C:\Program Files\qemu\'

.\qemu-system-x86_64.exe -m 8192 -smp 8,sockets=1 -hda D:\aaa\linux.img -usb -nic user,model=virtio -cdrom E:/download/tails-amd64-5.8.iso