import datetime
from datetime import datetime as dt
import sys
import subprocess
import os

# 日志配置
class Logger:
    def __init__(self):
        self.debug_mode = False
    
    def debug(self, msg):
        if self.debug_mode:
            print(f"[DEBUG] {msg}")
    
    def info(self, msg):
        print(f"[INFO] {msg}")
    
    def warning(self, msg):
        print(f"[WARNING] {msg}")
    
    def error(self, msg):
        print(f"[ERROR] {msg}")

logger = Logger()

class QiMenDunJia:
    def __init__(self, year_ganzhi, month_ganzhi, day_ganzhi, hour_ganzhi, 
             jieqi=None, yinyang=None, ju=None, method='zhebu',
             year=None, month=None, day=None, hour=None, minute=None):
        """初始化奇门遁甲排盘"""
        self.ganzhi_input = {
            'year': year_ganzhi,
            'month': month_ganzhi, 
            'day': day_ganzhi,
            'hour': hour_ganzhi
        }
        self.jieqi = jieqi
        self.yinyang_input = yinyang
        self.ju_input = ju
        self.method = method
        
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute or 0
            
        # 60甲子序列
        self.liujiazi = [
            "甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉",
            "甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未",
            "甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳",
            "甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯",
            "甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑",
            "甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"
        ]
        
        # 天干地支
        self.tiangan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        self.dizhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        self.jiuxing = ["天蓬", "天芮", "天冲", "天辅", "天英", "天柱", "天心", "天禽", "天任"]
        self.bamen = ["休", "生", "伤", "杜", "景", "死", "惊", "开"]
        self.bashen = ["值符", "螣蛇", "太阴", "六合", "白虎", "玄武", "九地", "九天"]
        
        # 初始化值符值使
        self.zhifu = None
        self.zhishi = None
        self.zhifu_pos = -1
        self.zhishi_pos = -1
        
        self.jieqi_list = [
            "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
            "立夏", "小满", "芒种", "夏至", "小暑", "大暑", 
            "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
            "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"
        ]
        
        # 节气日期表（每年可能有±1-2天误差，这里取最常见日期）
        # 格式：(月, 日, 节气名)
        self.jieqi_dates = [
            (1, 5, "小寒"), (1, 20, "大寒"),
            (2, 3, "立春"), (2, 18, "雨水"), (3, 5, "惊蛰"),
            (3, 20, "春分"), (4, 4, "清明"), (4, 20, "谷雨"),
            (5, 5, "立夏"), (5, 21, "小满"), (6, 5, "芒种"),
            (6, 21, "夏至"), (7, 7, "小暑"), (7, 22, "大暑"),
            (8, 7, "立秋"), (8, 23, "处暑"), (9, 7, "白露"),
            (9, 23, "秋分"), (10, 8, "寒露"), (10, 23, "霜降"),
            (11, 7, "立冬"), (11, 22, "小雪"), (12, 7, "大雪"), (12, 21, "冬至")
        ]
        
        self.gongwei = ["坎一宫", "坤二宫", "震三宫", "巽四宫", "中五宫", "乾六宫", "兑七宫", "艮八宫", "离九宫"]
        self.fangwei = ["北方", "西南", "东方", "东南", "中方", "西北", "西方", "东北", "南方"]
        
        # 初始化盘局
        # 修正__init__中的pan初始化
        self.pan = {
            'gongs': [{'gongwei': self.gongwei[i], 
                    'fangwei': self.fangwei[i],  # 新增字段
                    'tiangan': None, 
                    'dipan': None,
                    'bamen': None, 
                    'jiuxing': None, 
                    'bashen': None} for i in range(9)]
        }
        
    def parse_ganzhi(self, ganzhi):
        """解析干支"""
        if not ganzhi:
            raise ValueError("必须输入年月日时干支")
            
        result = {}
        for key in ['year', 'month', 'day', 'hour']:
            if key not in ganzhi:
                raise ValueError(f"缺少{key}干支")
                
            gz = ganzhi[key]
            if len(gz) != 2:
                raise ValueError(f"{key}干支'{gz}'格式错误")
                
            gan = gz[0]
            zhi = gz[1]
            
            if gan not in self.tiangan:
                raise ValueError(f"{key}天干'{gan}'无效")
            if zhi not in self.dizhi:
                raise ValueError(f"{key}地支'{zhi}'无效")
                
            result[key] = gz
            result[f'{key}_gan'] = gan
            result[f'{key}_zhi'] = zhi
            
        return result

    def validate_inputs(self):
        """验证输入 - 修复版"""
        errors = []
        
        # 验证干支格式和有效性
        try:
            self.ganzhi_info = self.parse_ganzhi(self.ganzhi_input)
        except ValueError as e:
            errors.append(str(e))
        
        # 验证干支组合的有效性（甲子、乙丑等合法组合）
        if not errors:
            errors.extend(self.validate_ganzhi_combinations())
        
        # 验证节气
        if self.jieqi and self.jieqi not in self.jieqi_list:
            errors.append(f"节气'{self.jieqi}'无效")
        
        # 验证阴阳
        if self.yinyang_input and self.yinyang_input not in ['阳', '阴']:
            errors.append("阴阳遁应为'阳'或'阴'")
        
        # 验证用局数
        if self.ju_input is not None:
            try:
                ju = int(self.ju_input)
                if ju < 1 or ju > 9:
                    errors.append("用局数应为1-9")
            except ValueError:
                errors.append("用局数应为数字")
        
        # 验证起局方法
        if self.method not in ['zhebu', 'zhirun', 'maoshan']:
            errors.append("起局方法无效，应为zhebu、zhirun或maoshan")
        
        if errors:
            return False, "\n".join(errors)
        return True, "验证通过"

    def validate_ganzhi_combinations(self):
        """验证干支组合的有效性"""
        errors = []
        
        # 简化60甲子生成逻辑
        valid_combinations = [self.tiangan[i%10] + self.dizhi[i%12] for i in range(60)]
        valid_combinations = set(valid_combinations)

        gan_cycle = self.tiangan * 6  # 扩展以便匹配
        zhi_cycle = self.dizhi * 5    # 扩展以便匹配
        
        for i in range(60):
            valid_combinations.add(gan_cycle[i] + zhi_cycle[i])
        
        # 检查每个干支组合
        for key in ['year', 'month', 'day', 'hour']:
            ganzhi = self.ganzhi_input[key]
            if ganzhi not in valid_combinations:
                errors.append(f"{key}干支'{ganzhi}'不是有效的干支组合")
        
        # 检查月令和节气的一致性（如果提供了月份和节气）
        if self.month and self.jieqi:
            jieqi_to_month = {
                "立春": 2, "雨水": 2, "惊蛰": 3, "春分": 3, "清明": 4, "谷雨": 4,
                "立夏": 5, "小满": 5, "芒种": 6, "夏至": 6, "小暑": 7, "大暑": 7,
                "立秋": 8, "处暑": 8, "白露": 9, "秋分": 9, "寒露": 10, "霜降": 10,
                "立冬": 11, "小雪": 11, "大雪": 12, "冬至": 12, "小寒": 1, "大寒": 1
            }
            expected_month = jieqi_to_month.get(self.jieqi)
            if expected_month and self.month != expected_month:
                errors.append(f"节气'{self.jieqi}'通常出现在{expected_month}月，但输入的月份是{self.month}月")
        
        return errors
        
    def determine_yinyang_ju(self):
        """确定阴阳遁和用局"""
        # 如果用户明确指定了阴阳和局数，直接使用
        if self.yinyang_input and self.ju_input:
            return self.yinyang_input, self.ju_input
        
        # 如果有节气，自动推断阴阳遁和用局
        if self.jieqi:
            yinyang = self.get_yinyang_from_jieqi(self.jieqi)
            ju = self.get_ju_from_jieqi(self.jieqi)
            return yinyang, ju
        
        # 尝试从日期自动推断节气
        if self.year and self.month and self.day:
            inferred_jieqi = self.get_jieqi_from_date(self.year, self.month, self.day)
            if inferred_jieqi:
                self.jieqi = inferred_jieqi
                yinyang = self.get_yinyang_from_jieqi(self.jieqi)
                ju = self.get_ju_from_jieqi(self.jieqi)
                return yinyang, ju
        
        # 无法自动确定
        raise ValueError("局数判定错误：无法自动确定节气。请输入节气（如冬至、立春等）或提供完整日期。\n完整格式：python qimen.py 年柱 月柱 日柱 时柱 节气 [阴阳] [用局]")
    
    def get_yinyang_from_jieqi(self, jieqi_name):
        """根据节气确定阴阳遁"""
        yang_dun_jieqi = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", 
                        "春分", "清明", "谷雨", "立夏", "小满", "芒种"]
        return '阳' if jieqi_name in yang_dun_jieqi else '阴'
    
    def get_jieqi_from_date(self, year, month, day):
        """根据日期自动推断节气"""
        if not all([year, month, day]):
            return None
        
        input_date = datetime.date(year, month, day)
        
        # 精确匹配（±1天容差）
        for offset in [0, -1, 1, -2, 2]:
            try:
                check_date = input_date + datetime.timedelta(days=offset)
                for jq_month, jq_day, jq_name in self.jieqi_dates:
                    if check_date.month == jq_month and check_date.day == jq_day:
                        return jq_name
            except:
                continue
        
        # 使用节气区间判断
        for i, (jq_month, jq_day, jq_name) in enumerate(self.jieqi_dates):
            jq_date = datetime.date(year, jq_month, jq_day)
            next_jq = self.jieqi_dates[(i + 1) % len(self.jieqi_dates)]
            next_month, next_day, next_name = next_jq
            
            # 处理跨年情况（年末节气到次年）
            if i == len(self.jieqi_dates) - 1:  # 冬至(12月21日)之后
                next_date = datetime.date(year + 1, next_month, next_day)
                if input_date >= jq_date or input_date < next_date:
                    return jq_name
            else:
                next_date = datetime.date(year, next_month, next_day)
                if jq_date <= input_date < next_date:
                    return jq_name
        
        return None
    
    def get_ju_from_jieqi(self, jieqi_name):
        """根据节气确定用局 - 修复版"""
        # 传统奇门用局表（阳遁）
        jieqi_ju_yang = {
            "冬至": 1, "小寒": 2, "大寒": 3, "立春": 8, "雨水": 9, "惊蛰": 1,
            "春分": 3, "清明": 4, "谷雨": 5, "立夏": 4, "小满": 5, "芒种": 6
        }
        
        # 阴遁用局表
        jieqi_ju_yin = {
            "夏至": 9, "小暑": 8, "大暑": 7, "立秋": 2, "处暑": 1, "白露": 9,
            "秋分": 7, "寒露": 6, "霜降": 5, "立冬": 6, "小雪": 5, "大雪": 4
        }
        
        # 确定当前节气属于阳遁还是阴遁
        yang_dun_jieqi = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", 
                        "春分", "清明", "谷雨", "立夏", "小满", "芒种"]
        
        if jieqi_name in yang_dun_jieqi:
            return jieqi_ju_yang.get(jieqi_name, 1)
        else:
            return jieqi_ju_yin.get(jieqi_name, 1)
    
    def pai_dipan(self, ju, yinyang):
        """排地盘：阳遁顺转，阴遁逆转
        传统规则：戊己庚辛壬癸丁丙乙九宫排列
        阳遁：从局数宫位顺时针排列
        阴遁：从局数宫位逆时针排列
        """
        # 阴遁序列：乙丙丁癸壬辛庚己戊（阳遁序列的逆序）
        wuxu_order_yang = ["戊", "己", "庚", "辛", "壬", "癸", "丁", "丙", "乙"]
        wuxu_order_yin = ["乙", "丙", "丁", "癸", "壬", "辛", "庚", "己", "戊"]
        
        dipan = [""] * 9
        
        # 九宫位置索引：坎0 坤1 震2 巽3 中4 乾5 兑6 艮7 离8
        start = ju - 1  # 起始宫位索引
        
        if yinyang == '阳':
            # 阳遁：从起始宫位顺时针排列
            wuxu_order = wuxu_order_yang
            for i in range(9):
                pos = (start + i) % 9
                dipan[pos] = wuxu_order[i]
        else:
            # 阴遁：从起始宫位逆时针排列
            wuxu_order = wuxu_order_yin
            for i in range(9):
                pos = (start - i) % 9
                dipan[pos] = wuxu_order[i]
        
        return dipan

    def get_xunshou_simple(self, shi_gan, shi_zhi):
        """根据时干支计算旬首
        传统规则：
        - 每10天为一旬，共6旬（甲子、甲戌、甲申、甲午、甲辰、甲寅）
        - 旬首规律：甲+该旬地支
        """
        # 60甲子中寻找时柱
        shi_ganzhi = shi_gan + shi_zhi
        
        if shi_ganzhi in self.liujiazi:
            shi_idx = self.liujiazi.index(shi_ganzhi)
            # 计算属于哪一旬（0-5）
            xun_index = shi_idx // 10
            
            # 旬首列表
            xunshou_list = ["甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅"]
            return xunshou_list[xun_index]
        
        return "甲子"

    def get_zhifu_by_xunshou(self, xunshou):
        """根据旬首确定值符 - 新增辅助函数"""
        xunshou_zhifu_map = {
            "甲子": "天蓬", "甲戌": "天芮", "甲申": "天冲", 
            "甲午": "天辅", "甲辰": "天禽", "甲寅": "天心"
        }
        return xunshou_zhifu_map.get(xunshou, "天蓬")

    def get_zhishi_by_xunshou(self, xunshou):
        """根据旬首确定值使 - 新增辅助函数"""
        xunshou_zhishi_map = {
            "甲子": "休", "甲戌": "生", "甲申": "伤", 
            "甲午": "杜", "甲辰": "景", "甲寅": "死"
        }
        return xunshou_zhishi_map.get(xunshou, "休")

    def pai_tianpan(self, shi_gan, yinyang):
        """排天盘：值符随时干
        传统规则：
        - 时干落在哪个宫，天盘该宫就显示时干
        - 其他八宫的天盘天干根据地盘旋转
        - 阳遁：天盘从天盘原位顺旋
        - 阴遁：天盘从天盘原位逆旋
        """
        tianpan = [""] * 9
        
        if not shi_gan or not hasattr(self, 'dipan'):
            return [""] * 9
        
        # 1. 找到时干在地盘的位置
        try:
            shi_gan_pos = self.dipan.index(shi_gan)
        except ValueError:
            shi_gan_pos = 0
        
        # 2. 找到值符星当前落宫位置
        zhifu_pos = getattr(self, 'zhifu_pos', 0)
        
        # 3. 计算旋转偏移量：时干位置 - 值符落宫位置
        offset = (shi_gan_pos - zhifu_pos) % 9
        
        # 4. 天盘旋转
        if yinyang == '阳':
            # 阳遁：地盘天干顺旋到天盘
            for i in range(9):
                source_pos = (i - offset) % 9
                tianpan[i] = self.dipan[source_pos]
        else:
            # 阴遁：地盘天干逆旋到天盘
            for i in range(9):
                source_pos = (i + offset) % 9
                tianpan[i] = self.dipan[source_pos]
        
        # 5. 确保值符落宫的天盘等于时干
        tianpan[zhifu_pos] = shi_gan
        
        return tianpan
    
    def pai_pan(self):
        """主排盘函数 - 传统奇门遁甲规则"""
        global logger
        
        is_valid, message = self.validate_inputs()
        if not is_valid:
            raise ValueError(f"输入验证失败:\n{message}")
        
        logger.debug(f"四柱: {self.ganzhi_info}")
        logger.debug(f"节气: {self.jieqi}")
        
        # 1. 确定阴阳遁和用局
        self.yinyang, calculated_ju = self.determine_yinyang_ju()
        self.ju = int(self.ju_input) if self.ju_input is not None else int(calculated_ju)
        logger.debug(f"阴阳遁: {self.yinyang}, 用局: {self.ju}")
        
        # 2. 排地盘（九宫格基础）
        self.dipan = self.pai_dipan(self.ju, self.yinyang)
        logger.debug(f"地盘: {self.dipan}")
        
        # 3. 确定值符值使及其落宫（必须在排九星、八门之前）
        self.determine_zhifu_zhishi(self.ganzhi_info['hour_gan'], self.ganzhi_info['hour_zhi'])
        logger.debug(f"值符: {self.zhifu}, 值符落宫: {self.zhifu_pos}")
        logger.debug(f"值使: {self.zhishi}, 值使落宫: {self.zhishi_pos}")
        
        # 4. 排九星（值符星根据局数旋转）
        self.jiuxing = self.pai_jiuxing(self.ju, self.yinyang)
        logger.debug(f"九星: {self.jiuxing}")
        
        # 5. 排八门（值使门从旬首位置开始）
        self.bamen = self.pai_bamen(self.yinyang)
        logger.debug(f"八门: {self.bamen}")
        
        # 6. 排天盘（值符随时干）
        self.tianpan = self.pai_tianpan(self.ganzhi_info['hour_gan'], self.yinyang)
        logger.debug(f"天盘: {self.tianpan}")
        
        # 7. 排八神（值符落宫起）
        self.bashen = self.pai_bashen(self.yinyang)
        
        # 8. 判断旺衰
        self.wangshuai = self.get_wangshuai(self.ganzhi_info['day_gan'])
        
        # 填充盘局数据
        for i in range(9):
            self.pan['gongs'][i]['dipan'] = self.dipan[i] or ""
            self.pan['gongs'][i]['tiangan'] = self.tianpan[i] or ""
            self.pan['gongs'][i]['bamen'] = self.bamen[i] or ""
            self.pan['gongs'][i]['jiuxing'] = self.jiuxing[i] or ""
            self.pan['gongs'][i]['bashen'] = self.bashen[i] or ""
            self.pan['gongs'][i]['wangshuai'] = self.wangshuai[i] if i < len(self.wangshuai) else ""
        
        self.ensure_gongwei_completeness()
        return self.pan
    def ensure_gongwei_completeness(self):
        """确保9宫数据完整"""
        if len(self.pan['gongs']) < 9:
            # 补充缺失的宫位
            for i in range(len(self.pan['gongs']), 9):
                self.pan['gongs'].append(self.create_default_gong(i))
        
        # 确保每个宫位都有所有必要的字段
        for i in range(9):
            gong = self.pan['gongs'][i]
            required_fields = ['gongwei', 'tiangan', 'dipan', 'bamen', 'jiuxing', 'bashen', 'wangshuai']
            for field in required_fields:
                if field not in gong or gong[field] is None:
                    gong[field] = ""

    def create_default_gong(self, index):
        """创建默认宫位数据"""
        gongwei = self.gongwei[index] if index < len(self.gongwei) else f'宫{index+1}'
        fangwei = self.fangwei[index] if index < len(self.fangwei) else "未知"
        
        return {
            'gongwei': gongwei,
            'fangwei': fangwei,
            'tiangan': '', 
            'dipan': '',
            'bamen': '', 
            'jiuxing': '', 
            'bashen': '',
            'wangshuai': ''
        }
    
    def pai_bamen(self, yinyang):
        """排八门：从值使位置开始，按八门顺序排布
        传统规则：
        - 八门顺序：休生伤杜景死惊开
        - 值使从旬首天干在地盘的位置开始
        - 阳遁顺排八门，阴遁逆排八门
        - 八门不入中五宫（中五宫寄坤二宫）
        """
        bamen = [""] * 9
        
        if not hasattr(self, 'zhishi') or self.zhishi is None:
            return bamen
        
        # 八门顺序（永远按此顺序）
        bamen_order = ["休", "生", "伤", "杜", "景", "死", "惊", "开"]
        
        # 值使在八门中的索引
        try:
            zhishi_idx = bamen_order.index(self.zhishi)
        except ValueError:
            zhishi_idx = 0
        
        # 值使落宫位置（已在determine_zhifu_zhishi中计算）
        start_pos = getattr(self, 'zhishi_pos', 0)
        
        # 阳遁顺时针，阴遁逆时针
        if yinyang == '阳':
            direction = 1
        else:
            direction = -1
        
        # 从值使位置开始排八门，只排8个宫（跳过中五宫）
        assigned = 0
        
        for offset in range(9):
            pos = (start_pos + offset * direction) % 9
            
            if pos == 4:  # 跳过中五宫
                continue
            
            bamen[pos] = bamen_order[zhishi_idx]
            zhishi_idx = (zhishi_idx + 1) % 8
            assigned += 1
            
            if assigned >= 8:
                break
        
        return bamen

    def pai_jiuxing(self, ju, yinyang):
        """排九星：九星根据局数旋转
        传统规则：
        - 九星原始宫位：天蓬(坎一)、天芮(坤二)、天冲(震三)、天辅(巽四)、
          天禽(中五)、天心(乾六)、天柱(兑七)、天任(艮八)、天英(离九)
        - 阳遁：九星顺转（数字增大方向）
        - 阴遁：九星逆转（数字减小方向）
        - 中五宫天禽寄坤二宫
        """
        # 九星原始顺序（对应九宫位置）
        jiuxing_original = ["天蓬", "天芮", "天冲", "天辅", "天禽", "天心", "天柱", "天任", "天英"]
        jiuxing = [""] * 9
        
        # 九星旋转计算
        rotation = ju - 1
        if yinyang == '阳':
            # 阳遁顺转：原始宫位 + (局数-1)
            for i in range(9):
                jiuxing_idx = (i + rotation) % 9
                jiuxing[i] = jiuxing_original[jiuxing_idx]
        else:
            # 阴遁逆转：原始宫位 - (局数-1)
            rotation = -(ju - 1)
            for i in range(9):
                jiuxing_idx = (i + rotation) % 9
                jiuxing[i] = jiuxing_original[jiuxing_idx]
        
        # 中五宫寄坤二宫：天禽归坤二宫
        # 当九星排列后，中五宫显示为空或寄宫显示
        # 这里保持中五宫为空，因为天禽已寄坤二宫
        # jiuxing[4] = ""  # 中五宫不留星
        
        return jiuxing
    
    def pai_bashen(self, yinyang):
        """排八神：值符落宫起，按八神顺序排布
        传统规则：
        - 八神顺序：值符、螣蛇、太阴、六合、白虎、玄武、九地、九天
        - 从值符落宫开始排布
        - 阳遁顺时针排列，阴遁逆时针排列
        - 八神不入中五宫
        """
        bashen_order = ["值符", "螣蛇", "太阴", "六合", "白虎", "玄武", "九地", "九天"]
        bashen = [""] * 9
        
        # 值符落宫位置
        start_pos = getattr(self, 'zhifu_pos', 0)
        
        # 阳遁顺时针，阴遁逆时针
        if yinyang == '阳':
            direction = 1
        else:
            direction = -1
        
        # 从值符位置开始排八神
        assigned = 0
        for offset in range(9):
            pos = (start_pos + offset * direction) % 9
            
            if pos == 4:  # 跳过中五宫
                continue
            
            bashen[pos] = bashen_order[assigned]
            assigned += 1
            
            if assigned >= 8:
                break
        
        return bashen

    def get_wangshuai(self, ri_gan):
        """判断旺衰 - 根据日干五行与宫位五行生克
        传统规则：
        - 旺：宫位五行与日干五行相同
        - 相：宫位五行生日干五行
        - 休：日干五行生宫位五行
        - 囚：宫位五行克日干五行
        - 死：日干五行克宫位五行
        """
        if not ri_gan:
            return [""] * 9
        
        # 天干五行
        tiangan_wuxing = {
            "甲": "木", "乙": "木", "丙": "火", "丁": "火", "戊": "土",
            "己": "土", "庚": "金", "辛": "金", "壬": "水", "癸": "水"
        }
        
        # 九宫五行（洛书九宫对应）
        # 坎一宫水、坤二宫土、震三宫木、巽四宫木、中五宫土、乾六宫金、兑七宫金、艮八宫土、离九宫火
        gong_wuxing = ["水", "土", "木", "木", "土", "金", "金", "土", "火"]
        
        # 五行相生：木生火、火生土、土生金、金生水、水生木
        # 五行相克：木克土、土克水、水克火、火克金、金克木
        
        ri_wuxing = tiangan_wuxing.get(ri_gan, "土")
        wangshuai = []
        
        # 五行生克映射
        sheng_relation = {"木": "火", "火": "土", "土": "金", "金": "水", "水": "木"}  # 我生者
        ke_relation = {"木": "土", "土": "水", "水": "火", "火": "金", "金": "木"}  # 我克者
        
        for i in range(9):
            gong_wx = gong_wuxing[i]
            
            if gong_wx == ri_wuxing:
                status = "旺"      # 同我者旺
            elif sheng_relation.get(ri_wuxing) == gong_wx:
                status = "相"      # 我生者相（泄气）
            elif sheng_relation.get(gong_wx) == ri_wuxing:
                status = "休"      # 生我者休（得生）
            elif ke_relation.get(ri_wuxing) == gong_wx:
                status = "死"      # 我克者死（耗力）
            elif ke_relation.get(gong_wx) == ri_wuxing:
                status = "囚"      # 克我者囚（受制）
            else:
                status = ""
                
            wangshuai.append(status)
        
        return wangshuai
    
    def determine_zhifu_zhishi(self, shi_gan=None, shi_zhi=None):
        """确定值符值使及其落宫位置 - 传统奇门遁甲规则"""
        # 安全检查：确保ganzhi_info存在
        if not hasattr(self, 'ganzhi_info'):
            self.ganzhi_info = self.parse_ganzhi(self.ganzhi_input)
        
        # 使用传入参数或从ganzhi_info获取
        shi_gan = shi_gan or self.ganzhi_info.get('hour_gan', '甲')
        shi_zhi = shi_zhi or self.ganzhi_info.get('hour_zhi', '子')
        
        # 1. 根据时干支确定旬首
        xunshou = self.get_xunshou_simple(shi_gan, shi_zhi)

        # 2. 根据旬首确定值符（九星）
        xunshou_zhifu_map = {
            "甲子": "天蓬", "甲戌": "天芮", "甲申": "天冲", 
            "甲午": "天辅", "甲辰": "天禽", "甲寅": "天心"
        }
        self.zhifu = xunshou_zhifu_map.get(xunshou, "天蓬")
        
        # 3. 根据旬首确定值使（八门）
        xunshou_zhishi_map = {
            "甲子": "休", "甲戌": "生", "甲申": "伤", 
            "甲午": "杜", "甲辰": "景", "甲寅": "死"
        }
        self.zhishi = xunshou_zhishi_map.get(xunshou, "休")
        
        # 4. 计算值使落宫位置（值使从旬首天干在地盘的位置开始）
        # 旬首天干在60甲子中的索引
        xunshou_gan = xunshou[0]  # 旬首的第一个字是天干
        if hasattr(self, 'dipan') and self.dipan:
            try:
                self.zhishi_pos = self.dipan.index(xunshou_gan)
            except ValueError:
                self.zhishi_pos = 0
        else:
            # 如果地盘还没排，根据局数推算旬首天干的理论位置
            # 阳遁时戊在(ju-1)宫，阴遁时戊在(9-ju)宫
            # 旬首天干与戊的关系需要从60甲子推算
            xunshou_idx = self.liujiazi.index(xunshou) if xunshou in self.liujiazi else 0
            gan_in_60 = xunshou_idx % 10  # 天干在60甲子循环中的位置
            
            # 五鼠遁序：甲乙丙丁戊己庚辛壬癸对应位置0-9
            # 旬首天干位置 = (gan位置 - 戊的位置) 相对于局数
            wu_pos = 4  # 戊在10天干中的位置是4
            offset = (gan_in_60 - wu_pos) % 10
            
            # 结合局数计算落宫
            if self.yinyang == '阳':
                self.zhishi_pos = (self.ju - 1 + offset) % 9
            else:
                self.zhishi_pos = (8 - (self.ju - 1) + offset) % 9
        
        # 5. 计算值符落宫位置（九星根据局数旋转后的位置）
        zhifu_jiuxing = ["天蓬", "天芮", "天冲", "天辅", "天禽", "天心", "天柱", "天任", "天英"]
        if self.zhifu in zhifu_jiuxing:
            zhifu_index = zhifu_jiuxing.index(self.zhifu)
            # 九星根据局数旋转
            if self.yinyang == '阳':
                self.zhifu_pos = (zhifu_index + self.ju - 1) % 9
            else:
                self.zhifu_pos = (zhifu_index - self.ju + 1) % 9
        else:
            self.zhifu_pos = 0
    
    def print_jiugong_layout(self):
        """修正九宫打印顺序（洛书标准顺序：坎1、坤2、震3、巽4、中5、乾6、兑7、艮8、离9）"""
        print("九宫格布局:")
        print("=" * 30)
        
        # 正确的九宫打印顺序（洛书布局）：
        # 上排：巽4(3) 离9(8) 坤2(1)
        # 中排：震3(2) 中5(4) 兑7(6)
        # 下排：艮8(7) 坎1(0) 乾6(5)
        print_layout = [3, 8, 1, 2, 4, 6, 7, 0, 5]
        
        # 打印九宫格
        print("┌─────────┬─────────┬─────────┐")
        for i in range(3):
            line = "│"
            for j in range(3):
                idx = print_layout[i*3 + j]
                gong = self.pan['gongs'][idx]
                content = f"{gong['gongwei'][:3]}:{gong['tiangan'] or '-'}"
                line += f" {content:<6} │"
            print(line)
            if i < 2:
                print("├─────────┼─────────┼─────────┤")
        print("└─────────┴─────────┴─────────┘")

    def print_pan(self):
        """输出排盘结果"""
        print()
        print("奇门遁甲排盘结果")
        print("=" * 60)
        print()
        
        # 显示时间
        if self.year:
            print(f"时间: {self.year}年{self.month}月{self.day}日 {self.hour:02d}:{self.minute:02d}")
        
        # 显示四柱
        print(f"四柱: {self.ganzhi_info['year']} {self.ganzhi_info['month']} {self.ganzhi_info['day']} {self.ganzhi_info['hour']}")
        
        # 显示节气
        print(f"节气: {self.jieqi or '未知'}")
        
        # 显示阴阳、用局、方法
        method_name = {'zhebu': '拆补法', 'zhirun': '置闰法', 'maoshan': '茅山法'}.get(self.method, self.method)
        print(f"阴阳: {self.yinyang}遁  用局: {self.ju}  方法: {method_name}")
        print(f"值符: {self.zhifu}  值使: {self.zhishi}")
        print()
        print("-" * 60)
        print()

        # 只输出一个九宫八卦图
        self.print_simple_jiugong()
        print()

        # 确保有9宫数据
        if len(self.pan['gongs']) < 9:
            print("警告: 宫位数据不完整，正在修复...")
            # 补充缺失的宫位
            for i in range(len(self.pan['gongs']), 9):
                self.pan['gongs'].append({
                    'gongwei': self.gongwei[i] if i < len(self.gongwei) else f'宫{i+1}',
                    'tiangan': '', 
                    'dipan': '',
                    'bamen': '', 
                    'jiuxing': '', 
                    'bashen': '',
                    'wangshuai': ''
                })

        # 直接输出每宫内容
        for idx in range(9):
            if idx >= len(self.pan['gongs']):
                # 如果宫位数据仍然缺失，创建默认数据
                gong_data = {
                    'gongwei': self.gongwei[idx] if idx < len(self.gongwei) else f'宫{idx+1}',
                    'tiangan': '  ', 
                    'dipan': '  ',
                    'bamen': '  ', 
                    'jiuxing': '  ', 
                    'bashen': '  ',
                    'wangshuai': '  '
                }
            else:
                gong_data = self.pan['gongs'][idx]
            
            tian = gong_data.get('tiangan', '') or "  "
            di = gong_data.get('dipan', '') or "  "
            men = gong_data.get('bamen', '') or "  "
            xing = gong_data.get('jiuxing', '') or "  "
            shen = gong_data.get('bashen', '') or "  "
            wang = gong_data.get('wangshuai', '') or "  "
            
            gongwei = gong_data.get('gongwei', f'宫{idx+1}')
            fangwei = self.fangwei[idx] if idx < len(self.fangwei) else "未知"
            
            print(f"-- {gongwei}({fangwei}): 天{tian} 地{di} 门{men} 星{xing} 神{shen} 旺{wang} --")
        
        print()
        print("-" * 60)
        print()
        
        self.print_analysis()

    def print_simple_jiugong(self):
        """最简版九宫八卦图"""
        print("九宫简图:")
        print("=" * 40)
        print()
        
        print(" 东南四.离南九.西南二")
        print(" 震东三.中五中.兑西七") 
        print(" 东北八.坎北一.西北六")
        print()
        
    def print_analysis(self):
        """优化分析结果显示 - 完整修复版"""
        print("📊📊 盘局综合分析")
        print("=" * 60)
        print()
    
        # 安全检查：确保盘局数据存在
        if not hasattr(self, 'pan') or 'gongs' not in self.pan:
            print("❌ 盘局数据不完整，无法进行分析")
            return
    
        try:
            # 1. 吉凶方位分析
            print("🎯🎯 吉凶方位建议")
            print("-" * 40)
            print()
            
            # 大吉方位（三吉门）
            da_ji_gongs = []
            for idx in range(9):
                if idx >= len(self.pan['gongs']):
                    continue
                    
                gong = self.pan['gongs'][idx]
                # 安全检查：确保八门数据存在
                bamen = gong.get('bamen', '')
                if bamen in ['开', '休', '生']:
                    fangwei = self.fangwei[idx] if idx < len(self.fangwei) else "未知"
                    gongwei = gong.get('gongwei', f'宫{idx+1}')
                    da_ji_gongs.append((gongwei, fangwei, bamen))
            
            if da_ji_gongs:
                print("✅ 大吉方位（宜选择）")
                for gongwei, fangwei, men in da_ji_gongs:
                    men_desc = {
                        '开': '开门-开拓创新', 
                        '休': '休门-休息养生', 
                        '生': '生门-生机勃勃'
                    }.get(men, men)
                    print(f"   {gongwei}({fangwei}): {men_desc}")
                print()
            
            # 凶方位
            xiong_gongs = []
            for idx in range(9):
                if idx >= len(self.pan['gongs']):
                    continue
                    
                gong = self.pan['gongs'][idx]
                bamen = gong.get('bamen', '')
                if bamen in ['死', '惊', '伤']:
                    fangwei = self.fangwei[idx] if idx < len(self.fangwei) else "未知"
                    gongwei = gong.get('gongwei', f'宫{idx+1}')
                    xiong_gongs.append((gongwei, fangwei, bamen))
            
            if xiong_gongs:
                print("❌ 凶险方位（宜避开）")
                for gongwei, fangwei, men in xiong_gongs:
                    men_desc = {
                        '死': '死门-死气沉沉',
                        '惊': '惊门-惊恐不安', 
                        '伤': '伤门-伤害损失'
                    }.get(men, men)
                    print(f"   {gongwei}({fangwei}): {men_desc}")
                print()
            
            # 2. 特殊星神影响
            print("⭐ 特殊星神影响")
            print("-" * 40)
            print()
            
            # 吉星
            ji_xing = []
            for idx in range(9):
                if idx >= len(self.pan['gongs']):
                    continue
                    
                gong = self.pan['gongs'][idx]
                jiuxing = gong.get('jiuxing', '')
                if jiuxing in ['天辅', '天心', '天任', '天禽']:
                    fangwei = self.fangwei[idx] if idx < len(self.fangwei) else "未知"
                    gongwei = gong.get('gongwei', f'宫{idx+1}')
                    ji_xing.append((gongwei, fangwei, jiuxing))
            
            if ji_xing:
                print("✨ 吉星照临")
                for gongwei, fangwei, xing in ji_xing:
                    xing_desc = {
                        '天辅': '天辅星-文昌学业',
                        '天心': '天心星-医药健康',
                        '天任': '天任星-吉庆祥和', 
                        '天禽': '天禽星-中正尊贵'
                    }.get(xing, xing)
                    print(f"   {gongwei}({fangwei}): {xing_desc}")
                print()
            
            # 凶星
            xiong_xing = []
            for idx in range(9):
                if idx >= len(self.pan['gongs']):
                    continue
                    
                gong = self.pan['gongs'][idx]
                jiuxing = gong.get('jiuxing', '')
                if jiuxing in ['天芮', '天蓬', '天柱']:
                    fangwei = self.fangwei[idx] if idx < len(self.fangwei) else "未知"
                    gongwei = gong.get('gongwei', f'宫{idx+1}')
                    xiong_xing.append((gongwei, fangwei, jiuxing))
            
            if xiong_xing:
                print("⚠️  凶星影响")
                for gongwei, fangwei, xing in xiong_xing:
                    xing_desc = {
                        '天芮': '天芮星-疾病困扰',
                        '天蓬': '天蓬星-盗贼风险',
                        '天柱': '天柱星-破败损失'
                    }.get(xing, xing)
                    print(f"   {gongwei}({fangwei}): {xing_desc}")
                print()
            
            # 3. 八神影响
            print("🔮🔮 八神能量分布")
            print("-" * 40)
            print()
            
            shen_analysis = []
            for idx in range(9):
                if idx >= len(self.pan['gongs']):
                    continue
                    
                gong = self.pan['gongs'][idx]
                bashen = gong.get('bashen', '')
                if bashen:
                    fangwei = self.fangwei[idx] if idx < len(self.fangwei) else "未知"
                    gongwei = gong.get('gongwei', f'宫{idx+1}')
                    shen_analysis.append((gongwei, fangwei, bashen))
            
            for gongwei, fangwei, shen in shen_analysis:
                shen_desc = {
                    '值符': '领导贵人，大事可成',
                    '螣蛇': '虚诈多变，小心陷阱',
                    '太阴': '暗中助力，隐秘行事',
                    '六合': '合作顺利，婚姻和谐',
                    '白虎': '凶险压力，谨慎应对',
                    '玄武': '盗贼欺骗，防范小人',
                    '九地': '稳定持久，根基深厚', 
                    '九天': '高远发展，上升空间'
                }.get(shen, shen)
                
                shen_type = "吉" if shen in ['值符', '太阴', '六合', '九地', '九天'] else "凶"
                symbol = "✅" if shen_type == "吉" else "❌"
                print(f"   {symbol} {gongwei}({fangwei}): {shen} - {shen_desc}")
            
            print()
            
            # 4. 综合建议
            print("💡💡 综合建议")
            print("-" * 40)
            print()
            
            # 判断整体吉凶
            ji_count = len(da_ji_gongs) + len(ji_xing)
            xiong_count = len(xiong_gongs) + len(xiong_xing)
            
            if ji_count > xiong_count:
                print("✅ 整体格局偏向吉利，可积极行动")
                if len(da_ji_gongs) >= 2:
                    print("   多个吉门照临，适宜开展新项目")
            elif xiong_count > ji_count:
                print("⚠️  整体格局存在风险，建议谨慎行事")
                print("   可选择吉门方位化解不利因素")
            else:
                print("➖➖ 吉凶参半，需根据具体事项选择方位")
            
            print()
            
            # 特殊提醒
            health_tip = False
            for idx in range(9):
                if idx >= len(self.pan['gongs']):
                    continue
                    
                gong = self.pan['gongs'][idx]
                jiuxing = gong.get('jiuxing', '')
                bamen = gong.get('bamen', '')
                
                if jiuxing == '天芮' and bamen in ['死', '惊']:
                    print("💊💊 注意健康: 天芮星与凶门同宫，需关注身体健康")
                    health_tip = True
                    break
            
            if any(gong.get('bashen') == '玄武' for gong in self.pan['gongs']):
                print("🔒🔒 防范小人: 玄武星出现，注意财物安全和人际关系")
            
            # 检查是否有天芮星在特定宫位（健康提醒）
            for idx in range(9):
                if idx >= len(self.pan['gongs']):
                    continue
                    
                gong = self.pan['gongs'][idx]
                if gong.get('jiuxing') == '天芮' and gong.get('bamen') in ['休', '生']:
                    if not health_tip:
                        print("💊💊 健康提示: 天芮星临吉门，虽有小病但易康复，注意调养")
                    break
                    
        except Exception as e:
            print(f"⚠️  分析过程出错: {str(e)}")

