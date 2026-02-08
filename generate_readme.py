#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成index.md文件的脚本
为每个子目录生成index.md文件，包含该目录下所有文件的名称和链接
"""

import os
import re


def generate_index(directory):
    """
    为指定目录生成index.md文件
    
    Args:
        directory: 目录路径
    """
    # 获取目录下的所有文件和子目录
    items = os.listdir(directory)
    
    # 过滤掉index.md文件本身和系统专用文件/目录
    ignore_items = ['index.md', '.DS_Store', 'Thumbs.db', '.git', '.gitattributes', '.gitignore']
    items = [item for item in items if item not in ignore_items]
    
    # 按名称排序
    items.sort()
    
    # 生成index.md内容
    index_content = f"# {os.path.basename(directory)} 目录\n\n"
    index_content += "## 文件列表\n\n"
    
    for item in items:
        item_path = os.path.join(directory, item)
        # 计算相对路径（相对于博客根目录）
        root_dir = os.path.abspath('.')
        relative_path = os.path.relpath(item_path, root_dir).replace('\\', '/')
        
        if os.path.isdir(item_path):
            # 是目录，添加目录链接
            index_content += f"- **[{item}/](viewer.html?file={relative_path}/index.md)**\n"
        else:
            # 是文件，添加文件链接
            index_content += f"- **[{item}](viewer.html?file={relative_path})**\n"
    
    # 写入index.md文件
    index_path = os.path.join(directory, "index.md")
    with open(index_path, "w", encoding="utf-8", newline='\n') as f:
        f.write(index_content)
    
    print(f"生成了 {index_path}")


def main():
    """
    主函数，遍历所有子目录并生成index.md文件
    """
    # 从程序当前目录开始遍历
    root_dir = os.getcwd()
    
    for root, dirs, files in os.walk(root_dir):
        # 跳过.git目录和其他隐藏目录
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        # 为当前目录生成index.md
        generate_index(root)


if __name__ == "__main__":
    main()