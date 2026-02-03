#!/bin/bash 
 
 # 专注解决Firefox证书导入问题的终极脚本 
 # 生成真正的CA证书，避免"这不是一个证书颁发机构证书"的错误 
 
 set -e  # 遇到错误立即退出 
 
 DOMAIN="${1:-localhost}" 
 DAYS=3650 
 CERT_DIR="./certs" 
 mkdir -p ${CERT_DIR} 
 
 # 文件路径定义 
 CA_KEY="${CERT_DIR}/myca.key"           # CA私钥（必须保密） 
 CA_CRT="${CERT_DIR}/myca.crt"           # CA根证书（导入到Firefox的证书颁发机构） 
 SERVER_KEY="${CERT_DIR}/${DOMAIN}.key"  # 服务器私钥 
 SERVER_CSR="${CERT_DIR}/${DOMAIN}.csr"  # 证书签名请求 
 SERVER_CRT="${CERT_DIR}/${DOMAIN}.crt"  # 服务器证书 
 SERVER_P12="${CERT_DIR}/${DOMAIN}.p12"  # Firefox导入文件 
 CA_P12="${CERT_DIR}/myca.p12"           # CA的P12格式（备用） 
 CONF_FILE="${CERT_DIR}/openssl.cnf"     # OpenSSL配置文件 
 PASSWORD="123456" 
 
 # 颜色定义 
 RED='\033[0;31m' 
 GREEN='\033[0;32m' 
 YELLOW='\033[1;33m' 
 BLUE='\033[0;34m' 
 NC='\033[0m' 
 
 log_info() { echo -e "${GREEN}[INFO]${NC} $1"; } 
 log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; } 
 log_error() { echo -e "${RED}[ERROR]${NC} $1"; } 
 
 echo "🔐 生成真正的证书颁发机构(CA)和服务器证书..." 
 echo "⚠️  目标域名: ${DOMAIN}" 
 echo "⚠️  证书目录: ${CERT_DIR}" 
 
 # 检查OpenSSL是否安装 
 if ! command -v openssl &> /dev/null; then 
     log_error "OpenSSL未安装，请先安装OpenSSL" 
     exit 1 
 fi 
 
 # 创建详细的OpenSSL配置文件 
 log_info "创建OpenSSL配置文件..." 
 cat > ${CONF_FILE} << EOF 
 [ ca ] 
 default_ca = CA_default 
 
 [ CA_default ] 
 dir              = ${CERT_DIR} 
 certs            = \$dir 
 crl_dir          = \$dir/crl 
 database         = \$dir/index.txt 
 new_certs_dir    = \$dir/newcerts 
 certificate      = \$dir/myca.crt 
 serial           = \$dir/serial 
 private_key      = \$dir/myca.key 
 RANDFILE         = \$dir/.rand 
 default_days     = ${DAYS} 
 default_crl_days = 30 
 default_md       = sha256 
 preserve         = no 
 policy           = policy_match 
 
 [ policy_match ] 
 countryName             = match 
 stateOrProvinceName     = match 
 organizationName        = match 
 organizationalUnitName  = optional 
 commonName              = supplied 
 emailAddress            = optional 
 
 [ req ] 
 default_bits        = 2048 
 distinguished_name  = req_distinguished_name 
 req_extensions      = v3_req 
 x509_extensions     = v3_ca 
 prompt              = no 
 utf8                = yes 
 
 [ req_distinguished_name ] 
 countryName             = CN 
 stateOrProvinceName     = Beijing 
 localityName            = Beijing 
 organizationName        = My Local CA 
 commonName              = My Local Certificate Authority 
 
 [ v3_ca ] 
 subjectKeyIdentifier    = hash 
 authorityKeyIdentifier  = keyid:always,issuer:always 
 basicConstraints        = critical, CA:true 
 keyUsage                = critical, digitalSignature, cRLSign, keyCertSign 
 
 [ v3_req ] 
 basicConstraints        = CA:FALSE 
 keyUsage                = digitalSignature, keyEncipherment 
 extendedKeyUsage        = serverAuth, clientAuth 
 subjectAltName          = @alt_names 
 
 [ alt_names ] 
 DNS.1 = ${DOMAIN} 
 DNS.2 = *.${DOMAIN} 
 IP.1  = 127.0.0.1 
 IP.2  = ::1 
 EOF 
 
 # 初始化CA数据库 
 log_info "初始化CA数据库..." 
 mkdir -p "${CERT_DIR}/newcerts" 
 echo "01" > "${CERT_DIR}/serial" 
 touch "${CERT_DIR}/index.txt" 
 
 # 步骤1: 生成CA私钥和根证书 
 log_info "步骤 1/5: 生成CA私钥和根证书..." 
 openssl genrsa -out ${CA_KEY} 2048 
 openssl req -new -x509 -days ${DAYS} -key ${CA_KEY} -out ${CA_CRT} \ 
   -config ${CONF_FILE} -extensions v3_ca 
 
 # 验证CA证书 
 if openssl x509 -in ${CA_CRT} -text -noout | grep -q "CA:TRUE"; then 
     log_info "✅ CA证书验证通过" 
 else 
     log_error "❌ CA证书验证失败" 
     exit 1 
 fi 
 
 # 步骤2: 生成服务器证书 
 log_info "步骤 2/5: 生成服务器证书..." 
 openssl genrsa -out ${SERVER_KEY} 2048 
 
 # 创建服务器证书请求配置 
 cat > ${CERT_DIR}/server_req.cnf << EOF 
 [ req ] 
 default_bits        = 2048 
 distinguished_name  = req_distinguished_name 
 req_extensions      = v3_req 
 prompt              = no 
 
 [ req_distinguished_name ] 
 countryName             = CN 
 stateOrProvinceName     = Beijing 
 localityName            = Beijing 
 organizationName        = My Local CA 
 commonName              = ${DOMAIN} 
 
 [ v3_req ] 
 basicConstraints        = CA:FALSE 
 keyUsage                = digitalSignature, keyEncipherment 
 extendedKeyUsage        = serverAuth, clientAuth 
 subjectAltName          = @alt_names 
 
 [ alt_names ] 
 DNS.1 = ${DOMAIN} 
 DNS.2 = *.${DOMAIN} 
 IP.1  = 127.0.0.1 
 IP.2  = ::1 
 EOF 
 
 openssl req -new -key ${SERVER_KEY} -out ${SERVER_CSR} \ 
   -config ${CERT_DIR}/server_req.cnf 
 
 # 使用CA证书签发服务器证书 
 openssl ca -batch -in ${SERVER_CSR} -out ${SERVER_CRT} \ 
   -config ${CONF_FILE} -extensions v3_req 
 
 # 步骤3: 生成导入文件 
 log_info "步骤 3/5: 生成导入文件..." 
 openssl pkcs12 -export -inkey ${SERVER_KEY} -in ${SERVER_CRT} \ 
   -out ${SERVER_P12} -passout pass:${PASSWORD} -name "${DOMAIN} Certificate" 
 
 # 步骤4: 验证证书链 
 log_info "步骤 4/5: 验证证书链..." 
 if openssl verify -CAfile ${CA_CRT} ${SERVER_CRT} > /dev/null 2>&1; then 
     log_info "✅ 证书链验证通过" 
 else 
     log_error "❌ 证书链验证失败" 
     exit 1 
 fi 
 
 # 步骤5: 设置文件权限 
 log_info "步骤 5/5: 设置文件权限..." 
 chmod 600 ${CA_KEY} 
 chmod 644 ${CA_CRT} 
 chmod 600 ${SERVER_KEY} 
 chmod 644 ${SERVER_CRT} 
 
 # 最终输出 
 echo "" 
 echo "🎉 所有证书生成完成！" 
 echo "" 
 echo "📁 生成的文件清单 (位于 ${CERT_DIR}/):" 
 echo "   🔑 ${CA_KEY} - CA私钥 (保密文件)" 
 echo "   📜 ${CA_CRT} - CA根证书 (导入Firefox的关键文件)" 
 echo "   🔐 ${SERVER_KEY} - 服务器私钥 (Nginx配置使用)" 
 echo "   📄 ${SERVER_CRT} - 服务器证书 (Nginx配置使用)" 
 echo "   🌐 ${SERVER_P12} - Firefox导入文件" 
 echo "" 
 
 # 验证信息 
 echo "🔍 证书验证信息:" 
 echo "CA证书类型: $(openssl x509 -in ${CA_CRT} -text -noout | grep -q "CA:TRUE" && echo "✅ 这是CA证书" || echo "❌ 这不是CA证书")" 
 echo "服务器证书签发者: $(openssl x509 -in ${SERVER_CRT} -issuer -noout | cut -d= -f2-)" 
 echo "" 
 
 echo "🚀 使用指南:" 
 echo "1. Firefox导入: 将 ${CA_CRT} 导入到'证书颁发机构'" 
 echo "2. Nginx配置:" 
 echo "   ssl_certificate ${SERVER_CRT};" 
 echo "   ssl_certificate_key ${SERVER_KEY};" 
 echo "3. 访问: `https://${DOMAIN}` " 
 echo "" 
 
 echo "📝 Firefox导入详细步骤:" 
 echo "   1. Firefox地址栏输入: about:preferences#privacy" 
 echo "   2. 滚动到'安全'部分 → 点击'查看证书'" 
 echo "   3. 选择'证书颁发机构'标签页 → 点击'导入'" 
 echo "   4. 选择 ${CA_CRT} 文件" 
 echo "   5. 勾选'信任此CA以识别网站' → 确定" 
 echo "   6. 重启Firefox" 
 echo "" 
 
 echo "💡 提示:" 
 echo "- 如果Firefox仍有问题，尝试删除 cert9.db 缓存文件" 
 echo "- 确保访问的域名与证书中的域名一致" 
 echo "- 仅用于开发和测试环境"