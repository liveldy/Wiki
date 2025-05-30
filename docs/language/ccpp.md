---
title: C/C++
subtitle: 程序设计语言
description: C/C++
---

# C/C++

## 概览

### 什么是C/C++

=== "C"
	+ C是一种面向过程的、强调结构化编程的、高效的、偏向底层操作的、通用的编程语言，支持面向过程编程。
	+ C被认为是一种中级语言，它综合了高级语言和低级语言的特点。
	+ C是由Dennis Ritchie于1972年在贝尔实验室为开发UNIX操作系统而设计的。C最开始是于1972年在DEC PDP-11计算机上被首次实现。
=== "C++"
	+ C++是一种静态类型的、编译式的、通用的、大小写敏感的、不规则的编程语言，支持面向过程编程、面向对象编程和泛型编程。
	+ C++被认为是一种中级语言，它综合了高级语言和低级语言的特点。
	+ C++是由Bjarne Stroustrup 于1979年在新泽西州美利山贝尔实验室开始设计开发的。C++进一步扩充和完善了C语言，最初命名为带类的C，后来在1983年更名为C++。
	+ C++是C的一个超集，事实上，任何合法的C程序都是合法的C++程序。

### C/C++的特点

=== "C"
	+ 强调结构化编程，能够处理底层的活动，且能在多种计算机平台上编译，因此由C产生的程序也是高效精简的。
	+ 强大的多平台支持：C代码在Mac、UNIX、Windows计算机上都能通过编译，甚至在Android、iOS都有提供编译的程序。
=== "C++"
	+ C++完全支持面向对象设计，包括面向对象开发的四大特性：封装、继承、多态、抽象。
	+ 标准的C++由三个重要部分组成：核心语言、标准库、STL（标准模板库）
	+ 强大的多平台支持：C++代码在Mac、UNIX、Windows计算机上都能通过编译，甚至在Android、iOS都有提供编译的程序。

### C/C++的使用

=== "C"
	+ C语言最初是用于系统开发工作，特别是组成操作系统的程序。由于C语言所产生的代码运行速度与汇编语言编写的代码运行速度几乎一样，所以采用C语言作为系统开发语言。
	+ C语言更多地应用在偏向系统的开发，例如OS（操作系统）、或是SQL、Nginx等系统应用。
=== "C++"
	+ C++语言广泛使用在游戏开发、嵌入式系统开发、金融领域、图形图像处理、科学计算和数值分析。

### 学习C/C++

+ C/C++是一种学习周期长，难度较大，体系完善的高级语言，对于没有任何基础的初学者来说，是困难的。
+ C/C++的学习如同其它程序语言一样，一定要动手实践，“光说不做假把式”。
+ 如果你真的想把C/C++学好，绝不能浅尝辄止，要对其体系、逻辑有深层的理解。

## 环境安装

简单来说，如果想要在计算机上运行C/C++代码，只需要两样东西：

+ 文本编辑器：用于编写C/C++代码
+ C/C++编译器：将C/C++源代码编译成可执行程序

但是为了实现更丰富的功能和方便运行、调试等，或者你需要快速上手，可以使用集成环境，即集成编辑、运行、调试等一体的环境。

### 集成环境

+ Visual Studio： 面向.NET和C++开发人员的综合性Windows版IDE，可用于构建Web、云、桌面、移动应用、服务和游戏。
+ Visual Studio Code：一个通用的文本编辑器，但它有很多插件支持C/C++开发，使其成为一个流行的选择，通过安装C/C++插件和调整设置，你可以使其成为一个很好的C语言开发环境。
+ Dev-C++：一款免费的、自由软件的 C/C++ 集成开发环境（IDE），支持单文件和多文件开发，可对代码格式化和调试。

!!! note "说明"
	很多高校都是以Dev-C++为开发环境进行教学的，而且诸多比赛也使用该环境，但是作者个人认为，Dev-C++虽然方便、轻量、易用，但绝非长远的打算。而且，许多企业、公司都不使用Dev-C++。由于集成环境操作简单，这里不会对使用集成环境的操作进行说明，可以根据IDE的指引进行操作，或自行上网查询。

### GNU C/C++编译器

!!! note "说明"
	如果你是初学者或想要快速上手C/C++，请跳过这部分内容。

#### Windows安装

为了在Windows上安装GCC，您需要安装MinGW。请访问[MinGW](https://github.com/niXman/mingw-builds-binaries/releases)下载最新版本的MinGW安装程序。

将压缩包解压并将bin目录添加到环境变量中：例如，我解压到D:/MinGW中。bin文件夹所在的目录为D:\MinGW\x86_64-13.2.0-release-win32-seh-msvcrt-rt_v11-rev1\bin。

按下 ++win+r++ 打开运行对话框，输入`sysdm.cpl`回车进入系统属性窗口，选择高级>>环境变量，添加PATH变量：你的bin文件夹目录。添加完成后，点击确定关闭窗口。

按下 ++win+r++ 打开运行对话框，输入`cmd`进入命令行窗口，输入`gcc --version`回车便可看到版本信息，如果提示不存在该命令，说明添加环境变量失败。

#### Mac OS安装

如果您使用的是Mac OS X，最快捷的获取GCC的方法是从苹果的网站上下载Xcode开发环境，并按照安装说明进行安装。一旦安装上Xcode，您就能使用GNU编译器。

#### Linux安装

Linux的版本众多，常见的有CentOS、Ubuntu、Debian等等，安装方法不尽相同，读者可自行上网查询或进入[此处](https://gcc.gnu.org/install/)进行安装。

### C/C++编译与版本

#### 编译过程

=== "C"
	开发者使用**编辑程序**进行编辑得到**源程序文件`.c`**，由**编译程序**翻译得到**目标程序文件`.o`**，再由**链接程序**链接得到**可执行程序文件`.exe`**（Windows），运行可执行程序得到结果。写在源文件中的源代码是人类可读的源。它需要编译转为机器语言，这样CPU可以按给定指令执行程序。
=== "C++"
	开发者使用**编辑程序**进行编辑得到**源程序文件`.cpp`**，由**编译程序**翻译得到**目标程序文件`.obj`**，再由**链接程序**链接得到**可执行程序文件`.exe`**（Windows），运行可执行程序得到结果。写在源文件中的源代码是人类可读的源。它需要编译转为机器语言，这样CPU可以按给定指令执行程序。

#### 版本与标准化

=== "C"
	|发布时间|名称|说明|
	|-|-|-|
	|1987|K&RC|Brian Kernighan 和 Dennis Ritchie合著的The C Programming Language第1版是公认的C标准。它定义了c语言，但没有定义c库。它不是官方的标准。|
	|1989|ANSIC/C89/C90|国际标准为ISO/IEC9899-1990，中国国家标准GB/T 15272-94是国际ISO标准的中文翻译。ANSI于1989年批准该标准，因此通常称之为C89。ISO于1990年批准该标准，因而又有C90的叫法。|
	|1999|C99/C9X|ISO/IEC 9899：1999的非正式名称，在1999年推出，被ANSI于2000年3月采用。|
	|2011|C11/C1X|C11标准是 ISO/IEC 9899:2011-- C 的简称，曾用名为C1X。C11标准是C语言标准的第三版。|
=== "C++"
	|发布时间|名称|说明|
	|-|-|-|
	|2020|C++20|引入三方运算符、标准库改进等|
	|2017|C++17|标准库改进等|
	|2014|C++14|二进制字面量、变量模板等|
	|2011|C++11|引入众多的库、匿名函数等|
	|2003|C++03|错误修复版本|
	|1998|C++98|bool类型、模板实例化、export和mutable关键字等|

## 程序基本结构与运算符

在Windows，编辑C/C++源文件可以使用记事本、Notepad++或其他文本编辑器；在Linux，编辑C/C++源文件可以使用vi或者vim。

### 第一个程序

=== "C"
	下面是一个最简单的C程序，将这个文本保存为hello.c。
	```c
	#include <stdio.h>
	int main()
	{
	   printf("Hello, World!");
	   return 0;
	}
	```
	在当前目录打开命令行，运行：
	```bash
	gcc -o hello hello.c
	```
=== "C++"
	下面是一个最简单的C++程序，将这个文本保存为hello.cpp。
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		cout << "Hello,World!" << endl;
		return 0;
	}
	```
	在当前目录打开命令行，运行：
	```bash
	g++ -o hello hello.cpp
	```

你会在当前目录看到生成了一个hello.exe，双击hello.exe打开，会发现其一闪而过，这是因为该程序执行完任务后会直接关闭，如果想要看到输出的内容，有以下两个办法：

1.将程序改为下面内容：

=== "C"
	```c
	#include <stdio.h>
	#include <stdlib.h>

	int main()
	{
	   printf("Hello, World!\n");
	   system("pause");
	   return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		cout << "Hello,World!" << endl;
		system("pause");
		return 0;
	}
	```

2.直接在命令行进行运行，输入`.\hello.exe`回车，则可在命令行看到输出：

```bash
Hello, World!
```

我们目前只需要在main{...}中写需要的内容，其他部分在之后进行说明。

!!! note "说明"
	+ 试着修改引号内的内容，重新运行程序，观察输出的结果。
	+ 删掉末尾的分号，重新运行程序，看看会发生什么。

如果你随意地删掉上面代码的一部分，就很可能会出现报错，这是因为运行的代码不符合语法。如同自然语言，编程语言也要对应的一套语法，这是本教程的重点。但语法错误不是报错的唯一原因，还可能会因为其它原因报错，我们在之后的内容讲到。

如果你的代码中使用了中文等非ASCII字符，可能会出现乱码，是由于编码不一致导致的，因此，需要指定你的文件编码方式：

=== "C"
	```bash
	gcc -fexec-charset=UTF-8 -finput-charset=UTF-8 -o hello hello.c
	```
=== "C++"
	```bash
	g++ -fexec-charset=UTF-8 -finput-charset=UTF-8 -o hello hello.cpp
	```

### 词法规则与书写格式

#### 词法规则

C/C++的字符集从专业角度说是由[ASCII](https://ascii.org.cn/)码中的所有可见字符、空格和空字符（ASCII码为0）；从一般角度说是**英文字符、数字、空格**构成。除字符集的中的字符在C/C++语句中均为非法。  

标识符是由字母、下划线和数字组成的字符序列，必须以字母或下划线开头，不能是数字，且标识符区分大小写。已经被系统预定义的标识符称为关键字（保留字），用户在定义标识符时不能重复定义，也不能与关键字相重复。  

#### 书写格式

C/C++程序书写格式较为灵活，对于单个语句以分号（;）隔开，对于多个语句以花括号隔开（{}），以下是相关说明：

1. 一行可以写多个语句，一个语句也可以写多行（注意是以词切分）。习惯上一行一个语句，但语句较长时可分多行，语句较短时也可以一行多个语句，尽可能地提高可读性。
2. 多个语句构成复合语句（语句块），花括号是复合语句的定界符，分号是单语句的定界符。
3. 宏定义和注释不属于语句，因而编译器不会识别注释中的语句，宏定义也不需要写分号。单行注释写在“//”之后，多行注释写在“/\*”和“\*/”里面

!!! note "建议"
	1. 对于代码较多的中大型程序或者较为复杂的程序应当尽可能地多使用注释。
	2. 程序需要顾及可读性和运行效率，代码要求保证可读性的同时尽可能精简。
	3. 尽可能使用最优的算法，不要用繁杂的方式解决简单的问题。

=== "C"
	数据类型的四大基本类型为int（整数型/整型）、float（单精度浮点型）、double（双精度浮点型）、char（字符型）。修饰数据类型的关键字由long、short、unsigned和signed。以下是所有可行的修饰方式和相关数据类型描述：

	|基本类型|占用空间|数据表达范围|
	|-|-|-|
	|char|1字节|-128到127或0到255|
	|unsigned char|1字节|0到255|
	|signed char|1字节|-128到127|
	|int|2或4字节|-32,768到32,767或-2,147,483,648到2,147,483,647|
	|unsigned int|2或4字节|0到65,535或0到4,294,967,295|
	|short|2字节|-32,768到32,767|
	|unsigned short|2字节|0到65,535|
	|long|4字节|-2,147,483,648到2,147,483,647|
	|unsigned long|4字节|0到4,294,967,295|
	|float|4字节|1.2E-38到3.4E+38、6位有效位|
	|double|8字节|2.3E-308到1.7E+308、15位有效位|
	|long double|16字节|3.4E-4932到1.1E+4932、19位有效位|
=== "C++"
	数据类型的五大基本类型为int（整数型/整型）、float（单精度浮点型）、double（双精度浮点型）、char（字符型）、bool（布尔型/逻辑型）。修饰数据类型的关键字由long、short、unsigned和signed。以下是所有可行的修饰方式和相关数据类型描述：

	|基本类型|占用空间|数据表达范围|
	|-|-|-|
	|char|1 个字节|-128 到 127 或者 0 到 255|
	|unsigned char|1 个字节|0 到 255|
	|signed char|1 个字节|-128 到 127|
	|int|4 个字节|-2147483648 到 2147483647|
	|unsigned int|4 个字节|0 到 4294967295|
	|signed int|4 个字节|-2147483648 到 2147483647|
	|short int|2 个字节|-32768 到 32767|
	|unsigned short int|2 个字节|0 到 65,535|
	|signed short int|2 个字节|-32768 到 32767|
	|long int|8 个字节|-9,223,372,036,854,775,808 到 9,223,372,036,854,775,807|
	|signed long int|8 个字节|-9,223,372,036,854,775,808 到 9,223,372,036,854,775,807|
	|unsigned long int|8 个字节|0 到 18,446,744,073,709,551,615|
	|float|4 个字节|+/- 3.4e +/- 38 (~7 位数字)|
	|double|8 个字节|+/- 1.7e +/- 308 (~15 位数字)|
	|long long|8 个字节|-9,223,372,036,854,775,807 到 9,223,372,036,854,775,807|
	|long double|16 个字节|18-19位数字|
	|bool|1位|0和1，也可表示为true和false，本质上是0和1|

### 变量与常量

数据类型分为常量和变量，顾名思义，变量是指可以变化的量，而常量是固定不动的值。

=== "C"
	```c
	#include <stdio.h>
	int main()
	{
		int a; //定义一个名称为a的整数型变量
		a = 1; //给变量a赋值
		double b = 2.5; //定义一个名称为b的双精度浮点型变量的同时初始化
		printf("%d\n%f",a,b); //输出a和b的值，用换行符隔开
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		int a; //定义一个名称为a的整数型变量
		a = 1; //给变量a赋值
		double b = 2.5; //定义一个名称为b的双精度浮点型变量的同时初始化
		cout << a << endl << b; //输出a和b的值，用换行符隔开
		return 0;
	}
	```

对于变量的基本操作，主要有四种：定义、赋值、引用、转换。

在上述例子中，进行了变量a和b的定义。变量使用前必须先定义，其三要素为标识符（名字）、类型和值，定义时需说明前两者，值可以选择说明或者不说明。定义时，变量名表以逗号分隔。下面也是同样的一个例子。

=== "C"
	```c
	#include <stdio.h>

	int main()
	{
		char a, b; //变量名表
		a = 'f';
		printf("%c",a);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		char a, b; //变量名表
		a = 'f';
		cout << a;
		return 0;
	}
	```

你可能会注意到，我们赋值字符时使用了单引号但赋值数值没有使用，即等号左边是变量而右边是一个常量，常见的常量有以下几种。

=== "C"
	|常量类型|表示方法|
	|-|-|
	|整型|十进制直接表示，如154；八进制在数前加0，如022；十六进制在数前加0X或0x，如0x4E、0X6C|
	|浮点型|可以省略小数部分或整数部分其一，默认为0，但不能省略小数点，如0.55、.125、24.、47.20；还可以用指数形式表示，aEb或aeb，等价于a\*10^b，例如5E2，0.222e8|
	|字符|单引号括起来表示，例如's'|
	|字符串|双引号括起来表示，例如"nb"，"Hello"|
=== "C++"
	|常量类型|表示方法|
	|-|-|
	|整型|十进制直接表示，如154；八进制在数前加0，如022；十六进制在数前加0X或0x，如0x4E、0X6C|
	|浮点型|可以省略小数部分或整数部分其一，默认为0，但不能省略小数点，如0.55、.125、24.、47.20；还可以用指数形式表示，aEb或aeb，等价于a\*10^b，例如5E2，0.222e8|
	|字符|单引号括起来表示，例如's'|
	|字符串|双引号括起来表示，例如"nb"，"Hello"|
	|布尔常量|true或false|
	|符号常量|如NULL等|

变量在赋值时，可以使用常量进行赋值，也可以使用变量赋值，通常需要相同类型的量进行赋值，但是也可以使用不同类型的变量进行赋值，此时就需要进行数据类型的转换。显式转换是指人为的强制转换，利用相关的关键字进行转换。隐式转换是指程序识别到被赋值变量和所赋值变量类型不匹配后，自动进行的转换。注意高类型向低类型转换时，是不保值的，会有精度损失。具体请看下面的例子。

=== "C"
	```c
	#include <stdio.h>
	int main() {
		int a = 's'; // 不会报错：发生了隐式转换
		char b = (char)115; // 发生了显式转换
		int d = 1e7;
		short e = d; // 发生精度损失：高类型向低类型转换
		int f = e;
		printf("%d\n", a);
		printf("%c\n", b);
		printf("%d\n", f);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		int a = 's'; //不会报错：发生了隐式转换
		char b = char(115); //不会报错：发生了显式转换
		char c = (char)115; //也可以这样用
		int d = 1e7;
		short e = d; //发生精度损失：高类型向低类型转换
		int f = e;
		cout << a << endl;
		cout << b << endl;
		cout << f << endl;
		return 0;
	}
	```

!!! warning "注意"
	目前所讲到的基本变量类型全都可以互相转换，但是可能会有数值变化和精度损失，具体原因这里不作解释，和计算机内部数据存储的原理相关。有些数据类型之间不能隐式转换，需要进行人为的强制转换，使用到关键字。
	
注意变量定义后需要初始化或者赋值，引用未赋值的变量是不合法的，会产生报错，例如：

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int a;
		printf("%d", a); // 未初始化的变量
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		int a;
		cout << a;
		return 0;
	}
	```

变量可以进行引用，例如对别的变量赋值、作函数参数、参与运算等等，这些被称为变量的引用。可以使用sizeof关键字获取变量（变量类型）的占用字节。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int a;
		printf("%zu\n", sizeof(char));
		printf("%zu\n", sizeof(a));
		printf("%zu\n", sizeof(2.5));
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		int a;
		cout << sizeof(char) << endl;
		cout << sizeof(a) << endl;
		cout << sizeof(2.5) << endl;
		return 0;
	}
	```

变量的定义、赋值、引用、转换往往不都是独立发生的，更多的情况下都同时发生。

=== "C"
	```c
	#include <stdio.h>
	int main() {
		int a; // 定义
		a = 1; // 赋值
		printf("%d\n", a); // 引用
		int b = 2; // 定义、赋值（定义的同时赋值称为初始化）
		a = b; // 赋值、引用
		double c = b; // 定义、赋值、引用、转换
		c = a; // 赋值、引用、转换
		c = 's'; // 赋值、转换
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		int a; //定义
		a = 1; //赋值
		cout << a; //引用
		int b = 2; //定义、赋值（定义的同时赋值称为初始化）
		a = b; //赋值、引用
		double c = b; //定义、赋值、引用、转换
		c = a; //赋值、引用、转换
		c = 's'; //赋值、转换
		return 0;
	}
	```

在你的计算机上运行下面的代码，运行前，对输出的结果进行猜测，然后验证你的猜测。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		char a = 's';
		char b = a - 1;
		char c = 115;
		int d = a - 1;
		printf("%c\n", a);
		printf("%d\n", a - 1);
		printf("%c\n", b);
		printf("%c\n", c);
		printf("%d\n", d);
		char e = '2';
		char f = 2;
		int g = '2';
		int h = 2;
		printf("%c\n", e);
		printf("%d\n", f);
		printf("%d\n", g);
		printf("%d\n", h);
		printf("%d\n", 2);
		printf("%c\n", '2');
		return 0;
	}
	```
