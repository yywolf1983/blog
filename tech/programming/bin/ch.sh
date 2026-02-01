#!/bin/bash
# 目录哈希检查工具 - 增强版
# 哈希文件名: 目录名.sha256
# 用法: dirhash.sh -g <目录>   # 生成哈希
#       dirhash.sh -c <目录>   # 检查哈希

set -euo pipefail

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# 帮助信息
show_help() {
    cat << EOF
目录哈希检查工具
默认哈希文件保存在: $SCRIPT_DIR
默认哈希文件名: 目录名.sha256

用法:
  $0 -g <目录>                    生成目录哈希基准
  $0 -c <目录>                    检查目录是否变化
  $0 -g <目录> -o <哈希文件>      生成哈希到指定文件
  $0 -c <目录> -i <哈希文件>      使用指定的哈希文件检查
  $0 -l                          列出所有哈希文件
  $0 -h                          显示此帮助

选项:
  -g, --generate <目录>          生成目录哈希
  -c, --check <目录>             检查目录是否变化
  -i, --input <哈希文件>          指定输入的哈希文件
  -o, --output <哈希文件>         指定输出的哈希文件
  -l, --list                     列出所有哈希文件
  -h, --help                     显示此帮助

示例:
  $0 -g /sdcard/Documents
  $0 -c /sdcard/Documents
  $0 -g /sdcard/Documents -o /sdcard/backup/docs.sha256
  $0 -c /sdcard/Documents -i /sdcard/backup/docs.sha256
  $0 -l
EOF
    exit 0
}

# 检查必要工具
check_rhash() {
    if ! command -v rhash &> /dev/null; then
        echo "错误: 需要安装 rhash"
        echo "Termux: pkg install rhash"
        echo "Linux:  apt install rhash"
        echo "macOS:  brew install rhash"
        exit 1
    fi
}

# 获取目录的哈希文件名
get_hash_filename() {
    local dir="$1"
    local dir_name=$(basename "$(realpath "$dir" 2>/dev/null || echo "$dir")")
    # 替换特殊字符
    dir_name=$(echo "$dir_name" | sed 's/[^a-zA-Z0-9._-]/_/g')
    echo "${dir_name}.sha256"
}

# 验证哈希文件格式
validate_hash_file() {
    local hash_file="$1"
    
    if [ ! -f "$hash_file" ]; then
        echo "错误: 哈希文件不存在: $hash_file"
        return 1
    fi
    
    # 检查文件是否有效（至少有一行哈希数据）
    if ! grep -q '^[a-fA-F0-9]\{64\}\s' "$hash_file" 2>/dev/null; then
        echo "错误: 不是有效的哈希文件: $hash_file"
        echo "      文件格式不正确，应该包含 rhash 生成的 SHA256 哈希"
        return 1
    fi
    
    return 0
}

