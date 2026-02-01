
// 闰年计算
function leap_year(years){
    run = years%4;  //TODO 这里没考虑千禧年问题
    if (run === 0){
        return true
    }else{
        return false
    }
}

jz60 = [
    '甲子', '乙丑', '丙寅', '丁卯', '戊辰',
    '己巳', '庚午', '辛未', '壬申', '癸酉',
    '甲戌', '乙亥', '丙子', '丁丑', '戊寅',
    '己卯', '庚辰', '辛巳', '壬午', '癸未',
    '甲申', '乙酉', '丙戌', '丁亥', '戊子',
    '己丑', '庚寅', '辛卯', '壬辰', '癸巳',
    '甲午', '乙未', '丙申', '丁酉', '戊戌',
    '己亥', '庚子', '辛丑', '壬寅', '癸卯',
    '甲辰', '乙巳', '丙午', '丁未', '戊申',
    '己酉', '庚戌', '辛亥', '壬子', '癸丑',
    '甲寅', '乙卯', '丙辰', '丁巳', '戊午',
    '己未', '庚申', '辛酉', '壬戌', '癸亥'
  ]

// 甲子列表
function jaz_list(){

    var jaz_list = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
    var tg_list = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']

    var tl = tg_list.length;
    var t = 0;

    var jl = jaz_list.length;
    var j = 0;

    var jz60 = new Array();

    for(var i=0;i<60;i++){
        //console.log(jaz_list[j],tg_list[t]);

        jz60[i] = jaz_list[j]+tg_list[t]

        t++;
        j++;
        if(t>=tl){
            t=0;
        }
        if(j>=jl){
            j=0;
        }
    }
    return jz60;
}

// 天干年计算
function jaz_year(years){

    // 根据年份最后一个数字计算天干
    // 根据年份除以12 计算地支
    var tg_num = [4,5,6,7,8,9,0,1,2,3]
    var tg_list = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
    var dz_num = [4,5,6,7,8,9,10,11,0,1,2,3]
    var dz_list = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']

    var num = years%12;
    var dnum = dz_num.indexOf(num);

    var sy = years+"";
    var tnum=sy.split("")[sy.length-1]

    var tgnum = tg_num.indexOf(Number(tnum));

    return tg_list[tgnum]+dz_list[dnum]
}

// 按年份定首月干支
function jz_month(year){
    var tian = jaz_year(year)[0]
    var tg_list = {'甲':'丙寅','乙':'戊寅','丙':'庚寅','丁':'壬寅','戊':'甲寅',
                   '己':'丙寅','庚':'戊寅','辛':'庚寅','壬':'壬寅','癸':'甲寅'}

    dingyue = tg_list[tian]

    return dingyue

}

// 计算两个日期相差多少微秒
function time_day(start_time,end_time = today){
    let start = new Date(start_time)
    let end = new Date(end_time)
    return end.getTime()-start.getTime()
}

// 计算两个年份间有多少个闰年
function run_jisun(start_time,end_time){
    var num = 0;
    start = Number(start_time.split("-")[0])
    end = Number(end_time.split("-")[0])
    for(i=start; i<end+1;i++){
        if (leap_year(i)){
            num = num + 1
        }
    }
    return num;
}

// 12 节气 和 12 中气
jieqi =   ['立春', '惊蛰', '清明', '立夏', '芒种', '小暑',
           '立秋', '白露', '寒露', '立冬', '大雪', '小寒']
zhongqi = ['雨水', '春分', '谷雨', '小满', '夏至', '大暑',
           '处暑', '秋分', '霜降', '小雪', '冬至', '大寒']

jieqi24 = [
            '正  立春  东风解  蛰虫始  鱼陟冰', '正  雨水  獭祭鱼  候雁北  草木萌',
            '二  惊蛰  桃始华  仓庚鸣  鹰化鸠', '二  春分  玄鸟至  雷发声  电始至',
            '三  清明  桐始华  牡丹华  虹始见', '三  谷雨  萍始生  鸣鸠拂  戴胜桑',
            '四  立夏  蝼蝈鸣  蚯蚓出  王瓜生', '四  小满  苦菜秀  靡草死  麦秋至',
            '五  芒种  螳螂生  鹃始鸣  反舌无', '五  夏至  鹿角解  蜩始鸣  半夏生',
            '六  小暑  温风至  蟋蜂居  鹰始挚', '六  大暑  腐草萤  土润暑  大雨行',
            '七  立秋  凉风至  白露降  寒蝉鸣', '七  处暑  鹰祭鸟  天地肃  禾乃登',
            '八  白露  鸿雁南  玄鸟归  群鸟羞', '八  秋分  雷始收  蛰虫坯  水始涸',
            '九  寒露  鸿雁宾  雀入水  菊花黄', '九  霜降  豺祭兽  草黄落  蛰虫俯',
            '十  立冬  水始冻  地始冻  雉入水', '十  小雪  虹藏末  天气升  塞成冬',
            '冬  大雪  鹖鴠不  虎始交  荔挺出', '冬  冬至  蚯蚓结  麇角解  水泉动',
            '腊  小寒  雁北乡  鹊始巢  雉雊声', '腊  大寒  鸡乳卵  征鸟厉  泽腹坚'
          ]

// 月份天数
month_day = [31,28,31,30,31,30,31,31,30,31,30,31]