=== "C++"
	```cpp
	#include<iostream>
	using namespace std;
	int main()
	{
		char a='s';
		char b = a - 1;
		char c = 115;
		int d = a - 1;
		cout << a << endl;
		cout << a - 1 << endl;
		cout << b << endl;
		cout << c << endl;
		cout << d << endl;
		char e = '2';
		char f = 2;
		int g = '2';
		int h = 2;
		cout << e << endl;
		cout << f << endl;
		cout << g << endl;
		cout << h << endl;
		cout << 2 << endl;
		cout << '2' << endl;
		return 0;
	}
	```

### 运算符与表达式

#### 算术运算符

除名称和符号外，运算符有类别、结合性和优先级这三个重要的要素，类别是指运算符的目数，相当于数学中的元数，即其操作数的个数，例如5+6中加号需要两个数相加，其操作数为2，即其为双目。

我们知道，在数学中，有算式的运算顺序，一般都是从左至右运算，运算的符号默认优先和左边的数结合，例如5+-7会认为是5加上-7（但更多会加括号以避免歧义），这里加号优先和左边的数结合，但也有反例，例如2√4，根号优先和右边的数结合，即√4=2，再和左边的数相乘。这就是运算符的结合性。

优先级这个概念就很好理解了，在数学中，乘除的优先级高于加减，在运算时优先于加减，而加减具有相同的优先级。优先级低的先结合，高的后结合。

|名称|类别|运算符|结合性|优先级|
|-|-|-|-|-|
|加|双目|+|从左至右|3|
|减|双目|-|从左至右|3|
|乘|双目|\*|从左至右|2|
|除|双目|/|从左至右|2|
|取余|双目|%|从左至右|2|
|取负|单目|-|从右至左|1|
|自增（增1）|单目|++|从右至左|1|
|自减（减1）|单目|--|从右至左|1|

下面是算术运算符简单的使用和一些特殊说明。

=== "C"
	```c
	#include <stdio.h>
	int main() {
		int a = 4, b = 5;
		float c = 2.5;
		printf("%zu\n", sizeof(b + c)); // 在运算时也会发生隐式转换，但是如果没有给定应当转换的类型，会往高类型转换
		printf("%d\n", b / a); // 结果为1，均由整数类型参与的除法进行整除
		printf("%f\n", b / c); // 结果为2，如果有浮点数参与，被除数将会被除尽（常规除法）
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		int a = 4, b = 5;
		float c = 2.5;
		cout << sizeof(b + c) << endl; //在运算时也会发生隐式转换，但是如果没有给定应当转换的类型，会往高类型转换
		cout << b / a << endl; //结果为1，均由整数类型参与的除法进行整除
		cout << b / c << endl; //结果为2，如果有浮点数参与，被除数将会被除尽（常规除法）
		return 0;
	}
	```

输入两个数，分别输出其和与差。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		printf("请输入两个数（用空格分隔）：");
		double a, b;
		scanf("%lf %lf", &a, &b);
		double c = a + b, d = a - b;
		printf("和为：%lf\n差为：%lf\n", c, d);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		cout << "请输入两个数（用空格分隔）：";
		double a, b;
		cin >> a >> b;
		double c = a + b, d = a - b;
		cout << "和为：" << c << endl << "差为：" << d << endl;
	}
	```

输入一个三位数，将其倒序输出。例如输入874，输出478。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int num;
		scanf("%d", &num);
		printf("%d%d%d\n", num % 10, (num / 10) % 10, num / 100);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include<iostream>
	using namespace std;
	int main()
	{
		int num;
		cin >> num;
		cout << num % 10 << num / 10 % 10 << num / 100;
		return 0;
	}
	```

尤其要注意自增和自减运算的区别：符号在前先加减，符号在后先返值。运行下面的代码，体会这一差异。

=== "C"
	```c
	#include <stdio.h>
	
	int main() {
		int a;
		// 情况1
		a = 2;
		printf("%d\n", a++);
		// 情况2
		a = 2;
		printf("%d\n", ++a);
		// 情况3
		a = 2;
		a++;
		printf("%d\n", a);
		// 情况4
		a = 2;
		++a;
		printf("%d\n", a);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		int a;
		//情况1
		a = 2;
		cout << a++ << endl;
		//情况2
		a = 2;
		cout << ++a << endl;
		//情况3
		a = 2;
		a++;
		cout << a << endl;
		//情况4
		a = 2;
		++a;
		cout << a << endl;
		return 0;
	}
	```

运行前推测下程序的输出结果，并试着运行验证推测是否正确。

=== "C"
	```c
	#include <stdio.h>
	
	int main() {
		int i = 3, j = 7;
		int k = -i+++j;
		int s = --i+k---j;
		int t = i+++j--+k+++-s;
		printf("%d %d %d %d %d\n", i, j, k, s, t);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include<iostream>
	using namespace std;
	int main()
	{
		int i = 3, j = 7;
		int k = -i+++j;
		int s = --i+k---j;
		int t = i+++j--k+++-s;
		cout << i << j << k << s << t;
		return 0;
	}
	```

!!! warning "注意"
    上例子中的写法并不推荐！这只是娱乐性的案例，因为C语言在不同标准下，自增和自减有一定的结合性和优先级差异，而且程序代码务必要清晰明了，尽可能不出现有歧义的语句。

#### 关系运算符

|名称|类别|运算符|结合性|优先级|
|-|-|-|-|-|
|大于|关系|>|从左至右|5|
|小于|关系|<|从左至右|5|
|大于等于|关系|>=|从左至右|5|
|小于等于|关系|<=|从左至右|5|
|等于|关系|==|从左至右|6|
|不等于|关系|!=|从左至右|6|

关系运算符，顾名思义，用于判断两个量的关系，这里要注意以下几点：

+ 关系运算符的优先级普遍低于算术运算符；
+ 关系运算符的结果有且仅有两个，非0即1；
+ 关系运算符在参与运算时，不进行隐式类型转换，参与运算的类型需要一致。

=== "C"
	```c
	#include <stdio.h>
	
	int main() {
		printf("%d\n", 1 == 0); //输出0，注意比较等于和赋值等于的区别
		printf("%d\n", 2 > 1); //输出1
		int x = 2, y = 6;
		printf("%d\n", x <= y); //输出1
		char a = 'd', b = 'c';
		printf("%d\n", a < b); //输出0，字符比较实际上是比较其ASCII码值
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		cout << (1 == 0) << endl; //输出0，注意比较等于和赋值等于的区别
		cout << (2 > 1) << endl; //输出1
		int x = 2, y = 6;
		cout << (x <= y) << endl; //输出1
		char a = 'd', b = 'c';
		cout << (a < b) << endl; //输出0，字符比较实际上是比较其ASCII码值
	}
	```

赋值等于（=）和比较等于（==）并不一样，不能替换使用，如果误将赋值等于使用为比较等于，会得到意想不到的效果：

=== "C"
	```c
	#include <stdio.h>
	
	int main()
	{
		int a = 2, b = 3;
		printf("%d\n", a == b);
		printf("%d %d\n", a, b);
		printf("%d\n", a = b);
		printf("%d %d\n", a, b);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		int a = 2, b = 3;
		cout << (a == b) << endl;
		cout << a << " " << b << endl;
		cout << (a = b) << endl;
		cout << a << " " << b << endl;
	}
	```

运行上面的代码，你会发现：预期的结果应该是不等于，但是a=b却“判断”为了等于，输出了对应结果，这是因为实际上执行了a=b这个赋值操作后，返回了赋值的结果，即返回了3，故得到了对应输出。同样地，可以执行式子`a=(b=5)`之后a的值和b的值都是5。


#### 逻辑运算符

