// ========================================
// 二十四节气圆形信息图 - 核心逻辑
// ========================================

// 节气数据数组（与 jieqi24 对应）
const solarTermsData = [
    { name: "立春", phenomenon: "东风解冻", hou1: "东风解冻", hou2: "蛰虫始振", hou3: "鱼陟负冰" },
    { name: "雨水", phenomenon: "雨水降临", hou1: "獭祭鱼", hou2: "候雁北", hou3: "草木萌动" },
    { name: "惊蛰", phenomenon: "万物苏醒", hou1: "桃始华", hou2: "仓庚鸣", hou3: "鹰化为鸠" },
    { name: "春分", phenomenon: "春分时节", hou1: "玄鸟至", hou2: "雷乃发声", hou3: "始电" },
    { name: "清明", phenomenon: "天朗气清", hou1: "桐始华", hou2: "田鼠化为鴽", hou3: "虹始见" },
    { name: "谷雨", phenomenon: "谷雨时节", hou1: "萍始生", hou2: "鸣鸠拂其羽", hou3: "戴胜降于桑" },
    { name: "立夏", phenomenon: "夏季开始", hou1: "蝼蝈鸣", hou2: "蚯蚓出", hou3: "王瓜生" },
    { name: "小满", phenomenon: "谷物饱满", hou1: "苦菜秀", hou2: "靡草死", hou3: "麦秋至" },
    { name: "芒种", phenomenon: "芒种忙种", hou1: "螳螂生", hou2: "鵙始鸣", hou3: "反舌无声" },
    { name: "夏至", phenomenon: "夏至节气", hou1: "鹿角解", hou2: "蜩始鸣", hou3: "半夏生" },
    { name: "小暑", phenomenon: "小暑来临", hou1: "温风至", hou2: "蟋蟀居壁", hou3: "鹰始挚" },
    { name: "大暑", phenomenon: "大暑酷热", hou1: "腐草为萤", hou2: "土润溽暑", hou3: "大雨时行" },
    { name: "立秋", phenomenon: "秋季开始", hou1: "凉风至", hou2: "白露降", hou3: "寒蝉鸣" },
    { name: "处暑", phenomenon: "暑气消散", hou1: "鹰乃祭鸟", hou2: "天地始肃", hou3: "禾乃登" },
    { name: "白露", phenomenon: "白露凝霜", hou1: "鸿雁来", hou2: "玄鸟归", hou3: "群鸟养羞" },
    { name: "秋分", phenomenon: "秋分时节", hou1: "雷始收声", hou2: "蛰虫坯户", hou3: "水始涸" },
    { name: "寒露", phenomenon: "寒露降临", hou1: "鸿雁来宾", hou2: "雀入大水为蛤", hou3: "菊有黄华" },
    { name: "霜降", phenomenon: "霜降时节", hou1: "豺乃祭兽", hou2: "草木黄落", hou3: "蛰虫咸俯" },
    { name: "立冬", phenomenon: "冬季开始", hou1: "水始冰", hou2: "地始冻", hou3: "雉入大水为蜃" },
    { name: "小雪", phenomenon: "小雪飘飘", hou1: "虹藏不见", hou2: "天气上升地气下降", hou3: "闭塞而成冬" },
    { name: "大雪", phenomenon: "大雪纷飞", hou1: "鹖鴠不鸣", hou2: "虎始交", hou3: "荔挺出" },
    { name: "冬至", phenomenon: "冬至节气", hou1: "蚯蚓结", hou2: "麋角解", hou3: "水泉动" },
    { name: "小寒", phenomenon: "小寒寒冷", hou1: "雁北乡", hou2: "鹊始巢", hou3: "雉雊" },
    { name: "大寒", phenomenon: "大寒酷寒", hou1: "鸡乳", hou2: "征鸟厉疾", hou3: "水泽腹坚" }
];

