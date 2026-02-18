import datetime
from datetime import datetime as dt
import sys
import subprocess
import os

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
            
        # 基础定义
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
        
        self.gongwei = ["坎一宫", "坤二宫", "震三宫", "巽四宫", "中五宫", "乾六宫", "兑七宫", "艮八宫", "离九宫"]
        self.fangwei = ["北方", "西南", "东方", "东南", "中方", "西北", "西方", "东北", "南方"]
        
        # 初始化盘局
        self.pan = {
            'gongs': [{'gongwei': self.gongwei[i], 
                    'tiangan': None, 
                    'dipan': None,
                    'bamen': None, 
                    'jiuxing': None, 
                    'bashen': None} for i in range(9)]  # 确保是range(9)而不是range(8)
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
        
        # 合法的干支组合（60甲子循环）
        valid_combinations = set()
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
        if self.yinyang_input and self.ju_input:
            return self.yinyang_input, self.ju_input
            
        if self.jieqi:
            yinyang = self.get_yinyang_from_jieqi(self.jieqi)
            ju = self.get_ju_from_jieqi(self.jieqi)
            return yinyang, ju
            
        # 如果没有节气信息，根据月份判断
        if self.month:
            if 2 <= self.month <= 7:  # 立春到立秋之间为阳遁
                yinyang = '阳'
            else:
                yinyang = '阴'
        else:
            # 最终默认
            yinyang = '阳'
        
        # 根据月份确定用局数（传统方法）
        if self.ju_input:
            ju = self.ju_input
        else:
            # 月份对应用局表
            month_ju_map = {
                1: 1, 2: 8, 3: 1, 4: 3, 5: 4, 6: 6,
                7: 9, 8: 2, 9: 9, 10: 7, 11: 6, 12: 4
            }
            ju = month_ju_map.get(self.month, 1)
            
        return yinyang, ju
    
    def get_yinyang_from_jieqi(self, jieqi_name):
        """根据节气确定阴阳遁"""
        yang_dun_jieqi = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", 
                        "春分", "清明", "谷雨", "立夏", "小满", "芒种"]
        return '阳' if jieqi_name in yang_dun_jieqi else '阴'
    
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
        """排地盘"""
        wuxu_order = ["戊", "己", "庚", "辛", "壬", "癸", "丁", "丙", "乙"]
        dipan = [None] * 9
        
        if yinyang == '阳':
            start = ju - 1
            for i in range(9):
                pos = (start + i) % 9
                dipan[pos] = wuxu_order[i]
        else:
            start = ju - 1
            for i in range(9):
                pos = (start - i) % 9
                if pos < 0:
                    pos += 9
                dipan[pos] = wuxu_order[i]
        
        return dipan

    def determine_zhifu_zhishi(self, jiuxing, bamen, shi_gan):
        """修复版 - 最小化修改"""
        
        shi_zhi = self.ganzhi_info.get('hour_zhi', '子')
        
        # 修复1：正确的值符确定（基于旬首）
        xunshou = self.get_xunshou_simple(shi_gan, shi_zhi)
        self.zhifu = self.get_zhifu_by_xunshou(xunshou)
        
        # 修复2：正确的值使确定（基于旬首）
        self.zhishi = self.get_zhishi_by_xunshou(xunshou)
        
        # 保持原有的位置查找逻辑（这部分基本正确）
        self.zhifu_pos = -1
        self.zhishi_pos = -1
        
        for i in range(9):
            if jiuxing[i] == self.zhifu:
                self.zhifu_pos = i
            if bamen[i] == self.zhishi:
                self.zhishi_pos = i
        
        # 修复3：更好的默认值处理
        if self.zhifu_pos == -1:
            self.zhifu_pos = self.get_default_zhifu_position()
        if self.zhishi_pos == -1:
            self.zhishi_pos = self.get_default_zhishi_position()
        
        return True

    def get_xunshou_simple(self, shi_gan, shi_zhi):
        """简化版旬首计算 - 新增辅助函数"""
        # 六甲旬首：甲子、甲戌、甲申、甲午、甲辰、甲寅
        liujia_map = {
            "子": "甲子", "戌": "甲戌", "申": "甲申", "午": "甲午", 
            "辰": "甲辰", "寅": "甲寅"
        }
        
        # 如果不是六甲地支，向前找最近的甲
        if shi_zhi in liujia_map:
            return liujia_map[shi_zhi]
        
        # 简化处理：根据时支确定旬首
        zhi_to_xunshou = {
            "丑": "甲子", "亥": "甲戌", "酉": "甲申", "未": "甲午",
            "巳": "甲辰", "卯": "甲寅"
        }
        
        return zhi_to_xunshou.get(shi_zhi, "甲子")

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

    def pai_tianpan(self, dipan, shi_gan, yinyang, jiuxing):
        """排天盘 - 修复版（值符加临时干）"""
        if not shi_gan:
            return dipan.copy()
        
        tianpan = [None] * 9
        
        # 找到值符星的位置
        zhifu_pos = self.zhifu_pos  # 使用已经确定的值符位置
        
        # 找到时干对应的宫位（地盘上时干所在的宫）
        shi_gan_gong = -1
        for i in range(9):
            if dipan[i] == shi_gan:
                shi_gan_gong = i
                break
        
        # 如果没找到时干在地盘的位置，默认在坎宫
        if shi_gan_gong == -1:
            shi_gan_gong = 0
        
        # 计算值符应该加到的宫位（时干宫）
        target_gong = shi_gan_gong
        
        # 计算转动量：从值符当前位置转到时干宫位的偏移量
        rotation = target_gong - zhifu_pos
        
        # 转动天盘（九星带动天干）
        for i in range(9):
            if yinyang == '阳':
                # 阳遁顺转
                source_idx = (i - rotation) % 9
            else:
                # 阴遁逆转
                source_idx = (i + rotation) % 9
            
            tianpan[i] = dipan[source_idx] if dipan[source_idx] else ""
        
        return tianpan
    
    def pai_pan(self):
        """主排盘函数 - 完全修复版"""
        is_valid, message = self.validate_inputs()
        if not is_valid:
            raise ValueError(f"输入验证失败:\n{message}")
            
        # 确定阴阳遁和用局
        self.yinyang, calculated_ju = self.determine_yinyang_ju()
        if self.ju_input is None:
            self.ju = calculated_ju
        else:
            self.ju = self.ju_input
        
        # 正确的排盘顺序：
        # 1. 排地盘（基础）
        dipan = self.pai_dipan(self.ju, self.yinyang)
        
        # 2. 排九星（天盘主体）
        jiuxing = self.pai_jiuxing(self.ju, self.yinyang, self.ganzhi_info['hour_gan'])
        
        # 3. 排八门（人盘）
        bamen = self.pai_bamen(self.ju, self.yinyang, self.ganzhi_info['hour_zhi'])
        
        # 4. 确定值符值使（关键参照）
        self.determine_zhifu_zhishi(jiuxing, bamen, self.ganzhi_info['hour_gan'])
        
        # 5. 排天盘（值符加临时干）
        tianpan = self.pai_tianpan(dipan, self.ganzhi_info['hour_gan'], self.yinyang, jiuxing)
        
        # 6. 排八神（神盘）
        bashen = self.pai_bashen(self.yinyang, self.ganzhi_info['hour_gan'])
        
        # 7. 判断旺衰
        wangshuai = self.get_wangshuai(self.ganzhi_info['day_gan'])
        
        # 填充盘局数据
        for i in range(9):
            self.pan['gongs'][i]['dipan'] = dipan[i] or ""
            self.pan['gongs'][i]['tiangan'] = tianpan[i] or ""
            self.pan['gongs'][i]['bamen'] = bamen[i] or ""
            self.pan['gongs'][i]['jiuxing'] = jiuxing[i] or ""
            self.pan['gongs'][i]['bashen'] = bashen[i] or ""
            self.pan['gongs'][i]['wangshuai'] = wangshuai[i] if i < len(wangshuai) else ""
        
        # 确保有9宫数据
        if len(self.pan['gongs']) < 9:
            for i in range(len(self.pan['gongs']), 9):
                self.pan['gongs'].append({
                    'gongwei': self.gongwei[i] if i < len(self.gongwei) else f'宫{i+1}',
                    'tiangan': '', 'dipan': '', 'bamen': '', 
                    'jiuxing': '', 'bashen': '', 'wangshuai': ''
                })
        
        self.ensure_gongwei_completeness()

        # 修复输出格式，处理可能的None值
        for idx in range(9):
            gong_data = self.pan['gongs'][idx]
            
            # 安全获取各字段值
            tian = gong_data.get('tiangan', '') or "  "
            di = gong_data.get('dipan', '') or "  "
            men = gong_data.get('bamen', '') or "  "
            xing = gong_data.get('jiuxing', '') or "  "
            shen = gong_data.get('bashen', '') or "  "
            wang = gong_data.get('wangshuai', '') or "  "
            
            gongwei = gong_data.get('gongwei', f'宫{idx+1}')
            fangwei = gong_data.get('fangwei', self.fangwei[idx] if idx < len(self.fangwei) else "未知")
            
            # 格式化输出，确保对齐
            print(f"-- {gongwei:6}({fangwei:4}): 天{tian:2} 地{di:2} 门{men:2} 星{xing:4} 神{shen:4} 旺{wang:2} --")

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
    
    def pai_bamen(self, ju, yinyang, shi_zhi):
        """排八门 - 传统方法"""
        bamen_order = ["休", "生", "伤", "杜", "景", "死", "惊", "开"]
        bamen = [""] * 9
        
        if not shi_zhi:
            return bamen
            
        # 时支对应当起始门
        shizhi_men = {
            "子": 0, "丑": 1, "寅": 2, "卯": 3, "辰": 4, "巳": 5,
            "午": 6, "未": 7, "申": 0, "酉": 1, "戌": 2, "亥": 3
        }
        
        start_men = shizhi_men.get(shi_zhi, 0)
        
        # 按宫位顺序排八门
        for i in range(9):
            if i == 4:  # 中五宫
                bamen[i] = "生"  # 传统规则：中五宫借用生门
                continue
                
            if yinyang == '阳':
                # 阳遁顺排
                men_idx = (start_men + i) % 8
            else:
                # 阴遁逆排
                men_idx = (start_men - i) % 8
                if men_idx < 0:
                    men_idx += 8
            
            bamen[i] = bamen_order[men_idx]
        
        return bamen

    def pai_jiuxing(self, ju, yinyang, shi_gan):
        """排九星 - 使用传统顺序"""
        # 传统九星顺序
        jiuxing_order = ["天蓬", "天芮", "天冲", "天辅", "天禽", "天心", "天柱", "天任", "天英"]
        jiuxing = [""] * 9
        
        # 按用局数确定起始宫位
        start_gong = ju - 1
        
        for i in range(9):
            if yinyang == '阳':
                # 阳遁顺排
                gong_pos = (start_gong + i) % 9
            else:
                # 阴遁逆排
                gong_pos = (start_gong - i) % 9
                if gong_pos < 0:
                    gong_pos += 9
            
            jiuxing[gong_pos] = jiuxing_order[i]
        
        return jiuxing
        
    def pai_bashen(self, yinyang, shi_gan):
        """排八神 - 修复版"""
        bashen_order = ["值符", "螣蛇", "太阴", "六合", "白虎", "玄武", "九地", "九天"]
        bashen = [None] * 9
        
        if not shi_gan:
            # 给所有宫位分配空值
            return [""] * 9
        
        # 找到值符所在的宫位作为起始点
        start_pos = self.zhifu_pos
        
        if yinyang == '阳':
            # 阳遁顺排八神
            for i in range(9):
                shen_idx = i % 8  # 八神循环使用
                current_pos = (start_pos + i) % 9
                bashen[current_pos] = bashen_order[shen_idx]
        else:
            # 阴遁逆排八神
            for i in range(9):
                shen_idx = i % 8
                current_pos = (start_pos - i) % 9
                if current_pos < 0:
                    current_pos += 9
                bashen[current_pos] = bashen_order[shen_idx]
        
        return bashen

    def get_wangshuai(self, ri_gan):
        """判断旺衰 - 修复版"""
        wangshuai = []
        
        # 日干五行
        tiangan_wuxing = {
            "甲": "木", "乙": "木", "丙": "火", "丁": "火", "戊": "土",
            "己": "土", "庚": "金", "辛": "金", "壬": "水", "癸": "水"
        }
        
        # 九宫五行（1-9宫）
        gong_wuxing = ["水", "土", "木", "木", "土", "金", "金", "土", "火"]
        
        ri_wuxing = tiangan_wuxing.get(ri_gan, "土")
        wangshuai = []
        
        for i in range(9):
            gong_wx = gong_wuxing[i]
            
            # 正确的五行生克关系判断：
            if gong_wx == ri_wuxing:
                status = "旺"  # 同我者旺
            elif self.is_sheng_wo(ri_wuxing, gong_wx):  # 生我者
                status = "相"  # 生我者相（得生）
            elif self.is_wo_sheng(ri_wuxing, gong_wx):  # 我生者
                status = "休"  # 我生者休（泄气）
            elif self.is_ke_wo(ri_wuxing, gong_wx):     # 克我者
                status = "囚"  # 克我者囚（受制）
            else:  # 我克者
                status = "死"  # 我克者死（耗力）
                
            wangshuai.append(status)
        
        return wangshuai

    def is_sheng_wo(self, wo_wuxing, other_wuxing):
        """判断是否生我"""
        # 生我：金生水，水生木，木生火，火生土，土生金
        sheng_wo_map = {
            "金": "水", "水": "木", "木": "火", "火": "土", "土": "金"
        }
        return sheng_wo_map.get(other_wuxing) == wo_wuxing

    def is_wo_sheng(self, wo_wuxing, other_wuxing):
        """判断是否我生"""
        # 我生：金生水，水生木，木生火，火生土，土生金
        wo_sheng_map = {
            "金": "水", "水": "木", "木": "火", "火": "土", "土": "金"
        }
        return wo_sheng_map.get(wo_wuxing) == other_wuxing

    def is_ke_wo(self, wo_wuxing, other_wuxing):
        """判断是否克我"""
        # 克我：金克木，木克土，土克水，水克火，火克金
        ke_wo_map = {
            "金": "木", "木": "土", "土": "水", "水": "火", "火": "金"
        }
        return ke_wo_map.get(other_wuxing) == wo_wuxing
    
    def determine_zhifu_zhishi(self, jiuxing, bamen, shi_gan):
        """确定值符值使 - 传统方法"""
        # 根据时干确定旬首
        xunshou = self.get_xunshou_simple(shi_gan, self.ganzhi_info.get('hour_zhi', '子'))
        
        # 根据旬首确定值符（九星）
        xunshou_zhifu_map = {
            "甲子": "天蓬", "甲戌": "天芮", "甲申": "天冲", 
            "甲午": "天辅", "甲辰": "天禽", "甲寅": "天心"
        }
        self.zhifu = xunshou_zhifu_map.get(xunshou, "天蓬")
        
        # 根据旬首确定值使（八门）
        xunshou_zhishi_map = {
            "甲子": "休", "甲戌": "生", "甲申": "伤", 
            "甲午": "杜", "甲辰": "景", "甲寅": "死"
        }
        self.zhishi = xunshou_zhishi_map.get(xunshou, "休")
        
        # 确定值符值使的位置
        self.zhifu_pos = -1
        self.zhishi_pos = -1
        
        for i in range(9):
            if jiuxing[i] == self.zhifu:
                self.zhifu_pos = i
            if bamen[i] == self.zhishi:
                self.zhishi_pos = i
        
        # 如果没找到，使用默认位置
        if self.zhifu_pos == -1:
            self.zhifu_pos = 4  # 中五宫
        if self.zhishi_pos == -1:
            self.zhishi_pos = 4  # 中五宫
    
    def print_jiugong_layout(self):
        """打印九宫格布局"""
        print("九宫格布局:")
        print("=" * 30)
        print()
        
        chinese_numbers = ["一", "二", "三", "四", "五", "六", "七", "八", "九"]
        fangwei_full_map = {
            "北": "北方", "西南": "西南", "东": "东方", "东南": "东南", 
            "中": "中宫", "西北": "西北", "西": "西方", "东北": "东北", "南": "南方"
        }
        
        jiugong_order = [3, 8, 1, 2, 4, 6, 7, 0, 5]
        
        grid_data = []
        for idx in jiugong_order:
            fangwei_full = fangwei_full_map.get(self.fangwei[idx], self.fangwei[idx])
            gong_num_chinese = chinese_numbers[idx]
            grid_data.append(f"{fangwei_full}{gong_num_chinese}")
        
        print("─────────────────")
        print(f" {grid_data[0]}  {grid_data[1]}  {grid_data[2]} ")
        print(f" {grid_data[3]}  {grid_data[4]}  {grid_data[5]} ")
        print(f" {grid_data[6]}  {grid_data[7]}  {grid_data[8]} ")
        print("─────────────────")
        print()
        
        print("各宫详细信息:")
        print("-" * 60)
        for idx in range(9):
            gong = self.pan['gongs'][idx]
            
            tian = gong['tiangan'] or "  "
            di = gong['dipan'] or "  "
            men = gong['bamen'] or "  "
            xing = gong['jiuxing'] or "  "
            shen = gong['bashen'] or "  "
            wang = gong.get('wangshuai', '  ')
            fangwei = self.fangwei[idx]
            
            print(f"{gong['gongwei']}({fangwei}): 天{tian} 地{di} 门{men} 星{xing} 神{shen} 旺{wang}")
    
    def print_pan(self):
        """输出排盘结果 - 修复版"""
        print()
        print("奇门遁甲排盘结果")
        print("=" * 60)
        print()
        
        if self.year:
            print(f"时间: {self.year}年{self.month}月{self.day}日 {self.hour:02d}:{self.minute:02d}")
            print()
        
        print(f"四柱: {self.ganzhi_info['year']} {self.ganzhi_info['month']} {self.ganzhi_info['day']} {self.ganzhi_info['hour']}")
        print()
        
        if self.jieqi:
            print(f"节气: {self.jieqi}")
            
        print(f"阴阳: {self.yinyang}遁 {self.ju}局 {self.method}")
        print(f"值符: {self.zhifu} 值使: {self.zhishi}")
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
                    '螣蛇': '虚诈多变，小心陷阱',  # 修正：螣螣蛇 -> 螣蛇
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
            for idx in range(9):
                if idx >= len(self.pan['gongs']):
                    continue
                    
                gong = self.pan['gongs'][idx]
                jiuxing = gong.get('jiuxing', '')
                bamen = gong.get('bamen', '')
                
                if jiuxing == '天芮' and bamen in ['死', '惊']:
                    print("💊💊 注意健康: 天芮星与凶门同宫，需关注身体健康")
                    break
            
            if any(gong.get('bashen') == '玄武' for gong in self.pan['gongs']):
                print("🔒🔒 防范小人: 玄武星出现，注意财物安全和人际关系")
            
            # 检查是否有天芮星在特定宫位（健康提醒）
            for idx in range(9):
                if idx >= len(self.pan['gongs']):
                    continue
                    
                gong = self.pan['gongs'][idx]
                if gong.get('jiuxing') == '天芮' and gong.get('bamen') in ['休', '生']:
                    print("🌿 养生提示: 天芮星与吉门同宫，适宜调理养生")
                    break
            
            print()
            
        except Exception as e:
            print(f"❌ 分析过程中出现错误: {e}")
            import traceback
            traceback.print_exc()
            print("建议检查输入参数和排盘数据")

