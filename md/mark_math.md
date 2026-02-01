# Markdown 数学公式

本文档介绍在Markdown中使用LaTeX语法编写数学公式的方法。

## 行内与独行

- **行内公式**：将公式插入到本行内，符号：`$公式内容$`
  - 示例：`$xyz$` → $xyz$
  
- **独行公式**：将公式插入到新的一行内，并且居中，符号：`$$公式内容$$`
  - 示例：`$$xyz$$` → $$xyz$$

## 上标、下标与组合

- **上标符号**：符号：`^`
  - 示例：`$ x^4$` → $x^4$
  
- **下标符号**：符号：`_`
  - 示例：`$ x_1$` → $x_1$
  
- **组合符号**：符号：`{}`
  - 示例：`$ {16}_{8}O{2+}_{2}$` → ${16}_{8}O{2+}_{2}$

## 汉字、字体与格式

- **汉字形式**：符号：`\mbox{}`
  - 示例：`$ V_{\mbox{xxx}}$` → $V_{\mbox{xxx}}$
  
- **字体控制**：符号：`\displaystyle`
  - 示例：`$\displaystyle \frac{x+y}{y+z}$` → $\displaystyle \frac{x+y}{y+z}$
  
- **下划线符号**：符号：`\underline`
  - 示例：`$\underline{x+y}$` → $\underline{x+y}$
  
- **标签**：符号：`\tag{数字}`
  - 示例：`$\tag{11}$` → $\tag{11}$
  
- **上大括号**：符号：`\overbrace{算式}`
  - 示例：`$\overbrace{a+b+c+d}^{2.0}$` → $\overbrace{a+b+c+d}^{2.0}$
  
- **下大括号**：符号：`\underbrace{算式}`
  - 示例：`$a+\underbrace{b+c}_{1.0}+d$` → $a+\underbrace{b+c}_{1.0}+d$
  
- **上位符号**：符号：`\stackrel{上位符号}{基位符号}`
  - 示例：`$\vec{x}\stackrel{\mathrm{def}}{=}{x_1,\dots,x_n}$` → $\vec{x}\stackrel{\mathrm{def}}{=}{x_1,\dots,x_n}$

## 占位符

- **两个quad空格**：符号：`\qquad`
  - 示例：`$x \qquad y$` → $x \qquad y$
  
- **quad空格**：符号：`\quad`
  - 示例：`$x \quad y$` → $x \quad y$
  