// 节气数据（原有）
const solarTerms = [
    { name: "立春", phenomenon: "Spring begins\n春天开始", tradition: "时令播种，迎接新生命。" },
    { name: "雨水", phenomenon: "Rain starts falling\n雨水降临", tradition: "水润大地，适宜撒播种子。" },
    { name: "惊蛰", phenomenon: "Insects awaken\n万物苏醒", tradition: "雷声唤醒沉睡的生命。" },
    { name: "春分", phenomenon: "Spring Equinox\n春分时节", tradition: "白昼与黑夜长度相近，万象更新。" },
    { name: "清明", phenomenon: "Clear skies, bright days\n天朗气清", tradition: "祭扫墓地，缅怀先人。" },
    { name: "谷雨", phenomenon: "Grain Rain\n谷雨时节", tradition: "谷物滋养之雨，蔬菜种植的最佳时节。" },
    { name: "立夏", phenomenon: "Start of Summer\n夏季开始", tradition: "太阳能量显著增强，万物生长。" },
    { name: "小满", phenomenon: "Grain Fullness\n谷物饱满", tradition: "稻穗初现丰盈之态，夏熟作物籽粒开始饱满。" },
    { name: "芒种", phenomenon: "Glume Planting\n芒种忙种", tradition: "播种带芒的作物，收割早熟的农作。" },
    { name: "夏至", phenomenon: "Summer Solstice\n夏至节气", tradition: "一年中最长的一天，太阳能量达到顶峰。" },
    { name: "小暑", phenomenon: "Minor Heat\n小暑来临", tradition: "微热渐起，宜多进行降温活动。" },
    { name: "大暑", phenomenon: "Major Heat\n大暑酷热", tradition: "酷热难耐的盛夏高温期，常伴有暴雨。" },
    { name: "立秋", phenomenon: "Start of Autumn\n秋季开始", tradition: "酷暑退却，秋高气爽的季节来临。" },
    { name: "处暑", phenomenon: "End of Heat\n暑气消散", tradition: "热气消散之时，真正的秋凉尚未到来。" },
    { name: "白露", phenomenon: "White Dew\n白露凝霜", tradition: "清晨草叶上凝结出细微的白色露珠。" },
    { name: "秋分", phenomenon: "Autumn Equinox\n秋分时节", tradition: "秋季昼夜等长，气候转换的关键点。" },
    { name: "寒露", phenomenon: "Cold Dew\n寒露降临", tradition: "露水明显变冷，预示着冬季的临近。" },
    { name: "霜降", phenomenon: "Frost Descent\n霜降时节", tradition: "初霜开始在植物上覆盖，气温骤降。" },
    { name: "立冬", phenomenon: "Start of Winter\n冬季开始", tradition: "冬季的正式开启，进入寒冷季节活动期。" },
    { name: "小雪", phenomenon: "Minor Snow\n小雪飘飘", tradition: "轻微、温和的降雪开始出现。" },
    { name: "大雪", phenomenon: "Major Snow\n大雪纷飞", tradition: "大量且显著的积雪开始落下。" },
    { name: "冬至", phenomenon: "Winter Solstice\n冬至节气", tradition: "一年中最短的一天，标志着白昼变长的转折点。" },
    { name: "小寒", phenomenon: "Minor Cold\n小寒寒冷", tradition: "冬至后进入的极度严寒期。" },
    { name: "大寒", phenomenon: "Major Cold\n大寒酷寒", tradition: "全年中最冷的时期，深度的冰冻条件主导气候。" }
];

// 获取当前节气和候的信息
function getCurrentJieqiAndHou() {
    var today = to_day() + " 08:00:00";
    var year = today.split('-')[0];
    var jieqi_list = jieqi_d(year);
    
    // 确保有正确的节气列表
    var keys = Object.keys(jieqi_list);
    if (keys.length === 0) {
        return { termIndex: 0, hou: 0, daysInHou: 0, jieqi_list: {}, year: year, termsStatus: [] };
    }
    
    // 检查是否需要使用去年的数据（针对年初的节气）
    var firstJieqiDate = new Date(jieqi_list[keys[0]]).getTime();
    var nowTime = new Date(today).getTime();
    
    if (firstJieqiDate > nowTime) {
        year = Number(year) - 1;
        jieqi_list = jieqi_d(year);
        keys = Object.keys(jieqi_list);
    }
    
    // 准备下一年的数据
    var nextYearJieqiList = jieqi_d(Number(year) + 1);
    var nextYearKeys = Object.keys(nextYearJieqiList);
    
    // 构建完整的节气日期数组（包含下一年的立春）
    var allJieqiDates = [];
    for (var i = 0; i < keys.length; i++) {
        allJieqiDates.push(new Date(jieqi_list[keys[i]]).getTime());
    }
    allJieqiDates.push(new Date(nextYearJieqiList[nextYearKeys[0]]).getTime());
    
    // 查找当前节气
    var currentTermIndex = -1;
    var termStartDate, termEndDate;
    var termsStatus = [];
    var termDates = [];
    
    for (var i = 0; i < keys.length; i++) {
        var jieqiDate = allJieqiDates[i];
        var nextJieqiDate = allJieqiDates[i + 1];
        termDates.push({
            start: jieqi_list[keys[i]],
            end: i === keys.length - 1 ? nextYearJieqiList[nextYearKeys[0]] : jieqi_list[keys[i + 1]]
        });
        
        // 判断节气状态
        if (nowTime >= nextJieqiDate) {
            termsStatus[i] = 'past';
        } else if (nowTime >= jieqiDate && nowTime < nextJieqiDate) {
            termsStatus[i] = 'current';
            currentTermIndex = i;
            termStartDate = jieqiDate;
            termEndDate = nextJieqiDate;
        } else {
            termsStatus[i] = 'future';
        }
    }
    
    // 如果没找到，默认第一个
    if (currentTermIndex === -1) {
        currentTermIndex = 0;
        termStartDate = allJieqiDates[0];
        termEndDate = allJieqiDates[1];
    }
    
    // 计算候（每候约5天）
    var daysPassed = (nowTime - termStartDate) / (1000 * 60 * 60 * 24);
    var hou = Math.floor(daysPassed / 5);
    if (hou < 0) hou = 0;
    if (hou > 2) hou = 2;
    
    var daysInHou = Math.floor(daysPassed - hou * 5);
    if (daysInHou < 0) daysInHou = 0;
    if (daysInHou > 4) daysInHou = 4;
    
    return {
        termIndex: currentTermIndex,
        hou: hou,
        daysInHou: daysInHou,
        jieqi_list: jieqi_list,
        year: year,
        keys: keys,
        termsStatus: termsStatus,
        allJieqiDates: allJieqiDates,
        termDates: termDates,
        today: today
    };
}

