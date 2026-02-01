vi /etc/pki/tls/openssl.cnf

[ ca ]
default_ca       = CA_default   

[ CA_default ]
dir             = /etc/pki/CA           # Where everything is kept
certs           = $dir/certs            # Where the issued certs are kept
crl_dir         = $dir/crl              # Where the issued crl are kept
database        = $dir/index.txt        # database index file.
#unique_subject = no                    # Set to 'no' to allow creation of
                                        # several ctificates with same subject.
new_certs_dir   = $dir/newcerts         # default place for new certs.

certificate     = $dir/cacert.pem       # The CA certificate
serial          = $dir/serial           # The current serial number
crlnumber       = $dir/crlnumber        # the current crl number
                                        # must be commented out to leave a V1 CRL
crl             = $dir/crl.pem          # The current CRL
private_key     = $dir/private/cakey.pem# The private key
RANDFILE        = $dir/private/.rand    # private random number file

[ req ]
distinguished_name = req_distinguished_name

[ req_distinguished_name ]
countryName = Country Name (2 letter code)
countryName_default = CN
stateOrProvinceName = State or Province Name (full name)
stateOrProvinceName_default = ShangHai
localityName = Locality Name (eg, city)
localityName_default = ShangHai
organizationalUnitName = Organizational Unit Name (eg, section)
organizationalUnitName_default = Domain Control Validated
commonName = Internet Widgits Ltd
commonName_max = 64

[ policy_anything ]
    countryName             = optional
    stateOrProvinceName     = optional
    localityName            = optional
    organizationName        = optional
    organizationalUnitName  = optional
    commonName              = supplied
    emailAddress            = optional

mkdir -p /etc/pki/CA
cd /etc/pki/CA
touch {index.txt,serial}; mkdir -p {certs,newcerts,crl,private}

--------------------
创建ca私钥
openssl genrsa -aes128 -passout pass:123456 -out private.key 4096

修改密码
openssl rsa -in private.key -aes256 -passout pass:123456 -out pr.key

--------------------
生成CA的证书签发申请文件 就是CA的crt文件 (公钥) 给客户的公钥

openssl req -new -x509 -passin pass:123456 -days 3650 -key private.key -subj  "/C=CN/ST=ZheJiang/L=HangZhou/O=D7home/OU=ITinfo/CN=D7home-CA" -config /etc/pki/tls/openssl.cnf -batch -out ca_cert.crt

sudo cp ca_cert.crt /etc/pki/CA/cacert.pem

 -req         产生证书签发申请命令
 -new         表示新请求
 -key         密钥
 -out         输出路径
 -subj        指定用户信息

写入序号
echo 01 > /etc/pki/CA/serial

rm -f /etc/pki/CA/index.txt
touch /etc/pki/CA/index.txt

--------------------
生成www的私钥
生成认证文件
openssl req -new -nodes -keyout images.key -subj "/C=CN/ST=ZheJiang/L=HangZhou/O=bs789/OU=ITinfo/CN=images.bs789.vip" -out images.csr

-keyout 生成新的证书
-key 使用已有证书

--------------------
颁发证书 www.pem
openssl ca -policy policy_anything  -config /etc/pki/tls/openssl.cnf -days 3650 -cert ca_cert.crt -keyfile private.key -in images.csr -out www.pem

解密私钥
openssl rsa -in www.key -out www.crt

验证证书
openssl verify -CAfile  ca的公钥  www.pem

给自己颁发证书
openssl req -new -nodes -newkey rsa:2048 -keyout private.key -subj "/C=CN/ST=ZheJiang/L=HangZhou/O=D7home/OU=ITinfo/CN=*.d7home.com" -out www.crt
openssl req -new -x509 -key private.key -subj "/C=CN/ST=ZheJiang/L=HangZhou/O=D7home/OU=ITinfo/CN=*.d7home.com" -out www.pem -days 3650


 x509        签发X.509格式证书命令。
 -req        表示证书输入请求。
 -days       表示有效天数,这里为10000天。
 -shal       表示证书摘要算法,这里为SHA1算法。
 -extensions 表示按OpenSSL配置文件v3_ca项添加扩展。
 -signkey    表示自签名密钥,这里为private/ca.key.pem。
 -in         表示输入文件,这里为private/ca.csr。
 -out        表示输出文件,这里为certs/ca.cer。


/C=CN/ST=ZheJiang/L=HangZhou/O=D7home/OU=ITinfo/CN=*.d7home.com

Country Name                ISO国家代码（两位字符）       CN
State or Province Name    所在省份  Shanghai
Locality Name               所在城市        Shanghai
Organization Name               公司名称    TrustAsia Technologies, Inc.
Organizational Unit Name        部门名称    IT Dept.
Common Name                   申请证书的域名
Email Address               不需要输入       
A challenge password        不需要输入         


#忽略证书
curl --insecure

#指定证书
curl --cacert cacert.pem

cp /etc/pki/tls/certs/ca-bundle.crt{,.bak}    #备份以防出错
cat /etc/pki/CA/cacert.pem >> /etc/pki/tls/certs/ca-bundle.crt

curl --cacert cacert.pem https://www.wuranju.com


openssl s_client -connect www.d7home.com:443 -prexit 查看服务器证书类型


# 查看KEY信息
> openssl rsa -noout -text -in myserver.key

# 查看CSR信息
> openssl req -noout -text -in myserver.csr

# 查看证书信息
> openssl x509 -noout -text -in ca.cst

keytool -v -list -keystore /usr/local/ssl_file/Tomcat/*.jks | grep DNS
openssl x509 -noout -text -in /usr/local/ssl_file/Nginx/*.crt | grep DNS



--------------------



导出p12格式根证书 windows相关
openssl pkcs12 -export -clcerts -passin pass:123456 -in ca_cert.csr -inkey private.key -out root.p12 / root.pfx

提取key
openssl pkcs12 -in ssl.pfx -nocerts -nodes -out mycert.key

导出公私钥
openssl rsa -in private.key -out demo_pri.pem
openssl rsa -in private.key -pubout -out demo_pub.pem

生成root.jks文件 #java用
keytool -import -v -trustcacerts -storepass 123456 -alias root -file ca_cert.pem -keystore root.jks


X.509
KEY - 通常用来存放一个公钥或者私钥

PEM - Privacy Enhanced Mail
DER - Distinguished Encoding Rules 二进制的   
    -inform der
CSR - Certificate Signing Request,证书签名请求
    查看的办法:openssl req -noout -text -in my.csr

CRT - CRT应该是certificate的三个字母
CER - 还是certificate

PFX/P12 - predecessor of PKCS#12,对*nix服务器来说,一般CRT和KEY是分开存放在不同文件中的,但Windows的IIS则将它们存在一个PFX文件中
    PFX转换为PEM编码 openssl pkcs12 -in for-iis.pfx -out for-iis.pem -nodes
JKS - 即Java Key Storage,这是Java的专利