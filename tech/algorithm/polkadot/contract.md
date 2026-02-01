
## base

rustup component add rust-src --toolchain nightly
rustup target add wasm32-unknown-unknown --toolchain nightly

cargo install contracts-node --git https://github.com/paritytech/substrate-contracts-node.git --tag v0.20.0 --force --locked

brew install binaryen

cargo install dylint-link

cargo install cargo-contract --force

cargo contract --help

## create contract

cargo contract new flipper

cargo install cargo-dylint

## build contract

rustup toolchain install nightly-2022-08-15
rustup target add wasm32-unknown-unknown --toolchain nightly-2022-08-15
rustup component add rust-src --toolchain nightly-2022-08-15
cargo +nightly-2022-08-15 contract build

启动 substrate-contracts-node --dev

https://contracts-ui.substrate.io/

add flipper.contract

## template-node demo

https://github.com/substrate-developer-hub/substrate-node-template 

cargo run --release -- --dev --base-path ../my-chain/

cargo run --release -- purge-chain --base-path ../my-chain/  --chain local

purge-chain 清理数据

## 带合约的 substrate demo

git clone https://github.com/paritytech/substrate-contracts-node.git
git checkout v0.20.0

## 前端 demo

git clone https://github.com/substrate-developer-hub/substrate-front-end-template

cd substrate-front-end-template
yarn install
yarn start