// 设置容器为正方形
function setContainerSquare() {
    const container = document.getElementById('app-container');
    
    let availableWidth, availableHeight;
    
    // 方法1：检测是否在 iframe 中
    const isInIframe = window.self !== window.top;
    
    if (isInIframe) {
        // 在 iframe 中，尝试获取父窗口传递的尺寸或使用 iframe 内部可用空间
        try {
            // 尝试访问父窗口的尺寸信息
            if (window.parent && window.parent.innerWidth > 0) {
                availableWidth = window.parent.innerWidth;
                availableHeight = window.parent.innerHeight;
            }
        } catch (e) {
            // 跨域限制，无法访问父窗口
        }
    }
    
    // 如果还没有获取到有效尺寸，继续尝试其他方法
    if (!availableWidth || availableWidth <= 0) {
        // 方法2：尝试获取 window 尺寸
        if (window.innerWidth > 0 && window.innerHeight > 0) {
            availableWidth = window.innerWidth;
            availableHeight = window.innerHeight;
        }
        // 方法3：尝试获取 documentElement 尺寸
        else if (document.documentElement && document.documentElement.clientWidth > 0) {
            availableWidth = document.documentElement.clientWidth;
            availableHeight = document.documentElement.clientHeight;
        }
        // 方法4：尝试获取 body 尺寸
        else if (document.body && document.body.clientWidth > 0) {
            availableWidth = document.body.clientWidth;
            availableHeight = document.body.clientHeight;
        }
        // 方法5：尝试获取父元素尺寸
        else {
            const parent = container.parentElement;
            availableWidth = parent ? parent.clientWidth || 320 : 320;
            availableHeight = parent ? parent.clientHeight || 320 : 320;
        }
    }
    
    // 减去边距，防止超出屏幕
    const padding = 20; // 留 20px 边距
    const size = Math.min(availableWidth - padding, availableHeight - padding);
    const finalSize = Math.max(320, Math.min(800, size));
    
    container.style.width = `${finalSize}px`;
    container.style.height = `${finalSize}px`;
    
    return { width: finalSize, height: finalSize };
}

// 通知父窗口设置正确的 iframe 高度
function notifyParentIframeSize() {
    const container = document.getElementById('app-container');
    if (!container) return;
    
    const size = container.offsetWidth || container.style.width || 600;
    const height = typeof size === 'string' ? parseInt(size) : size;
    
    // 尝试通知父窗口
    try {
        // 使用 postMessage 通知父窗口
        if (window.parent && window.parent.postMessage) {
            window.parent.postMessage({
                type: 'iframeResize',
                height: height,
                width: height
            }, '*');
        }
    } catch (e) {
        // 跨域限制
    }
    
    // 同时设置 body 的高度，让 iframe 的 onload 能正确获取高度
    document.body.style.height = `${height}px`;
    document.documentElement.style.height = `${height}px`;
}

// 延迟重试设置正方形（用于 iframe 延迟加载场景）
function setContainerSquareWithRetry(maxAttempts = 5, delay = 100) {
    let attempts = 0;
    
    function trySet() {
        const container = document.getElementById('app-container');
        if (!container) return;
        
        const size = setContainerSquare();
        
        // 通知父窗口尺寸
        notifyParentIframeSize();
        
        // 如果尺寸还是最小的 320px，尝试延迟重试
        if (size.width === 320 && attempts < maxAttempts) {
            attempts++;
            setTimeout(trySet, delay * Math.pow(2, attempts));
        }
    }
    
    trySet();
}

// 设置 ResizeObserver 监听容器尺寸变化
function setupResizeObserver() {
    const container = document.getElementById('app-container');
    if (!container || typeof ResizeObserver !== 'function') return;
    
    const observer = new ResizeObserver((entries) => {
        for (const entry of entries) {
            const width = entry.contentRect.width;
            const height = entry.contentRect.height;
            
            // 如果当前尺寸和应该的正方形尺寸差异较大，重新设置
            const expectedSize = Math.min(window.innerWidth, window.innerHeight);
            const finalSize = Math.max(320, Math.min(800, expectedSize));
            
            if (Math.abs(width - finalSize) > 10) {
                setContainerSquare();
                // 触发重新渲染
                const currentInfo = getCurrentJieqiAndHou();
                container.innerHTML = '';
                const canvas = document.createElement('canvas');
                canvas.id = 'connection-canvas';
                container.appendChild(canvas);
                renderCentralHub(currentInfo);
                renderNodes(currentInfo);
            }
        }
    });
    
    observer.observe(container);
}

// 获取容器尺寸
function getContainerSize() {
    const container = document.getElementById('app-container');
    const rect = container.getBoundingClientRect();
    return { width: rect.width, height: rect.height };
}

