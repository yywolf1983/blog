
# mysql cluster
helm pull bitnami/mysql

sudo helm upgrade --install dev-mysql -f mysql-dev.yaml bitnami/mysql
kubectl apply -f mysql-pv.yaml