|名称|类别|运算符|结合性|优先级|备注|
|-|-|-|-|-|-|
|逻辑非|单目|!|从右至左|1|也叫逻辑求反|
|逻辑与|双目|&&|从左至右|10|“一假为假，全真为真”|
|逻辑或|双目|\|\||从左至右|11|“全假为假，一真为真”|

关于逻辑运算符主要说明以下两点：

1. 逻辑运算符预期希望的是布尔类型变量参与运算，如果不是布尔类型变量，则会先隐式转换成布尔类型变量进行运算。其转换方式具体为任何非0值全都转为1（true），0值转换为0（false）。
2. 短路规则（堕性求值）：由于在逻辑与运算中，“一假为假”，所以多个逻辑与在从左向右结合时，只要出现一个操作数为0，就不再进行后续运算；同样地，由于逻辑或运算中，“一真为真”，所以多个逻辑或在从左向右结合时，只要出现一个操作数为1，就不再进行后续运算。

=== "C"
	```c
	#include <stdio.h>

	int main()
	{
		printf("%d\n", 5 && 6);
		printf("%d\n", 5 && 5);
		printf("%d\n", 5 && 0);
		int a = 4, b = 0, c = 3;
		// 下面是证明短路规则的案例，如果一旦能够判断当前逻辑关系，就不会进行进一步的运算，即c || (a = 5)并没有进行
		printf("%d\n", (a && b) && (c || (a = 5)));
		printf("%d\n", a);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		cout << (5 && 6) << endl;
		cout << (5 && 5) << endl;
		cout << (5 && 0) << endl;
		int a = 4, b = 0, c = 3;
		//下面是证明短路规则的案例，如果一旦能够判断当前逻辑关系，就不会进行进一步的运算，即c || (a = 5)并没有进行
		cout << ((a && b) && (c || (a = 5))) << endl;
		cout << a << endl;
	}
	```


#### 位运算符

|名称|类别|运算符|结合性|优先级|实例|
|-|-|-|-|-|-|
|按位非|单目|~|从右至左|1|~15的值16|
|按位与|双目|&|从左至右|7|11&7的值为5|
|按位或|双目|\||从左至右|9|11\|7的值为15|
|按位异或|双目|^|从左至右|8|11^7的值为12|
|左移|移位|<<|从左至右|4|7<<2的值为28|
|右移|移位|>>|从左至右|4|7>>2的值为1|

按位非也叫按位取反。左移位是指左侧为操作数，右侧为位数，将操作数转换为二进制后向左移位数指定个数，多弃少补（0）；而右移位是指左侧为操作数，右侧为位数，将操作数转换为二进制后向右移位数指定个数，多弃少补（0）。

下面是位运算律表：

|名称|运算律|备注|
|-|-|-|
|按位非|~0=1，~1=0|-|
|按位与|0&0=0，0&1=1&0=0，1&1=1|“一假为假，全真为真”|
|按位或|0\|0=0，0\|1=1\|0=1，1\|1=1|“全假为假，一真为真”|
|按位异或|0^0=0，0^1=1^0=1，1^1=0|“相同为假，不同为真”|

#### 赋值运算符

除基本赋值运算符外，其它复合赋值运算符都是类似的，实质是简化了其它双目运算。如果设U为一个双目运算符，则aU=b等价于a=aUb，其中a表示变量，b表示表达式。例如a+=b表示a=a+b。

|名称|类别|运算符|结合性|优先级|
|-|-|-|-|-|
|基本赋值运算符|双目|=|从右至左|13|
|复合赋值运算符|双目|+=、-=、*=、/=、%=、&=、^=、\|=、<<=、>>=|从右至左|13|

#### 特殊运算符

除以上基本运算符外，接下来是一些特殊的运算符，部分特殊运算符将在后面的内容讲到。

|名称|类别|运算符|结合性|优先级|实例|备注|
|-|-|-|-|-|-|-|
|条件|三目|?:|从右至左|12|4<6?5:2的值为5|a?b:c意为条件a成立时输出b，否则输出c|
|逗号|逗号|,|从左至右|14|5,7的值为7|运算时从左至右，但只输出最后一个值|
|圆括号|-|()|从左至右|0|5*(4+2)的值为30|常用于改变优先级|
|下标|-|[]|从左至右|0|-|用于数组，在后文讲到|
|点|-|.|从左至右|0|-|用于结构体、共用体变量，在后文讲到|
|箭头|-|-\>|从左至右|0|-|用于结构体、共用体变量，在后文讲到|
|类|-|::|从左至右|0|-|用于类，在后文讲到|
|取内容|-|*|从右至左|1|-|用于指针，在后文讲到|
|取地址|-|&|从右至左|1|-|用于指针，在后文讲到|

常量、变量、运算符、函数和输入输出构成了表达式，能够独立成为语句，即表达式语句。

## 程序控制结构

### 输出格式控制与转义

定义标识符的语句成为定义语句，除此外还有表达式语句、复合语句和空语句，复合语句是若干语句用花括号括起来组成的一条语句。空语句在语法上需要一条语句，而语义上不需要执行任何操作时使用。

#### 转义符

转义符的出现是为了解决需要对字符进行操作且避免该字符被编译器识别为语句成分时出现错误这一情况。例如某程序需要输出英文双引号（"），但是直接进行输出显然会报错，这是因为编译器将需要输出的双引号视为了语句成分，从而出现一个多余的双引号，为了解决这个问题，使用右斜杠进行转义，这时编译器不再将中间需要输出的双引号视为语句词法，而是成为了字符实体。**虽然在代码中转义符由多个字符组成，但其实际输出时仅有一个字符。**  

转义符除了解决上述问题外，还用于扩充字符集，当C/C++不满足于已有的ASCII字符时，用右斜杠加ASCII字符来实现除ASCII字符外字符的功能。上述两个功能中，第一个功能对任意非第二个功能所涉及的字符加右斜杠时，即视为对该字符转义。第二个功能的相关转义符如下表：

|转义符|意义|
|-|-|
|\t|水平制表符，等价于tab键|
|\v|垂直制表符|
|\n|换行符|
|\0|终止符，也称为空字符或结束标志字符|
|\ddd|八进制数|
|\xhh|十六进制数|

值得注意的是，C/C++中使用斜杠（也称左斜杠，/）作除法运算符，使用反斜杠（也称右斜杠，\）作转义符。而在计算机系统中，左斜杠常作服务器文件路径（网站链接中多见），右斜杠作本地文件资源管理器路径。

#### 输出格式控制符

=== "C"
	在前文中常使用的scanf()和printf()是指标准输入输出，即在程序运行终端上的输入输出，除此外，还有其它输入输出符，在后文说明。下表是常使用的输出格式控制符。

	|格式控制符|说明|
	|-|-|
	|%c|输出一个单一的字符。|
	|%d、%ld|以十进制、有符号的形式输出short、int、long类型的整数。|
	|%u、%lu|以十进制、无符号的形式输出short、int、long类型的整数。|
	|%o、%lo|以八进制、不带前缀、无符号的形式输出short、int、long类型的整数。|
	|%#o、%#lo|以八进制、带前缀、无符号的形式输出short、int、long类型的整数。|
	|%x、%lx|以十六进制、不带前缀、无符号的形式输出short、int、long类型的整数。如果x小写，输出的十六进制数字也小写；如果X大写，输出的十六进制数字也大写。|
	|%#x、%#lx|以十六进制、带前缀、无符号的形式输出short、int、long类型的整数。如果x小写，输出的十六进制数字和前缀都小写；如果X大写，输出的十六进制数字和前缀都大写。|
	|%f、%lf|以十进制的形式输出float、double类型的小数。|
	|%e、%le|以指数的形式输出float、double类型的小数。如果e小写，输出结果中的e也小写；如果E大写，输出结果中的E也大写。|
	|%g、%lg|以十进制和指数中较短的形式输出float、double类型的小数，并且小数部分的最后不会添加多余的0。如果g小写，当以指数形式输出时e也小写；如果G大写，当以指数形式输出时E也大写。|
	|%s|输出一个字符串。|
=== "C++"
	在前文中常使用的cout和cin是指标准输入输出，即在程序运行终端上的输入输出，除此外，还有其它输入输出符，在后文说明。下表是常使用的输出格式控制符，使用后四个控制符前，应当引用头文件：`#include <iomanip>`。

	|格式控制符|说明|备注|
	|-|-|-|
	|endl|输出换行符|-|
	|dec|十进制表示|-|
	|hex|十六进制表示|-|
	|oct|八进制表示|-|
	|setw()|数据输出宽度|-|
	|setfill()|填充输出字符|-|
	|setprecision()|输出有效数字位数|-|
	|setiosflags()|输出格式指定|ios::fixed定点格式，ios::scientific指数格式|


输入一个十进制数，输出其八进制和十六进制。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int num;
		scanf("%d", &num);
		printf("%o\n", num);  // 输出八进制
		printf("%x\n", num);  // 输出十六进制
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		int num;
		cin >> num;
		cout << oct << num << endl;
		cout << hex << num << endl;
		return 0;
	}
	```

### 选择结构

C++程序控制结构（其实大多数语言的程序结构也是如此）有三种，顺序结构、选择结构（也称为条件结构、判断结构）、循环结构（也称为重复结构）

#### if……else语句

输入一个整数，判断其是否为奇数还是偶数，奇数则输出1，偶数则输出0。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int num;
		scanf("%d", &num);
		if (num % 2 == 1)
			printf("1");
		else
			printf("0");
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		int num;
		cin >> num;
		if (num % 2 == 1)cout << "1";
		else cout << "0";
		return 0;
	}
	```


```cpp title="if语法"
条件语句（if）：
形式1：
if (条件表达式)
	满足执行语句
形式2：
if (条件表达式)
	满足执行语句
else 
	不满足执行语句
形式3：
if (条件表达式1)
	满足条件表达式1执行语句
else if(条件表达式2)
	满足条件表达式2执行语句（不满足条件表达式1）
形式4：
if (条件表达式1)
	满足条件表达式1执行语句
else if(条件表达式2)
	满足条件表达式2执行语句（不满足条件表达式1）
else
	以上条件均不满足执行语句
形式3/4推广：
if (条件表达式1)
	满足条件表达式1执行语句
else if(条件表达式2)
	满足条件表达式2执行语句
else if(条件表达式3)
	满足条件表达式3执行语句
......
else if(条件表达式n)
	满足条件表达式n执行语句
......
else
	以上条件均不满足执行语句
此else语法上可以省略，形如形式3，也可以不省略，形如形式4
```

输入三边a，b，c，判断其是否能构成三角形，能则输出三角形的面积和周长，不能则输出-1.

=== "C"
	```c
	#include <stdio.h>
	#include <math.h>

	int main() {
		double a, b, c;
		scanf("%lf %lf %lf", &a, &b, &c);
		if (a + b > c && a + c > b && b + c > a) {
			double C = a + b + c;
			double p = C / 2;
			double S = sqrt(p * (p - a) * (p - b) * (p - c));
			printf("周长为：%lf 面积为：%lf\n", C, S);
		}
		else 
			printf("输入的三边不能构成三角形！");
		return 0;
	}
	```
	这里用到了math.h库函数：sqrt(参数:欲开方的数)返回值:开方结果，对于函数的具体内容，在后文讲解。
=== "C++"
	```cpp
	#include <iostream>
	#include <cmath>
	using namespace std;
	int main() {
		double a, b, c;
		cin >> a >> b >> c;
		if (a + b > c && a + c > b && b + c > a) {
			double C = a + b + c;
			double p = C / 2;
			double S = sqrt(p * (p - a) * (p - b) * (p - c));
			cout << "周长为：" << C << " 面积为：" << S << endl;
		}
		else cout << "输入的三边不能构成三角形！";
		return 0;
	}
	```
	这里用到了cmath库函数：sqrt(参数:欲开方的数)返回值:开方结果，对于函数的具体内容，在后文讲解。

输入形如ax^2+bx+c=0方程的a、b、c的值，输出该方程的解。

=== "C"
	```c
	#include <stdio.h>
	#include <math.h>

	int main() {
		double a, b, c;
		scanf("%lf %lf %lf", &a, &b, &c);
		double delta = b * b - 4 * a * c;
		if (delta > 0) {
			double x1 = (-b + sqrt(delta)) / (2 * a);
			double x2 = (-b - sqrt(delta)) / (2 * a);
			printf("方程有两个不相等的实数根：%lf %lf\n", x1, x2);
		}
		else if (delta == 0) {
			double x = -b / (2 * a);
			printf("方程有两个相等的实数根：%lf\n", x);
		}
		else {
			double r = (-b) / (2 * a);
			double i = sqrt(-delta) / (2 * a);
			printf("方程有两个不相等的复数根：%lf+%lfi %lf-%lfi\n", r, i, r, i);
		}
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	#include <cmath>
	using namespace std;
	int main() {
		double a, b, c;
		cin >> a >> b >> c;
		double delta = b * b - 4 * a * c;
		if (delta > 0) {
			double x1 = (-b + sqrt(delta)) / (2 * a);
			double x2 = (-b - sqrt(delta)) / (2 * a);
			cout << "方程有两个不相等的实数根：" << x1 << " " << x2 << endl;
		}
		else if (delta == 0) {
			double x = -b / (2 * a);
			cout << "方程有两个相等的实数根：" << x << endl;
		}
		else {
			double r = (-b) / (2 * a);
			double i = sqrt(-delta) / (2 * a);
			cout << "方程有两个不相等的复数根：" << r << "+" << i << "i " << r << "-" << i << "i" << endl;
		}
		return 0;
	}
	```

#### switch……case语句

