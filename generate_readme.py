#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成README.md文件的脚本
为每个子目录生成README.md文件，包含该目录下所有文件的名称和链接
"""

import os
import re


def generate_readme(directory):
    """
    为指定目录生成README.md文件
    
    Args:
        directory: 目录路径
    """
    # 获取目录下的所有文件和子目录
    items = os.listdir(directory)
    
    # 过滤掉README.md文件本身
    items = [item for item in items if item != 'README.md']
    
    # 按名称排序
    items.sort()
    
    # 生成README.md内容
    readme_content = f"# {os.path.basename(directory)} 目录\n\n"
    readme_content += "## 文件列表\n\n"
    
    for item in items:
        item_path = os.path.join(directory, item)
        # 计算相对路径（相对于博客根目录）
        relative_path = os.path.relpath(item_path, "d:\\download\\aaa\\blog").replace('\\', '/')
        
        if os.path.isdir(item_path):
            # 是目录，添加目录链接
            readme_content += f"- **[{item}/](viewer.html?file={relative_path}/README.md)**\n"
        else:
            # 是文件，添加文件链接
            readme_content += f"- **[{item}](viewer.html?file={relative_path})**\n"
    
    # 写入README.md文件
    readme_path = os.path.join(directory, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print(f"生成了 {readme_path}")


def main():
    """
    主函数，遍历所有子目录并生成README.md文件
    """
    # 从程序当前目录开始遍历
    root_dir = os.getcwd()
    
    for root, dirs, files in os.walk(root_dir):
        # 跳过.git目录和其他隐藏目录
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        # 为当前目录生成README.md
        generate_readme(root)


if __name__ == "__main__":
    main()
