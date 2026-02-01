
# WebAssembly

## wasm 安装

git clone <https://github.com/emscripten-core/emsdk.git>

    set -x
    set -e

    ./emsdk install latest
    ./emsdk activate latest
    source ./emsdk_env.sh --build=Release
    emcc -v

## 启动环境

source ./emsdk_env.sh --build=Release

    cat << EOF > hello.c
    #include <stdio.h>
    int main(int argc, char ** argv) {
    printf("Hello, world!\n");
    }
    EOF

## 生成字节码文件

emcc hello.c -o hello.html
emcc hello.c -s WASM=1 -o hello.js
