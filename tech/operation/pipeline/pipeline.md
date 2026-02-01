node {
  script{
       build_tag = sh(returnStdout:true, script:'git show -s').trim()
  }
  stage('send msg'){
    rocketSend message: "发布成功 发布消息如下: \n ${build_tag} \n\n",channel: '#devops', serverUrl: 'https://rc.arche.network/', trustSSL: true, webhookTokenCredentialId: '599b354c-a745-473e-896a-332c52471c11'
  }
}