// 智能绘制连接线
function drawSmartConnections(centerX, centerY, layoutType, ellipseParams, currentInfo) {
    const canvas = document.getElementById('connection-canvas');
    const ctx = canvas.getContext('2d');
    const containerSize = getContainerSize();
    
    canvas.width = containerSize.width;
    canvas.height = containerSize.height;
    
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    const { radiusX, radiusY } = ellipseParams;
    
    // 绘制黄道轨道（突出显示）
    ctx.beginPath();
    if (layoutType === 'fullCircle' || layoutType === 'compactCircle') {
        ctx.arc(centerX, centerY, radiusX, 0, Math.PI * 2);
    } else if (layoutType === 'landscapeSemiCircle') {
        ctx.arc(centerX, centerY, radiusX, Math.PI, 0);
    } else {
        drawEllipse(ctx, centerX, centerY, radiusX, radiusY);
    }
    ctx.strokeStyle = 'rgba(245, 214, 139, 0.4)';
    ctx.lineWidth = 3;
    ctx.stroke();
    
    // 添加黄道轨道光晕
    ctx.beginPath();
    if (layoutType === 'fullCircle' || layoutType === 'compactCircle') {
        ctx.arc(centerX, centerY, radiusX, 0, Math.PI * 2);
    } else if (layoutType === 'landscapeSemiCircle') {
        ctx.arc(centerX, centerY, radiusX, Math.PI, 0);
    } else {
        drawEllipse(ctx, centerX, centerY, radiusX, radiusY);
    }
    ctx.strokeStyle = 'rgba(230, 181, 80, 0.12)';
    ctx.lineWidth = 8;
    ctx.stroke();
    
    // 绘制内圈椭圆
    ctx.beginPath();
    if (layoutType === 'fullCircle' || layoutType === 'compactCircle') {
        ctx.arc(centerX, centerY, radiusX * 0.7, 0, Math.PI * 2);
    } else if (layoutType === 'landscapeSemiCircle') {
        ctx.arc(centerX, centerY, radiusX * 0.7, Math.PI, 0);
    } else {
        drawEllipse(ctx, centerX, centerY, radiusX * 0.7, radiusY * 0.7);
    }
    ctx.strokeStyle = 'rgba(196, 154, 108, 0.15)';
    ctx.lineWidth = 1;
    ctx.stroke();
    
    // 绘制24节气分度线（黄道24等分）
    const lineCount = layoutType === 'landscapeSemiCircle' ? 12 : 24;
    for (let i = 0; i < lineCount; i++) {
        let x, y;
        
        if (layoutType === 'landscapeSemiCircle') {
            const angle = (i * 180 / (lineCount - 1) - 90) * (Math.PI / 180);
            x = centerX + radiusX * Math.cos(angle);
            y = centerY - radiusY * Math.abs(Math.sin(angle));
        } else {
            const angle = (i * 360 / lineCount - 90) * (Math.PI / 180);
            x = centerX + radiusX * Math.cos(angle);
            y = centerY + radiusY * Math.sin(angle);
        }
        
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(x, y);
        ctx.strokeStyle = 'rgba(196, 154, 108, 0.15)';
        ctx.lineWidth = 1;
        ctx.stroke();
        
        // 绘制节气度数标记（每4个节气标注一次）
        if (i % 4 === 0 && layoutType !== 'landscapeSemiCircle') {
            const degree = (i * 15) % 360;
            const angle = (i * 360 / lineCount - 90) * (Math.PI / 180);
            const labelX = centerX + (radiusX * 1.1) * Math.cos(angle);
            const labelY = centerY + (radiusY * 1.1) * Math.sin(angle);
            
            ctx.font = `${Math.min(14, window.innerWidth * 0.015)}px "PingFang SC", sans-serif`;
            ctx.fillStyle = 'rgba(139, 90, 43, 0.6)';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(`${degree}°`, labelX, labelY);
        }
    }
    
    // 绘制太阳位置动画
    if (currentInfo) {
        drawSunAnimation(ctx, centerX, centerY, layoutType, ellipseParams, currentInfo);
    }
}

