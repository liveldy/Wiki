---
title: 组合逻辑电路
subtitle: 逻辑门电路、组合逻辑电路及应用
description: 组合逻辑电路
---

# 组合逻辑电路

## 逻辑门电路

在数字电路中所谓的**门**，是指一种开关作用，在一定的输入条件下，它允许信号通过；当条件不满足时，信号就不能通过。用高、低电平来表示二值逻辑的1和0两种逻辑状态。若用高电平表示逻辑1，低电平表示逻辑0，则称为**正逻辑**，反之称为**负逻辑**。若非特殊说明，一般使用正逻辑。

### 分立元件门电路

由电阻、二极管、三极管等分立元件门构成的逻辑门称为分立元件门。

|分立元件门|电路图|
|-|-|
|二极管与门|![二极管与门](../../images/and-flyjm.png)|
|二极管或门|![二极管或门](../../images/or-flyjm.png)|
|晶体三极管非门|![晶体三极管非门](../../images/not-flyjm.png)|

### TTL集成门电路

**集成电路（IC）**将数字电路中的元器件和连线制作在同一硅片上，因而较之分立元件具有高可靠性和微型化的优点。输入端和输出端均为三极管结构，称为三极管-三极管逻辑电路，简称**TTL电路**。TTL电路时目前双极型数字集成电路中用的最多的一种。

|TTL集成门电路|电路图|典型芯片名称|典型芯片管脚图|用途|
|-|-|-|-|-|
|非门（反相器）|![非门（反相器）](../../images/not-ic.png)|74LS04/CT4004|![74LS04](../../images/74ls04.png)||
|与非门|![与非门](../../images/nand-ic.png)|74LS00/CT4000|![74LS00](../../images/74ls00.png)||
|或非门|![或非门](../../images/nor-ic.png)|74LS02/CT4002|![74LS02](../../images/74ls02.png)||
|与或非门|![与或非门](../../images/aon-ic.png)|74LS51/CT405|![74LS51](../../images/74ls51.png)||
|异或门|![异或门](../../images/xor-ic.png)|74LS86/CT4086|![74LS86](../../images/74ls86.png)||
|OC门（集电极开路门）|![OC门](../../images/oc.png)|74LS03/CT4003|![74LS03](../../images/74ls03.png)|驱动不同负载<br>实现电平转换<br>实现“线与”|
|TS门（三态输出门）|![TS门](../../images/ts.png)|||接成总线结构<br>实现数据双向传输|

### CMOS集成门电路

两种不同类型的MOS管形成的电路结构，称为互补对称MOS，简称CMOS。**CMOS集成门电路**由CMOS构成。

|CMOS集成门电路|电路图|典型芯片名称|典型芯片管脚图|
|-|-|-|-|
|OD门（漏极开路门）|![OD门](../../images/cc40107.png)|CC40107||
|TG门（传输门）|![TG门](../../images/tg.png)|CC4016|![CC4016](../../images/cc4016.png)|

## 组合逻辑电路及分析与设计

**组合逻辑电路**有若干个输入$a_0,a_1,...,a_{i-1}$和若干个输出$y_0,y_1,...,y_{j-1}$，输入和输出之间的逻辑关系可以用一组逻辑函数表示：

$$
\begin{cases}
y_0=f_0(a_0,a_1,...,a_{i-1}) \\
y_1=f_1(a_0,a_1,...,a_{i-1}) \\
... \\
y_{j-1}=f_{j-1}(a_0,a_1,...,a_{i-1})
\end{cases}
$$

``` mermaid
---
title: 组合逻辑电路的分析过程
---
flowchart LR
  已知逻辑电路 --> 写出逻辑表达式 --> 适当地化简与变换 --> 列出真值表或功能表 --> 分析其逻辑功能
```


``` mermaid
---
title: 组合逻辑电路的设计过程
---
flowchart LR
  给定问题 --> 逻辑抽象 --> 列出真值表或功能表 --> 写逻辑函数式 --> 函数式化简或变换 -->画逻辑图
```

## 常用中规模组合逻辑电路

