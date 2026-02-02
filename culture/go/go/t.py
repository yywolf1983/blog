#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
from pathlib import Path

def check_sgf_ca_encoding(file_path):
    """
    检查SGF文件中CA[UTF-8]的位置和重复情况
    返回检查结果和详细信息
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        # 检查文件是否以SGF标准开头
        if not content.startswith('('):
            return {
                'status': 'error',
                'message': '不是有效的SGF文件格式'
            }
        
        # 查找根节点的结束位置（第一个分号后的内容）
        root_end = content.find(';', 1)
        if root_end == -1:
            return {
                'status': 'error',
                'message': 'SGF文件格式不完整'
            }
        
        # 提取根节点内容（从(;到第一个分号或)）
        root_content = content[2:root_end]
        
        # 检查CA属性是否存在（全局搜索，包括重复情况）
        ca_pattern = r'CA\s*\[\s*([^\]]+?)\s*\]'
        ca_matches = list(re.finditer(ca_pattern, content))
        
        if not ca_matches:
            return {
                'status': 'missing',
                'message': '缺少CA属性',
                'suggested_fix': '在根节点添加CA[UTF-8]'
            }
        
        # 检查重复的CA属性
        if len(ca_matches) > 1:
            ca_positions = []
            for match in ca_matches:
                # 计算CA属性在文件中的大致位置
                line_start = content.rfind('\n', 0, match.start()) + 1
                line_end = content.find('\n', match.end())
                if line_end == -1:
                    line_end = len(content)
                line_content = content[line_start:line_end].strip()
                ca_positions.append(f"位置: '{line_content}'")
            
            return {
                'status': 'duplicate',
                'message': f'发现 {len(ca_matches)} 个重复的CA属性',
                'details': ca_positions,
                'suggested_fix': '删除重复的CA属性，只保留根节点中的一个'
            }
        
        # 只有一个CA属性，检查其位置和值
        ca_match = ca_matches[0]
        encoding_value = ca_match.group(1).upper()
        
        # 检查CA是否在根节点内
        if ca_match.start() > root_end:
            return {
                'status': 'wrong_position',
                'message': 'CA属性不在根节点内',
                'suggested_fix': '将CA[UTF-8]移动到根节点开始处'
            }
        
        if encoding_value != 'UTF-8':
            return {
                'status': 'incorrect',
                'message': f'CA属性值不正确: {encoding_value}',
                'suggested_fix': '应改为CA[UTF-8]'
            }
        
        # 检查CA是否在正确位置（根节点内）
        # 验证CA前面没有其他节点内容
        before_ca = root_content[:ca_match.start()-2].strip()  # 减去(;的长度
        if before_ca and not re.match(r'^[A-Z]{1,2}\[[^\]]*\](\s+[A-Z]{1,2}\[[^\]]*\])*$', before_ca):
            return {
                'status': 'wrong_position',
                'message': 'CA属性位置可能不正确',
                'suggested_fix': 'CA应位于根节点开始处，与其他属性并列'
            }
        
        return {
            'status': 'correct',
            'message': 'CA[UTF-8]位置正确'
        }
        
    except UnicodeDecodeError:
        # 如果UTF-8解码失败，尝试其他编码
        try:
            with open(file_path, 'r', encoding='gbk') as f:
                content = f.read()
            return {
                'status': 'encoding_error',
                'message': '文件编码不是UTF-8，解码失败'
            }
        except:
            return {
                'status': 'error',
                'message': '文件编码无法识别'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': f'读取文件时出错: {str(e)}'
        }

def find_sgf_files(directory_path):
    """
    递归查找目录中的所有SGF文件（支持大小写后缀）
    """
    sgf_extensions = {'.sgf', '.SGF', '.Sgf'}  # 支持多种大小写变体
    sgf_files = []
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix in sgf_extensions:
                sgf_files.append(file_path)
    
    return sgf_files

def scan_sgf_files(directory_path):
    """
    扫描目录及所有子目录中的SGF文件
    """
    print(f"正在搜索目录: {directory_path}")
    sgf_files = find_sgf_files(directory_path)
    
    if not sgf_files:
        print(f"在目录 {directory_path} 及子目录中未找到SGF文件")
        print("支持的文件后缀: .sgf, .SGF, .Sgf")
        return
    
    results = {
        'correct': [],
        'missing': [],
        'incorrect': [],
        'duplicate': [],  # 新增：重复CA属性
        'wrong_position': [],
        'encoding_error': [],
        'error': []
    }
    
    print(f"找到 {len(sgf_files)} 个SGF文件，开始检查...\n")
    
    for i, file_path in enumerate(sgf_files, 1):
        result = check_sgf_ca_encoding(file_path)
        status = result['status']
        results[status].append((file_path, result))
        
        # 显示检查进度
        status_symbols = {
            'correct': '✓',
            'missing': '✗',
            'incorrect': '!',
            'duplicate': '↻',  # 重复符号
            'wrong_position': '?',
            'encoding_error': '�',
            'error': '×'
        }
        
        # 显示相对路径，便于查看文件位置
        try:
            relative_path = file_path.relative_to(directory_path)
        except:
            relative_path = file_path
        
        print(f"[{i:3d}/{len(sgf_files)}] {status_symbols.get(status, '?')} {relative_path}")
    
    # 输出统计结果
    print("\n" + "="*60)
    print("检查结果统计:")
    print("="*60)
    
    total_checked = sum(len(files) for files in results.values())
    print(f"\n总计检查文件: {total_checked}")
    
    for status, files in results.items():
        if files:
            print(f"\n{status.upper()}: {len(files)} 个文件")
            for file_path, result in files[:3]:  # 只显示前3个示例
                try:
                    relative_path = file_path.relative_to(directory_path)
                except:
                    relative_path = file_path
                print(f"  - {relative_path}: {result['message']}")
                
                # 显示重复CA的详细信息
                if status == 'duplicate' and 'details' in result:
                    for detail in result['details'][:2]:  # 显示前2个重复位置
                        print(f"    {detail}")
                    if len(result['details']) > 2:
                        print(f"    ... 还有 {len(result['details']) - 2} 个位置")
                
                if 'suggested_fix' in result:
                    print(f"    建议: {result['suggested_fix']}")
            
            if len(files) > 3:
                print(f"  ... 还有 {len(files) - 3} 个文件")
    
    return results

def fix_sgf_ca_encoding(file_path):
    """
    自动修复SGF文件中的CA编码问题
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否需要修复
        check_result = check_sgf_ca_encoding(file_path)
        
        if check_result['status'] == 'correct':
            print(f"✓ {file_path.name} 无需修复")
            return False
        
        # 修复逻辑
        if check_result['status'] == 'missing':
            # 在根节点添加CA[UTF-8]
            new_content = content.replace('(;', '(;CA[UTF-8]', 1)
            
        elif check_result['status'] == 'incorrect':
            # 替换错误的CA值
            ca_pattern = r'CA\s*\[\s*[^\]]+?\s*\]'
            new_content = re.sub(ca_pattern, 'CA[UTF-8]', content, count=1)
            
        elif check_result['status'] == 'duplicate':
            # 处理重复CA属性：删除所有CA，然后在根节点添加一个正确的
            ca_pattern = r'CA\s*\[\s*[^\]]+?\s*\]'
            # 先删除所有CA属性
            temp_content = re.sub(ca_pattern, '', content)
            # 在根节点添加正确的CA属性
            new_content = temp_content.replace('(;', '(;CA[UTF-8]', 1)
            
        elif check_result['status'] == 'wrong_position':
            # 移动CA属性到正确位置
            ca_pattern = r'CA\s*\[\s*([^\]]+?)\s*\]'
            ca_match = re.search(ca_pattern, content)
            if ca_match:
                # 保存CA值
                ca_value = ca_match.group(1)
                # 删除原来的CA
                temp_content = re.sub(ca_pattern, '', content, count=1)
                # 在根节点添加CA
                new_content = temp_content.replace('(;', f'(;CA[{ca_value}]', 1)
            else:
                new_content = content
        else:
            print(f"? {file_path.name} 需要手动修复: {check_result['message']}")
            return False
        
        # 备份原文件
        backup_path = file_path.with_suffix(file_path.suffix + '.backup')
        os.rename(file_path, backup_path)
        
        # 写入修复后的内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ {file_path.name} 已修复并备份到 {backup_path.name}")
        return True
        
    except Exception as e:
        print(f"× 修复 {file_path.name} 时出错: {str(e)}")
        return False