// 绘制太阳位置动画
function drawSunAnimation(ctx, centerX, centerY, layoutType, ellipseParams, currentInfo) {
    const { radiusX, radiusY } = ellipseParams;
    const termIndex = currentInfo.termIndex;
    const hou = currentInfo.hou;
    const daysInHou = currentInfo.daysInHou;
    
    // 计算太阳在黄道上的位置（更精确的位置）
    const totalProgress = termIndex + (hou * 5 + daysInHou) / 15;
    const angle = (totalProgress * 360 / 24 - 90) * (Math.PI / 180);
    
    let sunX, sunY;
    
    if (layoutType === 'landscapeSemiCircle') {
        const halfAngle = (totalProgress * 180 / (24 - 1) - 90) * (Math.PI / 180);
        sunX = centerX + radiusX * Math.cos(halfAngle);
        sunY = centerY - radiusY * Math.abs(Math.sin(halfAngle));
    } else {
        sunX = centerX + radiusX * Math.cos(angle);
        sunY = centerY + radiusY * Math.sin(angle);
    }
    
    // 绘制太阳光晕
    const gradient = ctx.createRadialGradient(sunX, sunY, 0, sunX, sunY, Math.min(radiusX, radiusY) * 0.12);
    gradient.addColorStop(0, 'rgba(245, 214, 139, 0.25)');
    gradient.addColorStop(0.5, 'rgba(230, 181, 80, 0.12)');
    gradient.addColorStop(1, 'rgba(212, 154, 60, 0)');
    
    ctx.beginPath();
    ctx.arc(sunX, sunY, Math.min(radiusX, radiusY) * 0.12, 0, Math.PI * 2);
    ctx.fillStyle = gradient;
    ctx.fill();
    
    // 绘制太阳本体
    ctx.beginPath();
    ctx.arc(sunX, sunY, Math.min(radiusX, radiusY) * 0.045, 0, Math.PI * 2);
    const sunGradient = ctx.createRadialGradient(sunX - 2, sunY - 2, 0, sunX, sunY, Math.min(radiusX, radiusY) * 0.045);
    sunGradient.addColorStop(0, '#FFF9E8');
    sunGradient.addColorStop(0.5, '#F5D68B');
    sunGradient.addColorStop(1, '#E6B550');
    ctx.fillStyle = sunGradient;
    ctx.fill();
    
    // 太阳光芒
    ctx.strokeStyle = 'rgba(245, 214, 139, 0.35)';
    ctx.lineWidth = 1.5;
    for (let i = 0; i < 8; i++) {
        const rayAngle = (i * Math.PI / 4) + (Date.now() / 2000 % Math.PI / 4);
        const innerRadius = Math.min(radiusX, radiusY) * 0.055;
        const outerRadius = Math.min(radiusX, radiusY) * 0.08;
        ctx.beginPath();
        ctx.moveTo(
            sunX + innerRadius * Math.cos(rayAngle),
            sunY + innerRadius * Math.sin(rayAngle)
        );
        ctx.lineTo(
            sunX + outerRadius * Math.cos(rayAngle),
            sunY + outerRadius * Math.sin(rayAngle)
        );
        ctx.stroke();
    }
}

// 绘制椭圆
function drawEllipse(ctx, cx, cy, rx, ry) {
    ctx.beginPath();
    for (let i = 0; i <= 360; i++) {
        const angle = (i - 90) * (Math.PI / 180);
        const x = cx + rx * Math.cos(angle);
        const y = cy + ry * Math.sin(angle);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
    }
    ctx.closePath();
}

// 获取中央枢纽尺寸（更大）
function getHubSize(layoutType) {
    const containerSize = getContainerSize();
    const size = Math.min(containerSize.width, containerSize.height);
    const width = window.innerWidth;
    
    let baseSize;
    if (width >= 1440 && layoutType === 'fullCircle') baseSize = 380;
    else if (layoutType === 'fullCircle') baseSize = 340;
    else if (layoutType === 'wideEllipse') baseSize = 300;
    else if (layoutType === 'landscapeSemiCircle') baseSize = 260;
    else if (layoutType === 'verticalEllipse') baseSize = 240;
    else if (layoutType === 'compactCircle') baseSize = 200;
    else baseSize = 180;
    
    return Math.min(baseSize, size * 0.55);
}

// 渲染中央枢纽（更大更像太阳）
function renderCentralHub(currentInfo) {
    const container = document.getElementById('app-container');
    const layoutType = getLayoutType();
    const hubSize = getHubSize(layoutType);
    
    const currentTermData = solarTermsData[currentInfo.termIndex];
    const houxian = ["初候", "二候", "三候"];
    const houList = [currentTermData.hou1, currentTermData.hou2, currentTermData.hou3];
    const currentHouText = houList[currentInfo.hou];
    const z_dic = { 1:"一", 2:"丁", 3:"上", 4:"止", 5:"正" };
    const currentDayChar = z_dic[currentInfo.daysInHou + 1];
    
    // 计算当前节气的黄道度数
    const currentDegree = (currentInfo.termIndex * 15 + Math.round((currentInfo.hou * 5 + currentInfo.daysInHou) / 15 * 15)) % 360;
    
    // 获取当前日期信息
    const now = new Date();
    const dateStr = now.getFullYear() + '年' + (now.getMonth() + 1) + '月' + now.getDate() + '日';
    
    const hub = document.createElement('div');
    hub.id = 'central-hub';
    hub.style.width = `${hubSize}px`;
    hub.style.height = `${hubSize}px`;
    
    // 简化后的黄道信息
    let contentHtml = '';
    if (hubSize >= 260) {
        contentHtml = `
            <div class="sun-icon">☀️</div>
            <div class="title">二十四节气</div>
            <div class="current-term">${currentTermData.name}</div>
            <div class="ecliptic-info">黄道 ${currentDegree}°</div>
            <div class="current-hou">${houxian[currentInfo.hou]} · ${currentDayChar}</div>
            <div class="current-phenomenon">${currentHouText}</div>
            <div class="date-info">${dateStr}</div>
        `;
    } else if (hubSize >= 200) {
        contentHtml = `
            <div class="sun-icon">☀️</div>
            <div class="current-term">${currentTermData.name}</div>
            <div class="ecliptic-info">黄道 ${currentDegree}°</div>
            <div class="current-hou">${houxian[currentInfo.hou]}</div>
            <div class="date-info">${dateStr}</div>
        `;
    } else {
        contentHtml = `
            <div class="sun-icon">☀️</div>
            <div class="current-term">${currentTermData.name}</div>
            <div class="ecliptic-info">${currentDegree}°</div>
        `;
    }
    
    hub.innerHTML = contentHtml;
    container.appendChild(hub);
}