def get_four_pillars():
    """调用shizhu.py获取当前时间的四柱信息"""
    try:
        # 获取当前目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        shizhu_path = os.path.join(current_dir, 'shizhu.py')
        
        # 调用shizhu.py获取简化输出
        result = subprocess.run(
            [sys.executable, shizhu_path, '--simple'],
            capture_output=True,
            text=True,
            check=True
        )
        
        # 解析输出
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
    print("  1. python qimen.py 年柱 月柱 日柱 时柱 [节气] [阴阳] [用局] [方法]")
    print("  2. python qimen.py            # 自动使用当前时间")
    print()
    print("参数说明:")
    print("  年柱月柱日柱时柱: 必须参数，如 甲子 丙子 甲子 庚午")
    print("  节气    : 可选，如 冬至、立春等")
    print("  阴阳    : 可选，阳 或 阴")
    print("  用局    : 可选，1-9的数字")
    print("  方法    : 可选，zhebu(拆补法)、zhirun(置闰法)、maoshan(茅山法)")
    print()
    print("示例:")
    print("  python qimen.py 甲子 丙子 甲子 庚午")
    print("  python qimen.py 甲子 丙子 甲子 庚午 冬至 阳 1 zhebu")
    print("  python qimen.py            # 自动使用当前时间")
    print()