def batch_fix_files(directory_path, results):
    """
    批量修复文件
    """
    fixable_statuses = ['missing', 'incorrect', 'duplicate', 'wrong_position']
    files_to_fix = []
    
    for status in fixable_statuses:
        files_to_fix.extend(results[status])
    
    if not files_to_fix:
        print("没有需要修复的文件")
        return
    
    print(f"\n找到 {len(files_to_fix)} 个需要修复的文件:")
    for file_path, result in files_to_fix:
        try:
            relative_path = file_path.relative_to(directory_path)
        except:
            relative_path = file_path
        print(f"  - {relative_path}: {result['message']}")
    
    print("\n是否要自动修复这些文件? (y/n): ")
    choice = input().strip().lower()
    
    if choice == 'y':
        print(f"\n开始修复 {len(files_to_fix)} 个文件...")
        fixed_count = 0
        
        for i, (file_path, _) in enumerate(files_to_fix, 1):
            try:
                relative_path = file_path.relative_to(directory_path)
            except:
                relative_path = file_path
            
            print(f"[{i:3d}/{len(files_to_fix)}] 修复: {relative_path}")
            if fix_sgf_ca_encoding(file_path):
                fixed_count += 1
        
        print(f"\n修复完成: {fixed_count}/{len(files_to_fix)} 个文件已修复")
    else:
        print("已取消修复操作")

def show_duplicate_details(results):
    """
    显示重复CA属性的详细信息
    """
    duplicate_files = results.get('duplicate', [])
    if not duplicate_files:
        return
    
    print("\n" + "="*60)
    print("重复CA属性详细分析:")
    print("="*60)
    
    for file_path, result in duplicate_files:
        try:
            relative_path = file_path.relative_to(sys.argv[1])
        except:
            relative_path = file_path
        
        print(f"\n文件: {relative_path}")
        print(f"问题: {result['message']}")
        if 'details' in result:
            for i, detail in enumerate(result['details'], 1):
                print(f"  {i}. {detail}")
        print(f"建议: {result.get('suggested_fix', '手动检查并修复')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python check_sgf_ca.py <目录路径>")
        print("示例: python check_sgf_ca.py ./sgf_files")
        print("功能: 递归检查所有子目录中的SGF文件（支持.sgf/.SGF/.Sgf后缀）")
        sys.exit(1)
    
    directory = sys.argv[1]
    
    if not os.path.exists(directory):
        print(f"错误: 目录 {directory} 不存在")
        sys.exit(1)
    
    # 执行检查
    results = scan_sgf_files(directory)
    
    # 显示重复CA的详细信息
    if results and results.get('duplicate'):
        show_duplicate_details(results)
    
    # 如果有可修复的文件，询问是否修复
    if results:
        fixable_files = sum(len(results[status]) for status in ['missing', 'incorrect', 'duplicate', 'wrong_position'])
        if fixable_files > 0:
            batch_fix_files(directory, results)