// 判断设备类型和获取最佳布局
function getLayoutType() {
    const containerSize = getContainerSize();
    const width = containerSize.width;
    const height = containerSize.height;
    const aspectRatio = width / height;
    
    if (width >= 1024 && aspectRatio >= 1) {
        return 'fullCircle'; // 大屏幕横屏：完整圆形
    } else if (width >= 768) {
        return 'wideEllipse'; // 中等屏幕：宽椭圆
    } else if (aspectRatio > 1.2) {
        return 'landscapeSemiCircle'; // 小屏横屏：半圆
    } else if (aspectRatio < 0.8) {
        return 'verticalEllipse'; // 竖屏：垂直椭圆
    } else {
        return 'compactCircle'; // 方形屏：紧凑圆形
    }
}

// 获取节点大小
function getNodeSize(layoutType) {
    const containerSize = getContainerSize();
    const size = Math.min(containerSize.width, containerSize.height);
    const width = window.innerWidth;
    
    let baseSize;
    if (layoutType === 'fullCircle') baseSize = width >= 1440 ? 150 : 130;
    else if (layoutType === 'wideEllipse') baseSize = 105;
    else if (layoutType === 'landscapeSemiCircle') baseSize = 80;
    else if (layoutType === 'verticalEllipse') baseSize = 70;
    else if (layoutType === 'compactCircle') baseSize = 55;
    else baseSize = 48;
    
    return Math.min(baseSize, size * 0.18);
}

// 获取椭圆参数
function getEllipseParams(layoutType, centerX, centerY) {
    const containerSize = getContainerSize();
    const width = containerSize.width;
    const height = containerSize.height;
    
    let radiusX, radiusY, padding;
    
    switch(layoutType) {
        case 'fullCircle':
            padding = width >= 1440 ? 90 : 80;
            radiusX = Math.min(centerX, centerY) - padding;
            radiusY = radiusX;
            break;
        case 'wideEllipse':
            radiusX = centerX - 60;
            radiusY = centerY - 70;
            break;
        case 'landscapeSemiCircle':
            radiusX = centerX - 40;
            radiusY = centerY - 50;
            break;
        case 'verticalEllipse':
            radiusX = centerX - 35;
            radiusY = centerY - 40;
            break;
        case 'compactCircle':
        default:
            const compactRadius = Math.min(centerX, centerY) - 35;
            radiusX = compactRadius;
            radiusY = compactRadius;
    }
    
    return { radiusX, radiusY };
}

// 获取节点位置 - 智能布局
function getNodePosition(index, total, layoutType, centerX, centerY, ellipseParams) {
    const { radiusX, radiusY } = ellipseParams;
    
    // 标准角度（从顶部开始顺时针）
    let angle = (index * 360 / total - 90) * (Math.PI / 180);
    
    let x, y;
    
    switch(layoutType) {
        case 'landscapeSemiCircle':
            // 横屏模式：仅显示上半圆
            const halfAngle = (index * 180 / (total - 1) - 90) * (Math.PI / 180);
            x = centerX + radiusX * Math.cos(halfAngle);
            y = centerY - radiusY * Math.abs(Math.sin(halfAngle));
            break;
            
        case 'verticalEllipse':
        case 'wideEllipse':
        case 'fullCircle':
        case 'compactCircle':
        default:
            // 椭圆或圆形布局
            x = centerX + radiusX * Math.cos(angle);
            y = centerY + radiusY * Math.sin(angle);
    }
    
    return { x, y };
}

// 动画循环
let animationFrameId = null;
let globalCurrentInfo = null;
let globalLayoutType = null;
let globalEllipseParams = null;

function startAnimationLoop() {
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
    }
    
    function animate() {
        if (globalCurrentInfo) {
            const containerSize = getContainerSize();
            const centerX = containerSize.width / 2;
            const centerY = containerSize.height / 2;
            const canvas = document.getElementById('connection-canvas');
            canvas.width = containerSize.width;
            canvas.height = containerSize.height;
            
            globalLayoutType = getLayoutType();
            globalEllipseParams = getEllipseParams(globalLayoutType, centerX, centerY);
            
            drawSmartConnections(centerX, centerY, globalLayoutType, globalEllipseParams, globalCurrentInfo);
        }
        animationFrameId = requestAnimationFrame(animate);
    }
    animate();
}

