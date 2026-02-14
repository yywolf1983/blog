# 重要数学公式汇总

## 1. 基础数学公式

### 1.1 代数公式

#### 二次方程求根公式
$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

#### 平方差公式
$$
a^2 - b^2 = (a - b)(a + b)
$$

#### 完全平方公式
$$
(a \pm b)^2 = a^2 \pm 2ab + b^2
$$

#### 立方和公式
$$
a^3 + b^3 = (a + b)(a^2 - ab + b^2)
$$

#### 立方差公式
$$
a^3 - b^3 = (a - b)(a^2 + ab + b^2)
$$

### 1.2 不等式

#### 均值不等式
$$
\frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n}
$$

#### 柯西不等式
$$
\left(\sum_{i=1}^{n} a_i^2\right) \left(\sum_{i=1}^{n} b_i^2\right) \geq \left(\sum_{i=1}^{n} a_i b_i\right)^2
$$

#### 三角不等式
$$
|a + b| \leq |a| + |b|
$$

## 2. 微积分公式

### 2.1 导数公式

#### 基本导数
$$
\frac{d}{dx} x^n = nx^{n-1}
$$

$$
\frac{d}{dx} \sin x = \cos x
$$

$$
\frac{d}{dx} \cos x = -\sin x
$$

$$
\frac{d}{dx} e^x = e^x
$$

$$
\frac{d}{dx} \ln x = \frac{1}{x}
$$

#### 乘积法则
$$
\frac{d}{dx} [f(x)g(x)] = f'(x)g(x) + f(x)g'(x)
$$

#### 商法则
$$
\frac{d}{dx} \left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}
$$

#### 链式法则
$$
\frac{d}{dx} f(g(x)) = f'(g(x))g'(x)
$$

### 2.2 积分公式

#### 基本积分
$$
\int x^n dx = \frac{x^{n+1}}{n+1} + C, \quad n \neq -1
$$

$$
\int \sin x dx = -\cos x + C
$$

$$
\int \cos x dx = \sin x + C
$$

$$
\int e^x dx = e^x + C
$$

$$
\int \frac{1}{x} dx = \ln|x| + C
$$

#### 定积分
$$
\int_{a}^{b} f(x) dx = F(b) - F(a), \quad \text{其中} F'(x) = f(x)
$$

#### 分部积分法
$$
\int u dv = uv - \int v du
$$

#### 换元积分法
$$
\int f(g(x))g'(x) dx = \int f(u) du, \quad u = g(x)
$$

### 2.3 极限公式

#### 重要极限
$$
\lim_{x \to 0} \frac{\sin x}{x} = 1
$$

$$
\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e
$$

#### 洛必达法则
$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}, \quad \text{当} \lim_{x \to a} f(x) = \lim_{x \to a} g(x) = 0 \text{或} \infty
$$

## 3. 线性代数公式

### 3.1 矩阵运算


#### 矩阵乘法
$$ (AB) {ij} = \sum {k=1}^{n} A_{ik}B_{kj} $$

#### 矩阵转置
$$ (A^T) {ij} = A {ji} $$

#### 矩阵求逆（2x2矩阵）
$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
$$

### 3.2 行列式

#### 2x2行列式
$$
\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc
$$

#### 3x3行列式
$$
\begin{vmatrix} a & b & c \\ d & e & f \\ g & h & i \end{vmatrix} = a(ei - fh) - b(di - fg) + c(dh - eg)
$$

### 3.3 特征值和特征向量

#### 特征方程
$$
\det(A - \lambda I) = 0
$$

#### 特征向量定义
$$
A\mathbf{v} = \lambda\mathbf{v}
$$

## 4. 概率统计公式

### 4.1 概率公式

#### 条件概率
$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

#### 全概率公式
$$
P(A) = \sum_{i=1}^{n} P(A|B_i)P(B_i)
$$

#### 贝叶斯公式
$$
P(B_i|A) = \frac{P(A|B_i)P(B_i)}{\sum_{j=1}^{n} P(A|B_j)P(B_j)}
$$

### 4.2 统计公式

#### 期望
$$
E[X] = \sum_{i} x_i P(X = x_i) \quad \text{（离散型）}
$$

$$
E[X] = \int_{-\infty}^{\infty} x f(x) dx \quad \text{（连续型）}
$$