def get_four_pillars(year=None, month=None, day=None, hour=None, minute=None):
    """调用shizhu.py获取四柱信息"""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        shizhu_path = os.path.join(current_dir, 'shizhu.py')
        
        # 构建参数
        args = [sys.executable, shizhu_path, '--simple']
        if year is not None:
            args.extend([str(year), str(month), str(day), str(hour), str(minute or 0)])
        
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        pillars = output.split()
        
        if len(pillars) != 4:
            raise ValueError(f"shizhu.py返回的四柱信息格式错误: {output}")
        
        return pillars
    except Exception as e:
        print(f"获取四柱信息失败: {e}")
        return None

def print_help():
    """打印帮助信息"""
    print()
    print("奇门遁甲排盘系统 - 使用说明")
    print("=" * 50)
    print()
    print("用法:")
    print("  1. python qimen.py                       # 自动使用当前时间")
    print("  2. python qimen.py 年 月 日 时 [分] [方法]")
    print()
    print("参数说明:")
    print("  年 月 日 时: 年月日时，例: 2026 4 28 23")
    print("  分      : 可选，默认为0")
    print("  方法    : 可选 zhebu/zhirun/maoshan，默认zhebu")
    print("  --debug : 可选，开启调试模式显示详细计算过程")
    print()
    print("自动推断（无需手动输入）:")
    print("  四柱: 由 shizhu.py 根据时间计算")
    print("  节气: 根据日期自动推断")
    print("  阴阳: 根据节气自动判断")
    print("  用局: 根据节气自动确定")
    print()
    print("示例:")
    print("  python qimen.py                 # 当前时间")
    print("  python qimen.py 2026 4 28 23     # 2026年4月28日23时")
    print("  python qimen.py 2026 4 28 23 30 # 2026年4月28日23:30")
    print()

