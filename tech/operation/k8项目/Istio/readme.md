service mesh

Envoy 默认代理
    xDS 协议


istio
    连接（代理注入） 安全 流量控制 观察


istio 支持 四层 七层


kubectl create namespace istio-system

helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update

helm install istio-base istio/base -n istio-system

helm install istiod istio/istiod -n istio-system --wait

网关可选
kubectl create namespace istio-ingress
kubectl label namespace istio-ingress istio-injection=enabled
helm install istio-ingress istio/gateway -n istio-ingress --wait



helm install \
  --namespace istio-system \
  --set auth.strategy="anonymous" \
  --repo https://kiali.org/helm-charts \
  kiali-server \
  kiali-server

kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.13/samples/addons/prometheus.yaml

kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.13/samples/addons/jaeger.yaml

获取 token
kubectl get secrets -n istio-system
kubectl describe secrets -n istio-system kiali-token-2fz92


helm uninstall --namespace istio-system kiali-server


kubectl create ingress kiali --class=nginx \
 --rule=test.usda.one/kiali=kiali:20001 -n istio-system