输入分数，输出其等级，规则为：100分为S，90分以上为A，80分以上为B，70分以上为C，60分以上为D，60分以下为E。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		float score;
		scanf("%f", &score);
		switch ((int)score / 10) {
			case 10: printf("S"); break;
			case 9: printf("A"); break;
			case 8: printf("B"); break;
			case 7: printf("C"); break;
			case 6: printf("D"); break;
			case 5:
			case 4:
			case 3:
			case 2:
			case 1:
			case 0: printf("E"); break;
			default: printf("error!");
		}
		printf("\n");
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		float score;
		cin >> score;
		switch (int(score) / 10) {
			case 10:cout << "S"; break;
			case 9:cout << "A"; break;
			case 8:cout << "B"; break;
			case 7:cout << "C"; break;
			case 6:cout << "D";break;
			case 5:
			case 4:
			case 3:
			case 2:
			case 1:
			case 0:cout << "E"; break;
			default:cout << "error!";
		}
		cout << endl;
		return 0;
	}
	```

```cpp title="switch语法"
条件语句（switch）：
    switch(表达式){
		case 常量表达式1:语句1
		case 常量表达式2:语句2
		......
		case 常量表达式n:语句n
		......
		*default:语句D*
	}
```

值得注意的是，switch语句的每一个case子句为入口点，并不能作为上一个入口点的结束，因而需要使用break语句进行分离，一般来说，存在以下等价关系：

```cpp title="if和switch关系"
switch(a){
	case b1:语句c1;
	case b2:语句c2;
}
等价于
if(a==b1){语句c1;语句c2;}
if(a==b2)语句c2;

switch(a){
	case b1:语句c1;break;
	case b2:语句c2;
}
等价于
if(a==b1)语句c1;
if(a==b2)语句c2;

switch(a){
	case b1:
	case b2:语句c;
}
等价于
if(a==b1||a==b2)语句c;
```

输入简单的两数加减乘除的运算式，输出运算结果。例如输入2+4，输出6。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		double x, y;
		char z;
		printf("请输入简单的四则运算算式：");
		scanf("%lf %c %lf", &x, &z, &y);
		switch (z) {
			case '+': printf("%lf+%lf=%lf\n", x, y, x + y); break;
			case '-': printf("%lf-%lf=%lf\n", x, y, x - y); break;
			case '*': printf("%lf*%lf=%lf\n", x, y, x * y); break;
			case '/':
				if (y == 0) {
					printf("除数不能为零！\n");
				} else {
					printf("%lf/%lf=%lf\n", x, y, x / y);
				}
				break;
		}
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main()
	{
		double x, y;
		char z;
		cout << "请输入简单的四则运算算式：";
		cin >> x >> z >> y;
		switch (z) {
		case '+':cout << x << "+" << y << "=" << x + y << endl; break;
		case '-':cout << x << "-" << y << "=" << x - y << endl; break;
		case '*':cout << x << "*" << y << "=" << x * y << endl; break;
		case '/':
			if (y == 0) {
				cout << "除数不能为零！" << endl;
			}
			else {
				cout << x << "/" << y << "=" << x / y << endl;
			}
			break;
		}
		return 0;
	}
	```

输入年，月，输出对应天数。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int year, month, day;
		scanf("%d %d", &year, &month);
		switch (month) {
			case 1:
			case 3:
			case 5:
			case 7:
			case 8:
			case 10:
			case 12:
				printf("31");
				break;
			case 4:
			case 6:
			case 9:
			case 11:
				printf("30");
				break;
			case 2:
				if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
					printf("29");
				else
					printf("28");
				break;
			default:
				printf("error");
		}
		printf("\n");
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		int year, month, day;
		cin >> year >> month;
		switch (month) {
			case 1:
			case 3:
			case 5:
			case 7:
			case 8:
			case 10:
			case 12:
				cout << "31";
				break;
			case 4:
			case 6:
			case 9:
			case 11:
				cout << "30";
				break;
			case 2:
				if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)cout << "29";
				else cout << "28";
				break;
			default:
				cout << "error";
		}
		cout << endl;
		return 0;
	}
	```

### 循环结构

#### while和do……while语句

输入一个正整数，将该数倒序输出。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int num;
		scanf("%d", &num);
		while (num) { // 等价于 num != 0
			printf("%d", num % 10);
			num /= 10;
		}
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		int num;
		cin >> num;
		while (num) {//等价于num!=0
			cout << num % 10;
			num /= 10;
		}
		return 0;
	}
	```

```cpp title="while语法"
循环语句（while）：
    while(循环条件表达式){
        循环体语句
    }
    另一种特殊形式：
    do{
        循环体语句
    }while(循环条件表达式)
    do while和while效果一样，只不过do while是先运行一次循环体，再进行判断循环条件进行循环
```

输入若干正数，以输入-1表示输入结束，输出其最大值和最小值。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int max, min, num;
		scanf("%d", &num);
		max = min = num;
		while (num != -1) {
			if (max < num)
				max = num;
			if (min > num)
				min = num;
			scanf("%d", &num);
		}
		printf("max=%d min=%d", max, min);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		int max, min, num;
		cin >> num;
		max = min = num;
		while (num != -1) {
			if (max < num)max = num;
			if (min > num)min = num;
			cin >> num;
		}
		cout << "max=" << max << " min=" << min;
		return 0;
	}
	```
	
#### for语句

输入n，输出从1到n的和。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int n, s = 0;
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
			s += i;
		printf("%d", s);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		int n, s = 0;
		cin >> n;
		for (int i = 1; i <= n; i++)s += i;
		cout << s;
		return 0;
	}
	```

```cpp title="for语法"
循环语句（for）：
    for(表达式1;表达式2;表达式3){
        循环体语句
    }
    等价于：
    表达式1;
    while(表达式2){
        循环体语句
        表达式3;
    }
```
习惯上，for循环的表达式1作循环变量的定义初始化语句，表达式2作循环条件语句，表达式3作循环变量变化语句，这只是习惯用法，并非是严格定义的，且三个表达式都可以任意省略。

输入n，输出n!。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int n, s = 1;
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
			s *= i;
		printf("%d", s);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		int n, s = 1;
		cin >> n;
		for (int i = 1; i <= n; i++)s *= i;
		cout << s;
		return 0;
	}
	```
累加变量应初始化为0，累积变量应初始化为1；while循环适用于不确定循环次数或未知循环次数的情况，for循环适用于确定循环次数，即已知循环次数的情况。while循环和for循环在一定程度上可以互换。  
永续循环又称为死循环，是指永不停息地运行的循环，如while(1)就是一个常用的永续循环，如果在调试程序过程中，结果迟迟没有输出，那么说明进入了死循环，应当检查循环语句。对于有形如永续循环的语句，不一定会进行永续循环，例如：

```cpp title="C/C++"
int i = 1;
while(1){
	if(i==10)break;
	i++;
}
```

输出ASCII码表。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		printf("ASCII码表（可见字符）\n");
		for (int i = 33; i < 127; i++) {
			printf("%d\t%c\t", i, (char)i);
			if (i % 8 == 0)
				printf("\n");
		}
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		cout << "ASCII码表（可见字符）" << endl;
		for (int i = 33; i < 127; i++) {
			cout << i << "\t" << char(i) << "\t";
			if (i % 8 == 0)cout << endl;
		}
		return 0;
	}
	```

输出九九乘法表。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		printf("九九乘法表\n");
		for (int i = 1; i <= 9; i++) {
			for (int j = 1; j <= i; j++)
				printf("%d*%d=%d\t", i, j, i * j);
			printf("\n");
		}
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		cout << "九九乘法表" << endl;
		for (int i = 1; i <= 9; i++) {
			for (int j = 1; j <= i; j++)cout << i << "*" << j << "=" << i * j << "\t";
			cout << endl;
		}
		return 0;
	}
	```

输入n，输出n行菱形图案，即n越大菱形越大。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int row;
		int i, j, n;
		printf("请输入行数：");
		scanf("%d", &row);
		if (row % 2 != 0)
			n = row / 2 + 1;
		else
			n = row / 2;
		for (i = 1; i <= n; i++) {
			for (j = 1; j <= n - i; j++)
				printf(" ");
			for (j = 1; j <= 2 * i - 1; j++)
				printf("*");
			printf("\n");
		}
		if (row % 2 == 0) {
			for (i = 1; i <= n; i++) {
				for (j = 1; j <= i - 1; j++)
					printf(" ");
				for (j = 1; j <= row - 2 * i + 1; j++)
					printf("*");
				printf("\n");
			}
		} else if (row % 2 != 0) {
			for (i = 1; i <= n - 1; i++) {
				for (j = 1; j <= i; j++)
					printf(" ");
				for (j = 1; j <= row - 2 * i; j++)
					printf("*");
				printf("\n");
			}
		}
		return 0;
	}
	```
=== "C++"
	```cpp
	#include<iostream>
	using namespace std;
	int main() {
		int row;
		int i, j, n;
		cout << "请输入行数：";
		cin >> row;
		if (row % 2 != 0)
			n = row / 2 + 1;
		else
			n = row / 2;
		for (i = 1; i <= n; i++) {
			for (j = 1; j <= n - i; j++)
				cout << ' ';
			for (j = 1; j <= 2 * i - 1; j++)
				cout << '*';
			cout << endl;
		}
		if (row%2==0) {
			for (i = 1; i <= n; i++) {
				for (j = 1; j <= i-1; j++)
					cout << ' ';
				for (j = 1; j <= row - 2 *i+1; j++)
					cout << '*';
				cout << endl;
			}
		}
		else if (row%2!=0) {
			for (i = 1; i <= n - 1; i++) {
				for (j = 1; j <= i; j++)
					cout << ' ';
				for (j = 1; j <= row - 2 * i; j++)
					cout << '*';
				cout << endl;
			}
		}

		return 0;
	}
	```

### 控制转向语句

|语句|作用|说明|
|-|-|-|
|break|结束（全部）循环/结束case子句|仅可用于结束for/while循环或者分离switch的case子句|
|continue|结束本次循环|不执行之后的循环体内容，直接继续下一次循环|
|goto|跳转到指定标号|标号属于标识符，在需跳转的位置以标识符加冒号的形式使用|

!!! warning "注意"
	不推荐使用goto，因为其会破坏顺序结构，使得代码的可读性变差。

使用牛顿迭代法解一元方程ax\^3+bx\^2+cx+d=0在x=xa附近的根，精度为e，输入a，b，c，d，e，xa，输出根。

=== "C"
	```c
	#include <stdio.h>
	#include <math.h>

	int main() {
		double a, b, c, d, e, xa, x, f, fa;
		scanf("%lf %lf %lf %lf %lf %lf", &a, &b, &c, &d, &e, &xa);
		do {
			x = xa;
			f = a * x * x * x + b * x * x + c * x + d;
			fa = 3 * a * x * x + 2 * b * x + c;
			xa = x - f / fa;
		} while (fabs(xa - x) >= e);
		printf("%lf", xa);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include<iostream>
	#include<cmath>
	using namespace std;
	int main() {
		double a, b, c, d, e, xa, x, f, fa;
		cin >> a >> b >> c >> d >> e >> xa;
		do {
			x = xa;
			f = a * x * x * x + b * x * x + c * x + d;
			fa = 3 * a * x * x + 2 * b * x + c;
			xa = x - f / fa;
		} while (fabs(xa - x) >= e);
		cout << xa;
		return 0;
	}
	```

现有公鸡5元1只，母鸡3元1只，小鸡1元3只，如果用百元买百鸡，有多少种购鸡方案？

=== "C"
	```c
	#include <stdio.h>

	int main() {
		printf("公鸡\t母鸡\t小鸡\n");
		for (int i = 1; i < 20; i++)
			for (int j = 1; j < 33; j++)
				for (int k = 1; k < 100; k++)
					if (i + j + k == 100 && 5 * i + 3 * j + k / 3.0 == 100)
						printf("%d\t%d\t%d\n", i, j, k);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include<iostream>
	using namespace std;
	int main() {
		cout << "公鸡\t母鸡\t小鸡" << endl;
		for (int i = 1; i < 20; i++)
			for (int j = 1; j < 33; j++)
				for (int k = 1; k < 100; k++)
					if (i + j + k == 100 && 5 * i + 3 * j + k / 3.0 == 100)
						cout << i << "\t" << j << "\t" << k << endl;
		return 0;
	}
	```

## 函数

### 函数的定义与调用

解决问题的一种方法就可以视为一种函数，一个程序是由众多函数构成的。在一个程序中，解决较小问题的功能模块使用函数实现，对于代码的重用和可读性能够大幅提升，具有很强的应用能力，是大部分程序语言不可或缺的一部分。

使用函数实现乘方运算，输入底数和幂，输出结果。

=== "C"
	```c
	#include<stdio.h>

	double power(double a, int n) {
		double s = 1;
		for (int i = 1; i <= n; i++)
			s *= a;
		return s;
	}

	int main() {
		double b;
		int m;
		scanf("%lf %d", &b, &m);
		printf("%lf", power(b, m));
		return 0;
	}
	```
=== "C++"
	```cpp
	#include<iostream>
	using namespace std;
	double power(double a, int n) {
		double s = 1;
		for (int i = 1; i <= n; i++)s *= a;
		return s;
	}
	int main() {
		double b;
		int m;
		cin >> b >> m;
		cout << power(b, m);
		return 0;
	}
	```

```cpp title="函数语法"
函数定义语句：
类型名 函数名(*形式参数列表*){
    函数体
}
函数调用语句：
函数名(*实际参数列表*)
```
函数不一定有参数，也不一定有返回值，都是可选的。把没有参数的函数称为无参函数，对应地，把有参数的函数称为有参函数，类型名和变量的类型相似，都整数型、字符型等等，函数的类型名实际上指的是返回值的类型，对于没有返回值的函数，使用空类型void指定。同时值得注意的是，函数的返回值的个数没有限制，零个或多个均可，但是函数被调用时有效的最多一个，这时因为函数的返回值不仅仅是进行数值的返回，而且还标志着函数的结束，所以说，一个函数的结束标志除了函数体运行完成（对于无返回值函数），还一个是进行了数值的返回（对于有返回值函数）。  

函数名和变量名类似，也是自行定义的标识符。我们把类型名和函数名称为函数原型，即把函数体去掉后的语句（形参列表可以省略），我们可以用函数原型进行函数的声明。函数声明操作有另一种叫法是提升，把后面的函数提升到了前面，这是从形象角度定义的；而声明是在编译时告诉编译器确实有这么个函数，在前面声明一下，这是从实质角度定义的。

