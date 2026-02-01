mkdir -p ~/.config/buildkit/

cat <<EOF > ~/.config/buildkit/buildkitd.toml
debug=true

[registry."docker.io"]
  mirrors = ["3.1.119.56:8090"]
  http = true
  insecure = true
EOF

docker buildx create --config=/Users/yy/.config/buildkit/buildkitd.toml

docker buildx use relaxed_pasteur

直接push
docker buildx build --platform linux/amd64 --push -t 3.1.119.56:8090/base/ubuntu2:latest -f Dockerfile .

load 到本地
docker buildx build --platform linux/amd64 --load -t 3.1.119.56:8090/base/ubuntu2:latest -f Dockerfile .


docker buildx ls
docker buildx rm