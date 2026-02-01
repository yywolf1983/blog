# sh兼容的一行命令
# find . \( -name "*.txt" -o -name "*.sgf" -o -name "*.SGF" \) -type f -exec vim -e -c "set fileencoding=utf-8" -c "wq" {} \;
find . \( -name "*.txt" -o -name "*.sgf" -o -name "*.SGF" \) -type f -exec sh -c '
for file; do
    # 检查编码，使用sh兼容的语法
    if file -b "$file" | grep -q "UTF-8"; then
        echo "跳过(UTF-8): $file"
    else
        echo "转换: $file"
        cp "$file" "$file.backup"
        if vim -e -s -c "set bomb" -c "set fileencoding=utf-8" -c "wq" "$file" 2>/dev/null; then
            echo "✓ 完成"
            rm "$file.backup"
        else
            echo "✗ 失败"
            mv "$file.backup" "$file"
        fi
    fi
done
' sh {} +
