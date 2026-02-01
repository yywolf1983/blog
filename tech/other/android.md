
keytool -genkeypair -alias yy -keyalg RSA -validity 100 -keystore yy.jks

jarsigner -verbose -sigalg SHA256withRSA -keystore yy.jks -signedjar signed.apk 未签名.apk yy

keytool -list -v -keystore xxx.jks