使用函数实现对给定a，b，c三边进行是否该三角形为直角三角形进行判断，在程序中输入三边，输出是否为直角三角形。

=== "C"
	```c
	#include<stdio.h>

	int RA_triangle(double a, double b, double c);

	int main() {
		double x, y, z;
		scanf("%lf %lf %lf", &x, &y, &z);
		printf("%d", RA_triangle(x, y, z));
		return 0;
	}

	int RA_triangle(double a, double b, double c) {
		if (a * a + b * b == c * c || a * a + c * c == b * b || b * b + c * c == a * a)
			return 1;
		return 0;
	}
	```
=== "C++"
	```cpp
	#include<iostream>
	using namespace std;
	bool RA_triangle(double a, double b, double c);
	int main() {
		double x, y, z;
		cin >> x >> y >> z;
		cout << RA_triangle(x, y, z);
	}
	bool RA_triangle(double a, double b, double c) {
		if (a * a + b * b == c * c || a * a + c * c == b * b || b * b + c * c == a * a)return true;
		return false;
	}
	```

```cpp title="函数语法"
函数声明语句：
类型名 函数名(*形式参数列表*)
注意声明语句也可以将形参列表的参数名的类型保留，标识符省略。
```

函数调用时可以独立成一个语句，不使用其返回值，也可以类似变量那样，出现在表达式中，还可以作为函数的参数。在一个函数中不能定义函数，但在函数中可以调用另一个函数，也可以调用自己，对于有返回值的有参函数而是而言，自己调用自己的情况被称为递归，将在之后讲到。  

在函数传递参数时，有三种传递方式：值传递，地址传递和引用传递。之前的案例使用的都是值传递，这种传递方式形参不能影响实参；而地址传递和引用传递形参都能影响实参，将在指针中讲到。  

对于函数的参数，可以设置默认值，但由于形参和实参的结合时从右向左进行的，所以设置默认的形参需要置于参数列表的最右方，否则会出错。

计算机程序有时使用循环实现延时，请编写一个延时函数，设置默认值，并在主函数中调用它。

=== "C"
	```c
	#include<stdio.h>

	void delay(double loop) {
		for (int i = 0; i < loop; i++);
	}

	int main() {
		double loop;
		printf("输入循环次数，如果使用默认值，请输入0：");
		scanf("%lf", &loop);
		printf("开始延时\n");
		if (loop)
			delay(loop);
		else
			delay(1000);
		printf("结束延时\n");
		return 0;
	}
	```
=== "C++"
	```cpp
	#include<iostream>
	using namespace std;
	void delay(double loop = 1000) {
		for (int i = 0; i < loop; i++);
	}
	int main() {
		double loop;
		cout << "输入循环次数，如果使用默认值，请输入0：";
		cin >> loop;
		cout << "开始延时" << endl;
		if (loop)delay(loop);
		else delay();
		cout << "结束延时" << endl;
		return 0;
	}
	```

除了用户可以自定义函数外，我们还可以使用开发环境预定义的函数，即库函数，C++有丰富的内置库，例如cmath等。具体内容将在后文讲到。  

有一种特殊的函数，相当于直接把函数体嵌入到引用处中，称为内置函数，也称内联函数、内嵌函数。一般来说这种函数是为了减少内存开销的提高效率的方法，定义方法和一般函数相同，只需要在首部加上关键字inline就可以了。注意内置函数不能有复杂的程序控制语句且不能是递归函数。

### 遍历与递归

遍历属于循环中的的概念，可以理解为从遍历结构中逐一提取元素，放在循环变量中，对于所提取的每个元素执行一次语句块。也就是说，遍历循环的次数是给定的，因而for就被称为遍历循环语句，对应地，while被称为条件循环语句。

显然，遍历循环时“公平”的，因为，轮到谁谁就会被先执行，遵循“先来后到”原则。而递归函数遵循“后来先到”原则，当一个函数被调用时，系统会为该函数的局部变量、参数和返回地址分配内存空间，这些信息会被保存在函数调用栈中。当函数执行完成后，相关的内存空间会被释放。在递归函数中，每次调用都会导致新的函数调用栈帧被压入栈中。出栈指的是从栈顶移除一个元素。当执行出栈操作时，栈的大小减小，而被移除的元素就是栈顶的元素。这通常伴随着返回被移除元素的值或执行与该元素相关的操作，也称为弹栈。


请试用递归函数解决汉诺塔问题，输入金片数，输出操作过程。

=== "C"
	```c
	#include<stdio.h>

	void hanoi(int n, char x, char y, char z) {
		if (n == 1)
			printf("%c->%c\n", x, z);
		else {
			hanoi(n - 1, x, z, y);
			printf("%c->%c\n", x, z);
			hanoi(n - 1, y, x, z);
		}
	}

	int main() {
		int n;
		scanf("%d", &n);
		hanoi(n, 'a', 'b', 'c');
		return 0;
	}
	```
=== "C++"
	```cpp
	#include<iostream>
	using namespace std;
	void hanoi(int n = 3, char x = 'a', char y = 'b', char z = 'c') {
		if (n == 1)cout << x << "->" << z << endl;
		else {
			hanoi(n - 1, x, z, y);
			cout << x << "->" << z << endl;
			hanoi(n - 1, y, x, z);
		}
	}
	int main() {
		int n;
		cin >> n;
		hanoi(n);
		return 0;
	}
	```

假设有一种粒子能进行分裂，分裂后的两个新粒子平分原粒子具有的能量，但也会耗散一部分，这部分能量占总能量的比率称为耗散率。输入粒子分裂次数，初始能量和耗散率，输出粒子分裂结束后一个粒子所具有的能量。

=== "C"
	```c
	#include<stdio.h>

	double ed(double e, double k) {
		return (e - e * k) / 2;
	}

	double boom(int n, double e, double k) {
		if (n <= 1)
			return ed(e, k);
		return boom(n - 1, ed(e, k), k);
	}

	int main() {
		int n;
		double e, k;
		scanf("%d %lf %lf", &n, &e, &k);
		printf("%lf", boom(n, e, k));
		return 0;
	}
	```
=== "C++"
	```cpp
	#include<iostream>
	using namespace std;
	inline double ed(double e, double k) {
		return (e - e * k) / 2;
	}
	double boom(int n, double e, double k) {
		if (n <= 1)return ed(e, k);
		return boom(n - 1, ed(e, k), k);
	}
	int main() {
		int n;
		double e, k;
		cin >> n >> e >> k;
		cout << boom(n, e, k);
		return 0;
	}
	```

### 作用域与生存期

变量属性除数据类型属性外，还有空间和时间两大属性。空间属性被称为作用域。一个变量有效的作用范围，即是其作用域。根据作用域进行对变量的分类，可以分为局部变量和全局变量。局部变量是定义在函数或者程序块里的变量，其只在本函数体内或程序块内有效，因而不同函数和程序块内的变量名并不冲突，所以局部变量的作用域是在定义其的函数或程序块内。 

全局变量又称外部变量，是定义在函数以外的变量，对整个源代码文件都有效，作用域广，因而每个函数里的代码都可以对全局变量产生影响。但值得注意的是，当外域局部变量和内域局部变量重名时，优先使用内域局部变量，当局部变量和全局变量重名时，优先使用局部变量，若想要使用全局变量，需要使用运算符::指定全局变量即可。  

时间属性被称为生存期，即变量在内存中存在的时间，如果未经特殊定义，局部变量的生存期会伴随着函数和程序块的运行结束而结束，而全局变量生存期是整个程序，程序运行结束，全局变量也就被销毁。存储类型分为动态存储方式和静态存储方式，相关说明如下：

|存储方式|名称|声明关键字|说明|
|-|-|-|-|
|动态|自动变量|auto|存储在动态数据存储区，可省略，默认值|
|动态|寄存器变量|register|存储在CPU的通用寄存器中，读写速度更快，但不宜定义过多|
|静态|外部变量|extern|即全局变量，可以被本文件或着在其它文件中引用，可省略，默认值|
|静态|静态变量|static|静态局部变量能扩展其生存期到程序结束，不会因为函数或者程序块运行结束而被销毁；静态全局变量能限制其作用域只在本文件内，而不能被其它文件引用|


运行前推测下程序的输出结果，并试着运行验证推测是否正确。

=== "C"
	```c
	#include <stdio.h>

	int a = 4;
	static int b = 2;

	int wcnb(int d) {
		static int nb = 3;
		nb++;
		return d - nb;
	}

	int main() {
		int a = 6;
		for (int e = 0; e <= a; e += b) {
			a--;
			::a++;
			int b = wcnb(a);
			{
				int d = b + ::b;
				auto c = e * e;
				printf("%d %d %d %d %d\n", a, b, c, d, e);
			}
			printf("%d %d\n", ::a, ::b);
		}
		return 0;
	}
	```
=== "C++"
	```cpp
	#include<iostream>
	using namespace std;
	int a = 4;
	static int b = 2;
	int wcnb(int d) {
		static int nb = 3;
		nb++;
		return d - nb;
	}
	int main() {
		int a = 6;
		for (int e = 0; e <= a; e += b) {
			a--;
			::a++;
			int b = wcnb(a);
			{
				int d = b + ::b;
				auto c = e * e;
				cout << a << " " << b << " " << c << " " << d << " " << e << endl;
			}
			cout << ::a << " " << ::b << endl;
		}
		return 0;
	}
	```
函数也可以分为两类：内部函数和外部函数。内部函数使用static关键字，只能在本文件内调用；外部函数也可以在其它文件调用，可省略，默认值。

### 编译预处理

编译预处理是指在编译前，对代码进行的提前处理，用于提高开发效率，便于程序的调试。注意预处理语句不是C++语句，语法也不遵循C++的语法。预处理主要有三种：宏定义、文件包含和条件编译，语法如下：

```cpp title="编译预处理"
不带参数的宏定义：
#define 宏名 字符串
带参数的宏定义：
#define 宏名(参数列表) 字符串
进行宏定义后，编译时遇到与宏名相同的词会被直接替换为字符串。注意宏定义不应该被滥用，尽可能地少使用宏定义。

文件包含：
#include <文件名>
#include "文件名"
文件包含是将别的文件的代码直接替换进来，以上两句功能相同，用法上略有区别。第一个是对库进行引用，且不能带路径；第二个是对用户文件或者库进行引用，可以使用路径。

条件编译：
条件编译有以下三种形式：
#ifdef 标识符
程序片段1
#else
程序片段2
#endif

#ifndef 标识符
程序片段1
#else
程序片段2
#endif

#if 标识符
程序片段1
#else
程序片段2
#endif
```

### 命名法

命名法是编程中非常重要的一环，它直接影响到代码的可读性、可维护性和可扩展性。一个好的命名法可以使代码更加清晰易懂，降低出错的概率，提高代码的效率和可靠性。本文将介绍常见的命名法，以及如何选择合适的命名。

#### 常用命名法

1. 驼峰命名法（Camel Case）是一种常用的命名法，它将单词首字母大写，其余字母小写，由于其看着两边是小写字母，中间是大写字母，像是一个驼峰，故得此名。如：firstName、lastName、emailAddress等。
2. 帕斯卡命名法（Pascal Case）也叫大驼峰命名法，它和驼峰命名法类似，但是首字母也要大写，如：FirstName、LastName、EmailAddress等。
3. 下划线命名法（Snake Case）是将单词用下划线连接起来，每个单词的字母都小写，如：first_name、last_name、email_address等。
4. 匈牙利命名法（Hungarian Notation）是由微软公司提出的一种命名法，它在变量名前加上一个小写字母前缀，表示变量的数据类型，如：strFirstName、iAge、bIsMale等。

#### 命名基本原则

1. 名称应该能够清晰地描述变量的含义和作用，避免使用过于简单的变量名，如：a、b、c等，这样不利于代码的阅读和维护。
2. 名称应该尽量短小，但是又不能过于简略，应该保证足够描述变量的含义和作用。
3. 名称应该避免使用数字和特殊字符，因为它们会让变量名变得难以理解和记忆。
4. 名称应该使用正确的命名法，可以使代码更加规范和易读。

## 数组与指针

### 数组

对于少量的数据，使用几个变量就可以表示和操作，但对于大量的数据，重复定义大量个变量是非常不现实而繁杂的，因而，引用了数组作为大量数据的存储方法，对数组可以进行访问和操作，下面是对一个数组的一些基础操作。

#### 一维数组

输入n（n < 50），输出斐波那契数列的前n个。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int num[50] = {1, 1}, n;
		scanf("%d", &n);
		for (int i = 2; i < n; i++)
			num[i] = num[i - 1] + num[i - 2];
		for (int i = 0; i < n; i++)
			printf("%d ", num[i]);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		int num[50]{1,1}, n;
		cin >> n;
		for (int i = 2; i < n; i++)num[i] = num[i - 1] + num[i - 2];
		for (int i = 0; i < n; i++)cout << num[i] << " ";
		return 0;
	}
	```

```cpp title="一维数组"
一维数组的定义：
类型符 数组名[常量表达式]
（方括号里的常量表达式是指数组内元素个数，注意不能使用变量指定数组个数）

一维数组的引用：
数组名[下标]
（注意下标是从0开始计算的，也就是说有n个元素的数组，最后一个元素的下标为n-1）

一维数组的初始化：
类型符 数组名[常量表达式]{*元素列表*}
类型符 数组名[*常量表达式*]{元素列表}
（花括号里的列表用逗号隔开，按照顺序依次赋值给数组的下标为0、1、2……的元素，元素列表是可选的，也就是说，可以只写一个花括号，而省略掉元素列表，也可以只写部分元素）
例如：
int x1[6]{1,2,3,4,5,6} //合法，每个元素都被显式地初始化
int x2[10]{5,4,8,1}    //合法，前4个元素被显式初始化，后6个元素默认为0
int x3[10]{}           //合法，每个元素都被隐式地初始化，默认为0
int x4[]{1,5,4,7}      //合法，元素个数被自动设定为了4
int x5[]{}             //非法，数组元素个数和元素列表不能同时省略
int x6[5]{1,5,4,8,7,4} //非法，元素列表的元素个数超过了指定元素个数

