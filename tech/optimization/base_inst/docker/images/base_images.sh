#!/bin/bash
#
# 用法示例：
#   sudo ./build-debian12-rootfs.sh
#   sudo ./build-debian12-rootfs.sh /opt/docker-rootfs/debian12-base.tar.gz
#
# 默认会生成 /tmp/debian12-rootfs.tar.gz

set -e

# ---------- 可配置参数 ----------
DEBIAN_SUITE="${DEBIAN_SUITE:-bookworm}"      # Debian 12 的代号
MIRROR_URL="${MIRROR_URL:-http://mirrors.aliyun.com/debian}"
ROOTFS_DIR="${ROOTFS_DIR:-/tmp/debian12-rootfs}"
OUTPUT_TAR="${1:-/tmp/debian12-rootfs.tar.gz}"
# --------------------------------

echo "================================================="
echo " 开始制作 Debian ${DEBIAN_SUITE} rootfs"
echo " 镜像源: ${MIRROR_URL}"
echo " 输出文件: ${OUTPUT_TAR}"
echo "================================================="

# 1. 安装依赖
echo "[1/5] 安装 debootstrap（若未安装）..."
if ! command -v debootstrap >/dev/null 2>&1; then
    if command -v apt-get >/dev/null 2>&1; then
        sudo apt-get update
        sudo apt-get install -y debootstrap
    else
        echo "错误：未找到 apt-get，且未安装 debootstrap。"
        exit 1
    fi
else
    echo "debootstrap 已安装，跳过安装步骤。"
fi

# 2. 创建并清理工作目录
echo "[2/5] 准备工作目录 ${ROOTFS_DIR} ..."
sudo rm -rf "${ROOTFS_DIR}"
sudo mkdir -p "${ROOTFS_DIR}"

# 3. 使用 debootstrap 创建 rootfs
echo "[3/5] 使用 debootstrap 创建 ${DEBIAN_SUITE} rootfs ..."
sudo debootstrap \
    --arch=amd64 \
    --variant=minbase \
    "${DEBIAN_SUITE}" \
    "${ROOTFS_DIR}" \
    "${MIRROR_URL}"

echo "=> rootfs 创建完成。"

# 4. (可选) 进入 chroot 环境进行自定义
# 例如安装常用工具：bash、iproute2、procps、net-tools、vim、less 等
# 如果不需要，可直接注释或删除以下代码块
# ----------------------------------------------------
echo "[4/5] (可选) 进入 chroot 环境安装额外软件包 ..."
sudo mount --bind /proc "${ROOTFS_DIR}/proc"
sudo mount --bind /sys  "${ROOTFS_DIR}/sys"
sudo mount --bind /dev  "${ROOTFS_DIR}/dev"

sudo chroot "${ROOTFS_DIR}" /bin/bash <<'EOF'
set -e
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y --no-install-recommends \
    bash \
    coreutils \
    iproute2 \
    procps \
    net-tools \
    openssh-client \
    curl \
    wget \
    less \
    vim
rm -rf /var/lib/apt/lists/*
EOF


sudo umount "${ROOTFS_DIR}/proc" "${ROOTFS_DIR}/sys" "${ROOTFS_DIR}/dev"
echo "=> 额外软件包安装完成。"
# ----------------------------------------------------

# 5. 打包 rootfs
echo "[5/5] 打包 rootfs 为 ${OUTPUT_TAR} ..."
sudo tar -C "${ROOTFS_DIR}" -c . | gzip -9 > "${OUTPUT_TAR}"

echo "================================================="
echo " 制作完成！"
echo " 输出文件: ${OUTPUT_TAR}"
echo "================================================="