#### 方差
$$
Var(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2
$$

#### 标准差
$$
\sigma(X) = \sqrt{Var(X)}
$$

### 4.3 常见分布

#### 正态分布概率密度函数
$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

#### 二项分布概率质量函数
$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

#### 泊松分布概率质量函数
$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$

## 5. 物理公式

### 5.1 经典力学

#### 牛顿第二定律
$$
F = ma
$$

#### 动能公式
$$
E_k = \frac{1}{2}mv^2
$$

#### 势能公式（重力）
$$
E_p = mgh
$$

#### 功的定义
$$
W = F \cdot d = Fd\cos\theta
$$

### 5.2 电磁学

#### 库仑定律
$$
F = k \frac{q_1 q_2}{r^2}
$$

#### 欧姆定律
$$
I = \frac{V}{R}
$$

#### 电磁感应定律
$$
\mathcal{E} = -N \frac{d\Phi}{dt}
$$

### 5.3 相对论

#### 质能方程
$$
E = mc^2
$$

#### 相对论质量
$$
m = \frac{m_0}{\sqrt{1 - \frac{v^2}{c^2}}}
$$

## 6. 其他重要公式

### 6.1 几何公式

#### 圆的面积
$$
A = \pi r^2
$$

#### 球的体积
$$
V = \frac{4}{3}\pi r^3
$$

#### 三角形面积（海伦公式）
$$
A = \sqrt{s(s-a)(s-b)(s-c)}, \quad s = \frac{a+b+c}{2}
$$

### 6.2 级数公式

#### 等差数列求和
$$
\sum_{i=1}^{n} (a + (i-1)d) = \frac{n}{2}[2a + (n-1)d]
$$

#### 等比数列求和
$$
\sum_{i=0}^{n-1} ar^i = a \frac{1 - r^n}{1 - r}, \quad r \neq 1
$$

#### 无穷等比数列求和
$$
\sum_{i=0}^{\infty} ar^i = \frac{a}{1 - r}, \quad |r| < 1
$$

#### 自然数平方和
$$
\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}
$$

#### 自然数立方和
$$
\sum_{i=1}^{n} i^3 = \left(\frac{n(n+1)}{2}\right)^2
$$

### 6.3 特殊函数

#### 阶乘
$$
n! = n \times (n-1) \times \cdots \times 2 \times 1
$$

#### 组合数
$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

#### 排列数
$$
P(n, k) = \frac{n!}{(n-k)!}
$$

#### 伽马函数
$$
\Gamma(n) = (n-1)! = \int_{0}^{\infty} x^{n-1} e^{-x} dx
$$

## 7. 高级数学公式

### 7.1 复变函数

#### 欧拉公式
$$
e^{i\theta} = \cos\theta + i\sin\theta
$$

#### 棣莫弗公式
$$
(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)
$$

### 7.2 偏微分方程

#### 拉普拉斯方程
$$
\nabla^2 u = 0
$$

#### 热传导方程
$$
\frac{\partial u}{\partial t} = \alpha \nabla^2 u
$$

#### 波动方程
$$
\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u
$$

### 7.3 数值分析

#### 泰勒展开
$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n
$$

#### 牛顿迭代法
$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

## 8. 数学符号表

### 8.1 基本符号

| 符号 | 名称 | 含义 |
|------|------|------|
| $+$ | 加号 | 加法运算 |
| $-$ | 减号 | 减法运算 |
| $\times$ | 乘号 | 乘法运算 |
| $\div$ | 除号 | 除法运算 |
| $=$ | 等号 | 等于关系 |
| $\neq$ | 不等号 | 不等于关系 |
| $<$ | 小于号 | 小于关系 |
| $>$ | 大于号 | 大于关系 |
| $\leq$ | 小于等于号 | 小于等于关系 |
| $\geq$ | 大于等于号 | 大于等于关系 |

### 8.2 微积分符号

| 符号 | 名称 | 含义 |
|------|------|------|
| $\frac{d}{dx}$ | 导数 | 对x求导 |
| $\int$ | 积分 | 积分运算 |
| $\lim$ | 极限 | 极限运算 |
| $\infty$ | 无穷大 | 无限大的量 |
| $\partial$ | 偏导数 | 偏导数符号 |
| $\nabla$ | 梯度 | 梯度算子 |

### 8.3 集合符号

| 符号 | 名称 | 含义 |
|------|------|------|
| $\in$ | 属于 | 元素属于集合 |
| $\notin$ | 不属于 | 元素不属于集合 |
| $\subset$ | 子集 | 集合包含于另一集合 |
| $\supset$ | 超集 | 集合包含另一集合 |
| $\cap$ | 交集 | 两个集合的公共元素 |
| $\cup$ | 并集 | 两个集合的所有元素 |
| $\emptyset$ | 空集 | 不含任何元素的集合 |
| $\mathbb{R}$ | 实数集 | 所有实数的集合 |
| $\mathbb{Z}$ | 整数集 | 所有整数的集合 |
| $\mathbb{N}$ | 自然数集 | 所有自然数的集合 |

## 9. 公式使用说明

### 9.1 行内公式
使用单个美元符号包围公式，如：$E = mc^2$

### 9.2 块级公式
使用两个美元符号包围公式，如：
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

### 9.3 公式编号
可以在公式后添加 `\tag{编号}` 来为公式编号，如：
$$
a^2 + b^2 = c^2 \tag{1}
$$

### 9.4 多行公式
使用 `\begin{align}` 和 `\end{align}` 环境来创建多行公式，如：
$$
\begin{align}
(a + b)^2 &= a^2 + 2ab + b^2 \\
(a - b)^2 &= a^2 - 2ab + b^2
\end{align}
$$

## 10. 参考资料

1. 《高等数学》（同济大学版）
2. 《线性代数》（同济大学版）
3. 《概率论与数理统计》（浙江大学版）
4. 《数学分析》（华东师范大学版）
5. 《复变函数论》（钟玉泉版）

---

**注**：本文件包含了数学各个分支的重要公式，可作为参考手册使用。所有公式均使用 LaTeX 语法编写，可在支持 MathJax 或 KaTeX 的 Markdown 编辑器中正确渲染。