一维数组的存储：
数组元素地址=数组起始地址+元素下标*数组类型字节数
```
值得注意的是，数组不能直接进行输入或者输出，例如`int a[10];cin>>a;`这种写法是错误的，其数组名实质是其首个元素的指针位置。

#### 二维数组

输入n（n < 20），输出杨辉三角的前n行。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int num[20][20], n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			num[i][i] = num[i][0] = 1;
			for (int j = 1; j < i; j++)
				num[i][j] = num[i - 1][j - 1] + num[i - 1][j];
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= i; j++)
				printf("%d ", num[i][j]);
			printf("\n");
		}
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		int num[20][20], n;
		cin >> n;
		for (int i = 0; i < n; i++) {
			num[i][i] = num[i][0] = 1;
			for (int j = 1; j < i; j++)num[i][j] = num[i - 1][j - 1] + num[i - 1][j];
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= i; j++)cout << num[i][j] << " ";
			cout << endl;
		}
		return 0;
	}
	```

```cpp title="二维数组"
二维数组的定义：
类型符 数组名[常量表达式1][常量表达式2]
（方括号里的常量表达式1是表示行数，常量表达式2表示列数）

二维数组的引用：
数组名[下标1][下标2]
（下标1指定行，下标2指定列）

二维数组的初始化：
类型符 数组名[常量表达式1][常量表达式2]{*元素列表*}
类型符 数组名[*常量表达式1*][常量表达式2]{元素列表}
（需要注意的是常量表达式2无论在何种情况下都不可省略）
例如：
int x1[3][2]{1,2,3,4,5,6}    //合法，每个元素都被显式地初始化
int x2[3][2]{{1,2,3},{4,5,6}}//合法，可以嵌套使用花括号严格指定行列
int x3[3][2]{5,4,8,1}        //合法，前4个元素被显式初始化，后2个元素默认为0
int x4[3][2]{}               //合法，每个元素都被隐式地初始化，默认为0
int x5[][2]{1,5,4,7}         //合法，元素个数被自动设定为了4
int x6[3][2]{{},{4,5}}       //合法，严格指定行列初始化时，可以部分初始化
int x7[][]{1,5,8,7}          //非法，常量表达式2不可省略
int x8[2][2]{1,5,4,8,7,4}    //非法，元素列表的元素个数超过了指定元素个数

二维数组的存储：
数组元素地址=数组起始地址+（元素下标1*4+元素下标2）*数组类型字节数
```

二维数组可以看作是特殊的一维数组，而它的成分又是一个数组。二维数组可以推广到多维数组，例如三维、四维等。

输入n（n < 20）个数据，再输入f，从n个数据中寻找和f相等的元素，并返回有几个相等的元素。请使用函数实现。

=== "C"
	```c
	#include <stdio.h>

	int lookup(int num[], int n, int f) {
		int s = 0;
		for (int i = 0; i < n; i++)
			if (num[i] == f)
				s++;
		return s;
	}

	int main() {
		int num[20], n, f;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &num[i]);
		scanf("%d", &f);
		printf("%d", lookup(num, n, f));
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int lookup(int num[], int n, int f) {
		int s = 0;
		for (int i = 0; i < n; i++)if (num[i] == f)s++;
		return s;
	}
	int main() {
		int num[20], n, f;
		cin >> n;
		for (int i = 0; i < n; i++)cin >> num[i];
		cin >> f;
		cout << lookup(num, n, f);
		return 0;
	}
	```

当数组作为函数参数时，只需将数组名写入即可，因为其数组名就是数组第一个元素的地址，其等价于`&num[0]`（&是取地址运算，将在后文讲到）。

输入n（n < 20）个数据，再输入f和t，从n个数据中寻找和f相等的元素，全部修改为t。请使用函数实现。

=== "C"
	```c
	#include <stdio.h>

	void mod(int num[], int n, int f, int t) {
		for (int i = 0; i < n; i++)
			if (num[i] == f)
				num[i] = t;
	}

	int main() {
		int num[20], n, f, t;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &num[i]);
		scanf("%d %d", &f, &t);
		mod(num, n, f, t);
		for (int i = 0; i < n; i++)
			printf("%d ", num[i]);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	void mod(int num[], int n, int f, int t) {
		for (int i = 0; i < n; i++)if (num[i] == f)num[i] = t;
	}
	int main() {
		int num[20], n, f, t;
		cin >> n;
		for (int i = 0; i < n; i++)cin >> num[i];
		cin >> f >> t;
		mod(num, n, f, t);
		for (int i = 0; i < n; i++)cout << num[i] << " ";
		return 0;
	}
	```
如果你仔细观察，你会发现数组作函数参数传递时，对于形参的操作会影响到实参，而我们之前对于一般变量作函数参数传递时，对于形参的操作却不会影响实参，这种方式称为值传递。而数组名我们说过是第一个元素的地址，即数组作函数参数时的传递方式称为地址传递。值传递具有形实分离的效果，而地址传递具有形实一体的效果。但如何获得一般变量的地址，也实现和数组一样的传递方式呢？将在后面讲到。

### 指针

如果想要获取一个变量的地址，我们可以使用取地址运算符&，对于变量a，&a就是其地址，但是如果想要把这个地址存储起来，我们可以使用一种专门存储地址的变量，即指针变量。例如对于`int a`，可以取其地址`int *p=&a`。

输入两个数，交换这两个数并输出。使用函数实现。

=== "C"
	```c
	#include <stdio.h>

	void swap(int* a, int* b) {
		int t = *a;
		*a = *b;
		*b = t;
	}

	int main() {
		int a, b;
		scanf("%d %d", &a, &b);
		swap(&a, &b);
		printf("%d %d", a, b);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	void swap(int* a, int* b) {
		int t = *a;
		*a = *b;
		*b = t;
	}
	int main() {
		int a, b;
		cin >> a >> b;
		swap(&a, &b);
		cout << a << " " << b;
		return 0;
	}
	```

```cpp title="指针语法"
指针变量的定义：
类型标识符 *标识符
指针变量的引用：
标识符
```

如果没有使用指针，函数不会产生应有的效果，只会在其作用域有效。指针很好的解决了这一问题。但是，有关指针的一些问题值得注意：

1. 指针不能被直接输入，但可以输出，即对于int *p=&a，cout << p是合法的而cin >> p是非法的。
2. 指针必须现指向一个变量，即初始化后才能进行使用，例如int \*p;cin >> \*p是非法的。
3. 指针运算符\*没有严格的格式要求，即int \* p、int\* p和int \*p是等价的。

```cpp title="指针使用"
int a = 2, *p = &a; //合法
*p = a;             //合法
p = a;              //非法
p = &a;             //合法
*p = &a;            //非法
int b = *p;         //合法
```


\*称为间址运算符，又成为解引用运算符，在定义时起到指针变量的标识符，在调用时起到指向地址的所对应的量，而指针变量被定义后，如果不带\*表示地址，带\*表示地址对应的量。  

指针可以通过加、减、自增和自减运算进行移动，例如对于int型指针p的p++是指向下移动一个整型变量的位置，若p初值为5000，则移动后的值为5000+1\*4=5008。两个指针变量相加减没有实际意义。  

指针可以进行比较，低地址端的存储单元小于高地址端的存储单元。

定义两个整型变量，输出其地址较小的变量的地址，使用函数实现。

=== "C"
	```c
	#include <stdio.h>

	int* p(int* x, int* y) {
		return x < y ? x : y;
	}

	int main() {
		int a = 3, b = 2;
		printf("%p", p(&a, &b));
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	inline int* p(int* x, int* y) {
		return x < y ? x : y;
	}
	int main() {
		int a = 3, b = 2;
		cout << p(&a, &b);
		return 0;
	}
	```

当指针变量作函数参数和返回值时也是类似的方法，使用*作为指针的标志符，而在调用时不需要再使用标志符，和指针变量的方法类似。

使用指向函数的指针实现指数运算。输入底数和指数，输出结果。

=== "C"
	```c
	#include <stdio.h>

	double power(double a, int n) {
		double s = 1;
		for (int i = 1; i <= n; i++)
			s *= a;
		return s;
	}

	int main() {
		double a, (*p)(double, int);
		p = power;
		int n;
		scanf("%lf %d", &a, &n);
		printf("%lf", p(a, n));
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	double power(double a, int n) {
		double s = 1;
		for (int i = 1; i <= n; i++)s *= a;
		return s;
	}
	int main() {
		double a, (*p)(double, int);
		p = power;
		int n;
		cin >> a >> n;
		cout << p(a, n);
		return 0;
	}
	```

```cpp title="指针与函数"
指向函数的指针的定义：
类型标识符 (*指针变量名)(形参类型表)
指向函数的指针的引用：
指针变量 (实参表)
指向函数的指针的赋值（初始化）：
指针变量 = 函数名
```

### 字符串

顾名思义，字符串是指一串字符，按照以往的内容，没有专门的类型表示字符串，char只能表示单个字符，不难想到，可以使用字符数组来表示一串字符。C/C++中可以使用这种方法，但为了表示一串字符的结束，使用结束表示字符（也称终止符）“/0”来标识。

输入一串字符（长度不超过100），仅保留其中的大小写字母，去除数字和符号，然后输出操作后的字符串。

=== "C"
	```c
	#include <stdio.h>

	void dalbet(char *s) {
		int i, j;
		for (i = j = 0; s[i]; i++)
			if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z'))
				s[j++] = s[i];
		s[j] = '\0';
	}

	int main() {
		char s[100];
		scanf("%s", s);
		dalbet(&s[0]);
		printf("%s", s);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	void dalbet(char *s) {
		int i, j;
		for (i = j = 0; s[i]; i++)
			if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z'))s[j++] = s[i];
		s[j] = '\0';
	}
	int main() {
		char s[100];
		cin >> s;
		dalbet(&s[0]);
		cout << s;
		return 0;
	}
	```

```cpp title="字符串"
字符数组定义和初始化：
基本的：
char s[6] = {'c','p','p','n','b','\0'}; //完全按照一般数组的方法定义
char s[] = {'c','p','p','n','b','\0'};  //当数组元素被初始化是元素数量可以省略
字符串独有的：
char s[6] = {"cppnb"}; //可以直接双引号加花括号初始化，这样做系统自动会在末尾加上\0，当然也可以认为去加，但一定空间要足够
char s[] = {"cppnb"};  //元素个数也可以省略
char s[] = "cppnb";    //甚至花括号也可以省略
使用指针的：
char *s = "cppnb";
```


=== "C"
	```c title="字符串"
	// 基本的：
	for (int i = 0; i < 5; i++) scanf(" %c", &s[i]); s[5] = '\0';
	for (int i = 0; i < 6; i++) printf("%c", s[i]);
	// 字符串独有的：
	scanf("%s", s);   //这种方式更为方便，会自动补\0
	printf("%s", s);
	```
=== "C++"
	```cpp title="字符串"
	字符数组的输入输出：
	基本的：
	for (int i = 0; i < 5; i++)cin >> s[i];s [5] = '\0';
	for (int i = 0; i < 6; i++)cout << s[i];
	字符串独有的：
	cin >> s;   //这种方式更为方便，会自动补\0
	cout << s;
	```
	其实，除了使用字符数组，有着更为方便的定义方式，即string标识符，但string定义的字符串变量不能像字符数组那样单字符操作，但在不同的场合，使用字符串和使用字符数组各有优劣。使用string标识符前，需先引用头文件，即`#include <string>`。
	```cpp
	字符数组：
	char s[6];
	s = "cppnb"; //非法的
	使用指针的字符数组：
	char *s;
	s = "cppnb"; //合法的
	使用字符串：
	string s;
	s = "cppnb"; //合法的
	```

下面是一些字符串的常用函数（需要引用头文件）：

=== "C"
	|名称|函数名|参数列表|返回值|作用|
	|-|-|-|-|-|
	|连接函数|strcat|目标字符串，\*源字符串缓冲空间值\*，源字符串|0：成功、EINVAL：字符串未初始化、ERANGE：越界|将源字符串连接到目标字符串之后，连接后源字符串的内容不变|
	|直接复制函数|strcpy|目标字符串，\*源字符串缓冲空间值\*，源字符串|0：成功、EINVAL：字符串未初始化、ERANGE：越界|将源字符串复制到目标字符串，连接后源字符串的内容不变，目标字符串被覆盖|
	|指定复制函数|strncpy|目标字符串，目标字符串长度，源字符串，欲拷贝字符数|0：成功、EINVAL：字符串未初始化、ERANGE：越界|将指定字符数的源字符串复制到目标字符串，连接后源字符串的内容不变，目标字符串被覆盖|
	|长度函数|strlen|字符串|字符串长度值|求字符串实际长度（不包括\0）|
	|比较函数|strcmp|字符串1，字符串2|0、正整数、负整数|字符串1和字符串2自左向右逐个字符比较ASCII码，直至出现不同字符或者遇到\0为止。如果字符都相等，则返回0，若字符串1不相等的首个字符小于与字符串2，则返回负数，否则返回正数。实质是返回两字符串不相等的首个字符的ASCII码差值|
	|转大写/小写字母函数|strupr/strlwr|欲要转换的字符串|-|将字符串的小写字母转大写/大写字母转小写|
	|查找函数|strstr|字符串1，字符串2|NULL、字符串2的位置|在字符串1里寻找字符串2，若找到，返回字符串2首次出现的位置，否则返回NULL|
