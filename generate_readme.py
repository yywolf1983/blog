#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成站点文件树配置文件（filetree.yaml）

旧方案：为每个目录生成一个 index.md —— 全站散落上百个文件，维护麻烦
新方案：仅在站点根目录生成单一配置文件，由 viewer.html 读取并渲染目录

用法：
    python3 generate_readme.py                  # 生成/更新 filetree.yaml
    python3 generate_readme.py --clean-index    # 删除历史生成的 index.md
    python3 generate_readme.py --output x.yaml  # 指定输出文件名
"""

import argparse
import os
import sys
from datetime import datetime

# 默认输出文件（位于站点根目录）
DEFAULT_OUTPUT = "filetree.yaml"

# 不出现在目录列表中的条目（含配置文件自身与自动生成物）
IGNORE_ITEMS = {
    "index.md",
    "filetree.yaml",
    ".DS_Store",
    "Thumbs.db",
    ".git",
    ".gitattributes",
    ".gitignore",
    "__pycache__",
    "node_modules",
}


def build_tree(root_dir, output_name):
    """扫描目录树，返回 {相对目录路径: {'dirs': [...], 'files': [...]}}"""
    tree = {}

    for root, dirnames, filenames in os.walk(root_dir):
        # 统一过滤：隐藏项与忽略项既不展示也不递归
        dirnames[:] = sorted(
            d for d in dirnames
            if not d.startswith(".") and d not in IGNORE_ITEMS
        )
        files = sorted(
            f for f in filenames
            if not f.startswith(".") and f not in IGNORE_ITEMS and f != output_name
        )

        rel = os.path.relpath(root, root_dir).replace("\\", "/")
        rel = "" if rel == "." else rel
        tree[rel] = {"dirs": list(dirnames), "files": files}

    return tree


def yaml_quote(text):
    return '"' + str(text).replace("\\", "\\\\").replace('"', '\\"') + '"'


def dump_yaml(tree, output_name, root_title):
    """序列化为 YAML（手写，避免依赖 PyYAML）"""
    lines = [
        "# 站点文件树配置",
        "# 由 generate_readme.py 自动生成，请勿手动编辑",
        "generated_at: " + yaml_quote(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        "root_title: " + yaml_quote(root_title),
        "config_file: " + yaml_quote(output_name),
        "ignore:",
    ]

    for item in sorted(IGNORE_ITEMS):
        lines.append("  - " + yaml_quote(item))

    lines.append("dirs:")

    # 根目录排在最前，其余按路径排序
    for path in sorted(tree.keys(), key=lambda p: (p != "", p)):
        node = tree[path]
        lines.append("  " + yaml_quote(path) + ":")
        for key in ("dirs", "files"):
            items = node[key]
            if not items:
                lines.append("    " + key + ": []")
            else:
                lines.append("    " + key + ":")
                for it in items:
                    lines.append("      - " + yaml_quote(it))

    return "\n".join(lines) + "\n"


def clean_index(root_dir):
    """删除历史生成的 index.md（可用 git 恢复）"""
    removed = []
    for root, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d != ".git"]
        if "index.md" in filenames:
            path = os.path.join(root, "index.md")
            os.remove(path)
            removed.append(os.path.relpath(path, root_dir).replace("\\", "/"))
    return removed


def main():
    parser = argparse.ArgumentParser(description="生成站点文件树配置")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="输出配置文件名")
    parser.add_argument("--clean-index", action="store_true", help="删除历史生成的 index.md")
    parser.add_argument("--root-title", default="blog", help="根目录展示名称")
    args = parser.parse_args()

    root_dir = os.getcwd()
    output_path = os.path.join(root_dir, args.output)

    # 配置文件自身也要排除，避免扫描时把自己算进去
    global IGNORE_ITEMS
    IGNORE_ITEMS = set(IGNORE_ITEMS) | {args.output}

    if args.clean_index:
        removed = clean_index(root_dir)
        print(f"已删除 {len(removed)} 个 index.md")
        for r in removed:
            print("  - " + r)
        if not removed:
            print("未找到 index.md")
        return

    tree = build_tree(root_dir, args.output)
    content = dump_yaml(tree, args.output, args.root_title)

    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    total_dirs = len(tree)
    total_files = sum(len(n["files"]) for n in tree.values())
    print(f"已生成 {args.output}")
    print(f"  目录: {total_dirs} 个")
    print(f"  文件: {total_files} 个")


if __name__ == "__main__":
    main()
