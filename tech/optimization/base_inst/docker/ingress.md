k8s服务暴露 ingress负载均衡

helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace

or

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.1.1/deploy/static/provider/cloud/deploy.yaml


kubectl get pods --namespace=ingress-nginx

检查启动就绪
kubectl wait --namespace ingress-nginx \
 --for=condition=ready pod \
 --selector=app.kubernetes.io/component=controller \
 --timeout=120s

测试

kubectl create deployment demo --image=httpd --port=80
kubectl expose deployment demo

创建
kubectl create ingress demo-localhost --class=nginx \
 --rule=demo.localdev.me/*=demo:80

端口转发
kubectl port-forward --namespace=ingress-nginx service/ingress-nginx-controller 8080:80


ingress.yml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ingress-nginx
  annotations:
    # use the shared ingress-nginx
    kubernetes.io/ingress.class: "nginx"
spec:
  rules:
  - host: nginx.kube.com
    http:
      paths:
      - path: /
        backend:
          serviceName: nginx
          servicePort: 80