=== "C++"
	|名称|函数名|参数列表|返回值|作用|
	|-|-|-|-|-|
	|连接函数|strcat_s|目标字符串，\*源字符串缓冲空间值\*，源字符串|0：成功、EINVAL：字符串未初始化、ERANGE：越界|将源字符串连接到目标字符串之后，连接后源字符串的内容不变|
	|直接复制函数|strcpy_s|目标字符串，\*源字符串缓冲空间值\*，源字符串|0：成功、EINVAL：字符串未初始化、ERANGE：越界|将源字符串复制到目标字符串，连接后源字符串的内容不变，目标字符串被覆盖|
	|指定复制函数|strncpy_s|目标字符串，目标字符串长度，源字符串，欲拷贝字符数|0：成功、EINVAL：字符串未初始化、ERANGE：越界|将指定字符数的源字符串复制到目标字符串，连接后源字符串的内容不变，目标字符串被覆盖|
	|长度函数|strlen|字符串|字符串长度值|求字符串实际长度（不包括\0）|
	|比较函数|strcmp|字符串1，字符串2|0、正整数、负整数|字符串1和字符串2自左向右逐个字符比较ASCII码，直至出现不同字符或者遇到\0为止。如果字符都相等，则返回0，若字符串1不相等的首个字符小于与字符串2，则返回负数，否则返回正数。实质是返回两字符串不相等的首个字符的ASCII码差值|
	|转大写/小写字母函数|strupr/strlwr|欲要转换的字符串|-|将字符串的小写字母转大写/大写字母转小写|
	|查找函数|strstr|字符串1，字符串2|NULL、字符串2的位置|在字符串1里寻找字符串2，若找到，返回字符串2首次出现的位置，否则返回NULL|

值得注意的是，字符串不能进行相等“==”或不相等“!=”比较，而是使用比较函数进行比较。

输入一串字符（例如一篇文章），输出大写字母、小写字母、数字、符号及空格的数量。

=== "C"
	```c
	#include <stdio.h>
	#include <string.h>

	int upper_s(char str[]) {
		int s = 0;
		for (int i = 0; i < strlen(str); i++)
			if (str[i] >= 'A' && str[i] <= 'Z')
				s++;
		return s;
	}

	int lower_s(char str[]) {
		int s = 0;
		for (int i = 0; i < strlen(str); i++)
			if (str[i] >= 'a' && str[i] <= 'z')
				s++;
		return s;
	}

	int num_s(char str[]) {
		int s = 0;
		for (int i = 0; i < strlen(str); i++)
			if (str[i] >= '0' && str[i] <= '9')
				s++;
		return s;
	}

	int space_s(char str[]) {
		int s = 0;
		for (int i = 0; i < strlen(str); i++)
			if (str[i] == ' ')
				s++;
		return s;
	}

	int other_s(char str[]) {
		return strlen(str) - lower_s(str) - upper_s(str) - num_s(str) - space_s(str);
	}

	int main() {
		char s[100];
		fgets(s, 100, stdin);
		printf("大写字母：%d\n", upper_s(s));
		printf("小写字母：%d\n", lower_s(s));
		printf("数字：%d\n", num_s(s));
		printf("空格：%d\n", space_s(s));
		printf("符号：%d\n", other_s(s));
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	#include <string>
	using namespace std;
	int upper_s(char str[]) {
		int s = 0;
		for (int i = 0; i < strlen(str); i++)if (str[i] >= 'A' && str[i] <= 'Z')s++;
		return s;
	}
	int lower_s(char str[]) {
		int s = 0;
		for (int i = 0; i < strlen(str); i++)if (str[i] >= 'a' && str[i] <= 'z')s++;
		return s;
	}
	int num_s(char str[]) {
		int s = 0;
		for (int i = 0; i < strlen(str); i++)if (str[i] >= '0' && str[i] <= '9')s++;
		return s;
	}
	int space_s(char str[]) {
		int s = 0;
		for (int i = 0; i < strlen(str); i++)if (str[i] == ' ')s++;
		return s;
	}
	int other_s(char str[]) {
		return strlen(str) - lower_s(str) - upper_s(str) - num_s(str) - space_s(str);
	}
	int main() {
		char s[100];
		cin.getline(s, 100, '\n');
		cout << "大写字母：" << upper_s(s) << endl;
		cout << "小写字母：" << lower_s(s) << endl;
		cout << "数字：" << num_s(s) << endl;
		cout << "空格：" << space_s(s) << endl;
		cout << "符号：" << other_s(s) << endl;
		return 0;
	}
	```

### 指针与数组

一般而言，数组中元素存储的地址是连续的，我们可以根据这一规律使用指针访问数组内的不同元素，首先我们研究一维数组如何使用指针表示，已有数组a[n]，且\*p=a或（\*p=&a[0]），则对于数组a的元素，可有以下表示方法：
|下标法|指针法|
|-|-|
|a[0]、p[0]|\*a、\*p|
|a[i]、p[i]|\*(a+i)、\*(p+i)|

输入n个整型数据（n < 100），将这n个数据倒序输出。

=== "C"
	```c
	#include <stdio.h>

	void num_d(int num[], int n) {
		int* start = num;
		int* end = &num[n - 1];
		while (start < end) {
			int t = *start;
			*start = *end;
			*end = t;
			start++;
			end--;
		}
	}

	int main() {
		int num[100], n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &num[i]);
		num_d(num, n);
		for (int i = 0; i < n; i++)
			printf("%d ", *(num + i));
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	void num_d(int num[], int n) {
		int* start = num;
		int* end = &num[n - 1];
		while (start < end) {
			int t = *start;
			*start = *end;
			*end = t;
			start++;
			end--;
		}
	}
	int main() {
		int num[100], n;
		cin >> n;
		for (int i = 0; i < n; i++)cin >> num[i];
		num_d(num, n);
		for (int i = 0; i < n; i++)cout << *(num + i) << " ";
		return 0;
	}
	```

接下来我们研究二维数组使用指针指定元素的方法。二维数组广义上讲可以认为就是一维数组，在此之前，简要说明指针法和下标法的对照表示：

||下标法|下标-指针法|指针法|
|-|-|-|-|
|首地址|-|&a[0]|a、\*a|
|首值|a[0][0]|\*a[0]|\*\*a|
|i行首地址|-|a[i]、&a[i][0]、&a[i]|a+i、*(a+i)|
|i行首值|a[i][0]|\*a[i]|\*\*(a+i)|
|i行j列首地址|-|a[i]+j、&a[i][j]|\*(a+i)+j|
|i行j列首值|a[i][j]|\*(a[i]+j)、(\*(a+i))[j]|\*(\*(a+i)+j)|

下面的案例会使你对用指针表示数组有新的认识：

先思考下面程序的可行性，再试着上机运行以验证你的猜想。

=== "C"
	```c
	#include <stdio.h>

	int main() {
		int a = 0, * p = &a;
		for (int i = 0; i < 5; i++)
			scanf("%d", p + i);
		for (int i = 0; i < 5; i++)
			printf("%d ", *(p + i));
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		int a = 0, * p = &a;
		for (int i = 0; i < 5; i++)cin >> *(p + i);
		for (int i = 0; i < 5; i++)cout << *(p + i) << " ";
	}
	```
把代码复制进编辑器后，点击运行，没有报错，然后输入数据调试，结束运行的一刻，出现了调试错误窗口（这是可能的情况之一）。但可以看到控制台上，能进行正确的输出。这个程序可以说是擅自创建了一个一维数组，但这种直接对内存操作的方式属于越权访问，是禁止的，但是我们可以对系统进行申请空间，而不是擅自使用，申请空间使用到关键字new，我们可以使用一个指针变量将申请的空间的首地址存储起来，当我们使用完后，再进行释放，把空间归还给系统。这样一来，就解决了不能用变量指定数组元素个数的尴尬情况：
=== "C"
	```c
	// 申请一个整型变量
	int *num = (int*)malloc(sizeof(int));
	// 释放
	free(num);

	// 用变量指定n个元素的一维数组
	int *num = (int*)malloc(n * sizeof(int));
	// 释放
	free(num);

	// 用变量指定i行j列的二维数组
	int** num = (int**)malloc(i * sizeof(int*));
	for (int s = 0; s < i; s++) {
		num[s] = (int*)malloc(j * sizeof(int));
	}
	// 释放
	for (int s = 0; s < i; s++) {
		free(num[s]);
	}
	free(num);
	```
=== "C++"
	```cpp title="动态申请空间"
	//申请一个整型变量
	int *num = new int; 
	//释放
	delete num; 

	//用变量指定n个元素的一维数组
	int *num = new int[n];
	//释放
	delete []num; 

	//用变量指定i行j列的二维数组
	int** num = new int*[i];
	for (int s = 0; s < i; s++) {
		num[s] = new int[j];
	}
	//释放
	for (int s = 0; s < i; s++) {
		delete []num[s];
	}
	delete []num;
	```

输入若干数据，以0作为结束，再输出这些数据。

=== "C"
	```c
	#include <stdio.h>
	#include <stdlib.h>

	int main() {
		int* array = NULL;
		int size = 0;
		int input;
		printf("输入数据，以0结束：");
		do {
			scanf("%d", &input);
			if (input != 0) {
				int* tempArray = (int*)realloc(array, (size + 1) * sizeof(int));
				if (tempArray == NULL) {
					printf("内存分配失败\n");
					if (array != NULL)
						free(array);
					return 1;
				}
				array = tempArray;
				array[size] = input;
				size++;
			}

		} while (input != 0);
		printf("数据为：");
		for (int i = 0; i < size; ++i) {
			printf("%d ", array[i]);
		}
		free(array);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	int main() {
		int* array = nullptr;
		int size = 0;
		int input;
		cout << "输入数据，以0结束：";
		do {
			cin >> input;
			if (input != 0) {
				int* tempArray = new int[size + 1];
				for (int i = 0; i < size; ++i) {
					tempArray[i] = array[i];
				}
				tempArray[size] = input;
				delete[] array;
				array = tempArray;
				size++;
			}

		} while (input != 0);
		cout << "数据为：";
		for (int i = 0; i < size; ++i) {
			cout << array[i] << " ";
		}
		delete[] array;
		return 0;
	}
	```

我们通过之前的内容了解到，数组名的实质是指针，那么，数组可以存储指针变量吗？显然是可以的，这就需要说到指针数组，其定义方法和指针变量类似，在其标识符前加一个\*号即可。除此之外，还有多级指针，即指针的指针，一个二级指针的定义如下：

```cpp title="多维指针"
int a = 0, * p = &a, ** pp = &p;
```

数组除二维数组还有三维、四维……数组、指针除二级指针还有三级、四级……指针。

在C++中，除了可以使用变量名直接访问变量、使用地址访问变量外，还可以使用引用。引用就是给变量起一个别名，其效用和变量本名等价。引用的方法如下：

```cpp title="引用"
int a = 0, & b = a;
```

引用是没有次数上限的，也就是说，一个变量可以有很多个别名。引用可以作函数参数和返回值。

## 自定义数据类型

除了之前讲到的变量类型外，本节将讲解其它一些特殊的变量类型，包括结构体类型、共用体类型、枚举类型这三类可以自定义的数据类型，在描述一些复杂的数据对象时，这些类型起到重要作用。例如结构体类型时不同类型数据的组合，且子数据直接彼此存在联系。

### 结构体

结构体是由一系列具有相同类型或不同类型的数据构成的数据集合，也叫结构。结构体和其他类型基础数据类型一样，例如int类型，char类型只不过结构体可以做成你想要的数据类型。以方便日后的使用。在实际问题中有时候我们需要几种数据类型一起来修饰某个变量。这些数据类型都不同但是他们又是表示一个整体，要存在联系，那么我们就需要一个新的数据类型。结构体就将不同类型的数据存放在一起，作为一个整体进行处理。

有10个学生，每个学生的数据包括学号、姓名、三门课的成绩，从键盘输入10个学生的数据，要求打印出三门课的平均分，以及最高分和最低分的学生的相关信息。

=== "C"
	```c
	#include <stdio.h>
	#include <stdlib.h>
	#include <string.h>

	struct student {
		int id;
		char name[50];
		double score[3];
	};

	void bubbleSort(struct student arr[], int n, int s) {
		for (int i = 0; i < n - 1; i++) {
			for (int j = 0; j < n - i - 1; j++) {
				if (arr[j].score[s] < arr[j + 1].score[s]) {
					struct student temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
				}
			}
		}
	}

	int main() {
		struct student stu[10];
		printf("请输入学生信息：\n");
		printf("\t学号\t姓名\t课程1分数\t课程2分数\t课程3分数\n");
		for (int i = 0; i < 10; i++) {
			printf("%d ", i + 1);
			scanf("%d %s %lf %lf %lf", &stu[i].id, stu[i].name, &stu[i].score[0], &stu[i].score[1], &stu[i].score[2]);
		}
		for (int j = 0; j < 3; j++) {
			printf("课程%d情况：\n", j + 1);
			double sum = 0;
			for (int i = 0; i < 10; i++) {
				sum += stu[i].score[j];
			}
			printf("平均分：%.2lf\n", sum / 10);
			bubbleSort(stu, 10, j);
			int stunum = 0;
			while (stunum <= 9) {
				if (stunum == 0)printf("最高分学生情况：\n");
				if (stunum == 9)printf("最低分学生情况：\n");
				printf("学号：%d\n", stu[stunum].id);
				printf("姓名：%s\n", stu[stunum].name);
				printf("成绩：%.2lf/%.2lf/%.2lf\n", stu[stunum].score[0], stu[stunum].score[1], stu[stunum].score[2]);
				printf("平均分：%.2lf\n\n", (stu[stunum].score[0] + stu[stunum].score[1] + stu[stunum].score[2]) / 3);
				stunum += 9;
			}
			printf("\n");
		}
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	#include <string>
	using namespace std;
	struct student {
		int id;
		string name;
		double score[3];
	};
	void bubbleSort(student arr[], int n, int s) {
		for (int i = 0; i < n - 1; i++) {
			for (int j = 0; j < n - i - 1; j++) {
				if (arr[j].score[s] < arr[j + 1].score[s]) {
					student temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
				}
			}
		}
	}
	int main()
	{
		student stu[10];
		cout << "请输入学生信息：" << endl;
		cout << "\t学号\t姓名\t课程1分数\t课程2分数\t课程3分数" << endl;
		for (int i = 0; i < 10; i++) {    
			cout << i + 1 << " ";
			cin >> stu[i].id >> stu[i].name >> stu[i].score[0] >> stu[i].score[1] >> stu[i].score[2];
		}
		for (int j = 0; j < 3; j++) {
			cout << "课程" << j + 1 << "情况：" << endl;
			float sum = 0;
			for (int i = 0; i < 10; i++) {
				sum += stu[i].score[j];
			}
			cout << "平均分：" << sum / 10 << endl;
			bubbleSort(stu, 10, j);
			int stunum = 0;
			while (stunum <= 9) {
				if (stunum == 0)cout << "最高分学生情况：" << endl;
				if (stunum == 9)cout << "最低分学生情况：" << endl;
				cout << "学号：" << stu[stunum].id << endl;
				cout << "姓名：" << stu[stunum].name << endl;
				cout << "成绩：" << stu[stunum].score[0] << "/" << stu[stunum].score[1] << "/" << stu[stunum].score[2] << endl;
				cout << "平均分：" << (stu[stunum].score[0] + stu[stunum].score[1] + stu[stunum].score[2]) / 3 << endl << endl;
				stunum += 9;
			}
			cout << endl;
		}
		return 0;
	}
	```