def main():
    """主函数 - 时间参数版本"""
    global logger
    
    # 检查帮助参数
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        print_help()
        return
    
    year = month = day = hour = minute = None
    method = 'zhebu'
    
    # 检查调试模式
    if '--debug' in sys.argv:
        logger.debug_mode = True
        sys.argv.remove('--debug')
        logger.info("调试模式已启用")
    
    if len(sys.argv) == 1:
        # 无参数：使用当前时间
        now = dt.now()
        year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute
        print(f"时间: {year}年{month}月{day}日 {hour:02d}:{minute:02d}")
    else:
        # 解析时间参数
        try:
            year = int(sys.argv[1])
            month = int(sys.argv[2])
            day = int(sys.argv[3])
            hour = int(sys.argv[4])
            minute = int(sys.argv[5]) if len(sys.argv) > 5 else 0
            
            # 验证方法参数
            if len(sys.argv) > 6:
                method = sys.argv[6]
                if method not in ['zhebu', 'zhirun', 'maoshan']:
                    logger.warning(f"起局方法'{method}'无效，使用默认拆补法")
                    method = 'zhebu'
        except (ValueError, IndexError) as e:
            logger.error(f"参数错误: {e}")
            print_help()
            sys.exit(1)
    
    # 调用 shizhu.py 计算四柱
    pillars = get_four_pillars(year, month, day, hour, minute)
    if not pillars:
        print("无法获取四柱信息")
        sys.exit(1)
    
    year_ganzhi, month_ganzhi, day_ganzhi, hour_ganzhi = pillars
    
    # 自动推断节气
    qmdj_temp = QiMenDunJia(year_ganzhi, month_ganzhi, day_ganzhi, hour_ganzhi)
    inferred_jieqi = qmdj_temp.get_jieqi_from_date(year, month, day)
    
    try:
        qmdj = QiMenDunJia(
            year_ganzhi=year_ganzhi,
            month_ganzhi=month_ganzhi,
            day_ganzhi=day_ganzhi,
            hour_ganzhi=hour_ganzhi,
            jieqi=inferred_jieqi,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            method=method
        )
        
        qmdj.pai_pan()
        qmdj.print_pan()
        
    except Exception as e:
        print(f"排盘过程中发生错误: {e}")
        print_help()

if __name__ == "__main__":
    main()
        

