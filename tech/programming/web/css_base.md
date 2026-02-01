@charset "utf-8";
/*****************************
 *  css制作案例
 *
 *  2011-12-18
 *  
 *  yywolf
 *
 */

/* css头设定 */
* {margin:0; padding:0;}  /* 配通符 */
body{ font-size:12px; margin:0px; padding:0px; text-align:left; color:#000; background:#fff; font-family:Tahoma, Verdana; }
a {margin: 0px;padding:0px;border:0px;} /* 属性选择器 */
a:link,a:visited {color:#000;text-decoration:none;}
a:hover {color:red;text-decoration: none;}

/*link rel="stylesheet" type="text/css" href="../c3.css"*/


body > p { font-size:14px; }  /* 子对象包含选择器 */
/* 所有作为body的子对象的p对象字体尺寸为14px */

h1 + p + p + p {margin-top:50px;font-size:14px;}   /* 相邻兄弟 标签之后的一个选择器属性 */

p.important {color:red;}  /* 包含属性选择器 */

a:link {font-size:12px;} /* 链接 */  
a:visited {font-size:12px;} /* 已访问 */  
a:hover {font-size:14px;} /* 悬停 */  
/* 以上使用标记选择器 */

span[class=demo] { color: red; }  /* 属性包含选择器 */

img:hover {background:#E0E0E0;}

/**  伪类
:link CSS1 IE4+ , NS4+ 设置a对象在未被访问前的样式表属性
:hover CSS1/CSS2 IE4+ , NS4+ 设置对象在其鼠标悬停时的样式表属性
:active CSS1/CSS2 IE4+ 设置对象在被用户激活（在鼠标点击与释放之间发生的事件）时的样式表属性
:visited CSS1 IE4+ , NS4+ 设置a对象在其链接地址已被访问过时的样式表属性
:focus CSS2 NONE 设置对象在成为输入焦点（该对象的onfocus事件发生）时的样式表属性
:first-child CSS2 NONE 设置对象（Selector1）的第一个子对象（Selector2）的样式表属性
:first CSS2 IE4+ 设置页面容器第一页使用的样式表属性。仅用于@page规则
:left CSS2 IE4+ 设置页面容器位于装订线左边的所有页面使用的样式表属性。仅用于@page规则
:right CSS2 IE4+ 设置页面容器位于装订线右边的所有页面使用的样式表属性。仅用于@page规则
:lang CSS2 NONE 设置对象使用特殊语言的内容样式表属性  
 * */


/*选择器集体声明*/
div,img,ol,ul,li,dl,dt,dd{    /* 分组选择器 */
  border:0;
  list-style:none; /*无前置符号*/
  overflow:hidden;  
  margin:0;
  padding:0;
}
h1,h2,h3,h4,h5,h6 {  
  font-size:12px;
  margin:0;
  padding:0;
}
div { display: block; }

#container {         /* id 选择器 */
    margin:0 auto;
    /* 宽度 */
    width:auto;
    min-width:450px;
    max-width:960px;
}
#header { height:130px; background:#fff; margin-bottom:5px;}
#mainContent {
/* 尺寸 */
height:auto;
min-height:350px;
max-height:900px;
margin:5px;
}
#footer {height:80px; background:#6cf; }

#menu { background: url(images/nav_bg.gif) -2px 0px repeat-x; border-top: #EEE 1px solid; height:40px; }
#menu ul { float:left; margin-left:40px;} /* 定位 */   /* 属性包含选择器 */
#menu ul li {width:122px; line-height:39px; float:left; text-align:center; background: url(images/img.gif) 120px 0px no-repeat;}
#menu ul li a { display: block; margin-top:0px; width: 100%;height: 100%;color: #333333;display: block; font-weight: bolder; }
#menu ul li a:hover { background-color:#333; color:#FFF; outline: red groove thin ; }

.auto { margin-bottom:10px; margin:auto; width:520px; text-align:center; display:block; overflow:hidden; clear:both; }  /* 类选择器 */
.auto ul { height:25px; margin-top:10px;}
.auto ul li { padding: 4px 0 0; color: #1e50a2; height:21px; width:80px; float:left;}
.auto ul li a { line-height:21px; width:80px; color:#000; font-size:12px; }

#state { text-align:center; font-size:12px; margin-top:10px; }


/*字体设置*/
/* font : font-style || font-variant || font-weight || font-size || line-height || font-family */
.font {
font: italic small-caps bold  15px 20px Tahoma,Verdana;
font-style:none;   /*字体格式*/
font-variant:normal ;  /*小型大写字母*/
font-weight:bold;  /*粗体*/
font-size:15px;
line-height:26px;
font-family:幼圆;
color:#000;  
font-size-adjust:15px;  /*强制大小 不允许改变*/
font-stretch:wider;   /*拉伸变形*/
letter-spacing:0px;   /* 字间距 */
word-spacing : 10;  /* 单词间空格*/

text-decoration:none;  /*字体装饰 */
/*
underline :  下划线
line-through :  贯穿线
overline :  上划线
*/

/*特殊效果*/
text-shadow:0px 0px 13px #000, 0px 0px 10px orange, red 1px 1px;  /* 渲染 ie下无效*/

text-transform:none;
/*
capitalize : 将每个单词的第一个字母转换成大写，其余无转换发生
uppercase : 转换成大写
lowercase : 转换成小写      
*/

}


/* 文本设置 */
.text{
text-indent :20px;  /* 首行缩进 */
overflow: hidden;
text-overflow:ellipsis; /* 溢出省略 */
vertical-align:middle;  /* 垂直对齐 */
text-align:left;   /* 对齐方式 */
--layout-flow:vertical-ideographic;  /* 文字竖排 IE下生效 */
--writing-mode : tb-rl;  /* 更变文字书写格式  上-下 右-左 */
--direction : rtl;   /* 文本流方向 */
--unicode-bidi:bidi-override;
word-break:normal;   /* 文字断行格式 */
white-space : nowrap;   /* 强制在同一行现实文本 */
break-word:word-wrap;   /* 边界换行 */
text-kashida-space : 50%;   /* 膨胀系数 */
}

/* 设置背景 */
/* background : background-color || background-image || background-repeat || background-attachment || background-position */
.background {
background-attachment : fixed; /* 固定背景  */
background-position: 35% 80%; /* 检索背景图片 */
/* background-positionX:
   background-positionY: */
background-repeat : no-repeat; /* 不重复 repeat-x  repeat-y */
layer-background-color : transparent;   /* 检索区域背景颜色 背景透明 */
layer-background-image : url();      /* 检索区域背景图片 */
}

/* 定位 */

/* position : static | absolute | fixed | relative
 * position : 无特殊定位 | 拖出定位 | 不可层叠 | 相对定位
 */

/*  top
 *  left
 *  right
 *  bottom
 * */


#clip {position:absolute; z-index:10; width:960px; height:80px; clip:rect(20px 925px 60px 880px); visibility:inherit;} /* 切割对象 */

.layout{
    clear:none; /*浮动 both 不允许  left左不允许  right右不允许*/
    overflow:visible; /* visible 显示全部  auto 自动 hidden 不显示超出内容  scroll  显示滚动条 */
    /* overflow-x overflow-y */
    display:none; /* none 不显示 block 添加新行 inline 内联 */
    visibility: inherit; /* inherit 集成 visible 可视 hidden 隐藏    这个属性会保留空间*/
}

body {

/* 轮廓 画线  */
/* outline : outline-color ||outline-style || outline-width */
outline:#E9E9E9 dotted thin;

/* 边框 */
/* border : border-width || border-style || border-color */
/* border-top : border-width || border-style || border-color */
/* border-right : border-width || border-style || border-color */
/* border-bottom : border-width || border-style || border-color */
/* border-left : border-width || border-style || border-color */
/*
 * border-bottom-color
 * border-bottom-style
 * border-bottom-width
 * /

/*
 * outline-style
none :  无边框。与任何指定的outline-width值无关
dotted :  点线边框
dashed :  虚线边框
solid :  实线边框
double :  双线边框。两条单线与其间隔的和等于指定的oueline-width值
groove :  根据outline-color的值画3D凹槽
ridge :  根据outline-color的值画菱形边框
inset :  根据outline-color的值画3D凹边
outset :  根据outline-color的值画3D凸边
*/

/*
 * outline-width
medium :  默认宽度
thin :  小于默认宽度
thick :  大于默认宽度
length :  由浮点数字和单位标识符组成的长度值。不可为负值。请参阅长度单位
*/

}


#include {
position: absolute;
top: 100px; left: 5px; width: 20px; height: 30px;
border: thin solid black;
include-source:url("http://www.baidu.com/img/baidu_sylogo1.gif");
}

q { quotes:"***" "****" "\:" ""; }  /* 指定q标签的引用标识  q嵌套后 前两个是外层 后两个是内层*/

/* 列表 */
/* list-style : list-style-image || list-style-position || list-style-type
 * list-style-image: url("images/ie.gif");
 * list-style-position : outside | inside  标记在文本外  标记在文本内
 * list-style-type : disc;  标记样式
 * marker-offset : auto | length   列表距离
disc :   实心圆
circle :   空心圆
square :   实心方块
decimal :   阿拉伯数字
lower-roman :   小写罗马数字
upper-roman :   大写罗马数字
lower-alpha :   小写英文字母
upper-alpha :   大写英文字母
none :   不使用项目符号
armenian :   传统的亚美尼亚数字
cjk-ideographic :   浅白的表意数字
georgian :   传统的乔治数字
lower-greek :   基本的希腊小写字母
hebrew :   传统的希伯莱数字
hiragana :   日文平假名字符
hiragana-iroha :   日文平假名序号
katakana :   日文片假名字符
katakana-iroha :   日文片假名序号
lower-latin :   小写拉丁字母
upper-latin :   大写拉丁字母
 * /

/* 更改鼠标
 * cursor : auto | crosshair | default | hand | move | help | wait | text | w-resize |s-resize | n-resize |e-resize | ne-resize |sw-resize | se-resize | nw-resize |pointer | url (url)
 */



/* 表格
 * border-collapse : separate | collapse   是否显示边框
 * border-spacing :   边框宽度
 * caption-side : bottom | left |right | top   设置表格的caption在表格的那一边
 * empty-cells : hide | show    单元格无内容时是否显示边框
 * table-layout : auto | fixed  表格布局算法
 * speak-header : once | always 表格头
 * */


/* 滚动条
 * scrollbar-3d-light-color :   滚动条边框颜色
 * scrollbar-highlight-color    滚动条底色
 * scrollbar-face-color         滚动条表面颜色
 * scrollbar-arrow-color        箭头颜色
 * scrollbar-shadow-color       检索边界颜色
 * scrollbar-dark-shadow-color  暗框颜色
 * scrollbar-base-color         基准颜色
 * */




/*
 * content: 插入
attr(alt) : 使用alt的文字
counter(name) :  使用已命名的计数器
counter(name, list-style-type) :  使用已命名的计数器并遵从指定的list-style-type属性
counters(name, string) :  使用所有已命名的计数器
counters(name, string, list-style-type) :  使用所有已命名的计数器并遵从指定的list-style-type属性
no-close-quote :  并不插入quotes属性的后标记。但增加其嵌套级别
no-open-quote :  并不插入quotes属性的前标记。但减少其嵌套级别
close-quote :  插入quotes属性的后标记
open-quote :  插入quotes属性的前标记
string :  使用用引号括起的字符串
url :  使用指定的绝对或相对地址


counter-increment : none | identifier number;   content 计数器
counter-reset : none | identifier number;   计数器复位

*/
/* 后 */
/* 在字段前后添加文字 */
.link {}

/*
a:after { content: attr(href); text-decoration: none; } 后
a:before { content: url("http://www.baidu.com/") }  前
*/
.link a:before { content:" ---"; color:#000;}
.link a:after {content:"--- "; color:#000; }

/* 打印属性
 * page
 * page-break-after : auto | always | avoid | left | right | null
 * page-break-before : auto | always | avoid | left | right | null
 * page-break-inside : auto | avoid
 * marks : none | crop || cross
 * orphans : number
 * size : auto | portrait | landscape | length
 * widows : number
 * */

/*
voice-family   有 设置或检索当前声音类型
volume   有 设置或检索音量
elevation   有 设置或检索当前声音的音源仰角
azimuth   有 设置或检索当前声音的音场角度
stress   有 和pitch-range相似。设置或检索当前声音波形的最高峰值
richness   有 设置或检索当前声音的音色
speech-rate   有 设置或检索发音速度
cue   无 设置在对象前后播放的声音
cue-after   无 设置在对象后播放的声音
cue-before   无 设置在对象前播放的声音
pause   无 设置对象前后的声音暂停
pause-after   无 定义对象内容被发音后的暂停
pause-before   无 定义对象内容发音前的暂停
pitch   有 设置或检索音高
pitch-range   有 设置或检索声音的平滑程度
play-during   无 设置或检索背景音乐的播放
speak   有 设置或检索声音是否给出
speak-numeral   有 设置或检索数字如何发音
speak-punctuation   有 设置或检索标点符号如何发音
*/
/*
s ms hz khz
*/


/* DHTML 行为
 * behavior : url (url) | url (#objID ) | url (#default#behaviorName)
 * div { behavior: url(fly.htc) url(shy.htc); }
 *
 * */

/* css 滤镜
div { width:200px; filter:blur(strength=50) flipv() ; }


zoom : normal | number   缩放比例


*/

/*  代码备忘  
 ***************************************************************/

/*css图片自适应代码 */

.lefta{
        width:160px;
        height:180px;
        vertical-align:middle;
        background:#ff0;
        margin:0 auto;
      }  

.lefta img{
   vertical-align:middle;
   border:1px solid #ff0000;
   max-width:150px;  
   max-height:170px;
   width:expression(this.width > 150 ? "150px" : this.width+"px");
   height:expression(this.height > 170 ? "170px" : this.height+"px");
   position: relative; /* 相对定位 */
   position: absolute ; /* 绝对定位*/
   top:5%;
   }
/*一上使用类别选择器*/

/* div li img  选择器嵌套*/
/* .abc > li >a {....}  子选择器 不包含孙选择器*/

.kuai {
        z-index:10; /* 层叠位置 */
      }

@import url("foo.css") screen, print;
@import "print.css"
@charset "Shift-JIS";   指定字符集

/* !important 提升样式优先权！可以在一个类中用同样两个定义！不支持优先权时！使用另一个！  */
#someNode
{
    position: fixed;  /*定位*/
   #position: fixed;
   _position: fixed;
}
/*
    * 第一排给Firefox以及其他浏览器看
    * 第二排给IE7（可能以后的IE8、IE9也是如此，谁知道呢）看
    * 第三排给IE6以及更老的版本看
*/
#abc {
       margin-top:20px; /* 火狐 */
       *margin-top:40px !important; /* ie7 */
       *margin-top:80px; /* ie6 */  
     }
/* 要注意先后顺序 */
/* 一上为id选择器*/

/* 长度元素
em CSS1 IE4+ , NS4+ 相对于当前对象内文本的字体尺寸
ex CSS1 IE4+ , NS4+ 相对于字符 “ x ” 的高度。通常为字体高度的一半
px CSS1 IE3+ , NS4+ 像素（Pixel）
绝对长度单位  Absolute Length Units
pt CSS1 IE3+ , NS4+ 点（Point）
pc CSS1 IE3+ , NS4+ 派卡（Pica）。相当于我国新四号铅字的尺寸
in CSS1 IE3+ , NS4+ 英寸（Inch）
cm CSS1 IE3+ , NS4+ 厘米（Centimeter）
mm CSS1 IE3+ , NS4+ 毫米（Millimeter）
*/

/* 角度
deg CSS2 NONE 度。一个圆圈的360等分之一
grad CSS2 NONE 梯度。一个直角的100等分之一。一个圆圈相当于400grad
rad CSS2 NONE 弧度。把一个圆圈分成2*PI单位
*/

/* 颜色
#RRGGBB CSS1 IE4+ , NS4+ 三个两位十六进制正整数。取值范围为：00 - FF
rgb ( R,G,B ) CSS1 IE4+ , NS4+ 表示红，绿，蓝的正整数或百分数数值
Color Name CSS1 IE4+ , NS4+ 颜色名称。不同的浏览器会有不同的预定义颜色名称。请查看附录：颜色表  
 * */

/*
IE6下DIV布局会多出一条线和多出最后1-2个字的解决办法
<div style="height:0px;overflow:hidden;"><br /></div>
<div style="overflow:hidden;">浮动内容</div>
*/
/*引用服务器字体*/
@font-face { font-family: dreamy; font-weight: bold; src: url(http://www.example.com/font.eot); }
@fontdef url("http://www.example.com/sample.pfr");
@page thin:first { size: 3in 8in }  /* 页面属性 */

/* 使用字体 */
.fontyes {font-family:dreamy;}

/* 设备属性 */
/* 设置显示器用字体尺寸 */
@media screen {
BODY {font-size:12pt; }
}

/* 设置打印机用字体尺寸 */
@media print {
@import "print.css"
BODY {font-size:8pt;}
}

@media screen and (min-width: 600px) and (max-width: 900px) {
/* 自适应设置 */
 }

/*  设备列表
all CSS2 IE4+ 用于所有设备类型
aural CSS2 NONE 用于语音和音乐合成器  
braille CSS2 NONE 用于触觉反馈设备
embossed CSS2 NONE 用于凸点字符（盲文）印刷设备
handheld CSS2 NONE 用于小型或手提设备  
print CSS2 IE4+ 用于打印机
projection CSS2 NONE 用于投影图像，如幻灯片
screen CSS2 IE4+ 用于计算机显示器
tty CSS2 NONE 用于使用固定间距字符格的设备。如电传打字机和终端
tv CSS2 NONE 用于电视类设备   
 * */

@font-face {
    font-family:'Anivers';
    src: url('/images/Anivers.otf') format('opentype');
    }
@font-face {
        font-family: 'YourWebFontName';
        src: url('YourWebFontName.eot'); /* IE9 Compat Modes */
        src: url('YourWebFontName.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
             url('YourWebFontName.woff') format('woff'), /* Modern Browsers */
             url('YourWebFontName.ttf')  format('TrueType'), /* Safari, Android, iOS */
             url('YourWebFontName.svg#YourWebFontName') format('svg'); /* Legacy iOS */
   }
/*
可以使用的文件格式为OpenType文件格式和TrueType文件格式
*/

命名规则

头：header
内容：content/container
尾：footer
导航：nav
侧栏：sidebar
栏目：column
页面外围控制整体佈局宽度：wrapper
左右中：left right center
登录条：loginbar
标志：logo
广告：banner
页面主体：main
热点：hot
<a href="http://www.html5cn.org/portal.php?mod=list&catid=9" target="_blank" class="relatedlink">新闻</a>：news
下载：download
子导航：subnav
菜单：menu
子菜单：submenu
搜索：search
友情链接：friendlink
页脚：footer
版权：copyright
滚动：scroll
内容：content
标签：tags
文章列表：list
提示信息：msg
小技巧：tips
栏目标题：title
加入：joinus
指南：guide
服务：service
注册：regsiter
状态：status
投票：vote
合作伙伴：partner
导航：nav
主导航：mainnav
子导航：subnav
顶导航：topnav
边导航：sidebar
左导航：leftsidebar
右导航：rightsidebar
菜单：menu
子菜单：submenu
标题: title
摘要: summary
