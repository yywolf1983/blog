
## 锚点连接

[锚点](#jump)<!--这些是注释文本，不会显示-->

[Google] : http://google.com/  

<http://www.163.com/>   直接链接

上标 <sup>[1]</sup> 下标<sub>2</sub>

30&deg;

img<img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" style="zoom:50%" />

![鹤隐](images/鹤隐.jpg "鹤隐")

## 标题

``` txt
# 这是 H1

## 这是 H2
### 这是 H3
#### 这是 H4
##### 这是 H5
###### 这是 H6
```

## 划线

*******

```
-------------
******
```

换行是行尾两个空格  
换行是行尾两个空格  

_single underscores_  斜体  
__double underscores__  粗体  
***加粗加斜***  

## 引用

Use the `printf()` function.

`` There is a literal backtick (`) here. ``

Use the `printf()` function.

> ## 段内标题。
> 这是一个段落
>>> 这是一个段落这是一个段落这是一个段落  
asd
>>>>> 新的段落

-   Green
+   Blue
*   Red


1.  Bird
2.  McHale
3.  Parish


- [x] list
- [ ] list


## 表格
aaaa | aaaa
- | -
aaaaa | aaaa

## 代码段


* 这是一个段落这是一个段落这是一个段落这是一个段落  
这是一个段落这是一个段落这是一个段落这是一个段落

``` python
import os
print os.path
def abc():
    pass
```

    import os
    print os.path
    def abc():
        pass

    四个空格也形成代码段


<span id = "jump">锚点位置</span> 

## 以下为特有
#### 流程图
```
graph TD
    A[网易特有格式]-->B(aaaa)
    B--> D{ }
    B--> |文字| C(圆角)
    D--> |注视| A
    D--> C
```

#### 序列图
```
sequenceDiagram
    loop day 嵌套
        A-> B:  不带尖头
        B-->> A: 带尖头虚线
        A->>B: 实线
        A--> B: 虚线
        B->> B: 
    end
```

#### 甘特图

```
gantt
    dateFormat YY-MM-DD
    title 计划表
    section aaa
    aaa: 18-10-10,10d 
    aaa: 18-11-10,5d
    section bbb
    bbb: 18-10-10,30d 
    section ccc
    bbb: 18-11-2,30d
    xxx: 18-11-10,10d
```

#### 数学公式

Inline math: 
`$\tfrac{1}{N}=s_n^\kappa$`

```math
E = mc^2

\left[<\right]

\tfrac{1}{2}

1\,2


\left[\left(\tfrac{2\times2-(a-x)}{a^2-X}\right)\right]

1. \sum^\infty_{m-1} 

2. \oint

3. \phi_i 

4. \pi^2 

5. \kappa_1

6. \int_1

7. \partial

8. \infty

sin(a)

\sqrt{a}

```

mathjax 使用的这个引擎
mermaid 甘特图插件


