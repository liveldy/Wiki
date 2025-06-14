---
title: 算法分析与思想
subtitle: 算法性质与表示、渐进复杂度、均摊分析
description: 算法分析与思想
---

# 算法分析与思想

## 算法及其表示

### 算法及其性质

**算法**是对特定问题求解步骤的一种描述，是指令的有限序列。通常一个问题可以有多种算法，而一个算法可以求解某个特定的问题。算法满足下面5个性质：

1. 输入：一个算法有零个或多个输入（即算法可以没有输入），这些输入通常取自于某个特定的对象集合。
2. 输出：一个算法有一个或多个输出（即算法必须有输出），通常输入和输出之间有某种特定的关系。
3. 有穷性（有限性）：一个算法必须在执行有穷步之后结束，且每一步都在有穷时间内完成。
4. 确定性：算法中的每一条指令必须有确切的含义，不存在二义性。并且，在任何条件下，对于相同的输入只能得到相同的输出。
5. 可行性（有效性）：算法描述的操作可以通过已经实现的基本操作执行有限次来实现。

一个符合规范的算法除了以上5个性质外，还需要具备以下特性：

1. 正确性：算法能满足具体问题的需求，对于任何合法的输入，算法都会得出正确的结果。
2. 健壮性（鲁棒性）：算法对于非法输入应能识别并做出处理，而不是产生错误行为或者陷入瘫痪。
3. 简单性：算法容易理解和实现，不能追求复杂和冗余。
4. 抽象分级：算法应该进行模块化和进行抽象分级，即使是大体量的算法，也能方便地阅读、理解、使用和修改。
5. 高效性：算法应该尽可能地使用更少的空间和更短的时间，是衡量算法优劣的重要标准。

### 算法的表示

**程序**是对一个算法使用某种程序设计语言的具体实现，原则上算法可以用任何一种程序设计语言实现。但并非所有的计算机程序都是算法，相反，可能一个计算机程序没有任何算法，也可能由很多算法组成。

常用的描述算法的方法有自然语言、流程图、程序设计语言和伪代码等。下面以 欧几里得 算法（辗转相除法）为例进行介绍。

+ 自然语言

自然语言描述算法，容易理解但是也容易出现二义性，并且描述通常会很冗长。欧几里得算法用自然语言描述如下：

步骤1：将m除以n得到余数r；

步骤2：若r等于0，则n为最大公约数，算法结束；否则执行步骤3；

步骤3：将n的值放在m中，将r的值放在n中，重新执行步骤1。

+ 流程图

流程图描述算法，直观易懂但是严密性不如抽象设计语言，灵活性不如自然语言。欧几里得算法用流程图描述如图。

+ 伪代码

**伪代码**是介于自然语言和程序设计语言之间的方法，伪代码不是实际的编程语言，但在表达能力上类似于编程语言，同时又极小化了描述算法所不需要的技术细节。欧几里得算法用伪代码描述如下：

``` title=""
r=m%n
while r!=0
m=n
n=r
r=m%n
return n
```

算法体现的是一种计算思想，“数据结构与算法”部分不会拘泥于语法，除“完整示例”外，我们一律采用伪代码表示。这类伪代码接近C++但同时去掉了一些不必要的部分。

+ 程序设计语言

程序设计语言描述的算法能够直接被计算机执行，但抽象性差。欧几里得算法用C++描述如下：

```cpp title="欧几里得算法"
int CommonFactor(int m, int n)
{
	int r = m % n;
	while (r != 0)
	{
		m = n;
		n = r;
		r = m % n;
	}
	return n;
} 
```

## 渐进复杂度[^1]

### 算法的效率

