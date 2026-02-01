#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
四柱八字计算器 - 完整修正版
修复月份计算错误，优化时柱计算
"""

import sys
from datetime import datetime, timedelta
from typing import Dict, Tuple

class FourPillarsCalculator:
    def __init__(self):
        # 天干地支
        self.tiangan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        self.dizhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        
        # 十二生肖
        self.zodiac = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
        
        # 节气对应月支
        self.solar_terms_month_zhi = {
            "立春": "寅", "惊蛰": "卯", "清明": "辰", "立夏": "巳",
            "芒种": "午", "小暑": "未", "立秋": "申", "白露": "酉",
            "寒露": "戌", "立冬": "亥", "大雪": "子", "小寒": "丑"
        }
        
        # 节气近似日期（简化版）
        self.solar_terms_days = {
            1: ("小寒", 5), 2: ("立春", 4), 3: ("惊蛰", 5), 4: ("清明", 4),
            5: ("立夏", 5), 6: ("芒种", 5), 7: ("小暑", 7), 8: ("立秋", 7),
            9: ("白露", 7), 10: ("寒露", 8), 11: ("立冬", 7), 12: ("大雪", 7)
        }
        
        # 月支表
        self.month_zhi_list = ["寅", "卯", "辰", "巳", "午", "未", 
                              "申", "酉", "戌", "亥", "子", "丑"]
        
        # 五虎遁诀
        self.wuhudun = {
            "甲": "丙", "己": "丙", "乙": "戊", "庚": "戊",
            "丙": "庚", "辛": "庚", "丁": "壬", "壬": "壬",
            "戊": "甲", "癸": "甲"
        }
        
        # 时辰对应表
        self.shizhi_table = [
            ("子", 23, 1, 0),    # 子时: 23:00-1:00
            ("丑", 1, 3, 1),     # 丑时: 1:00-3:00
            ("寅", 3, 5, 2),     # 寅时: 3:00-5:00
            ("卯", 5, 7, 3),     # 卯时: 5:00-7:00
            ("辰", 7, 9, 4),     # 辰时: 7:00-9:00
            ("巳", 9, 11, 5),    # 巳时: 9:00-11:00
            ("午", 11, 13, 6),   # 午时: 11:00-13:00
            ("未", 13, 15, 7),   # 未时: 13:00-15:00
            ("申", 15, 17, 8),   # 申时: 15:00-17:00
            ("酉", 17, 19, 9),   # 酉时: 17:00-19:00
            ("戌", 19, 21, 10),  # 戌时: 19:00-21:00
            ("亥", 21, 23, 11),  # 亥时: 21:00-23:00
        ]
        
        # 基准日期（1900年1月1日为甲午日）
        self.base_date = datetime(1900, 1, 1)
        self.base_ganzhi_index = 30  # 甲午日的索引（甲=0, 午=6, 但按60甲子序）
    
    def calculate_year_pillar(self, year: int, month: int, day: int) -> Tuple[str, str]:
        """计算年柱"""
        # 以立春为年分界
        if month < 2 or (month == 2 and day < 4):
            year = year - 1
        
        # 计算年干支（1900年为庚子年）
        base_year = 1900  # 庚子年
        base_index = 36   # 庚子年在60甲子中的索引
        
        year_diff = year - base_year
        year_index = (base_index + year_diff) % 60
        
        year_gan_index = year_index % 10
        year_zhi_index = year_index % 12
        
        year_gan = self.tiangan[year_gan_index]
        year_zhi = self.dizhi[year_zhi_index]
        
        return f"{year_gan}{year_zhi}", year_gan
    
    def get_month_zhi(self, month: int, day: int) -> str:
        """获取月支"""
        # 简化处理：直接按月份分配月支
        month_zhi_map = {
            1: "丑",  2: "寅",  3: "卯",  4: "辰",  5: "巳",  6: "午",
            7: "未",  8: "申",  9: "酉", 10: "戌", 11: "亥", 12: "子"
        }
        
        # 2月4日立春后为寅月
        if month == 2 and day >= 4:
            return "寅"
        elif month == 2 and day < 4:
            return "丑"
        
        return month_zhi_map.get(month, "寅")
    
    def calculate_month_pillar(self, year: int, month: int, day: int, year_gan: str) -> str:
        """计算月柱"""
        month_zhi = self.get_month_zhi(month, day)
        
        # 使用五虎遁诀计算月干
        yin_month_gan = self.wuhudun.get(year_gan, "丙")
        yin_gan_index = self.tiangan.index(yin_month_gan)
        
        # 计算月支对应的偏移量
        month_zhi_index = self.month_zhi_list.index(month_zhi)
        month_gan_index = (yin_gan_index + month_zhi_index) % 10
        month_gan = self.tiangan[month_gan_index]
        
        return f"{month_gan}{month_zhi}"
    
    def calculate_day_pillar(self, year: int, month: int, day: int) -> str:
        """计算日柱 - 修正版"""
        try:
            # 创建目标日期
            target_date = datetime(year, month, day)
            
            # 计算与基准日期的天数差
            days_diff = (target_date - self.base_date).days
            
            # 计算干支索引
            ganzhi_index = (self.base_ganzhi_index + days_diff) % 60
            
            # 计算天干地支
            day_gan_index = ganzhi_index % 10
            day_zhi_index = ganzhi_index % 12
            
            day_gan = self.tiangan[day_gan_index]
            day_zhi = self.dizhi[day_zhi_index]
            
            return f"{day_gan}{day_zhi}"
            
        except Exception as e:
            raise ValueError(f"计算日柱错误: {e}")
    
    def calculate_hour_pillar(self, hour: int, minute: int, day_gan: str) -> str:
        """计算时柱 - 修正版"""
        # 处理分钟，45分后进入下一个时辰
        adjusted_hour = hour
        if minute >= 45:
            adjusted_hour = (hour + 1) % 24
        
        # 确定时支
        hour_zhi = "子"
        hour_zhi_index = 0
        
        for zhi, start, end, index in self.shizhi_table:
            if start <= end:  # 正常时间段
                if start <= adjusted_hour < end:
                    hour_zhi = zhi
                    hour_zhi_index = index
                    break
            else:  # 跨日的情况（子时）
                if adjusted_hour >= start or adjusted_hour < end:
                    hour_zhi = zhi
                    hour_zhi_index = index
                    break
        
        # 计算时干（日上起时法）
        # 甲己还加甲，乙庚丙作初，丙辛从戊起，丁壬庚子居，戊癸何方发，壬子是真途
        wushudun_map = {
            "甲": "甲", "己": "甲",  # 甲己日：甲子时起
            "乙": "丙", "庚": "丙",  # 乙庚日：丙子时起
            "丙": "戊", "辛": "戊",  # 丙辛日：戊子时起
            "丁": "庚", "壬": "庚",  # 丁壬日：庚子时起
            "戊": "壬", "癸": "壬"   # 戊癸日：壬子时起
        }
        
        start_gan = wushudun_map.get(day_gan, "甲")
        start_gan_index = self.tiangan.index(start_gan)
        
        # 计算时干
        hour_gan_index = (start_gan_index + hour_zhi_index) % 10
        hour_gan = self.tiangan[hour_gan_index]
        
        return f"{hour_gan}{hour_zhi}"
    
    def get_hour_info(self, hour: int, minute: int) -> Tuple[str, int, str]:
        """获取时辰信息"""
        adjusted_hour = hour
        if minute >= 45:
            adjusted_hour = (hour + 1) % 24
        
        for zhi, start, end, index in self.shizhi_table:
            if start <= end:
                if start <= adjusted_hour < end:
                    time_range = f"{start:02d}:00-{end:02d}:00"
                    return zhi, index, time_range
            else:
                if adjusted_hour >= start or adjusted_hour < end:
                    time_range = f"{start:02d}:00-{end:02d}:00"
                    return zhi, index, time_range
        
        return "子", 0, "00:00-00:00"
    
    def calculate_four_pillars(self, year: int, month: int, day: int, 
                               hour: int = 0, minute: int = 0) -> Dict:
        """计算四柱八字"""
        try:
            # 验证日期有效性
            datetime(year, month, day)
            
            if not (0 <= hour <= 23):
                raise ValueError("小时必须在0-23之间")
            if not (0 <= minute <= 59):
                raise ValueError("分钟必须在0-59之间")
            
            # 计算各柱
            year_pillar, year_gan = self.calculate_year_pillar(year, month, day)
            month_pillar = self.calculate_month_pillar(year, month, day, year_gan)
            day_pillar = self.calculate_day_pillar(year, month, day)
            day_gan = day_pillar[0]
            hour_pillar = self.calculate_hour_pillar(hour, minute, day_gan)
            
            # 时辰信息
            hour_zhi, hour_index, time_range = self.get_hour_info(hour, minute)
            
            # 计算生肖
            year_zhi = year_pillar[1]
            zodiac_index = self.dizhi.index(year_zhi)
            zodiac = self.zodiac[zodiac_index]
            
            result = {
                "date": f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}",
                "four_pillars": {
                    "year": year_pillar,
                    "month": month_pillar,
                    "day": day_pillar,
                    "hour": hour_pillar
                },
                "zodiac": zodiac,
                "hour_info": {
                    "hour_zhi": hour_zhi,
                    "time_range": time_range,
                    "hour": hour,
                    "minute": minute,
                    "adjusted": minute >= 45
                }
            }
            
            return result
            
        except ValueError as e:
            raise e
        except Exception as e:
            raise ValueError(f"计算四柱时出错: {e}")


def print_simple_result(result):
    """简化输出结果"""
    fp = result['four_pillars']
    print(f"{fp['year']} {fp['month']} {fp['day']} {fp['hour']}")


def print_detailed_result(result):
    """详细输出结果"""
    print("\n" + "=" * 60)
    print("四柱八字计算结果")
    print("=" * 60)
    print(f"出生时间: {result['date']}")
    print(f"生    肖: {result['zodiac']}")
    
    # 时辰信息
    hour_info = result['hour_info']
    print(f"时    辰: {hour_info['hour_zhi']}时 ({hour_info['time_range']})")
    if hour_info['adjusted']:
        print(f"时辰调整: {hour_info['minute']}分 ≥ 45分，已进入下一时辰")
    
    print("-" * 60)
    
    fp = result['four_pillars']
    print("四柱八字:")
    print(f"  年柱: {fp['year']}")
    print(f"  月柱: {fp['month']}")
    print(f"  日柱: {fp['day']}")
    print(f"  时柱: {fp['hour']}")
    
    print("=" * 60)


def main():
    # 解析命令行参数
    args = sys.argv[1:]
    
    # 检查简化输出标志
    simple_output = False
    simplify_flags = ["--simple", "-s"]
    for flag in simplify_flags:
        if flag in args:
            simple_output = True
            args = [arg for arg in args if arg != flag]
    
    # 处理输入参数
    if len(args) == 0:
        # 无参数：使用当前时间
        now = datetime.now()
        year, month, day = now.year, now.month, now.day
        hour, minute = now.hour, now.minute
        if not simple_output:
            print(f"使用当前时间: {year}年{month}月{day}日 {hour:02d}:{minute:02d}")
    
    elif len(args) >= 3:
        try:
            year = int(args[0])
            month = int(args[1])
            day = int(args[2])
            
            # 处理时间参数
            if len(args) >= 4:
                hour = int(args[3])
            else:
                hour = 0
                
            if len(args) >= 5:
                minute = int(args[4])
            else:
                minute = 0
                
        except (ValueError, IndexError) as e:
            print(f"参数错误: {e}")
            print("用法: python sizhu_fixed.py [年 月 日 [时 [分]]] [--simple]")
            return
    else:
        print("四柱八字计算器 - 完整修正版")
        print("=" * 60)
        print("用法:")
        print("  1. python sizhu_fixed.py")
        print("      - 使用当前时间计算")
        print("  2. python sizhu_fixed.py 年 月 日 [时] [分]")
        print("      - 指定日期和时间计算")
        print("  3. python sizhu_fixed.py --simple 年 月 日 时 分")
        print("      - 简化输出模式")
        print()
        print("示例:")
        print("  python sizhu_fixed.py")
        print("  python sizhu_fixed.py 2025 1 1")
        print("  python sizhu_fixed.py 1983 2 28 19 30")
        print("  python sizhu_fixed.py --simple 1983 2 28 19 30")
        return
    
    try:
        # 计算四柱
        calculator = FourPillarsCalculator()
        result = calculator.calculate_four_pillars(year, month, day, hour, minute)
        
        # 输出结果
        if simple_output:
            print_simple_result(result)
        else:
            print_detailed_result(result)
            
    except ValueError as e:
        print(f"错误: {e}")
    except Exception as e:
        print(f"计算错误: {e}")


if __name__ == "__main__":
    # 测试你的具体日期
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        print("测试 1983年2月28日19:30 的四柱:")
        calculator = FourPillarsCalculator()
        result = calculator.calculate_four_pillars(1983, 2, 28, 19, 30)
        print_detailed_result(result)
    else:
        main()

