<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- ie中  DOCTYPE 前不能有任何东西 -->
<!--   
过渡的(Transitional):要求非常宽松的DTD，它允许你继续使用HTML4.01的标识
严格的(Strict):要求严格的DTD，你不能使用任何表现层的标识和属性
框架的(Frameset):专门针对框架页面设计使用的DTD，如果你的页面中包含有框架，需要采用这种DTD   
-->

<html xmlns="http://www.w3.org/1999/xhtml" lang="UTF-8"> <!-- 名字空间 -->
<head>
<title>标题</title>

  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Language" content="zh-cn" />
  <meta name="Generator" content="notepad2">
  <meta name="Author" content="作者">
  <meta name="Keywords" content="关键字">
  <meta name="Description" content="简介">
  <meta name="Copyright" content="自由版权,任意转载" />   
  <!--指定时间跳转指定网址 META HTTP-EQUIV="REFRESH" CONTENT="x; URL=*.*" -->

  <meta name="viewport" content="width=1280, initial-scale=1"> <!-- 针对手机显示像素点 -->

  <link rel="icon" href="/static/ico.ico" mce_href="/static/ico.ico" type="image/x-icon" />
  <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
  <link rel="icon" href="animated_favicon.gif" type="image/gif" >

<!-- 基准链接 -->   
<base href="http://www.w3school.com.cn/i/" />
<base target="_blank" />

</head>
<body>

<A NAME="aaaa">设置锚点</A>  <!-- rel="nofollow"  告诉搜索引擎 我不能控制其链接 -->
<A HREF="#aaaa" title="锚点">返回锚点</A>   
<!-- 锚点在其她档案用 HREF="URL#aaaa" -->

<A HREF="#" target="_self" title="说明文字">链接</A>
<!--   
     _blank,  开在新的浏览视窗中   
     _self,   显示在目前的视窗中。   
     _parent, 当成文件的上一个画面。   
     _top     整个画面重新显示成连结的内容   
-->   

<p>段落标签</p>

<addr title="yywolf">yy.</addr>定义缩写
<address>地址元素</address>
<article>独立内容 外部引用</article>
<aside>与article相关内容</aside>
<cite>标题<cite>
<code> 代码 </code>

<bdo dir="rtl">hello. 你好</bdo> 文字方向

<blockquote>长定义换行</blockquote>

特殊字符   
&reg; &nbsp; &copy; &lt; &gt; &trade; &quot; &euro;
<!--商标  空格  版权  <  >  tm  "   欧元-->

<!--表单-->
<form action="" method="post"> <!-- get url传递 post本地传递 -->
<label for="name">这里是有好提示</label> <!-- 根据id提示表单 -->
<input onmouseover="this.focus()" onmousedown="this.value=''" maxlength="10" type="text" name="name" id="name" value="单击更换内容">
<input type="button" value="submit1" onclick="javascript:document.f.action='login1';document.f.submit();" />


<SELECT NAME="" size = multiple onChange="Menu(this.form,1);">
<option value="" selected>---请选择---</option>
<option value="1">列表框1</option>   
<option value="2">列表框2</option>   
<option value="3">列表框3</option>   
</SELECT><!-- multiple 多选 -->

<TEXTAREA NAME="" ROWS="" COLS="20">文本框</TEXTAREA> <!-- ROWS 行 COLS 列 -->

<input type="button" value="按钮" onclick="abc()" ><!--按钮-->
<input type="txt" readonly="readonly" value="这是只读表单">
<INPUT TYPE="radio" NAME=""><!-- 单选按钮  用name 绑定组-->   
<INPUT TYPE="checkbox" NAME="" checked><!-- 复选框 --><!-- checked 以选定 -->
密码<INPUT TYPE="password">
<INPUT TYPE="hidden"><!-- 隐藏字段 -->   
<INPUT TYPE="image" SRC="" alt="图片按钮"> <!-- 图象  -->   
<INPUT TYPE="reset"><!-- 重置按钮 -->
<INPUT TYPE="submit"><!-- 提交按钮 -->
</form>

//按钮
<button type="button" onclick="loadXMLDoc()">请求数据</button>

<canvas id="myCanvas"> 标签只是图形容器，您必须使用脚本来绘制图形。</canvas>
<script type="text/javascript">
var canvas=document.getElementById('myCanvas');
var ctx=canvas.getContext('2d');
ctx.fillStyle='#FF0000';
ctx.fillRect(0,0,80,10);
</script>


<br />  换行符

