#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
胎元和命宫计算程序
用法: python taiyuan_minggong.py 年柱 月柱 日柱 时柱
示例: python taiyuan_minggong.py 甲子 丙寅 戊辰 庚申
"""

import sys
import argparse

class TaiYuanMingGong:
    """胎元和命宫计算器"""
    
    TIAN_GAN = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    DI_ZHI = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    
    SHENG_XIAO = {
        "子": "鼠", "丑": "牛", "寅": "虎", "卯": "兔", "辰": "龙", "巳": "蛇",
        "午": "马", "未": "羊", "申": "猴", "酉": "鸡", "戌": "狗", "亥": "猪"
    }
    
    def __init__(self, nian_zhu: str, yue_zhu: str, ri_zhu: str, shi_zhu: str):
        """初始化四柱"""
        self.validate_input(nian_zhu, yue_zhu, ri_zhu, shi_zhu)
        
        self.nian_zhu = nian_zhu
        self.yue_zhu = yue_zhu
        self.ri_zhu = ri_zhu
        self.shi_zhu = shi_zhu
        
        self.nian_gan = nian_zhu[0]
        self.nian_zhi = nian_zhu[1]
        self.yue_gan = yue_zhu[0]
        self.yue_zhi = yue_zhu[1]
        self.shi_zhi = shi_zhu[1]
    
    def validate_input(self, *sizhu):
        """验证四柱输入"""
        for i, zhu in enumerate(sizhu):
            if len(zhu) != 2:
                sys.exit(f"错误: '{zhu}' 必须为两个字符，如'甲子'")
            
            gan, zhi = zhu[0], zhu[1]
            if gan not in self.TIAN_GAN:
                sys.exit(f"错误: 天干 '{gan}' 无效，应为{''.join(self.TIAN_GAN)}之一")
            if zhi not in self.DI_ZHI:
                sys.exit(f"错误: 地支 '{zhi}' 无效，应为{''.join(self.DI_ZHI)}之一")
    
    def calculate_taiyuan(self) -> str:
        """计算胎元: 月干进一位，月支进三位"""
        gan_idx = self.TIAN_GAN.index(self.yue_gan)
        zhi_idx = self.DI_ZHI.index(self.yue_zhi)
        
        tai_gan = self.TIAN_GAN[(gan_idx + 1) % 10]
        tai_zhi = self.DI_ZHI[(zhi_idx + 3) % 12]
        
        return f"{tai_gan}{tai_zhi}"
    
    def calculate_minggong(self) -> str:
        """计算命宫"""
        # 月份数字（正月为寅=1）
        month_num = (self.DI_ZHI.index(self.yue_zhi) - 2) % 12 + 1
        hour_num = self.DI_ZHI.index(self.shi_zhi) + 1
        
        # 命宫地支：(14 - 月 + 时) mod 12
        mg_zhi_num = (14 - month_num + hour_num) % 12
        mg_zhi_num = mg_zhi_num if mg_zhi_num != 0 else 12
        
        # 数字转地支
        mg_zhi = self.DI_ZHI[(mg_zhi_num + 1) % 12] if mg_zhi_num < 12 else self.DI_ZHI[1]
        
        # 五虎遁定天干
        yin_gan = {
            "甲": "丙", "乙": "戊", "丙": "庚", "丁": "壬", "戊": "甲",
            "己": "丙", "庚": "戊", "辛": "庚", "壬": "壬", "癸": "甲"
        }[self.nian_gan]
        
        yin_idx = self.TIAN_GAN.index(yin_gan)
        mg_zhi_idx = self.DI_ZHI.index(mg_zhi)
        yin_zhi_idx = 2  # 寅
        
        offset = (mg_zhi_idx - yin_zhi_idx) % 12
        mg_gan_idx = (yin_idx + offset) % 10
        mg_gan = self.TIAN_GAN[mg_gan_idx]
        
        return f"{mg_gan}{mg_zhi}"
    
    def calculate_shengong(self) -> str:
        """计算身宫"""
        month_num = (self.DI_ZHI.index(self.yue_zhi) - 2) % 12 + 1
        hour_num = self.DI_ZHI.index(self.shi_zhi) + 1
        
        # 身宫地支：(月 + 时 - 1) mod 12
        sg_zhi_num = (month_num + hour_num - 1) % 12
        sg_zhi_num = sg_zhi_num if sg_zhi_num != 0 else 12
        
        # 数字转地支
        sg_zhi = self.DI_ZHI[(sg_zhi_num + 1) % 12] if sg_zhi_num < 12 else self.DI_ZHI[1]
        
        # 天干计算同命宫
        yin_gan = {
            "甲": "丙", "乙": "戊", "丙": "庚", "丁": "壬", "戊": "甲",
            "己": "丙", "庚": "戊", "辛": "庚", "壬": "壬", "癸": "甲"
        }[self.nian_gan]
        
        yin_idx = self.TIAN_GAN.index(yin_gan)
        sg_zhi_idx = self.DI_ZHI.index(sg_zhi)
        yin_zhi_idx = 2
        
        offset = (sg_zhi_idx - yin_zhi_idx) % 12
        sg_gan_idx = (yin_idx + offset) % 10
        sg_gan = self.TIAN_GAN[sg_gan_idx]
        
        return f"{sg_gan}{sg_zhi}"
    
    def get_shengxiao(self, ganzhi: str) -> str:
        """获取生肖"""
        return self.SHENG_XIAO.get(ganzhi[1], "")
    
    def print_results(self, simple_mode=False):
        """输出结果"""
        taiyuan = self.calculate_taiyuan()
        minggong = self.calculate_minggong()
        shengong = self.calculate_shengong()
        
        if simple_mode:
            # 简洁输出
            print(f"四柱: {self.nian_zhu} {self.yue_zhu} {self.ri_zhu} {self.shi_zhu}")
            print(f"胎元: {taiyuan}({self.get_shengxiao(taiyuan)})")
            print(f"命宫: {minggong}({self.get_shengxiao(minggong)})")
            print(f"身宫: {shengong}({self.get_shengxiao(shengong)})")
        else:
            # 详细输出
            print("=" * 50)
            print("四柱八字胎元和命宫计算")
            print("=" * 50)
            print(f"输入四柱: {self.nian_zhu} {self.yue_zhu} {self.ri_zhu} {self.shi_zhu}")
            print()
            print("【胎元】")
            print(f"  结果: {taiyuan} ({self.get_shengxiao(taiyuan)})")
            print(f"  推算: 月柱{self.yue_zhu} → 月干{self.yue_gan}进1位, 月支{self.yue_zhi}进3位")
            print(f"  含义: 受孕月份，先天禀赋")
            print()
            print("【命宫】")
            print(f"  结果: {minggong} ({self.get_shengxiao(minggong)})")
            print(f"  推算: 年干{self.nian_gan}+月支{self.yue_zhi}+时支{self.shi_zhi}")
            print(f"  含义: 先天命运，性格基础")
            print()
            print("【身宫】")
            print(f"  结果: {shengong} ({self.get_shengxiao(shengong)})")
            print(f"  含义: 后天运势，努力成果")
            print("=" * 50)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='计算胎元和命宫',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  %(prog)s 甲子 丙寅 戊辰 庚申
  %(prog)s 乙丑 戊寅 辛未 癸巳 -s
  %(prog)s 庚午 己卯 壬戌 丙午 -j
        '''
    )
    
    parser.add_argument('sizhu', nargs=4, help='四柱: 年柱 月柱 日柱 时柱')
    parser.add_argument('-s', '--simple', action='store_true', help='简洁输出模式')
    parser.add_argument('-j', '--json', action='store_true', help='JSON输出格式')
    parser.add_argument('-e', '--example', action='store_true', help='显示示例')
    
    args = parser.parse_args()
    
    if args.example:
        print("四柱示例:")
        print("  甲子 丙寅 戊辰 庚申")
        print("  乙丑 戊寅 辛未 癸巳")
        print("  庚午 己卯 壬戌 丙午")
        print("  癸酉 甲子 丁亥 庚子")
        return
    
    try:
        nian_zhu, yue_zhu, ri_zhu, shi_zhu = args.sizhu
        calculator = TaiYuanMingGong(nian_zhu, yue_zhu, ri_zhu, shi_zhu)
        
        if args.json:
            import json
            result = {
                "四柱": {
                    "年柱": nian_zhu,
                    "月柱": yue_zhu,
                    "日柱": ri_zhu,
                    "时柱": shi_zhu
                },
                "计算结果": {
                    "胎元": {
                        "干支": calculator.calculate_taiyuan(),
                        "生肖": calculator.get_shengxiao(calculator.calculate_taiyuan())
                    },
                    "命宫": {
                        "干支": calculator.calculate_minggong(),
                        "生肖": calculator.get_shengxiao(calculator.calculate_minggong())
                    },
                    "身宫": {
                        "干支": calculator.calculate_shengong(),
                        "生肖": calculator.get_shengxiao(calculator.calculate_shengong())
                    }
                }
            }
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            calculator.print_results(args.simple)
            
    except SystemExit as e:
        print(f"错误: {e}")
    except Exception as e:
        print(f"计算错误: {e}")


if __name__ == "__main__":
    # 如果没有参数，显示使用方法
    if len(sys.argv) == 1:
        print(__doc__)
        print("\n使用方法: python taiyuan_minggong.py 年柱 月柱 日柱 时柱")
        print("示例: python taiyuan_minggong.py 甲子 丙寅 戊辰 庚申")
        print("\n添加 -h 参数查看详细帮助")
        sys.exit(1)
    
    main()