// 节气定位
function jieqi_d(year){

    var jieqi_list={};

    if (leap_year(year)){
        month_day[1]=29
    }

    var yd = year+"".split()
    yd_num = Number(yd[2]+yd[3])

    // TODO 不知道这里怎么计算出C值的
    // 计算公式 [Y×D+C]-L
    // Y = 后两位
    // 立春C值
    year20 = [4.6295,19.4599,6.3826,21.4155,5.59,20.88,6.318,21.86,6.5,22.2,7.28,
              23.65,28.35,23.95,8.44,23.822,9.098,24.218,8.218,23.08,7.9,22.6,6.11,20.84]
    year21 = [3.87,18.73,5.63,20.646,4.81,20.1,5.52,21.04,5.678,21.37,7.108,22.83,
              7.5,23.13,7.646,23.042,8.318,23.438,7.438,22.36,7.18,21.94,5.4055,20.12]

    const D = 0.2422

    month_1 = [2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,1,1]

    if ((Number(yd[0]+yd[1])+1)===20){
        year2 = year20
    }

    if ((Number(yd[0]+yd[1])+1)===21){
        year2 = year21
    }

    for (var j=0;j<jieqi24.length;j++){
        lichun = parseInt(yd_num*D+year2[j])-parseInt((yd_num-1)/4)
        jieqi_list[jieqi24[j]]=year+"-"+month_1[j]+"-"+lichun
        if (j==21)
            year=Number(year)+1
    }

    return jieqi_list;

}

function to_day(){
    var myDate = new Date();
    var y = myDate.getFullYear();
    var m = myDate.getMonth()+1;
    var d = myDate.getDate();

    today = y+"-"+m+"-"+d //格林威治时间是从 1970-1-1 08:00:00 开始计算的

    return today
}

// 日柱计算计算
function rizhu(date=null){

    today = to_day()+" 08:00:00"

    var start_time = '1970-04-14'
    var s_end_time = end_time = date
    if (!end_time){
        s_end_time = "今天"
        end_time = today
    }

    var str_h;
    var week = new Date().getDay();
    switch (week) {
        case 0 :
                str_h = "日";
                break;
        case 1 :
                str_h = "一";
                break;
        case 2 :
                str_h = "二";
                break;
        case 3 :
                str_h = "三";
                break;
        case 4 :
                str_h = "四";
                break;
        case 5 :
                str_h = "五";
                break;
        case 6 :
                str_h = "六";
                break;
    }

    year = end_time.split('-')[0]
    month = end_time.split('-')[1]

    var jm = jz_month(year)  //计算第一个月

    //获取第一个月在干支中的位置
    var jz = jaz_list()
    var m_one = jz.indexOf(jm)

    // 节气日期对照表
    var jieqi_list = jieqi_d(year);
    for( let jieqi of jieqi24){
        var jieqi_time = new Date(jieqi_list[jieqi]).getTime()
        var now_time = new Date(end_time).getTime()-8*60*60*1000
        if (jieqi_time>=now_time){
            j_time = parseInt((jieqi_time-now_time)/1000/60/60/24)
            if (j_time === 0){
                j_time = "今天"
            }else{
                j_time = j_time+"日后"
            }

            j_is = jieqi
            break
        }
    }

    // 根据当前节气 推算出月份
    var jieqi_time = new Date(jieqi_list[jieqi[Number(month)-2]]).getTime()
    var now_time = new Date(end_time).getTime()

    //当月节气时间 和 当前时间对比
    if(jieqi_time<now_time)
    {
        gz_month=jz[m_one+Number(month)-2]
    }else{
        gz_month=jz[m_one+Number(month)-3]
    }

    var to_times = time_day(start_time,end_time)

    var day = to_times/1000/60/60/24

    // 暴力计算当天干支
    var jz = jaz_list()
    var jm = day%60
    // console.log(jz[jm],"日")

    // 当前时间 干支年-月-日
    var rt_list = new Array();
    rt_list.push(end_time," 星期"+str_h,j_time+j_is,jaz_year(year),gz_month,jz[jm]);
    return rt_list
}

function shichen(h,m=0){
    var tg_list = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
    var hh = 0;
    if (h>23 && h<1)
    {
        hh = tg_list[0];
    }
    for(i=1;i<=23;i=i+2)
    {
       if(Number(h)<=Number(i) && Number(h)>=Number(i-1) ){
            sh = tg_list[hh]
            if(i-h===1){
               k1 = 0
            }else{
               k1 = 2
            }
       }
       hh++;

    }
    ke = ['1','2','3','4']
    var mm = 0;
       if(Number(m)>30){
            sk = ke[mm+k1+1]
       }else{
            sk = ke[mm+k1]
       }

    console.log(sh,"时",sk,"刻")
}


//打印节气列表
var jieqi_list = jieqi_d(2023);
// console.log(jieqi_list)

console.log(rizhu())

//当前时刻
var n = new Date();
hh = n.getHours();
mm = n.getMinutes();
shichen(hh,mm)

// 计算两个时间差异
start_time = "1983-02-28"
end_time = to_day()
var run_num = run_jisun(start_time,end_time)

to_times = time_day(start_time,end_time+" 08:00:00")

// console.log(start_time/1000)          //秒
// console.log(start_time/1000/60)       //分钟
// console.log(start_time/1000/60/60)    //小时

console.log("从",start_time,"到",end_time,"相距",to_times/1000/60/60/24,"天")
// console.log(parseInt(((to_times/1000/60/60/24)-run_num)/365),"年 零",((to_times/1000/60/60/24)-run_num)%365,"天")

function getQueryString() {
  var qs = location.search.substr(1), // 获取url中"?"符后的字串
    args = {}, // 保存参数数据的对象
    items = qs.length ? qs.split("&") : [], // 取得每一个参数项,
    item = null,
    len = items.length;

  for(var i = 0; i < len; i++) {
    item = items[i].split("=");
    var name = decodeURIComponent(item[0]),
      value = decodeURIComponent(item[1]);
    if(name) {
      args[name] = value;
    }
  }
  return args;
}