// 渲染节气节点
function renderNodes(currentInfo) {
    globalCurrentInfo = currentInfo;
    
    const container = document.getElementById('app-container');
    const containerSize = getContainerSize();
    const centerX = containerSize.width / 2;
    const centerY = containerSize.height / 2;
    
    // 获取智能布局配置
    const layoutType = getLayoutType();
    const nodeSize = getNodeSize(layoutType);
    const ellipseParams = getEllipseParams(layoutType, centerX, centerY);
    
    // 候的进度字符映射
    const z_dic = { 1:"一", 2:"丁", 3:"上", 4:"止", 5:"正" };
    const houxian = ["初候", "二候", "三候"];
    
    // 绘制连接线（根据布局类型调整）
    drawSmartConnections(centerX, centerY, layoutType, ellipseParams, currentInfo);
    
    solarTermsData.forEach((term, index) => {
        const pos = getNodePosition(index, 24, layoutType, centerX, centerY, ellipseParams);
        const x = pos.x - nodeSize / 2;
        const y = pos.y - nodeSize / 2;
        
        const node = document.createElement('div');
        node.className = 'node';
        node.dataset.index = index;
        
        // 添加节气状态类
        const status = currentInfo.termsStatus[index];
        if (status === 'current') {
            node.classList.add('current-term');
        } else if (status === 'past') {
            node.classList.add('past-term');
        } else if (status === 'future') {
            node.classList.add('future-term');
        }
        
        // 动态设置节点尺寸
        node.style.width = `${nodeSize}px`;
        node.style.height = `${nodeSize}px`;
        node.style.left = `${x}px`;
        node.style.top = `${y}px`;
        node.style.animationDelay = `${index * 0.05}s`;
        
        // 设置 z-index：当前节气节点在最前面，其他节点按索引顺序覆盖
        if (status === 'current') {
            node.style.zIndex = 100; // 当前节气在最前面
        } else {
            // 其他节点按索引设置 z-index，实现鳞甲性覆盖效果
            node.style.zIndex = 10 + index;
        }
        
        // 构建候指示器 - 所有节点都显示
        let houIndicatorHtml = '';
        
        if (status === 'past') {
            // 已过去的节气，显示全部三候为完成
            houIndicatorHtml = `
                <div class="hou-indicator">
                    <div class="hou-dot past">正</div>
                    <div class="hou-dot past">正</div>
                    <div class="hou-dot past">正</div>
                </div>
            `;
        } else if (status === 'current') {
            // 当前节气，显示候进度
            let houDotsHtml = '';
            for (let h = 0; h < 3; h++) {
                let dotClass = '';
                let dotText = '';
                
                if (h < currentInfo.hou) {
                    // 已过的候
                    dotClass = 'past';
                    dotText = '正';
                } else if (h === currentInfo.hou) {
                    // 当前候，显示天数进度
                    dotClass = 'active';
                    dotText = z_dic[currentInfo.daysInHou + 1];
                } else {
                    // 未来的候
                    dotText = '〇';
                }
                
                houDotsHtml += `<div class="hou-dot ${dotClass}">${dotText}</div>`;
            }
            
            houIndicatorHtml = `
                <div class="hou-indicator">
                    ${houDotsHtml}
                </div>
            `;
        } else {
            // 未来的节气，显示空白候
            houIndicatorHtml = `
                <div class="hou-indicator">
                    <div class="hou-dot">〇</div>
                    <div class="hou-dot">〇</div>
                    <div class="hou-dot">〇</div>
                </div>
            `;
        }
        
        node.innerHTML = `
            <div class="term-name">${term.name}</div>
            <div class="term-phenomenon">${term.phenomenon}</div>
            ${houIndicatorHtml}
        `;
        
        // 添加悬浮事件（桌面设备）
        node.addEventListener('mouseenter', (e) => {
            // 悬停时提高 z-index，但不超过当前节气的 z-index
            if (status !== 'current') {
                node.style.zIndex = 80; // 悬停时提高，但低于当前节气的 100
            }
            showTooltip(term, index, currentInfo, e);
        });
        
        node.addEventListener('mousemove', (e) => {
            moveTooltip(e);
        });
        
        node.addEventListener('mouseleave', () => {
            // 离开时恢复原来的 z-index
            if (status !== 'current') {
                node.style.zIndex = 10 + index;
            }
            hideTooltip();
        });
        
        // 添加触摸事件（移动设备）
        node.addEventListener('touchstart', (e) => {
            e.preventDefault();
            const touch = e.touches[0];
            const touchEvent = {
                clientX: touch.clientX,
                clientY: touch.clientY
            };
            showTooltip(term, index, currentInfo, touchEvent);
        });
        
        node.addEventListener('touchmove', (e) => {
            const touch = e.touches[0];
            const touchEvent = {
                clientX: touch.clientX,
                clientY: touch.clientY
            };
            moveTooltip(touchEvent);
        });
        
        node.addEventListener('touchend', () => {
            // 延迟隐藏，让用户有时间看到提示
            setTimeout(hideTooltip, 2000);
        });
        
        container.appendChild(node);
    });
}