结构体类型：

=== "C"
	```cpp title="结构体"
	结构体类型定义：
	struct 结构体类型名{
		成员说明列表
	};

	结构体变量定义：
	1.定义结构体类型后定义
	struct 结构体类型名 变量名
	2.在定义结构体类型时同时定义
	struct 结构体类型名{
		成员说明列表
	}变量名;
	3.直接定义结构体变量
	struct{
		成员说明列表
	}变量名;

	结构体变量引用：
	1.使用结构体变量名引用其成员
	结构体变量名.成员名
	2.使用指向结构体变量的指针引用其成员
	指针变量名->成员名
	(*指针变量名).成员名

	结构体变量初始化：
	struct 结构体类型名 变量名{成员值表}

	结构体变量作参数：
	函数类型 函数名(struct 结构体类型名)
	```
=== "C++"
	```cpp title="结构体"
	结构体类型定义：
	struct 结构体类型名{
		成员说明列表
	};

	结构体变量定义：
	1.定义结构体类型后定义
	*struct* 结构体类型名 变量名   （struct习惯上省略）
	2.在定义结构体类型时同时定义
	struct 结构体类型名{
		成员说明列表
	}变量名;
	3.直接定义结构体变量
	struct{
		成员说明列表
	}变量名;

	结构体变量引用：
	1.使用结构体变量名引用其成员
	结构体变量名.成员名
	2.使用指向结构体变量的指针引用其成员
	指针变量名->成员名
	(*指针变量名).成员名  （不常用）

	结构体变量初始化：
	*struct* 结构体类型名 变量名{成员值表}   （和数组类似）

	结构体变量作参数：
	函数类型 函数名(*struct* 结构体类型名)
	```

### 共用体

共用体是一种特殊的数据类型，允许您在相同的内存位置存储不同的数据类型。您可以定义一个带有多成员的共用体，但是任何时候只能有一个成员带有值。共用体提供了一种使用相同的内存位置的有效方式。

有10个学生，每个学生的数据包括学号、姓名、课程（有的学生有三门课，有的学生有四门课）的成绩，从键盘输入10个学生的数据，要求打印出课程的平均分，并按课程数分类将学生姓名打印出来）。

=== "C"
	```c
	#include <stdio.h>
	#include <string.h>

	union score_n {
		double score_3[3];
		double score_4[4];
	};

	struct student {
		int id;
		char name[100];
		union score_n score;
	};

	int main() {
		struct student stu[10];
		char stu_3[10][100], stu_4[10][100];
		double score_s[7] = {0};
		int i3 = 0, i4 = 0;
		printf("请输入学生信息：\n");
		printf("\t学生类型\t学号\t姓名\t课程1分数\t课程2分数\t课程3分数\t课程4分数\n");
		for (int i = 0; i < 10; i++) {
			printf("%d ", i + 1);
			int type;
			scanf("%d", &type);
			switch (type) {
				case 3:
					scanf("%d%s%lf%lf%lf", &stu[i].id, stu[i].name, &stu[i].score.score_3[0], &stu[i].score.score_3[1], &stu[i].score.score_3[2]);
					for (int j = 0; j < 3; j++)
						score_s[j] += stu[i].score.score_3[j];
					strcpy(stu_3[i3++], stu[i].name);
					break;
				case 4:
					scanf("%d%s%lf%lf%lf%lf", &stu[i].id, stu[i].name, &stu[i].score.score_4[0], &stu[i].score.score_4[1], &stu[i].score.score_4[2], &stu[i].score.score_4[3]);
					for (int j = 3; j < 7; j++)
						score_s[j] += stu[i].score.score_4[j - 3];
					strcpy(stu_4[i4++], stu[i].name);
					break;
				default:
					printf("error!\n");
					i--;
			}
		}
		printf("\n有三门课的学生：");
		for (int i = 0; i < i3; i++)
			printf(" %s", stu_3[i]);
		printf("\n平均成绩：");
		for (int i = 0; i < 3; i++)
			printf(" %.2lf", score_s[i] / i3);
		printf("\n有四门课的学生：");
		for (int i = 0; i < i4; i++)
			printf(" %s", stu_4[i]);
		printf("\n平均成绩：");
		for (int i = 3; i < 7; i++)
			printf(" %.2lf", score_s[i] / i4);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	#include <string>
	using namespace std;
	union score_n {
		double score_3[3];
		double score_4[4];
	};
	struct student {
		int id;
		string name;
		score_n score;
	};
	int main()
	{
		student stu[10];
		string stu_3[10], stu_4[10];
		double score_s[7]{};
		int i3 = 0, i4 = 0;
		cout << "请输入学生信息：" << endl;
		cout << "\t学生类型\t学号\t姓名\t课程1分数\t课程2分数\t课程3分数\t课程4分数" << endl;
		for (int i = 0; i < 10; i++) {
			cout << i + 1 << " ";
			int type;
			cin >> type;
			switch (type) {
			case 3:
				cin >> stu[i].id >> stu[i].name >> stu[i].score.score_3[0] >> stu[i].score.score_3[1] >> stu[i].score.score_3[2]; 
				for (int j = 0; j < 3; j++)score_s[j] += stu[i].score.score_3[j];
				stu_3[i3++] = stu[i].name;
				break;
			case 4:
				cin >> stu[i].id >> stu[i].name >> stu[i].score.score_4[0] >> stu[i].score.score_4[1] >> stu[i].score.score_4[2] >> stu[i].score.score_4[3]; 
				for (int j = 3; j < 7; j++)score_s[j] += stu[i].score.score_4[j - 3];
				stu_4[i4++] = stu[i].name;
				break;
			default:cout << "error!" << endl; i--;
			}
		}
		cout << endl << "有三门课的学生：";
		for (int i = 0; i < i3; i++)cout << stu_3[i] << " ";
		cout << endl << "平均成绩：";
		for (int i = 0; i < 3; i++)cout << score_s[i] / i3 << " ";
		cout << endl << "有四门课的学生：";
		for (int i = 0; i < i4; i++)cout << stu_4[i] << " ";
		cout << endl << "平均成绩：";
		for (int i = 3; i < 7; i++)cout << score_s[i] / i4 << " ";
		return 0;
	}
	```

共用体类型：

=== "C"
	```cpp title="共用体"
	共用体类型定义：
	union 共用体类型名{
		成员说明列表
	};

	共用体变量定义：
	1.定义共用体类型后定义
	union 共用体类型名 变量名
	2.在定义共用体类型时同时定义
	union 共用体类型名{
		成员说明列表
	}变量名;
	3.直接定义共用体变量
	union{
		成员说明列表
	}变量名;

	共用体变量引用：
	1.使用共用体变量名引用其成员
	共用体变量名.成员名
	2.使用指向共用体变量的指针引用其成员
	指针变量名->成员名
	(*指针变量名).成员名

	共用体类型用于结构体：
	共用体类型名 结构体变量成员名
	（共用体类型一般不单独使用，而是多用于结构体）
	```
=== "C++"
	```cpp title="共用体"
	共用体类型定义：
	union 共用体类型名{
		成员说明列表
	};

	共用体变量定义：
	1.定义共用体类型后定义
	*union* 共用体类型名 变量名   （union习惯上省略）
	2.在定义共用体类型时同时定义
	union 共用体类型名{
		成员说明列表
	}变量名;
	3.直接定义共用体变量
	union{
		成员说明列表
	}变量名;

	共用体变量引用：
	1.使用共用体变量名引用其成员
	共用体变量名.成员名
	2.使用指向共用体变量的指针引用其成员
	指针变量名->成员名
	(*指针变量名).成员名  （不常用）

	共用体类型用于结构体：
	共用体类型名 结构体变量成员名
	（共用体类型一般不单独使用，而是多用于结构体）
	```

### 枚举和自定义类型

除结构体和共用体外，还有枚举类型enum和自定义类型typedef。

=== "C"
	```c
	#include <stdio.h>

	enum os { Windows, Mac, Linux };

	void print_os(enum os p_os) {
		switch (p_os) {
			case Windows:
				printf("Windows\n");
				break;
			case Linux:
				printf("Linux\n");
				break;
			case Mac:
				printf("Mac\n");
				break;
		}
	}

	int main() {
		enum os my_os = Windows;
		enum os t_os = Linux;
		print_os(my_os);
		return 0;
	}
	```
=== "C++"
	```cpp
	#include <iostream>
	using namespace std;
	enum os { Windows, Mac, Linux };
	void print_os(os p_os) {
		switch (p_os) {
		case Windows:cout << "Windows" << endl; break;
		case Linux:cout << "Linux" << endl; break;
		case Mac:cout << "Mac" << endl; break;
		}
	}
	int main()
	{
		os my_os = Windows;
		os t_os = Linux;
		print_os(my_os);
		return 0;
	}
	```

枚举类型：

=== "C"
	```cpp title="枚举和自定义类型"
	枚举类型定义：
	enum 枚举类型名 {枚举表}
	枚举类型变量定义：
	enum 枚举类型名 变量名

	自定义类型定义：
	typedef 变量名 标识符
	```
=== "C++"
	```cpp title="枚举和自定义类型"
	枚举类型定义：
	enum 枚举类型名 {枚举表}
	枚举类型变量定义：
	*enum* 枚举类型名 变量名

	自定义类型定义：
	typedef 变量名 标识符
	```

枚举类型的本质是枚举表中第一项起分别是0，1，2...的列表，使用枚举符进行赋值，使得其值为对应的项号，默认情况下是这样的，也可以指定其项号，对于不指定的，自动进行顺延。例如enum sex{female=2,male,none}，male的项号为3，none的项号为4。  
自定义类型其实就是给数据类型起一个别的名字而已，既没有创造一个新的变量类型，也没有影响原来的变量类型，原变量标识符仍然是可用的。

## C输入输出流

C的输入输出是通过流的方式进行的。C语言中的输入输出主要通过标准输入输出库（stdio.h）来实现，包括键盘输入、屏幕输出以及文件输入输出。C++输入输出见“C++面向对象”。

### 标准输入输出流

在C语言中，标准输入输出流主要通过以下函数来实现：

- `scanf`: 从标准输入（键盘）读取输入。
- `printf`: 将输出内容发送到标准输出（屏幕）。
- `fprintf`: 将输出内容发送到文件流。
- `fscanf`: 从文件流读取输入。

```c
#include <stdio.h>

int main() {
    char name[20];
    int age;
    
    // 从键盘输入数据
    printf("请输入您的姓名和年龄：");
    scanf("%s %d", name, &age);
    
    // 输出到屏幕
    printf("您的姓名是：%s，年龄是：%d\n", name, age);
    
    return 0;
}
```

### 文件操作与文件流

C语言中文件的操作相对复杂一些，需要手动打开和关闭文件，并使用不同的函数进行读写操作。

打开/关闭文件

```c
#include <stdio.h>

int main() {
    FILE *file;
    
    // 打开文件
    file = fopen("example.txt", "w");
    
    // 写入数据到文件
    
    // 关闭文件
    fclose(file);
    
    return 0;
}
```

文本文件读写

```c
#include <stdio.h>

int main() {
    FILE *infile, *outfile;
    char ch;
    
    // 打开源文件和目标文件
    infile = fopen("source.txt", "r");
    outfile = fopen("destination.txt", "w");
    
    // 从源文件读取数据，写入到目标文件
    while ((ch = fgetc(infile)) != EOF)
        fputc(ch, outfile);
    
    // 关闭文件
    fclose(infile);
    fclose(outfile);
    
    return 0;
}
```

二进制文件读写

```c
#include <stdio.h>

int main() {
    FILE *infile, *outfile;
    char buffer[4096];
    int n;
    
    // 打开源文件和目标文件
    infile = fopen("source.bin", "rb");
    outfile = fopen("destination.bin", "wb");
    
    // 从源文件读取数据，写入到目标文件
    while ((n = fread(buffer, sizeof(char), sizeof(buffer), infile)) > 0)
        fwrite(buffer, sizeof(char), n, outfile);
    
    // 关闭文件
    fclose(infile);
    fclose(outfile);
    
    return 0;
}
```

其他常用操作

```c
#include <stdio.h>

int main() {
    FILE *file;
    char buff[255];
    
    // 打开文件
    file = fopen("example.txt", "r");
    
    // 读取文件内容
    fscanf(file, "%s", buff);
    printf("1: %s\n", buff );
    
    // 忽略前五个字符
    fseek(file, 5, SEEK_SET);
    
    // 再次读取文件内容
    fscanf(file, "%s", buff);
    printf("2: %s\n", buff );
    
    // 关闭文件
    fclose(file);
    
    return 0;
}
```