# 列出哈希文件
list_hash_files() {
    echo "哈希文件列表 ($SCRIPT_DIR):"
    echo "================================"
    
    local count=0
    for file in "$SCRIPT_DIR"/*.sha256; do
        [ -e "$file" ] || continue
        count=$((count + 1))
        
        local fname=$(basename "$file")
        local size=$(wc -c < "$file" 2>/dev/null || echo "?")
        local lines=$(wc -l < "$file" 2>/dev/null | tr -d ' ' || echo "?")
        local dir_info=$(grep "^# 目录:" "$file" 2>/dev/null | head -1 | cut -d: -f2-)
        
        echo "📄 $fname"
        [ -n "$dir_info" ] && echo "   目录: $dir_info"
        echo "   大小: ${size} 字节, 行数: ${lines}"
        echo ""
    done
    
    if [ "$count" -eq 0 ]; then
        echo "暂无哈希文件"
    else
        echo "共找到 $count 个哈希文件"
    fi
}

# 生成目录哈希
generate_hash() {
    local dir="$1"
    local hash_file="${2:-}"  # 可选的输出文件
    
    if [ ! -d "$dir" ]; then
        echo "错误: 目录不存在: $dir"
        exit 1
    fi
    
    local dir_path=$(cd "$dir" && pwd 2>/dev/null || echo "$dir")
    
    # 如果未指定输出文件，使用默认文件名
    if [ -z "$hash_file" ]; then
        hash_file="$SCRIPT_DIR/$(get_hash_filename "$dir")"
    else
        # 确保输出文件是绝对路径
        if [[ "$hash_file" != /* ]]; then
            hash_file="$(pwd)/$hash_file"
        fi
    fi
    
    # 检查输出目录是否存在
    local output_dir=$(dirname "$hash_file")
    if [ ! -d "$output_dir" ]; then
        echo "错误: 输出目录不存在: $output_dir"
        exit 1
    fi
    
    echo "正在生成目录哈希..."
    echo "目录: $dir_path"
    echo "哈希文件: $hash_file"
    
    # 检查文件是否已存在
    if [ -f "$hash_file" ]; then
        read -p "哈希文件已存在，是否覆盖? (y/N): " confirm
        if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
            echo "操作已取消"
            exit 0
        fi
    fi
    
    # 生成哈希
    (cd "$dir_path" && rhash -r --sha256 .) > "$hash_file" 2>&1
    
    if [ $? -ne 0 ] || [ ! -s "$hash_file" ]; then
        echo "错误: 生成哈希失败"
        rm -f "$hash_file" 2>/dev/null || true
        exit 1
    fi
    
    # 添加基本信息
    local file_count=$(wc -l < "$hash_file" 2>/dev/null | tr -d ' ' || echo "0")
    local temp_file="$(dirname "$hash_file")/.tmp_$$.sha256"
    
    {
        echo "# 目录: $dir_path"
        echo "# 生成时间: $(date '+%Y-%m-%d %H:%M:%S')"
        echo "# 哈希文件: $hash_file"
        echo "# 文件数: $file_count"
        echo ""
        cat "$hash_file"
    } > "$temp_file" && mv "$temp_file" "$hash_file"
    
    echo ""
    echo "✓ 哈希生成完成"
    echo "文件数: $file_count"
    echo "哈希文件: $hash_file"
    echo ""
    echo "检查命令: $0 -c \"$dir\" -i \"$hash_file\""
}

# 检查目录是否变化
check_directory() {
    local dir="$1"
    local hash_file="${2:-}"  # 可选的输入文件
    
    if [ ! -d "$dir" ]; then
        echo "错误: 目录不存在: $dir"
        exit 1
    fi
    
    local dir_path=$(cd "$dir" && pwd 2>/dev/null || echo "$dir")
    
    # 如果未指定输入文件，使用默认文件名
    if [ -z "$hash_file" ]; then
        hash_file="$SCRIPT_DIR/$(get_hash_filename "$dir")"
    else
        # 确保输入文件是绝对路径
        if [[ "$hash_file" != /* ]]; then
            hash_file="$(pwd)/$hash_file"
        fi
    fi
    
    # 验证哈希文件
    if ! validate_hash_file "$hash_file"; then
        echo "请先生成哈希: $0 -g \"$dir\""
        exit 1
    fi
    
    echo "正在检查目录..."
    echo "目录: $dir_path"
    echo "哈希文件: $hash_file"
    
    # 显示基本信息
    if grep -q "^# " "$hash_file" 2>/dev/null; then
        echo ""
        echo "哈希文件信息:"
        grep "^# " "$hash_file" 2>/dev/null | head -4
    fi
    
    echo ""
    
    # 生成当前哈希
    local current_file="$SCRIPT_DIR/.current_$$.sha256"
    (cd "$dir_path" && rhash -r --sha256 .) > "$current_file" 2>&1
    
    if [ $? -ne 0 ] || [ ! -s "$current_file" ]; then
        echo "错误: 计算当前目录哈希失败"
        rm -f "$current_file" 2>/dev/null || true
        exit 1
    fi
    
    # 创建临时文件
    local old_hashes="$SCRIPT_DIR/.old_$$"
    local new_hashes="$SCRIPT_DIR/.new_$$"
    local diff_output="$SCRIPT_DIR/.diff_$$"
    
    # 提取纯哈希（排除注释行和空行，只保留哈希和文件路径）
    grep -v '^#' "$hash_file" 2>/dev/null | grep -v '^$' | sort > "$old_hashes"
    sort "$current_file" > "$new_hashes"
    
    # 使用 comm 比较文件，更准确
    diff "$old_hashes" "$new_hashes" > "$diff_output" || true
    
    if [ ! -s "$diff_output" ]; then
        echo "✓ 目录未发生变化"
        local result=0
    else
        echo "✗ 目录已发生变化"
        
        # 重新统计变化
        local added=0
        local removed=0
        
        # 统计新增/修改的文件（在 new_hashes 中但不在 old_hashes 中）
        comm -13 "$old_hashes" "$new_hashes" > "$SCRIPT_DIR/.added_$$" 2>/dev/null
        added=$(wc -l < "$SCRIPT_DIR/.added_$$" 2>/dev/null | tr -d ' ' || echo 0)
        
        # 统计删除的文件（在 old_hashes 中但不在 new_hashes 中）
        comm -23 "$old_hashes" "$new_hashes" > "$SCRIPT_DIR/.removed_$$" 2>/dev/null
        removed=$(wc -l < "$SCRIPT_DIR/.removed_$$" 2>/dev/null | tr -d ' ' || echo 0)
        
        echo ""
        echo "变化统计:"
        [ "$added" -gt 0 ] && echo "  新增/修改文件: $added"
        [ "$removed" -gt 0 ] && echo "  删除文件: $removed"
        
        # 显示部分变化
        if [ "$added" -gt 0 ]; then
            echo ""
            echo "新增/修改的文件(前5个):"
            head -5 "$SCRIPT_DIR/.added_$$" 2>/dev/null | while read -r line; do
                # 提取文件名（rhash 格式: 哈希值 文件名）
                local filename=$(echo "$line" | awk '{for(i=2;i<=NF;i++) printf "%s ", $i; print ""}' | sed 's/ $//')
                echo "  + $filename"
            done
        fi
        
        if [ "$removed" -gt 0 ]; then
            echo ""
            echo "删除的文件(前5个):"
            head -5 "$SCRIPT_DIR/.removed_$$" 2>/dev/null | while read -r line; do
                # 提取文件名
                local filename=$(echo "$line" | awk '{for(i=2;i<=NF;i++) printf "%s ", $i; print ""}' | sed 's/ $//')
                echo "  - $filename"
            done
        fi
        
        # 如果是修改而不是新增/删除，可以进一步分析
        if [ "$added" -eq "$removed" ] && [ "$added" -gt 0 ]; then
            echo ""
            echo "提示: 可能有 $added 个文件被修改（哈希值变化但文件数相同）"
        fi
        
        local result=1
    fi
    
    # 清理临时文件
    rm -f "$current_file" \
          "$old_hashes" \
          "$new_hashes" \
          "$diff_output" \
          "$SCRIPT_DIR/.added_$$" \
          "$SCRIPT_DIR/.removed_$$" \
          2>/dev/null || true
    
    exit $result
}

# 主函数
main() {
    check_rhash
    
    if [ $# -eq 0 ]; then
        show_help
    fi
    
    local mode=""
    local dir=""
    local input_file=""
    local output_file=""
    
    # 解析参数
    while [[ $# -gt 0 ]]; do
        case "$1" in
            -h|--help)
                show_help
                ;;
            -l|--list)
                list_hash_files
                exit 0
                ;;
            -g|--generate)
                mode="generate"
                if [ $# -ge 2 ] && [[ ! "$2" =~ ^- ]]; then
                    dir="$2"
                    shift
                else
                    echo "错误: -g 需要指定目录"
                    show_help
                fi
                ;;
            -c|--check)
                mode="check"
                if [ $# -ge 2 ] && [[ ! "$2" =~ ^- ]]; then
                    dir="$2"
                    shift
                else
                    echo "错误: -c 需要指定目录"
                    show_help
                fi
                ;;
            -i|--input)
                if [ $# -ge 2 ] && [[ ! "$2" =~ ^- ]]; then
                    input_file="$2"
                    shift
                else
                    echo "错误: -i 需要指定哈希文件"
                    show_help
                fi
                ;;
            -o|--output)
                if [ $# -ge 2 ] && [[ ! "$2" =~ ^- ]]; then
                    output_file="$2"
                    shift
                else
                    echo "错误: -o 需要指定哈希文件"
                    show_help
                fi
                ;;
            *)
                echo "错误: 未知参数: $1"
                show_help
                ;;
        esac
        shift
    done
    
    # 检查模式
    if [ -z "$mode" ]; then
        echo "错误: 请指定操作模式 (-g 或 -c)"
        show_help
    fi
    
    if [ -z "$dir" ]; then
        echo "错误: 请指定目录"
        show_help
    fi
    
    # 执行对应操作
    case "$mode" in
        generate)
            if [ -n "$input_file" ]; then
                echo "警告: -i 参数在生成模式下无效，忽略"
            fi
            generate_hash "$dir" "$output_file"
            ;;
        check)
            if [ -n "$output_file" ]; then
                echo "警告: -o 参数在检查模式下无效，忽略"
            fi
            check_directory "$dir" "$input_file"
            ;;
    esac
}

# 清理函数
cleanup() {
    rm -f "$SCRIPT_DIR"/.tmp_* \
          "$SCRIPT_DIR"/.current_*.sha256 \
          "$SCRIPT_DIR"/.old_* \
          "$SCRIPT_DIR"/.new_* \
          "$SCRIPT_DIR"/.diff_* \
          "$SCRIPT_DIR"/.added_* \
          "$SCRIPT_DIR"/.removed_* \
          2>/dev/null || true
}

# 设置陷阱
trap cleanup EXIT INT TERM

# 运行主函数
main "$@"