// 显示悬浮提示
function showTooltip(term, index, currentInfo, event) {
    let tooltip = document.getElementById('term-tooltip');
    if (!tooltip) {
        tooltip = document.createElement('div');
        tooltip.id = 'term-tooltip';
        tooltip.className = 'term-tooltip';
        document.body.appendChild(tooltip);
    }
    
    const status = currentInfo.termsStatus[index];
    const houxian = ["初候", "二候", "三候"];
    const houList = [term.hou1, term.hou2, term.hou3];
    const z_dic = { 1:"一", 2:"丁", 3:"上", 4:"止", 5:"正" };
    
    let houHtml = '';
    for (let i = 0; i < 3; i++) {
        let dotClass = 'future';
        let dotText = '〇';
        
        if (status === 'past') {
            dotClass = 'past';
            dotText = '正';
        } else if (status === 'current') {
            if (i < currentInfo.hou) {
                dotClass = 'past';
                dotText = '正';
            } else if (i === currentInfo.hou) {
                dotClass = 'active';
                dotText = z_dic[currentInfo.daysInHou + 1];
            }
        }
        
        houHtml += `
            <div class="tooltip-hou-item">
                <div class="tooltip-hou-dot ${dotClass}">${dotText}</div>
                <div><span class="font-semibold">${houxian[i]}：</span>${houList[i]}</div>
            </div>
        `;
    }
    
    let dateInfo = '';
    if (currentInfo.termDates && currentInfo.termDates[index]) {
        dateInfo = `<div class="tooltip-date">开始时间：${currentInfo.termDates[index].start}</div>`;
    }
    
    tooltip.innerHTML = `
        <div class="tooltip-term-name">${term.name}</div>
        <div class="tooltip-hou-section">
            <div class="tooltip-hou-title">物候现象</div>
            ${houHtml}
        </div>
        ${dateInfo}
    `;
    
    moveTooltip(event);
    
    requestAnimationFrame(() => {
        tooltip.classList.add('show');
    });
}

// 检测是否为移动设备
function isMobileDevice() {
    return window.innerWidth <= 768;
}

// 移动悬浮提示
function moveTooltip(event) {
    const tooltip = document.getElementById('term-tooltip');
    if (!tooltip) return;
    
    let x, y;
    
    if (isMobileDevice()) {
        // 移动设备优化：将提示框放在屏幕中央
        x = window.innerWidth / 2;
        y = window.innerHeight / 2;
        
        tooltip.style.left = '50%';
        tooltip.style.top = '50%';
        tooltip.style.transform = 'translate(-50%, -50%)';
    } else {
        // 桌面设备：跟随鼠标
        x = event.clientX + 15;
        y = event.clientY + 15;
        
        // 确保提示框不超出屏幕
        const tooltipRect = tooltip.getBoundingClientRect();
        let finalX = x;
        let finalY = y;
        
        if (x + tooltipRect.width > window.innerWidth) {
            finalX = event.clientX - tooltipRect.width - 15;
        }
        if (y + tooltipRect.height > window.innerHeight) {
            finalY = event.clientY - tooltipRect.height - 15;
        }
        
        tooltip.style.left = `${finalX}px`;
        tooltip.style.top = `${finalY}px`;
        tooltip.style.transform = 'translate(0, 0)';
    }
}

// 隐藏悬浮提示
function hideTooltip() {
    const tooltip = document.getElementById('term-tooltip');
    if (tooltip) {
        tooltip.classList.remove('show');
    }
}

// 初始化应用
function init() {
    setContainerSquareWithRetry();
    const currentInfo = getCurrentJieqiAndHou();
    renderCentralHub(currentInfo);
    renderNodes(currentInfo);
    
    // 通知父窗口尺寸
    setTimeout(notifyParentIframeSize, 100);
}

// 页面加载完成后执行
document.addEventListener('DOMContentLoaded', () => {
    init();
    startAnimationLoop();
    setupResizeObserver();
    
    // 添加额外的延迟检查，确保 iframe 完全加载
    setTimeout(() => {
        const container = document.getElementById('app-container');
        if (container && container.offsetWidth === 320) {
            setContainerSquareWithRetry();
            // 重新渲染
            const currentInfo = getCurrentJieqiAndHou();
            container.innerHTML = '';
            const canvas = document.createElement('canvas');
            canvas.id = 'connection-canvas';
            container.appendChild(canvas);
            renderCentralHub(currentInfo);
            renderNodes(currentInfo);
        }
    }, 500);
});

// 防抖函数
function debounce(func, wait = 250) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// 窗口大小改变时重新渲染（带防抖）
function handleResize() {
    setContainerSquare();
    const container = document.getElementById('app-container');
    const canvas = document.getElementById('connection-canvas');
    const tooltip = document.getElementById('term-tooltip');
    if (tooltip) tooltip.remove();
    container.innerHTML = '';
    container.appendChild(canvas);
    const currentInfo = getCurrentJieqiAndHou();
    renderCentralHub(currentInfo);
    renderNodes(currentInfo);
    
    // 更新全局参数
    const containerSize = getContainerSize();
    const centerX = containerSize.width / 2;
    const centerY = containerSize.height / 2;
    globalLayoutType = getLayoutType();
    globalEllipseParams = getEllipseParams(globalLayoutType, centerX, centerY);
    
    // 通知父窗口尺寸变化
    notifyParentIframeSize();
}

// 添加带防抖的 resize 事件监听
window.addEventListener('resize', debounce(handleResize, 300));
