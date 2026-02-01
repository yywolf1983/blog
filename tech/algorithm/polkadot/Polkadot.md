# Polkadot

## base

- |kusama| polkadot
-|-|-
决策部署时间 | 7day | 28day
优势 | 成本 | 安全
群体 | 初创 | 企业

rococo 平行链测试
wesrend 质押 拍卖 注册

Kusama 金丝雀网络

Substrate 开发框架 
Cumulus SDK 基于Substrate的Polkadot 平行链的工具


RocksDB 做存储

Merkle tree 效验

Rust 实现 libp2p

平行链     真实链 需要拍卖
    以上在网络 拍卖 众筹中拍卖
平行线程   依附于中继 按需付费
    以上在网络 平行线程中质押

平行链 （类似工厂，APP）
中继链  polkadot 核心链
验证器  polkadot 节点
    质押 验证人 需要节点 key

## 协议

Wasm 解释器和虚拟机。

XCPM 消息传递协议
NPOS 共识机制
BABE CRANDPA 共识算法
    https://research.web3.foundation/en/latest/polkadot/block-production/Babe.html
    https://github.com/w3f/consensus/blob/master/pdf/grandpa.pdf
libp2p p2p核心库
VRF 随机函数

## Substrate 构建

![Substrate-node](./images/Substrate-node.jpg)

git clone --branch polkadot-v0.9.25 https://github.com/substrate-developer-hub/substrate-node-template

rustup toolchain install nightly
rustup default nightly
rustup target add wasm32-unknown-unknown --toolchain nightly

rustup target add wasm32-unknown-unknown

cargo test --target wasm32-unknown-unknown

cargo build --package node-template --release

./target/release/node-template key inspect //Alice

./target/release/node-template --dev

## rpc

https://polkadot.js.org/docs/substrate/rpc/

HTTP 端点： http://localhost:9933/
Websocket端点： ws://localhost:9944/

curl -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "state_getMetadata"}' http://localhost:9933/

## app

Acala     兼容并升级
Moonbeam  兼容以太坊
Astar     solidity -> wasm

libp2p
jsonRPC

https://github.com/paritytech/parity-common.git
kvdb-rocksdb
kvdb-memorydb

## substrate 开发概念

https://github.com/paritytech/substrate.git

托盘
    FRAME 是 Framework for Runtime Aggregation of Modularized Entities
    https://docs.substrate.io/reference/frame-pallets/

    托盘文档
    https://paritytech.github.io/substrate/master/sc_service/all.html


rust
    https://doc.rust-lang.org/rust-by-example/
    https://doc.rust-lang.org/book/

    no_std
    https://docs.rust-embedded.org/book/intro/index.html


    https://github.com/polkadot-js/apps

合约
    https://github.com/paritytech/substrate-contracts-node

EVM兼容
    https://github.com/paritytech/frontier

web3基金会
    https://research.web3.foundation/en/latest/