[^1]:该节的部分内容（渐进复杂度的性质、主定理及其证明等）选取自[OI Wiki](https://oi-wiki.org/basic/complexity/)

一个算法所消耗的资源在以下4个方面：

1. 时间：算法的执行需要消耗时间。
2. 空间：算法在执行时，往往会进行空间的分配和使用，在计算机上主要体现为内存的占用。
3. 数据传输量：算法会涉及数据传输或者网络消耗。
4. 耗电量：算法最终都是在电子设备上运行的，因此也会有电量的消耗。

对于某些算法，即使输入规模相同，如果输入数据不同，则其时间开销也不同。例如（从n个元素中）顺序查找算法，从第一个元素开始，依次比较每一个元素，直至查找到待查找元素为止。如果待查找元素恰好在第一个，则算法只需要比较第一个元素就行了，这是**最好情况**；如果待查找元素在最后一个，则算法必须比较n－1个元素，这是**最坏情况**；假设数据等概率分布，则平均要比较n/2个元素，这是**平均情况**。

度量一个算法的效率，可以通过事前分析和事后测试（事后统计）的方法，事后测试是指将算法实现编写成程序，如何输入适当的数据运行，测算其时间和空间开销。同一个算法在不同的计算机上运行的速度会有一定的差别，并且实际运行速度难以在理论上进行计算，实际去测量又比较麻烦，所以我们通常考虑的不是算法运行的实际用时，而是算法运行所需要进行的基本操作的数量，而事前分析的方法即为渐进复杂度。

### 渐进复杂度及其性质

渐进复杂度是指在算法分析中用来描述算法运行时间或空间需求如何随着输入规模增加而增加的一种数学模型。**输入规模（数据规模）**是指输入量的多少，通常用n表示，一般可以从描述的问题中得到，且输入规模越大算法就需要越长的运行时间。**基本语句**是指执行次数与整个算法的执行次数成正比的语句，基本语句对算法运行时间的贡献最大，是算法中重要的操作。

算法的**时间复杂度**是其运行所需的计算时间，算法的**空间复杂度**是其运行所需的存储空间。算法中基本语句的执行次数在渐进意义下的阶，称为算法的**渐进复杂度**。**渐进符号**是函数的阶的规范描述。简单来说，渐进符号忽略了一个函数中增长较慢的部分以及各项的系数，而保留了可以用来表明该函数增长趋势的重要部分。

大$Ο$符号（**渐进上界**）：对于函数$f(n)$和$g(n)$,$f(n)=Ο(g(n))$,当且仅当$\exists c,n_0>0$,使得$\forall n \geq n_0$,$0 \leq f(n) \leq c \cdot g(n)$.

大$\Omega$符号（**渐进下界**）：对于函数$f(n)$和$g(n)$,$f(n)=\Omega(g(n))$,当且仅当$\exists c,n_0>0$,使得$\forall n \geq n_0$,$0 \leq c \cdot g(n) \leq f(n)$.

大$\Theta$符号（**渐进界**）：对于函数$f(n)$和$g(n)$,$f(n)=\Theta(g(n))$,当且仅当$\exists c_1,c_2,n_0>0$,使得$\forall n \geq n_0$,$0 \leq c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$.

小$o$符号：对于函数$f(n)$和$g(n)$,$f(n)=o(g(n))$,当且仅当$\exists c,n_0>0$,使得$\forall n \geq n_0$,$0 \leq f(n) < c \cdot g(n)$.

小$\omega$符号：对于函数$f(n)$和$g(n)$,$f(n)=\omega(g(n))$,当且仅当$\exists c,n_0>0$,使得$\forall n \geq n_0$,$0 \leq c \cdot g(n) < f(n)$.

渐进复杂度的常用性质：

+ $f(n) = \Theta(g(n))\iff f(n)=O(g(n))\land f(n)=\Omega(g(n))$
+ $f_1(n) + f_2(n) = O(\max(f_1(n), f_2(n)))$
+ $f_1(n) \times f_2(n) = O(f_1(n) \times f_2(n))$
+ $\forall a \neq 1, \log_a{n} = O(\log_2 n)$。由换底公式可以得知，任何对数函数无论底数为何，都具有相同的增长率，因此渐进时间复杂度中对数的底数一般省略不写。

```cpp title=""
int n, m;
std::cin >> n >> m;
for (int i = 0; i < n; ++i) {
  for (int j = 0; j < n; ++j) {
	for (int k = 0; k < m; ++k) {
	  std::cout << "hello world\n";
	}
  }
}
```

如果以输入的数值 $n$ 和 $m$ 的大小作为数据规模，则上面这段代码的时间复杂度为 $\Theta(n^2m)$。

### 主定理（MT）

**主定理（Master Theorem）**可以快速求得关于递归算法的复杂度。 主定理递推关系式如下：
如果

$$
T(n) = a T\left(\frac{n}{b}\right)+f(n)\qquad \forall n > b
$$

那么

$$
T(n) = \begin{cases}\Theta(n^{\log_b a}) & f(n) = O(n^{\log_b (a)-\epsilon}),\epsilon > 0 \\ \Theta(f(n)) & f(n) = \Omega(n^{\log_b (a)+\epsilon}),\epsilon\ge 0\\ \Theta(n^{\log_b a}\log^{k+1} n) & f(n)=\Theta(n^{\log_b a}\log^k n),k\ge 0 \end{cases}
$$

??? note "证明"
    依据上文提到的证明思路，具体证明过程如下
    
    对于第 $0$ 层（最高层），合并子问题需要花费 $f(n)$ 的时间
    
    对于第 $1$ 层（第一次划分出来的子问题），共有 $a$ 个子问题，每个子问题合并需要花费 $f\left(\frac{n}{b}\right)$ 的时间，所以合并总共要花费 $a f\left(\frac{n}{b}\right)$ 的时间。
    
    层层递推，我们可以写出类推树如下：![](../images/master-theorem-proof.svg)
    
    这棵树的高度为 ${\log_b n}$，共有 $n^{\log_b a}$ 个叶子，从而 $T(n) = \Theta(n^{\log_b a}) + g(n)$，其中 $g(n) = \sum_{j = 0}^{\log_{b}{n - 1}} a^{j} f(n / b^{j})$。
    
    针对于第一种情况：$f(n) = O(n^{\log_b a-\epsilon})$，因此 $g(n) = O(n^{\log_b a})$。
    
    对于第二种情况而言：首先 $g(n) = \Omega(f(n))$，又因为 $a f(\dfrac{n}{b}) \leq c f(n)$，只要 $c$ 的取值是一个足够小的正数，且 $n$ 的取值足够大，因此可以推导出：$g(n) = O(f(n)$)。两侧夹逼可以得出，$g(n) = \Theta(f(n))$。
    
    而对于第三种情况：$f(n) = \Theta(n^{\log_b a})$，因此 $g(n) = O(n^{\log_b a} {\log n})$。$T(n)$ 的结果可在 $g(n)$ 得出后显然得到。

下面举几个例子来说明主定理如何使用。

1.  $T(n) = 2T\left(\frac{n}{2}\right) + 1$，那么 $a=2, b=2, {\log_2 2} = 1$，那么 $\epsilon$ 可以取值在 $(0, 1]$ 之间，从而满足第一种情况，所以 $T(n) = \Theta(n)$。

2.  $T(n) = T\left(\frac{n}{2}\right) + n$，那么 $a=1, b=2, {\log_2 1} = 0$，那么 $\epsilon$ 可以取值在 $(0, 1]$ 之间，从而满足第二种情况，所以 $T(n) = \Theta(n)$。

3.  $T(n) = T\left(\frac{n}{2}\right) + {\log n}$，那么 $a=1, b=2, {\log_2 1}=0$，那么 $k$ 可以取值为 $1$，从而满足第三种情况，所以 $T(n) = \Theta(\log^2 n)$。

4.  $T(n) = T\left(\frac{n}{2}\right) + 1$，那么 $a=1, b=2, {\log_2 1} = 0$，那么 $k$ 可以取值为 $0$，从而满足第三种情况，所以 $T(n) = \Theta(\log n)$。

## 均摊分析[^2]

[^2]: 该节内容选取自[OI Wiki](https://oi-wiki.org/basic/amortized-analysis/)

**均摊分析（Amortized Analysis）**也称为摊还分析，是一种用于分析算法和动态数据结构性能的技术。它不仅仅关注单次操作的成本，还通过评估一系列操作的平均成本，为整体性能提供更加准确的评估。均摊分析不涉及概率，且只能确保最坏情况性能的每次操作耗费的平均时间，并不能确认系统的平均性能。在最坏情况下，均摊分析通过将高成本操作的开销分摊到低成本操作上，确保整体操作的平均成本保持在合理范围内。

均摊分析通常采用三种主要分析方法：聚合分析、记账分析和势能分析。这些方法各有侧重，分别适用于不同的场景，但它们的共同目标是通过均衡操作成本，优化数据结构在最坏情况下的整体性能表现。

考虑一个可扩展的数组，例如 C++ 中的 `vector`，其初始容量为 $m = 1$。每次插入新元素时，如果数组已满，则需要将数组的大小加倍，然后将原数组中的元素复制到新数组中，最后插入新元素。

接下来，将以动态数组的插入操作为例，通过聚合分析、记账分析和势能分析三种方法，分析其均摊成本。

### 聚合分析

**聚合分析（Aggregate Analysis）**通过计算一系列操作的总成本，并将其平均到每次操作上，从而得出每次操作的均摊时间复杂度。

以动态数组为例，首先，可以得到插入操作的两个关键成本：

+ 如果数组未满，插入操作的成本为 $O(1)$。
+ 如果数组已满，则插入操作需要扩容，扩容后复制元素的成本为 $O(m)$，其中 $m$ 为当前数组的大小。

所以，为了计算 n 次插入操作的总成本，可以将其分开为两部分计算：

1. 插入操作的成本：每次插入新元素的直接成本是常数时间 $O(1)$，对于 $n$ 次操作，总成本是 $O(n)$。
2. 数组扩容的成本：每次扩容涉及到复制原数组元素到新数组。这些操作发生在数组大小为 $1, 2, 4, \ldots , 2^k$ 的时刻，其中 $2^k$ 是小于等于 $n$ 的最大幂。扩容操作的成本分别是 $1, 2, 4, \ldots , 2^{k-1}$，总和为 $1 + 2 + 4 + \ldots  + 2^{k-1} = 2^k - 1$，这是一个等比数列的和，其结果为 $O(n)$。

因此，该数组总的插入成本为 $O(n)$，均摊到每次操作的成本为 $O(1)$。即使在最坏情况下，平均每次插入操作的成本依然是常数时间。

### 记账分析

**记账分析（Accounting Method）**通过为每次操作预先分配一个固定的均摊成本来确保所有操作的总成本不超过这些预分配的成本总和。记账法类似于一种费用前置支付的机制，其中较低成本的操作会存储部分费用，以支付未来高成本的操作。

以动态数组为例，可以为每次插入操作分配一个固定的均摊成本，以确保在需要扩容时已经预留了足够的费用。

1. 费用分配：
   + 假设每次插入操作的实际成本为 $1$，均摊成本设为 $3$。
   + 其中 $1$ 用于当前插入操作，$2$ 用于未来可能的扩容操作。

2. 费用使用：
   + 当数组已满时，需要进行扩容操作，实际成本为 $O(m)$，其中 $m$ 是当前数组的大小。
   + 假设扩容前数组的元素数量为 $n$，由于原数组的后半部分 $n/2$ 个元素在插入时共预存了 $n$ 单位的均摊成本，恰好足够支付扩容操作的成本。

以下是一个具体的示例：

```c title=""
初始状态：
arr    = [1, 2, 3, 4]  // 初始数组
amount = [2, 2, 2, 2]  // 每个元素预存的费用

// 第一轮扩容：数组已满，需要扩容
arr    = [1, 2, 3, 4, null, null, null, null]  // 扩容后数组
amount = [2, 2, 0, 0, 0, 0, 0, 0]  // 3, 4的费用用于支付扩容

// 继续插入新元素，直至再次满载
arr    = [1, 2, 3, 4, 5, 6, 7, 8]  // 继续填充数组
amount = [2, 2, 0, 0, 2, 2, 2, 2]  // 新插入的元素同样预存费用

// 第二轮扩容：数组再次满载，需要更大的空间
arr    = [1, 2, 3, 4, 5, 6, 7, 8, null, null, null, null, null, null, null, null]  // 扩容后数组
amount = [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  // 5, 6, 7, 8的费用用于支付扩容
```

以上过程表明，每次插入操作所存储的均摊成本足够支付未来的扩容操作，从而确保了每次操作的均摊成本维持在 $O(1)$。

### 势能分析

**势能分析（Potential Method）**通过定义一个势能函数（通常表示为 $\Phi$），度量数据结构的潜在能量，即系统状态中的预留资源，这些资源可以用来支付未来的高成本操作。势能的变化用于平衡操作序列的总成本，从而确保整个算法的均摊成本在合理范围内。

首先，定义**状态**$S$为某一时刻数据结构的状态，该状态可能包含元素数量、容量、指针等信息，其中定义初始状态为 $S_0$，即未进行任何操作时的状态。

其次，定义**势能函数** $\Phi(S)$ 用于度量数据结构状态 $S$ 的势能，其满足以下两个性质：

1. **初始势能**：在数据结构的初始状态 $S_0$ 下，势能 $\Phi(S_0) = 0$。
2. **非负性**：在任意状态 $S$ 下，势能 $\Phi(S) \geq 0$。

对于每个操作，其**均摊成本** $\hat{c}$ 定义为：

$$
\hat{c} = c + \Phi(S') - \Phi(S)
$$

其中 $c$ 为操作的实际成本，$S$ 和 $S'$ 分别表示操作前后的数据结构状态。该公式表明，均摊成本等于实际成本加上势能的变化。如果操作增加了势能（即 $\Phi(S') > \Phi(S)$），则均摊成本上升；如果操作消耗了势能（即 $\Phi(S') < \Phi(S)$），则均摊成本下降。

我们可以通过势能函数来分析一系列操作的总成本。设 $S_1, S_2, \dots, S_m$ 为从初始状态 $S_0$ 开始，经过 $m$ 次操作后产生的状态序列，$c_i$ 为第 $i$ 次操作的实际开销，那么第 $i$ 次操作的均摊成本 $p_i$ 为：

$$
p_i = c_i + \Phi(S_i) - \Phi(S_{i-1})
$$

因此，$m$ 次操作的总时间花销为：

$$
\sum_{i=1}^m c_i = \sum_{i=1}^m p_i + \Phi(S_0) - \Phi(S_m)
$$

由于 $\Phi(S) \geq \Phi(S_0)$，总时间花销的上界为：

$$
\sum_{i=1}^m p_i \geq \sum_{i=1}^m c_i
$$

因此，若 $p_i = O(T(n))$，则 $O(T(n))$ 是均摊复杂度的一个上界。

以动态数组 `vector` 的插入操作为例，定义如下的势能函数 $\Phi(h)$：

$$
\Phi(h) = 2n - m
$$

其中，$n$ 是数组中的元素数量，$m$ 是数组的当前容量。这个势能函数反映了数组中剩余可用空间的数量，即当前容量和实际使用空间之间的差异。

1.  **插入操作（无需扩容）**：
    -   **操作成本**：$O(1)$，因为只需插入一个元素。
    -   **势能变化**：插入后，元素数量增加 1，势能增加 $2$。
        -   $\Phi(h') - \Phi(h) = 2(n + 1) - m - (2n - m) = 2$
    -   **均摊成本**：$1 + 2 = 3$

2.  **插入操作（触发扩容）**：
    -   假设当前容量 $m = n$，插入一个新元素时触发扩容，新的容量变为 $2n$。
    -   **操作成本**：$O(n)$，因为需要将所有元素复制到新数组中，并插入新元素。
    -   **势能变化**：扩容后，容量增加，势能减少，变化大小为 $2 - n$。
        -   $\Phi(h') - \Phi(h) = 2(n + 1) - 2n - (2n - n) = 2 - n$
    -   **均摊成本**：$n + 1 + (2 - n) = 3$

通过上述分析可以看出，尽管扩容操作的实际成本较高，但由于势能函数的设计，整体均摊成本仍然保持在常数级别 $O(1)$。

## 算法思想

### 枚举

**枚举（Enumerate）**也称为穷举，是基于已有知识来猜测答案的一种问题求解策略。枚举的思想是不断地猜测，从可能的集合中一一尝试，然后再判断问题的条件是否成立。枚举是最普遍最易用的方法，但它也在处理大部分问题时效率远不如其它算法。

### 模拟

**模拟（Simulation）**就是用计算机来模拟问题中要求的操作，通常具有码量大、操作多、思路繁复的特点。由于它码量大，经常会出现难以查错的情况。

### 递归

**递归（Recursion）**在数学和计算机科学中是指在函数的定义中使用函数自身的方法，在计算机科学中还额外指一种通过重复将问题分解为同类的子问题而解决问题的方法。递归的基本思想是某个函数直接或者间接地调用自身，这样原问题的求解就转换为了许多性质相同但是规模更小的子问题。求解时只需要关注如何把原问题划分成符合条件的子问题，而不需要过分关注这个子问题是如何被解决的。

在程序执行中，递归是利用堆栈来实现的。每当进入一个函数调用，栈就会增加一层栈帧，每次函数返回，栈就会减少一层栈帧。而栈不是无限大的，当递归层数过多时，就会造成栈溢出的后果。显然有时候递归处理是高效的，比如归并排序；有时候是低效的，因为堆栈会消耗额外空间，而简单的递推不会消耗空间。

尾递归是指一个函数在调用自身之后不再执行任何其他操作，而是将返回值直接传递给函数调用的上级，从而避免了新的调用栈帧的创建。换句话说，尾递归是指递归调用发生在函数的最后一个语句中，从而使得函数调用不需要保存多个调用栈帧，而只需一个即可。理论上递归都可以改成循环的形式，尤其尾递归可以以固定的模式转换。

### 分治

**分治（Divide and Conquer）**字面上的解释是“分而治之”，就是把一个复杂的问题分成两个或更多的相同或相似的子问题，直到最后子问题可以简单的直接求解，原问题的解即子问题的解的合并。如果各子问题是不独立的，则分治法要重复地解公共的子问题，也就做了许多不必要的工作。此时虽然也可用分治法，但一般使用动态规划的效果更好。

枚举是横向地把问题划分，然后依次求解子问题；而递归是把问题逐级分解，是纵向的拆分。递归是一种编程技巧，一种解决问题的思维方式；分治算法很大程度上是基于递归的，解决更具体问题的算法思想。

### 贪心

**贪心（Greedy）**是用计算机来模拟一个“贪心”的人做出决策的过程。这个人十分贪婪，每一步行动总是按某种指标选取最优的操作。而且他目光短浅，总是只看眼前，并不考虑以后可能造成的影响。可想而知，并不是所有的时候贪心法都能获得最优解，所以一般使用贪心算法的时候，都要确保自己能证明其正确性。

贪心算法在有最优子结构的问题中尤为有效。最优子结构的意思是问题能够分解成子问题来解决，子问题的最优解能递推到最终问题的最优解。

最常见的贪心有两种，一种是排序型，用排序法常见的情况是输入一个包含几个（一般一到两个）权值的数组，通过排序然后遍历模拟计算的方法求出最优值。另一种是后悔型，思路是无论当前的选项是否最优都接受，然后进行比较，如果选择之后不是最优了，则反悔，舍弃掉这个选项；否则，正式接受。如此往复。二者的区别在于一种是离线的，先处理后选择；一种是在线的，边处理边选择。