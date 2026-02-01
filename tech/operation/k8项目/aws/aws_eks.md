
## 设置自动伸缩 

eksctl create nodegroup \
  --cluster aws \
  --name lp \
  --node-type t3.medium \
  --nodes 6 \
  --nodes-min 4 \
  --nodes-max 30 \
  --ssh-access \
  --managed false \
  --ssh-public-key yy