|组合逻辑电路|电路图|逻辑函数表达式|典型芯片名称|典型芯片管脚图|功能表（真值表）|功能说明|
|-|-|-|-|-|-|-|
|4位奇偶校验器|![4位奇偶校验器](../../images/4-odd.png)|$F=A\oplus B\oplus C\oplus D$|||![4位奇偶校验器](../../images/4-odd-list.png)|检测输入数据中包含1的个数是偶数还是奇数|
|4选1数据选择器|![4选1数据选择器](../../images/4-1-select.png)||74LS153|![74LS153](../../images/74ls153.png)|![](../../images/4-1-select-list.png)|从4个输入数据中选择1个输出数据|
|8选1数据选择器|||74LS151|![74LS151](../../images/74ls151.png)|![74LS151](../../images/74ls151-list.png)|从8个输入数据中选择1个输出数据|
|8线-3线编码器|![8线-3线编码器](../../images/8-3-encode.png)|$\begin{cases}Y_2=I_4+I_5+I_6+I_7\\Y_1=I_2+I_3+I_6+I_7\\Y_0=I_1+I_3+I_5+I_7 \end{cases}$||||将二进制数码进行编码，只允许一个输入有效|
|8线-3线优先编码器|![8线-3线优先编码器](../../images/8-3-encode-n.png)||74LS148|![74LS148](../../images/74ls148.png)|![74LS148](../../images/74ls148-list.png)|将二进制数码进行编码，允许多个输入有效，优先给优先级高的输入进行编码|
|8位二-十进制优先编码器|![8位二-十进制优先编码器](../../images/2-10-encode.png)||74LS147|![74LS147](../../images/74ls147.png)|![74LS147](../../images/74ls147-list.png)|将二进制数码进行编码为十进制BCD码，允许多个输入有效，优先给优先级高的输入进行编码|
|3线-8线译码器|![3线-8线译码器](../../images/3-8-decode.png)||74LS138|![74LS138](../../images/74ls138.png)|![74LS138](../../images/74ls138-list.png)|将二进制代码进行译码|
|8位二-十进制译码器|![8位二-十进制译码器](../../images/2-10-decode.png)||74LS42|![74LS42](../../images/74ls42.png)|![74LS42](../../images/74ls42-list.png)|将十进制BCD码译码为二进制数码|
|BCD-七段显示译码器|![BCD-七段显示译码器](../../images/bcd-7-led.png)||74LS48|![74LS48](../../images/74ls48.png)|![74LS48](../../images/74ls48-list.png)|将二进制代码进行译码为显示器字形|
|1位半加器|![1位半加器](../../images/1-add.png)|$\begin{cases}S=A\oplus B\\CO=AB\end{cases}$|||![1位半加器](../../images/1-add-list.png)|不考虑有来自低位的进位将两个二进制数相加|
|1位全加器|![1位全加器](../../images/1-adda.png)|$\begin{cases}S=A\oplus B\oplus CI\\CO=\overline{\overline{AB}\cdot \overline{(A+B)CI}} \end{cases}$|||![1位全加器](../../images/1-adda-list.png)|将两个多位二进制数相加时，除了最低位以外，每一位都考虑来自低位的进位|
|4位串行进位加法器|![4位串行进位加法器](../../images/4-add.png)|||||将多个全加器串接|
|4位超前进位加法器|![4位超前进位加法器](../../images/4-adda.png)|$\begin{cases}S_i=A_i\oplus B_i\oplus (CI)_i\\(CO)_i=A_iB_i+(A_i\oplus B_i)(CI)_i \end{cases}$|74LS283|![74LS283](../../images/74ls283.png)|![74LS283](../../images/74ls283-list.png)|各级进位信号同时送到各位全加器的进位输入端|
|1位数值比较器|![1位数值比较器](../../images/1-compare.png)|$\begin{cases}Y_{(A>B)}=A\overline{B}\\Y_{(A<B)}=\overline{A}B\\Y_{(A=B)}=\overline{\overline{A}B+A\overline{B}} \end{cases}$||||对1位数进行比较|
|4位数值比较器|![4位数值比较器](../../images/4-compare.png)||CC14585|![CC14585](../../images/cc14585.png)||对4位数进行比较|

## 组合逻辑电路中的竞争-冒险现象