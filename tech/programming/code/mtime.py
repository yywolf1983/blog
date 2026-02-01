import argparse
from datetime import datetime, timedelta
import sys

def calculate_date_difference(start_date, end_date=None):
    """
    计算两个日期之间的差值
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d") if end_date else datetime.now()
    
    # 确保结束日期晚于开始日期
    if end < start:
        start, end = end, start
    
    delta = end - start
    return start, end, delta

def format_detailed_output(days):
    """
    将天数转换为详细的中文描述（年、月、周、天）
    """
    years = days // 365
    months = (days % 365) // 30
    weeks = (days % 365 % 30) // 7
    remaining_days = days % 365 % 30 % 7
    
    parts = []
    if years > 0:
        parts.append(f"{years}年")
    if months > 0:
        parts.append(f"{months}个月")
    if weeks > 0:
        parts.append(f"{weeks}周")
    if remaining_days > 0:
        parts.append(f"{remaining_days}天")
    
    return "".join(parts) if parts else "0天"

def main():
    parser = argparse.ArgumentParser(
        description="日期差计算工具 - 支持简化输出和详细中文描述",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        'start_date',
        nargs='?',  # 设为可选参数，支持交互式输入
        type=str,
        help='起始日期（格式: YYYY-MM-DD）'
    )
    
    parser.add_argument(
        '-e', '--end_date',
        type=str,
        default=None,
        help='结束日期（格式: YYYY-MM-DD），不提供则使用当前日期'
    )
    
    parser.add_argument(
        '-s', '--simple',
        action='store_true',
        help='简化输出，只显示天数'
    )
    
    parser.add_argument(
        '-d', '--detailed',
        action='store_true',
        help='详细输出，显示年/月/周/天的完整描述'
    )
    
    parser.add_argument(
        '-a', '--all',
        action='store_true',
        help='显示所有输出格式'
    )
    
    args = parser.parse_args()
    
    # 交互式输入处理
    if not args.start_date:
        print("📅 日期差计算工具（输入格式: YYYY-MM-DD）")
        args.start_date = input("请输入起始日期: ").strip()
        end_input = input("请输入结束日期（直接回车使用今天）: ").strip()
        args.end_date = end_input if end_input else None
    
    try:
        start, end, delta = calculate_date_difference(args.start_date, args.end_date)
        days = delta.days
        
        # 输出结果
        print("\n" + "="*50)
        print("📊 日期差计算结果")
        print("="*50)
        print(f"起始日期: {start.strftime('%Y年%m月%d日')}")
        print(f"结束日期: {end.strftime('%Y年%m月%d日')}")
        print("-"*50)
        
        # 根据参数选择输出格式
        if args.simple or not (args.detailed or args.all):
            print(f"简化输出: {days}天")
        
        if args.detailed or args.all:
            detailed_str = format_detailed_output(days)
            print(f"详细输出: {detailed_str}")
        
        if args.all:
            # 显示所有可能的时间单位
            total_seconds = int(delta.total_seconds())
            weeks = days // 7
            remaining_days = days % 7
            
            print(f"完整输出: {days}天（{weeks}周{remaining_days}天）")
            print(f"总小时数: {total_seconds // 3600}小时")
            print(f"总分钟数: {total_seconds // 60}分钟")
            print(f"总秒数: {total_seconds}秒")
            
            # 额外信息
            start_weekday = start.strftime("%A")
            end_weekday = end.strftime("%A")
            print(f"起始日是: {start_weekday}")
            print(f"结束日是: {end_weekday}")
        
        print("="*50)
        
    except ValueError as e:
        print(f"❌ 错误：日期格式不正确！请使用 YYYY-MM-DD 格式。")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 发生错误：{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