def main():
    """主函数 - 修复参数处理"""
    if len(sys.argv) == 1:
        # 自动使用当前时间
        print("正在获取当前时间的四柱信息...")
        print()
        
        # 获取当前时间
        now = dt.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        
        pillars = get_four_pillars()
        if not pillars:
            print("无法获取四柱信息，请手动输入")
            print_help()
            return
        
        year_ganzhi, month_ganzhi, day_ganzhi, hour_ganzhi = pillars
        print(f"获取到四柱信息: {year_ganzhi} {month_ganzhi} {day_ganzhi} {hour_ganzhi}")
        print()
        
        # 默认参数
        jieqi = None
        yinyang = None
        ju = None
        method = 'zhebu'
    else:
        # 基本参数检查
        if len(sys.argv) < 5:
            print("错误: 需要至少4个参数（年柱 月柱 日柱 时柱）")
            print_help()
            sys.exit(1)
        
        # 安全获取参数
        year_ganzhi = sys.argv[1]
        month_ganzhi = sys.argv[2]
        day_ganzhi = sys.argv[3]
        hour_ganzhi = sys.argv[4]
        
        # 可选参数的安全处理
        jieqi = sys.argv[5] if len(sys.argv) > 5 else None
        yinyang = sys.argv[6] if len(sys.argv) > 6 else None
        
        # 用局数安全转换
        ju = None
        if len(sys.argv) > 7 and sys.argv[7]:
            try:
                ju = int(sys.argv[7])
                if ju < 1 or ju > 9:
                    print("警告: 用局数应在1-9之间，使用默认计算")
                    ju = None
            except ValueError:
                print("警告: 用局数应为数字，使用默认计算")
        
        method = sys.argv[8] if len(sys.argv) > 8 else 'zhebu'
        
        # 验证方法参数
        if method not in ['zhebu', 'zhirun', 'maoshan']:
            print("警告: 起局方法无效，使用默认的拆补法")
            method = 'zhebu'
    
    try:
        print("正在排盘...")
        print()
        
        qmdj = QiMenDunJia(
            year_ganzhi=year_ganzhi,
            month_ganzhi=month_ganzhi,
            day_ganzhi=day_ganzhi,
            hour_ganzhi=hour_ganzhi,
            jieqi=jieqi,
            yinyang=yinyang,
            ju=ju,
            method=method,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute
        )
        
        qmdj.pai_pan()
        qmdj.print_pan()
        
    except Exception as e:
        print(f"排盘过程中发生错误: {e}")
        print("请检查输入参数是否正确")
        print_help()

if __name__ == "__main__":
    main()
        