- **大空格**：符号：`\`
  - 示例：`$x \ y$` → $x \ y$
  
- **中空格**：符号：`\:`
  - 示例：`$x\: y$` → $x\: y$
  
- **小空格**：符号：`\,`
  - 示例：`$x\, y$` → $x\, y$
  
- **没有空格**：符号：``
  - 示例：`$xy$` → $xy$
  
- **紧贴**：符号：`\!`
  - 示例：`$x\! y$` → $x\! y$

## 定界符与组合

- **括号**：符号：`\big(\big) \Big(\Big) \bigg(\bigg) \Bigg(\Bigg)`
  - 示例：`$\big(\big) \Big(\Big) \bigg(\bigg) \Bigg(\Bigg)$` → $\big(\big) \Big(\Big) \bigg(\bigg) \Bigg(\Bigg)$
  
- **中括号**：符号：`[]`
  - 示例：`$[x+y]$` → $[x+y]$
  
- **大括号**：符号：`\{ \}`
  - 示例：`${x+y}$` → ${x+y}$
  
- **自适应括号**：符号：`\left \right`
  - 示例：`$\left(x\right)$` → $\left(x\right)$
  
- **组合公式**：符号：`{上位公式 \choose 下位公式}`
  - 示例：`${n+1 \choose k}={n \choose k}+{n \choose k-1}$` → ${n+1 \choose k}={n \choose k}+{n \choose k-1}$
  
- **组合公式**：符号：`{上位公式 \atop 下位公式}`
  - 示例：`$\sum_{k_0,k_1,\ldots>0 \atop k_0+k_1+\cdots=n}A_{k_0}A_{k_1}\cdots$` → $\sum_{k_0,k_1,\ldots>0 \atop k_0+k_1+\cdots=n}A_{k_0}A_{k_1}\cdots$

## 四则运算

- **加法运算**：符号：`+`
  - 示例：`$x+y=z$` → $x+y=z$
  
- **减法运算**：符号：`-`
  - 示例：`$x-y=z$` → $x-y=z$
  
- **加减运算**：符号：`\pm`
  - 示例：`$x \pm y=z$` → $x \pm y=z$
  
- **减加运算**：符号：`\mp`
  - 示例：`$x \mp y=z$` → $x \mp y=z$
  
- **乘法运算**：符号：`\times`
  - 示例：`$x \times y=z$` → $x \times y=z$
  
- **点乘运算**：符号：`\cdot`
  - 示例：`$x \cdot y=z$` → $x \cdot y=z$
  
- **星乘运算**：符号：`\ast`
  - 示例：`$x \ast y=z$` → $x \ast y=z$
  
- **除法运算**：符号：`\div`
  - 示例：`$x \div y=z$` → $x \div y=z$
  
- **斜法运算**：符号：`/`
  - 示例：`$x/y=z$` → $x/y=z$
  
- **分式表示**：符号：`\frac{分子}{分母}`
  - 示例：`$\frac{x+y}{y+z}$` → $\frac{x+y}{y+z}$
  
- **分式表示**：符号：`{分子} \over {分母}`
  - 示例：`${x+y} \over {y+z}$` → ${x+y} \over {y+z}$
  
- **绝对值表示**：符号：`||`
  - 示例：`$|x+y|$` → $|x+y|$

## 高级运算

- **平均数运算**：符号：`\overline{算式}`
  - 示例：`$\overline{xyz}$` → $\overline{xyz}$
  
- **开二次方运算**：符号：`\sqrt`
  - 示例：`$\sqrt x$` → $\sqrt x$
  
- **开方运算**：符号：`\sqrt[开方数]{被开方数}`
  - 示例：`$\sqrt[3]{x+y}$` → $\sqrt[3]{x+y}$
  
- **对数运算**：符号：`\log`
  - 示例：`$\log(x)$` → $\log(x)$
  
- **极限运算**：符号：`\lim`
  - 示例：`$\lim^{x \to \infty}_{y \to 0}{\frac{x}{y}}$` → $\lim^{x \to \infty}_{y \to 0}{\frac{x}{y}}$
  
- **极限运算**：符号：`\displaystyle \lim`
  - 示例：`$\displaystyle \lim^{x \to \infty}_{y \to 0}{\frac{x}{y}}$` → $\displaystyle \lim^{x \to \infty}_{y \to 0}{\frac{x}{y}}$
  
- **求和运算**：符号：`\sum`
  - 示例：`$\sum^{x \to \infty}_{y \to 0}{\frac{x}{y}}$` → $\sum^{x \to \infty}_{y \to 0}{\frac{x}{y}}$
  
- **求和运算**：符号：`\displaystyle \sum`
  - 示例：`$\displaystyle \sum^{x \to \infty}_{y \to 0}{\frac{x}{y}}$` → $\displaystyle \sum^{x \to \infty}_{y \to 0}{\frac{x}{y}}$
  
- **积分运算**：符号：`\int`
  - 示例：`$\int^{\infty}_{0}{xdx}$` → $\int^{\infty}_{0}{xdx}$
  
- **积分运算**：符号：`\displaystyle \int`
  - 示例：`$\displaystyle \int^{\infty}_{0}{xdx}$` → $\displaystyle \int^{\infty}_{0}{xdx}$
  
- **微分运算**：符号：`\partial`
  - 示例：`$\frac{\partial x}{\partial y}$` → $\frac{\partial x}{\partial y}$
  
- **矩阵表示**：符号：`\begin{matrix} \end{matrix}`
  - 示例：`$\left[ \begin{matrix} 1 &2 &\cdots &4\\5 &6 &\cdots &8\\\vdots &\vdots &\ddots &\vdots\\13 &14 &\cdots &16\end{matrix} \right]$` → $\left[ \begin{matrix} 1 &2 &\cdots &4\\5 &6 &\cdots &8\\\vdots &\vdots &\ddots &\vdots\\13 &14 &\cdots &16\end{matrix} \right]$

## 逻辑运算

- **等于运算**：符号：`=`
  - 示例：`$x+y=z$` → $x+y=z$
  
- **大于运算**：符号：`>`
  - 示例：`$x+y>z$` → $x+y>z$
  
- **小于运算**：符号：`<`
  - 示例：`$x+y<z$` → $x+y<z$
  
- **大于等于运算**：符号：`\geq`
  - 示例：`$x+y \geq z$` → $x+y \geq z$
  
- **小于等于运算**：符号：`\leq`
  - 示例：`$x+y \leq z$` → $x+y \leq z$
  
- **不等于运算**：符号：`\neq`
  - 示例：`$x+y \neq z$` → $x+y \neq z$
  
- **不大于等于运算**：符号：`\ngeq` 或 `\not\geq`
  - 示例：`$x+y \ngeq z$` → $x+y \ngeq z$
  
- **不小于等于运算**：符号：`\nleq` 或 `\not\leq`
  - 示例：`$x+y \nleq z$` → $x+y \nleq z$
  
- **约等于运算**：符号：`\approx`
  - 示例：`$x+y \approx z$` → $x+y \approx z$
  
- **恒定等于运算**：符号：`\equiv`
  - 示例：`$x+y \equiv z$` → $x+y \equiv z$

## 集合运算

- **属于运算**：符号：`\in`
  - 示例：`$x \in y$` → $x \in y$
  
- **不属于运算**：符号：`\notin` 或 `\not\in`
  - 示例：`$x \notin y$` → $x \notin y$
  
- **子集运算**：符号：`\subset` 或 `\supset`
  - 示例：`$x \subset y$` → $x \subset y$
  
- **真子集运算**：符号：`\subseteq` 或 `\supseteq`
  - 示例：`$x \subseteq y$` → $x \subseteq y$
  
- **非真子集运算**：符号：`\subsetneq` 或 `\supsetneq`
  - 示例：`$x \subsetneq y$` → $x \subsetneq y$
  
- **非子集运算**：符号：`\not\subset` 或 `\not\supset`
  - 示例：`$x \not\subset y$` → $x \not\subset y$
  
- **并集运算**：符号：`\cup`
  - 示例：`$x \cup y$` → $x \cup y$
  
- **交集运算**：符号：`\cap`
  - 示例：`$x \cap y$` → $x \cap y$
  
- **差集运算**：符号：`\setminus`
  - 示例：`$x \setminus y$` → $x \setminus y$
  
- **同或运算**：符号：`\bigodot`
  - 示例：`$x \bigodot y$` → $x \bigodot y$
  
- **同与运算**：符号：`\bigotimes`
  - 示例：`$x \bigotimes y$` → $x \bigotimes y$
  
- **实数集合**：符号：`\mathbb{R}`
  - 示例：`\mathbb{R}` → $\mathbb{R}$
  
- **自然数集合**：符号：`\mathbb{Z}`
  - 示例：`\mathbb{Z}` → $\mathbb{Z}$
  
- **空集**：符号：`\emptyset`
  - 示例：`$\emptyset$` → $\emptyset$

## 数学符号

### 特殊符号

- **无穷**：符号：`\infty`
  - 示例：`$\infty$` → $\infty$
  
- **虚数**：符号：`\imath` 或 `\jmath`
  - 示例：`$\imath$` → $\imath$，`$\jmath$` → $\jmath$

### 修饰符

- **数学符号**：符号：`\hat{a}`
  - 示例：`$\hat{a}$` → $\hat{a}$
  
- **数学符号**：符号：`\check{a}`
  - 示例：`$\check{a}$` → $\check{a}$
  
- **数学符号**：符号：`\breve{a}`
  - 示例：`$\breve{a}$` → $\breve{a}$
  
- **数学符号**：符号：`\tilde{a}`
  - 示例：`$\tilde{a}$` → $\tilde{a}$
  
- **数学符号**：符号：`\bar{a}`
  - 示例：`$\bar{a}$` → $\bar{a}$
  
- **矢量符号**：符号：`\vec{a}`
  - 示例：`$\vec{a}$` → $\vec{a}$
  
- **数学符号**：符号：`\acute{a}`
  - 示例：`$\acute{a}$` → $\acute{a}$
  
- **数学符号**：符号：`\grave{a}`
  - 示例：`$\grave{a}$` → $\grave{a}$
  
- **数学符号**：符号：`\mathring{a}`
  - 示例：`$\mathring{a}$` → $\mathring{a}$
  
- **一阶导数符号**：符号：`\dot{a}`
  - 示例：`$\dot{a}$` → $\dot{a}$
  
- **二阶导数符号**：符号：`\ddot{a}`
  - 示例：`$\ddot{a}$` → $\ddot{a}$

### 箭头符号

- **上箭头**：符号：`\uparrow` 或 `\Uparrow`
  - 示例：`$\uparrow$` → $\uparrow$，`$\Uparrow$` → $\Uparrow$
  
- **下箭头**：符号：`\downarrow` 或 `\Downarrow`
  - 示例：`$\downarrow$` → $\downarrow$，`$\Downarrow$` → $\Downarrow$
  
- **左箭头**：符号：`\leftarrow` 或 `\Leftarrow`
  - 示例：`$\leftarrow$` → $\leftarrow$，`$\Leftarrow$` → $\Leftarrow$
  
- **右箭头**：符号：`\rightarrow` 或 `\Rightarrow`
  - 示例：`$\rightarrow$` → $\rightarrow$，`$\Rightarrow$` → $\Rightarrow$

### 省略号

- **底端对齐的省略号**：符号：`\ldots`
  - 示例：`$1,2,\ldots,n$` → $1,2,\ldots,n$
  
- **中线对齐的省略号**：符号：`\cdots`
  - 示例：`$x_1^2 + x_2^2 + \cdots + x_n^2$` → $x_1^2 + x_2^2 + \cdots + x_n^2$
  
- **竖直对齐的省略号**：符号：`\vdots`
  - 示例：`$\vdots$` → $\vdots$
  
- **斜对齐的省略号**：符号：`\ddots`
  - 示例：`$\ddots$` → $\ddots$

## 希腊字母表

| 大写 | 实现 | 小写 | 实现 |
|------|------|------|------|
| A | A | α | \alpha |
| B | B | β | \beta |
| Γ | \Gamma | γ | \gamma |
| Δ | \Delta | δ | \delta |
| E | E | ε | \epsilon |
| Z | Z | ζ | \zeta |
| H | H | η | \eta |
| Θ | \Theta | θ | \theta |
| I | I | ι | \iota |
| K | K | κ | \kappa |
| Λ | \Lambda | λ | \lambda |
| M | M | μ | \mu |
| N | N | ν | \nu |
| Ξ | \Xi | ξ | \xi |
| O | O | ο | \omicron |
| Π | \Pi | π | \pi |
| P | P | ρ | \rho |
| Σ | \Sigma | σ | \sigma |
| T | T | τ | \tau |
| Υ | \Upsilon | υ | \upsilon |
| Φ | \Phi | φ | \phi |
| X | X | χ | \chi |
| Ψ | \Psi | ψ | \psi |
| Ω | \Omega | ω | \omega |