<font size="8" color="#FF0000" face="幼圆">字体设置</font>

<!-- 常用字体列表
宋体 黑体 楷体_GB2312 仿宋_GB2312

新宋体 幼圆 隶书 方正舒体

华文新魏 华文行楷 华文细黑 华文彩云
 -->


<!--  常用颜色列表
浅绿-aqua 黑-black 兰-blue 紫红-fuchsia
灰-gray 绿-green 亮绿-lime 茶-maroon
深兰-navy 橄榄-olive 紫-pourple 红-red
银-silver 青-teal 白-white 黄-yellow
紫红-purple
-->

<HR ALIGN=LEFT WIDTH=50%  SIZE="2"><!--划线-->   

A
<sup>上标</sup>   
A
<sub>下标</sub>   

<ins>插入字</ins>

<tt>打印机字体</tt>

<pre><!-- 保留文件格式 预定格式宽度 -->
保 留 文 件 格 式   
</pre>

<div style="width:50px; height:50px;background:#ff0000;">框架</div>
<span style="background:#ff0000;">行内单元</span>
<!-- ALIGN=LEFT|CENTER|RIGHT -->
<CENTER>居中对齐</CENTER>

<B> 加粗 </b>
<I> 斜体 </i>
<U> 底线 </u>
<S> 删除线 </s>


<em>em定义文字</em>

<!-- 简单的图像映射 -->

<img src="http://www.google.cn/intl/zh-CN/images/logo_cn.gif" border="5" title="图片说明" usemap="#planetmap" alt="Planets" />

<!-- 图片连接   
        BORDER="2" 图形边缘   
        usemap="url" 点选图   
        lowsrc="url" 底解析度图片   
-->
<map name="planetmap" id="planetmap">
<area shape="circle" coords="50,50,14" href ="http://www.google.cn" target ="_blank" alt="Venus" />
<!-- 圆形 左边 加半径 -->
<area shape="rect" alt="" coords="10,10,30,30" href="http://www.google.cn"><!-- 矩形 -->
<area shape=poly alt=""  coords=232,70,285,70,300,90,250,90,200,78 href="URL"><!-- 多边形 -->
</map>

<UL> <!-- 定义符号 type = disc|circle|square -->
    <LI type = circle>无序列举     
        <LI type = square>无序列举   
        <LI type = disc  >无序列举
</UL>   

<OL type = I><!-- type=a|A|I|i|1|L  -->
    <LI> 有续列举     
        <LI> 有续列举   
</OL>

<dl><!-- 定义列表 -->   
        <dt>项目
                <dd>定义
</dl>


<table border="1" width="100" summary="">   
<caption>表格标题</caption>
<!--   
border="" 边框线   
-->   
<TR> <!--表格列 ALIGN=LEFT|CENTER|RIGHT 列对齐方式-->   
    <Th colspan=3 noweap >标题</Th> <!--colspan=3 储存格式横向连接  noweap 不换行-->   
</tr>   
<tr>   
    <TD rowspan=2>1</TD><!--存储格 rowspan=2 储存格式竖向连接 -->   
    <TD>1</TD> <TD>1</TD>   
</TR>   
<TR>   
    <TD>1</TD> <TD>1</TD>   
</TR>   
</TABLE>

<audio src="/i/horse.ogg" controls="controls">html5声音 </audio> ie ?

<iframe src="http://www.google.cn/intl/zh-CN/images/logo_cn.gif" scrolling="No" frameborder="0" onload="" />
<!--
hspace:网页右上角的的横坐标；
vspace:网页右上角的纵坐标；
name：内嵌帧名称
width：内嵌帧宽度(可用像素值或百分比)
height：内嵌帧高度(可用像素值或百分比)
frameborder：内嵌帧边框
marginwidth：帧内文本的左右页边距
marginheight：帧内文本的上下页边距z
scrolling：是否出现滚动条(“auto”为自动，“yes”为显示，“no”为不显示)
src：内嵌入文件的地址
style：内嵌文档的样式(如设置文档背景等)
allowtransparency：是否允许透明   
 -->
<script type="text/javascript">
function iframeFitHeight(oIframe)
 {//Iframe窗口自适应高度 兼容IE6.0 FF2.0以上
     try
      {
        var oWin = oIframe.name ? window.frames[oIframe.name] : oIframe.contentWindow;
         oIframe.style.height = oWin.document.body.scrollHeight + "px";
      }
     catch(e){}
  }
</script>

</body>
</html>
