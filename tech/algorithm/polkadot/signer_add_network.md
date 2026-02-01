
## base

git clone https://github.com/paritytech/substrate.git
cargo +nightly build --package subkey --release

export PATH=$PATH:/Users/yy/aaa/obj/polkadot/substrate/target/release/


## add network 

parity-signer/rust/generate_message

// e.g.
cargo run add-specs -d -u ws://127.0.0.1:9944 --encryption sr25519 --title test


brew install protobuf

cat sign_me_add_specs_substrate-contracts-node_sr25519 | subkey sign --suri "bottom drive obey lake curtain smoke basket hold race lonely fit walk//Alice"


// e.g.
cargo run --release make --goal qr --crypto sr25519 --msg add-specs --payload sign_me_add_specs_substrate-contracts-node_sr25519 --verifier-hex 0xd43593c715fdd31c61141abd04a99fd6822c8558854ccde39a5684e7a56da27d --signature-hex 969f3b1bda276fefefacfa1caac39d3da6175855bd25ec2aee340c242bf3f85e794ee204c0cc5aeed1c5547376af87e04ad7dce38d388a0dc553f6533d37a783

file 里生成 二维码


## add load-metadata
cargo run load-metadata -d -u ws://127.0.0.1:9944

cat sign_me_load_metadata_substrate-contracts-nodeV150 | subkey sign --suri "bottom drive obey lake curtain smoke basket hold race lonely fit walk//Alice"


// e.g.
cargo run --release make --goal qr --crypto sr25519 --msg load-metadata --payload sign_me_load_metadata_substrate-contracts-nodeV150 --verifier-hex 0xd43593c715fdd31c61141abd04a99fd6822c8558854ccde39a5684e7a56da27d --signature-hex 46677ca1bfed2fa17803230e084b32d3d3919139f48e1fd18ca8b6bd07ae5a177396e66e22acf841ae2a59703706f21182fd89ca7b677332534e48fc579a3484



