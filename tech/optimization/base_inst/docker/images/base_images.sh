#!/bin/bash
#
# 用法示例：
#   sudo ./build-debian12-rootfs.sh
#   sudo ./build-debian12-rootfs.sh /opt/docker-rootfs/debian12-base.tar.gz
#
# 默认会生成 /tmp/debian12-rootfs.tar.gz

set -e

# ---------- 可配置参数 ----------
DEBIAN_SUITE="${DEBIAN_SUITE:-bookworm}"      # 修正为 bookworm
MIRROR_URL="${MIRROR_URL:-https://mirrors.tuna.tsinghua.edu.cn/debian}"
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

# 4. 配置安全更新源
echo "[4/5] 配置安全更新源和安装软件包..."
sudo mount --bind /proc "${ROOTFS_DIR}/proc"
sudo mount --bind /sys  "${ROOTFS_DIR}/sys"
sudo mount --bind /dev  "${ROOTFS_DIR}/dev"

sudo chroot "${ROOTFS_DIR}" /bin/bash <<'EOF'
set -e
export DEBIAN_FRONTEND=noninteractive

# 配置完整的源列表（包括安全更新）
cat > /etc/apt/sources.list <<'SOURCES_EOF'
deb http://deb.debian.org/debian/ bookworm main contrib non-free
deb http://deb.debian.org/debian/ bookworm-updates main contrib non-free
deb http://deb.debian.org/debian-security/ bookworm-security main contrib non-free
SOURCES_EOF

# 更新并安装软件包
apt-get update
apt-get upgrade -y
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
    vim \
    ca-certificates

# 清理
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EOF

sudo umount "${ROOTFS_DIR}/proc" "${ROOTFS_DIR}/sys" "${ROOTFS_DIR}/dev"
echo "=> 软件包安装和配置完成。"

# 5. 打包 rootfs
echo "[5/5] 打包 rootfs 为 ${OUTPUT_TAR} ..."
sudo tar -C "${ROOTFS_DIR}" -c . | gzip -9 > "${OUTPUT_TAR}"

echo "================================================="
echo " 制作完成！"
echo " 输出文件: ${OUTPUT_TAR}"
echo "================================================="