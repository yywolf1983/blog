
# rust

## install 

curl --proto '=https' --tlsv1.3 https://sh.rustup.rs -sSf | sh

termux
https://rust-lang.github.io/rustup/installation/other.html

mkdir -p ~/.zfunc
rustup completions zsh > ~/.zfunc/_rustup
fpath+=~/.zfunc

export RUSTUP_UPDATE_ROOT=https://mirrors.tuna.tsinghua.edu.cn/rustup/rustup
export RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup

RUSTUP_USE_CURL=1 rustup update

cd ~/.cargo/bin
cat << EOF > rustup.sh
rust_list="cargo  cargo-clippy  cargo-fmt  clippy-driver  rust-gdb  rust-gdbgui  rust-lldb  rustc  rustdoc  rustfmt"
rust_path=~/.rustup/toolchains/stable-aarch64-unknown-linux-musl/bin

for i in \$rust_list
do
unlink \$i
echo \$i
cp \$rust_path/\$i \$i
done
EOF

source "$HOME/.cargo/env"

## 交叉编译

cat << EOF > ~/.cargo/config.toml
[target.x86_64-unknown-linux-musl]
linker = "rust-lld"
rustflags = ["-C", "linker-flavor=ld.lld"]
EOF

    rustc --print target-list
    or
    rustup target list

    rustup target add aarch64-linux-android
    cargo build --target aarch64-linux-android

## base

rustc main.rs

rustc --version
cargo --version

## Cargo.toml

[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"

[dependencies]

cargo build
cargo run
cargo check



## wasm-pack

 curl https://rustwasm.github.io/wasm-pack/installer/init.sh -sSf | sh 



    Run wasm-pack new hello-wasm.
    cd hello-wasm
    Run wasm-pack build.
    This tool generates files in a pkg dir
    To publish to npm, run wasm-pack publish. You may need to login to the registry you want to publish to. You can login using wasm-pack login.


### wasm 转 js
wasm2js pkg/wasm2js_bg.wasm -o pkg/wasm2js_bg.wasm.js


## rustup

rustup default stable  # nightly
rustup toolchain list

设置当前项目版本
rustup override set nightly

rustup update