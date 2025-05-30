---
title: C++面向对象
subtitle: 面向对象
description: C++面向对象
---

# C++面向对象

## 类与对象的基本操作

C语言输入面向过程的编程语言，而C++是对C的一个拓展，增加了面向对象的内容，因而前面的内容是C和C++共有的面向过程部分，接下来的内容是面向对象部分，是C++独有的特点。面向过程的一个显著的特点是数据和处理数据的程序时分离的，这个处理数据的程序被称为函数；而面向对象将数据和处理数据的程序封装起来，放到一个类中，而属于类的变量称为对象。

### 类与对象及其成员函数

输入n，输出n!。

```cpp
#include <iostream>
using namespace std;
class fac {
    int n, sum;
public:
    void set(int x) {
        n = x;
        sum = 1;
    }
    void cal() {
        for (int i = 1; i <= n; i++)sum *= i;
    }
    void print() {
        cout << n << "!=" << sum << endl;
    }
};
int main() {
    int x;
    cin >> x;
    fac f;
    f.set(x);
    f.cal();
    f.print();
    return 0;
}
```
```cpp title="类与对象的基本操作"
类的定义：
class 类名{
    public:
        数据成员或成员函数的定义（共有：可以在类外访问）
    private:
        数据成员或成员函数的定义（私有：只能被类的成员函数访问）
    protected:
        数据成员或成员函数的定义（保护：只能被类的成员函数或派生类的成员函数访问）
};
定义类时指定的访问权限均可省略，省略时默认为私有（private）

类成员函数定义：
在类内定义：和普通函数定义方法一样
在类外定义：需在类内进行声明，类外定义：
函数类型 类名::函数名(形参表){
	函数体
}

对象的定义：
类名 对象名（表）

对象成员引用：
对象名.数据成员名
对象名.成员函数名(实参表)
```
类与结构体比较相似，但也有区别，首先结构体成员默认访问权限时public，而类成员默认访问权限时private，除此之外，类还有很多丰富的功能，将在后面逐步讲到。

### 三类特殊成员函数

输入n个学生的数据，包括学号、姓名、成绩，要求输出这些学生数据并计算平均分。

```cpp
#include <iostream>
#include <string>
using namespace std;
class Student {
    int n;
    string* name;
    int* id;
    float* score;
public:
    Student(int x) {
        n = x;
        name = new string[n];
        id = new int[n];
        score = new float[n];
    }
    ~Student() {
        delete[]name, id, score;
    }
    void in() {
        cout << "学号\t姓名\t成绩" << endl;
        for (int i = 0; i < n; i++)cin >> id[i] >> name[i] >> score[i];
    }
    void out() {
        cout << "学号\t姓名\t成绩" << endl;
        for (int i = 0; i < n; i++)cout << id[i] << "\t" << name[i] << "\t" << score[i] << endl;
    }
    float avg() {
        float sum = 0;
        for (int i = 0; i < n; i++)sum += score[i];
        return sum / n;
    }
};
int main() {
    int n;
    cout << "请输入N：";
    cin >> n;
    Student s(n);
    s.in();
    cout << "平均分：" << s.avg() << endl;
    s.out();
    return 0;
}
```

```cpp title="三类特殊成员函数"
构造函数定义：
类名(形参表){
    函数体
}

析构函数定义
~类名(){
    函数体
}

复制构造函数定义：
类名(const 类名 &){
    函数体
}
```

构造函数、析构函数和复制构造函数是类特殊的函数，都没有返回值。如果没有人为地显式定义，系统会自动进行隐式定义，即默认函数。其特点如下：

|函数类型|特点|调用时机|默认函数|备注|
|-|-|-|-|-|
|构造函数|可定义多个、系统根据传入的实参与定义的形参进行比较来判断哪个构造函数应当被调用|对象被创建时|无函数体的无参函数|-|
|析构函数|只能定义1个、不带参数、不能重载|对象被销毁时|无函数体的函数|一般不需要进行显式定义|
|复制构造函数|只能定义1个|对已有对象初始化一个新对象时被调用|把初始化对象的每个数据成员的值都复制到新建的对象中|-|

### 对象数组与对象指针

对象和一般变量及结构体类似，也有对象数组和对象指针，其使用形式和一般变量的数组与指针相同。

|名称|定义形式|赋值形式|调用形式1|调用形式2|
|-|-|-|-|-|
|对象指针|类名 \*对象指针名|-|指向对象的指针->数据成员名<br>指向对象的指针->成员函数名(实参表)|(\*指向对象的指针).数据成员名<br>(\*指向对象的指针).成员函数名(实参表)|
|指向类成员的指针|数据类型 类名::\*数据成员指针名<br>函数类型 (类名::\*成员函数指针名)(参数表)|数据成员指针名=&类名::数据成员名<br>成员函数指针名=&类名::成员函数名|对象指针名->\*数据成员指针名<br>(对象指针名->\*成员函数指针名)(实参表)|对象名.\*数据成员指针名<br>(对象名.\*成员函数指针名)(实参表)|

除对象指针和指向类成员的指针外，还有一种特殊的指针，即this指针，是类的每一个成员函数都有的一个隐含的常量指针，this指针的类型就是成员函数所属类的类型。当调用成员函数时，它被初始化为被调函数的对象的地址，注意this指针是一个不可修改的常量，且其作用域仅在一个对象内部。  

对于不同的对象，其成员是彼此独立的，如果需要一个公有的成员，我们可以用public或者private函数即可，但是其值仍然是独立的，因而，如果需要一个能被所有类的对象共享的成员，可以使用static关键字定义静态成员。因为静态成员只存储一次，所有常常认为其不是“对象的成员”，而是“类的成员”。  

静态数据成员在初始化时，习惯上在类外进行，且在对象定义之前，一般在主函数之前。静态成员函数仅能访问静态成员，不能访问非静态成员，这是由于静态的成员函数没有this指针，且静态成员函数的调用不需要对象名。

求空间两点距离，分别输入两点的坐标值x，y，z，输出距离。

```cpp
#include <iostream>
#include <cmath>
using namespace std;
class point {
    double x, y, z;
public:
    point(int a, int b, int c) {
        x = a; y = b; z = c;
    }
    friend double tpd(point& p1, point& p2);
};
inline double p(double a, double b) {
    return (a - b) * (a - b);
}
double tpd(point& p1, point& p2) {
    return sqrt(p(p1.x, p2.x) + p(p1.y, p2.y) + p(p1.z, p2.z));
}
int main() {
    double x, y, z;
    cout << "依次输入两点x，y，z值：";
    cin >> x >> y >> z;
    point p1(x, y, z);
    cin >> x >> y >> z;
    point p2(x, y, z);
    cout << "两点距离为：" << tpd(p1, p2);
    return 0;
}
```

### 友元函数

有时需要定义一些函数，这些函数不是类的一部分，但有需要访问类的数据成员，为了解决这种问题，可以使用友元标识符friend进行函数声明，使得被声明函数能够访问数据成员，这种函数被称为友元函数，这种关系被称为友元关系。和函数一样，类之间也可以有友元关系，即友元类。注意友元关系具有单向性，且不能传递。  

在定义常量时，使用到const标识符，同样的，常对象和类中的常数据成员也可以使用const标识符，使得其在定义时必须初始化，且一经初始化，不能再被修改，和常量有着类似的性质。

设计一个日期类Date，包括日期的年、月、日，编写一个友元函数，求两个日期之间相差的天数。依次输入日期1和日期2，输出相差天数。

```cpp
#include <iostream>
using namespace std;
inline int year_r(int year) {
    if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0)return 1;
    return 0;
}
int day_t[2][12]{
        {31,28,31,30,31,30,31,31,30,31,30,31},
        {31,29,31,30,31,30,31,31,30,31,30,31}
};
int year_t[2]{ 365,366 };
class Date {
    int year, month, day, r_day;
public:
    Date(int y, int m, int d) {
        int f = 0;
        if (m > 12 || m < 1) { m = 1; f = 1; }
        if (d > day_t[year_r(y)][m - 1] || d < 1) { d = day_t[year_r(y)][m - 1]; f = 1; }
        year = y; month = m; day = d;
        if (f) { cout << "使用了不合法的日期，已修正！修正后的日期为："; out(); cout << endl; }
        r_day = 0; r_ds();
    }
    void r_ds() {
        for (int j = 0; j < month - 1; j++)r_day += day_t[year_r(year)][j];
        r_day += day;
    }
    void out() {
        cout << year << "-" << month << '-' << day;
    }
    friend int day_s(Date& d1, Date& d2);
};
int day_s(Date& d1, Date& d2) {
    int sum = 0;
    for (int y = d1.year; y < d2.year - 1; y++)sum += year_t[year_r(y)];
    if (d1.month > d2.month) sum += year_t[year_r(d1.year)] - d1.r_day + d2.r_day;
    else sum += d2.r_day - d1.r_day;
    return sum;
}
int main() {
    int y, m, d;
    cout << "请输入日期1：";
    cin >> y >> m >> d;
    Date da1(y, m, d);
    cout << "请输入日期2：";
    cin >> y >> m >> d;
    Date da2(y, m, d);
    da1.out();cout << "与";da2.out();cout << "相差" << day_s(da1, da2) << "天" << endl;
    return 0;
}
```

编写一个程序，统计学生成绩，其功能包括输入学生的姓名和成绩，按成绩从高到低排列打印输出，对前70%的学生定为合格（输出PASS），对后30%的学生定为不合格（输出FAIL）。

```cpp
#include <iostream>
#include <string>
using namespace std;
class student {
    string name;
    float deg;
public:
    void setname(string n) {
        name = n;
    }
    void setdeg(float d) {
        deg = d;
    }
    string getname() {
        return name;
    }
    float getdeg() {
        return deg;
    }
};
class compute {
    int ns;
    student na[100];
public:
    void getdata(int n) {
        ns = n;
        string namel;
        float degl;
        cout << "姓名\t分数" << endl;
        for (int i = 0; i < ns; i++) {
            cin >> namel;
            na[i].setname(namel);
            cin >> degl;
            na[i].setdeg(degl);
        }
    }
    void sort() {
        for (int i = 0; i < ns - 1; i++) {
            for (int j = 0; j < ns - i - 1; j++) {
                if (na[j].getdeg() < na[j + 1].getdeg()) {
                    student sk = na[j];
                    na[j] = na[j + 1];
                    na[j + 1] = sk;
                }
            }
        }
    }
    void disp() {
        cout << "姓名\t分数\t评定" << endl;
        string PF;
        for (int i = 0; i < ns; i++) {
            if (i < ns * 0.7)PF = "PASS";
            else PF = "FAIL";
            cout << na[i].getname() << "\t" << na[i].getdeg() << "\t" << PF << endl;
        }
    }
};
int main() {
    int n;
    cout << "请输入学生数量：";
    cin >> n;
    compute c1;
    c1.getdata(n);
    c1.sort();
    c1.disp();
    return 0;
}
```

## 重载与模板

### 重载

重载是指一个名称对应多种功能，对于应当时哪种功能，通过相关的上下文进行判断。重载分为函数重载和运算符重载。函数重载通过参数列表等的不同进行区分，在调用时，通过实参与形参进行比对，判断应当使用哪个函数。一般来说，函数重载主要是在参数类型或者参数个数上存在区别。

输入三角形的三边长、或者输入矩形的两边长、或者输入圆的半径，返回面积。

```cpp
#include <iostream>
#include <cmath>
using namespace std;
double area(double r) {
    return 3.14 * r * r;
}
double area(double a, double b) {
    return a * b;
}
double area(double a, double b, double c) {
    if (a + b > c && a + c > b && b + c > a) {
        double p = (a + b + c) / 2;
        return sqrt(p * (p - a) * (p - b) * (p - c));
    }
    return -1;
}
int main() {
    cout << "圆：" << area(2.5) << " 矩形：" << area(4, 5) << " 三角形：" << area(3, 4, 5);
    return 0;
}
```

当一个函数在特定的域被多次声明时，编译器解析第二个及后面函数时是通过下面的步骤分析判断是否重载的：

1. 当参数个数或类型不同时，则认为是重载
2. 函数返回类型和参数表完全相同，则认为第二个函数是第一个函数的重复声明，注意参数表的比较过程和参数名称无关
3. 如果两个函数的参数表相同但返回类型不同，则第二个声明被视为第一个的错误，重复声明会被标记为编译错误
4. 如果两个函数的参数表中只有默认参数不同，则第二个声明被视为第一个的重复声明
5. 如果两个函数的参数表中参数类型是因使用了typedef关键字而不同，实际上是同一个类型时，则参数表视为相同
6. 一般情况下识别函数声明是否相同时并不考虑const和volatile修饰符
7. 对于在命名空间内重载了的函数使用using关键字引入时不能指定引入哪个函数，只能指定函数名，具体调用哪个函数在调用时决定

运算符重载是指对已有运算符赋予多重意义，也就是说同一个运算符可以完成不同的运算操作，在C++中，运算符可以完成两个对象的复杂操作。并非所有运算符都能重载，不能重载的运算符有作用域解析运算符::，条件运算符?:，直接成员访问运算符.，sizeof运算符，解除对指向类成员的指针运算符.*

定义一个复数类，使用重载运算符，使其能完成复数的赋值、加减乘除运算。

```cpp
#include <iostream>
using namespace std;
class Complex {
private:
	double Real, Image;
public:
	Complex(double r = 0, double i = 0) {
		Real = r; Image = i;
	}
	void Show(int i) {
		cout << "c" << i << "=" << Real << "+" << Image << "i" << endl;
	}
	void operator=(const Complex& c) {
		Real = c.Real;
		Image = c.Image;
	}
	Complex operator+(Complex& c) {
		Complex t;
		t.Real = Real + c.Real;
		t.Image = Image + c.Image;
		return t;
	}
	Complex operator-(Complex& c) {
		Complex t;
		t.Real = Real - c.Real;
		t.Image = Image - c.Image;
		return t;
	}
	Complex operator+(double s) {
		Complex t;
		t.Real = Real + s;
		t.Image = Image;
		return t;
	}
	Complex operator+=(Complex& c) {
		Complex t;
		Real += c.Real;
		Image += c.Image;
		return t;
	}
};
int main() {
	Complex c1(21, 17), c2(15, 44), c3, c4;
	c3 = c1 + c2;
	c3.Show(3);
	c4 = c1 - c2;
	c4.Show(4);
	c1 += c2;
	c1.Show(1);
	c2 = c1 + 12;
	c2.Show(2);
	return 0;
}
```

```cpp title="二元运算符的重载"
二元运算符的重载：
1.重载为类的成员函数：
类型 operator 重载运算符 (形参表){
	函数体
}
2.重载为类的友元函数：
类型 operator 重载运算符 (形参1,形参2){
	函数体
}
friend 类型 operator 重载运算符 (形参1,形参2)
```

定义一个描述时间计数器的类，其三个数据成员分别用于存放时、分、秒。用成员函数重载自增++和自减--运算符，实现对计数器对象的加1，减1运算。

```cpp
#include <iostream>
using namespace std;
class tcount {
private:
	int hour, minute, second;
public:
	tcount(int h = 0, int m = 0, int s = 0) {
		hour = h; minute = m; second = s;
	}
	void show(int i) {
		cout << "t" << i << "=" << hour << ":" << minute << ":" << second << endl;
	}
	tcount operator++() {
		second++;
		if (second == 60) {
			second = 0;
			minute++;
			if (minute == 60) {
				minute = 0;
				hour++;
				if (hour == 24)hour = 0;
			}
		}
		return *this;
	}
	tcount operator++(int) {
		tcount temp = *this;
		second++;
		if (second == 60) {
			second = 0;
			minute++;
			if (minute == 60) {
				minute = 0;
				hour++;
				if (hour == 24)hour = 0;
			}
		}
		return temp;
	}
	tcount operator--() {
		second--;
		if (second == -1) {
			second = 59;
			minute--;
			if (minute == -1) {
				minute = 59;
				hour--;
				if (hour == -1)hour = 23;
			}
		}
		return *this;
	}
	tcount operator--(int) {
		tcount temp = *this;
		second--;
		if (second == -1) {
			second = 59;
			minute--;
			if (minute == -1) {
				minute = 59;
				hour--;
				if (hour == -1)hour = 23;
			}
		}
		return temp;
	}
};
int main() {
	tcount t1(15, 12, 16), t2(11, 56, 58);
	t1.show(1);
	t1--;
	--t1;
	t1.show(1);
	t2.show(2);
	t2++;
	++t2;
	t2.show(2);
	return 0;
}
```

```cpp title="一元运算符的重载"
一元运算符的重载：
1.重载为类的成员函数：
类型 operator 一元运算符 (形参表){
	函数体
}
2.重载为类的友元函数：
类型 operator 一元运算符 (类名 &对象){
	函数体
}
```

定义一个描述时间计数器的类，其三个数据成员分别用于存放时、分、秒。编写一个能将时、分、秒转换成以秒为单位的等价整数。

```cpp
#include <iostream>
using namespace std;
class tcount {
private:
	int hour, minute, second;
public:
	tcount(int h = 0, int m = 0, int s = 0) {
		hour = h; minute = m; second = s;
	}
	void show(int i) {
		cout << "t" << i << "=" << hour << ":" << minute << ":" << second << endl;
	}
	operator int() {
		return hour * 3600 + minute * 60 + second;
	}
};
int main() {
	tcount t(15, 12, 56);
	int s;
	t.show(0);
	s = t;
	cout << s << endl;
	s = int(t);
	cout << s << endl;
	s = (int)t;
	return 0;
}
```

```cpp title="转换函数的重载"
转换函数重载：
operator 转换后的数据类型(){
	函数体
}
```

编写字符串运算符=、+、>的重载运算符，使运算符=、+、>分别用于字符串的赋值、连接、比较运算，实现字符串的直接操作运算。

```cpp
#include <iostream>
#include <string>
using namespace std;
class String {
protected:
	unsigned int Length;
	char* Sp;
public:
	String() { Sp = 0; }
	~String() { if (Sp)delete[]Sp; }
	String(const String& s) {
		if (s.Sp) {
			Length = strlen(s.Sp);
			Sp = new char[Length + 1];
			strcpy_s(Sp, Length + 1, s.Sp);
		}
		else Sp = 0;
	}
	String(const char* s) {
		Length = strlen(s);
		Sp = new char[Length + 1];
		strcpy_s(Sp, Length + 1, s);
	}
	void Show() { cout << Sp << endl; }
	String& operator=(const String& s) {
		if (Sp)delete[]Sp;
		if (s.Sp) {
			Length = strlen(s.Sp);
			Sp = new char[Length + 1];
			strcpy_s(Sp, Length + 1, s.Sp);
		}
		else Sp = 0;
		return *this;
	}
	int operator>(const String& s) {
		if (strcmp(Sp, s.Sp) > 0)return 1;
		else return 0;
	}
	friend String operator+(const String&, const String&);
};
String operator+(const String& s1, const String& s2) {
	String t;
	t.Length = s1.Length + s2.Length;
	t.Sp = new char[t.Length + 1];
	strcpy_s(t.Sp, s1.Length + 1, s1.Sp);
	strcat_s(t.Sp, t.Length + 1, s2.Sp);
	return t;
}
int main() {
	String s1("soft"), s2("hard"), s3("ware"), s4(s2);
	String s5 = s1 + s3;
	String s6 = s2 + s3;
	if (s5 > s6)s5.Show();
	else s6.Show();
	s4.Show();
	return 0;
}
```

### 模板

当一个程序的功能是对某种特定的数据类型进行处理时，则可以将所处理的数据类型说明为参数，便于在其他数据类型的情况下使用。模板是一种完全通用的方法来设计函数或类而不先说明将被使用的每个对象的类型，注意模板类型不具有隐式的数据转换。模板分为函数模板和类模板，类模板本身不是类，而只是某种编译器用来生成类代码的类的“配方”。其语法如下。

```cpp title="模板语法"
函数模板的定义：
template 类型参数表
返回值类型 函数名(形参表){
	函数体
}

类模板的定义：
template 类型参数表
class 类名{
	类说明体
}
template 类型参数表
返回类型 类名 类型名表::成员函数(形参表){
	成员函数定义体
}
```

## 继承与派生

面向对象不能失去继承与派生，就像西方不能失去耶路撒冷。

继承与派生是面向对象的重要组成部分，也是C++的重要组成部分，通过继承可以自动地为一个类提供来自另一个类的成员，正因为如此，继承是实现软件可重用性的重要机制，可以大大提高软件的开发效率和质量。

+ 继承与派生的三个特征：共享特征、差别或新增特征、层次结构特征
+ 继承与派生的三大好处：避免公共代码重复开发、增强代码一致性、有利于开发者掌握不同对象的共性和特性

如果类A派生了类B，即类B继承了类A，则称类A是基类（也称父类或超类）、类B是类A的派生类（也称子类）。基类和派生类之间，通过继承和派生，形成了层次结构。

定义一个点类，在从点类派生出一个四边形类。实现计算四边形周长的功能。

```cpp
#include <iostream>
#include <cmath>
using namespace std;

class point {
    double x, y;
public:
    void in(int a, int b) {
        x = a; y = b;
    }
    friend double tpd(point& p1, point& p2);
};

class quad : public point {
    point p[4];
    double c;
public:
    void setp() {
        for (int i = 0; i < 4; i++) {
            double x, y;
            cin >> x >> y;
            p[i].in(x, y);
        }
    }
    void calc() {
        c = 0;
        for (int i = 0; i < 3; i++) c += tpd(p[i], p[i + 1]);
        c += tpd(p[3], p[0]);
    }
    void out() {
        cout << c;
    }
};

inline double p(double a, double b) {
    return (a - b) * (a - b);
}
double tpd(point& p1, point& p2) {
    return sqrt(p(p1.x, p2.x) + p(p1.y, p2.y));
}

int main() {
    cout << "输入四边形四点坐标x，y：";
    quad q1;
    q1.setp();
    q1.calc();
    q1.out();
	return 0;
}
```

```cpp title="派生"
派生类的声明：
class 派生类名:*派生存取说明符* 基类名{  //合法的派生存取说明符有public、protected和private，如果不指定，默认为private派生
	派生类新增的数据成员
}

派生类的构造函数声明：
派生类的构造函数名称(参数表):基类的构造函数名(参数表){
	派生类构造函数体
}

派生类的构造函数声明（派生类中有对象成员）：
派生类的构造函数名称(参数表):基类的构造函数名(参数表),对象成员名(参数表){
	派生类构造函数体
}
```

在不同的派生方式下，派生类成员的访问控制分为两部分：一部分是派生类在新增成员的访问控制；另一部分是基类成员在派生类的访问控制。具体内容如下两表：  

类成员访问控制规则：

|存取说明符|访问控制规则|
|-|-|
|private|此派生类的非静态成员和友元函数均可直接访问|
|protected|此派生类和其子类非静态成员函数和友元函数可以访问|
|public|任何非静态成员函数、友元函数和非成员函数都可以直接访问|

基类成员在派生类的访问控制规则：

|基类成员的存取说明符|public派生|protected派生|private派生|
|-|-|-|-|
|private|在派生类中被隐藏|在派生类中被隐藏|在派生类中被隐藏|
|protected|派生类中为protected|派生类中为protected|派生类中为private|
|public|派生类中为public|派生类中为protected|派生类中为private|

当声明一个派生类时，根据它所继承基类的构造函数的声明情况不同，必须采用不同的方式声明和定义派生类的构造函数。而派生类的析构函数与基类无关，与其派生类本身有关。派生类构造函数的构造规则：

1. 基类有不带参数的构造函数，则派生类可以自由定义构造函数。
2. 基类仅有带参数的构造函数，则派生类必须显式定义构造函数，并在声明时指定基类的某一构造函数和参数表，且把参数传递给基类构造函数。
3. 基类没有显式定义构造函数，则派生类可以自由定义构造函数，且构造函数可以省略。

派生类只有一个基类的派生方式称为单一继承（单基派生），如果从多个基类派生出新的子类，这种派生方法称为多重继承（多基派生），这使得派生功能大大提高软件重用的灵活性。在使用时相关规则与单一继承相同，但要注意过多地使用多重继承容易形成系统的复杂性和模糊性，因而能用单一继承就不使用多重继承。

```cpp title="多重继承"
多重继承的声明：
class 派生类名:*派生存取说明符* 基类名1,...,*派生存取说明符* 基类名n{
	派生类新增的数据成员
}
```

通常来说，定义的类会被实例化为对象使用，但是，会有一种类时不希望被实例化，都往往用于作为基类，这种类称为虚类或抽象类，对应地，希望被实例化的基类被称为实基类或者具体基类。虚基类初始化时，构造函数的调用顺序规则如下所述：

1. 同一层派生中包含多个基类时，虚基类的构造函数按它们派生时声明的先后次序调用。
2. 如果虚基类是由实基类派生而来的，则先调用此实基类的构造函数，再调用虚基类的构造函数，最后才是派生类的构造函数。
3. 若在同一层派生中，同时存在虚基类和实基类，应先调用虚基类的构造函数，在调用实基类的构造函数，最后调用派生类的构造函数。

&emsp;&emsp;虚基类是为其他类提供一个合适的基类，以便派生类可以从它那里继承和实现所需的接口。在多重继承时，当派生类的多个基类有一个共同的基类时，为防止产生二义性问题可以使用虚基类方法。

```cpp title="虚基类"
虚基类的声明：
class 派生类名:virtual *派生存取说明符* 虚基类名{
	派生类新增的数据成员
}
```

由于派生类是从基类继承而来的，所有任何派生类的对象也是基类的对象。在public继承方式下，派生类对象可以视为基类对象，因为派生类中有与其基类一一对应的成员，因而在对象赋值等操作中，都可以将派生类对象直接转换为基类对象使用，但不适宜将基类对象转换为派生类对象使用，这是由于派生类的成员会比基类更多，可能出现非法的情况。  

派生类对象到基类对象的自动转换通常称为赋值兼容规则。当派生类从基类public继承时，允许以下4种派生类对象到基类对象的自动转换：

1. 可以用派生类对象为基类对象赋值
2. 可以用派生类对象初始化基类引用对象
3. 可以把指向派生类对象的指针赋给基类对象的指针
4. 可以把派生类对象的地址赋给基类对象的指针

## 多态性与虚函数

定义几何图形基类，从该基类派生出矩形、圆形和三角形，求相应图形的周长、面积。

```cpp
#include <iostream>
#include <cmath>
using namespace std;
const double PI = 3.1415926535;
class shape {
public:
	virtual double perimeter() = 0;
	virtual double area() = 0;
	virtual void show() {}
};
class circle :public shape {
	double radius;
public:
	circle() { radius = 0; }
	circle(double r) { radius = r; }
	double perimeter() { return 2 * PI * radius; }
	double area() { return PI * radius * radius; }
	void show() { cout << "radius=" << radius << endl; }
};
class rectangle :public shape {
	double width, length;
public:
	rectangle() { width = 0; length = 0; }
	rectangle(double w, double l) { width = w; length = l; }
	rectangle(rectangle& a) { width = a.width; length = a.length; }
	double perimeter() { return 2 * (width + length); }
	double area() { return width * length; }
	void show() { cout << "width=" << width << " length=" << length << endl; }
};
class triangle :public shape {
	double a, b, c;
public:
	triangle() { a = 0; b = 0; c = 0; }
	triangle(double x, double y, double z) { a = x; b = y; c = z; }
	double perimeter() { return a + b + c; }
	double area() { double p = (a + b + c) / 2; return sqrt(p * (p - a) * (p - b) * (p - c)); }
	void show() { cout << "a=" << a << " b=" << b << " c=" << c << endl; }
};
int main() {
	shape* s;
	double i, j, k;
	cout << "请输入圆的半径：";
	cin >> i;
	circle c(i);
	cout << "请输入三角形的三边长：";
	cin >> i >> j >> k;
	triangle t(i, j, k);
	cout << "请输入矩形的相邻两边长：";
	cin >> i >> j;
	rectangle r(i, j);
	cout << "形状\t周长\t面积" << endl;
	cout << "圆\t" << c.perimeter() << "\t" << c.area() << endl;
	cout << "三角形\t" << t.perimeter() << "\t" << t.area() << endl;
	cout << "矩形\t" << r.perimeter() << "\t" << r.area() << endl;
	s = &c; s->show();
	s = &t; s->show();
	s = &r; s->show();
	cout << "形状\t周长\t面积" << endl;
	cout << "圆\t" << c.perimeter() << "\t" << c.area() << endl;
	cout << "三角形\t" << t.perimeter() << "\t" << t.area() << endl;
	cout << "矩形\t" << r.perimeter() << "\t" << r.area() << endl;
	return 0;
}
```
运行结果：
```
请输入圆的半径：5
请输入三角形的三边长：3 4 5
请输入矩形的相邻两边长：7 9
形状    周长    面积
圆      31.4159 78.5398
三角形  12      6
矩形    32      63
radius=5
a=3 b=4 c=5
width=7 length=9
形状    周长    面积
圆      31.4159 78.5398
三角形  12      6
矩形    32      63
```

多态性是面向对象程序设计的一个重要特征，是指不同类的对象对于同一消息的处理具有不同的实现。每个对象都有各自内部的状态和运动规律，在外界对象和环境的影响下对象本身根据发生的具体事件而做出不同的反应，对象能够根据自己的需要对所接受到的消息进行处理。  

多态性分为两类，一类称为编译时多态性，也称静态多态性，是指编译器在编译时就可以确定所要调用的是函数的哪一个具体实现，这种在编译时进行的函数调用与被调用函数的实现的对应被称为静态联编，也称静态绑定；另一类称为运行时多态性，也称动态多态性，是指编译时无法确定所调用的函数的哪一个实现，需要运行时才能够决定，这种在运行时将函数调用与具体实现代码相对应的方法称为的动态联编，也称动态绑定。  

编译时多态性通过重载实现，运行时多态性通过动态联编机制实现，其效率低于编译时多态性，虽然如此，但是动态联编为程序的具体实现带来了灵活性，因而使得面向对象程序设计更为方便，是面向对象的一个非常重要的特征。  

为了能够支持运行时多态性，可以使用虚函数，虚函数是从表现形式看是指那些被virtual关键字修饰的成员函数，其实现机制和调用方式与非虚函数不同，还有虚构造函数、虚析构函数等。具体的内容这里不作详细描述，在之后的内容以实例的形式说明。  

还有一种虚函数称为纯虚函数，是指在声明时被“初始化”为0的函数，0不表示其返回值或函数体，只起到形式上的作用，告诉编译程序这是纯虚函数，纯虚函数没有函数体，只起到为派生类提供一个统一接口的作用，在派生类中只有重新定义了虚函数的函数体，该函数才成为具有实际意义的函数。具有纯虚函数的类无法创建对象，因为它的纯虚函数无函数体，所以又把这种含有纯虚函数的类称为抽象类。

## 输入输出流

C++的输入输出是以流（字符序列）的形式进行的，输入输出时数据传送的过程，数据如流水一样从一处流到另一处，C++将此形象地称为流。C++的输入输出流分为以下三种：

1. 从键盘输入数据，输出到屏幕，称为标准设备的输入输出，简称标准输入输出
2. 以外存磁盘文件为对象进行的输入输出，称为文件输入输出
3. 对内存指定的空间输入输出，通常时指定一个字符数组作为存储空间，称为字符串输入输出

C++的流可以按照数据的格式可以分为文本流和二进制流。通常传送源程序文件和文本文件使用文本流，传送音频、图像、视频等文件时使用二进制流。也可以按照是否使用缓冲区分为缓冲流和非缓冲流，缓冲区是系统在主存中开辟的临时存放输入输出流信息的区域。通常情况下使用缓冲流。  

<<和>>本来是C++中的左位移运算符和右位移运算符，由于在文件isotream中进行了重载，使得能进行从流中获取数据的操作，即提取操作（>>），以及向流中添加数据的操作，即插入操作（<<）。

### 标准输入输出流

|类名|作用|类型|流类|
|-|-|-|-|
|cin|处理标准输入（键盘输入）|输入类|缓冲流|
|cout|处理标准输出（屏幕输出）|输出类|缓冲流|
|cerr|错误信息输出|输出类|非缓冲流|
|clog|日志信息输出|输出流|缓冲流|

函数格式如下：cout,setf(格式标准)，格式标志见下表：

|格式标志|作用|
|-|-|
|ios::left|左对齐|
|ios::right|右对齐|
|ios::internal|符号位左对齐、数值右对齐、中间由填充字符填充|
|ios::dec|十进制输出（默认）|
|ios::oct|八进制输出|
|ios::hex|十六进制输出|
|ios::showbase|整数基数输出|
|ios::showpoint|浮点整体输出|
|ios::uppercase|大写输出十六进制数及其科学计数法E|
|ios::showpos|正数符号输出|
|ios::scientific|科学计数法输出浮点数|
|ios::fixed|定点格式输出浮点数|
|ios::unitbuf|输出后刷新流|
|ios::stdio|输出后清除stdout和stderr|

|函数名|参数|返回值|作用|用例|
|-|-|-|-|-|
|cin.get<br>cin.getline|字符数组或字符指针、字符个数、终止字符|0、1、读取字符|如果没有传递参数，则返回读取到的字符；如果传递了参数，实参变量被赋读取到的字符，返回是否操作成功；字符个数为允许读取的字符数（包括终止符），遇到终止字符提前结束读取，默认终止字符为`\0`。|char=cin.get();<br>cin.get(char,20,'\n');|
|cout.put<br>cout.write|字符串、\*字符个数\*|0、1|put用于单字符输出，write用于字符串输出，且可以指定字符个数，默认为输出至终止符|cout.put('s');<br>cout.write("cppnb\n",4)|

### 文件操作与文件流

文件分为二进制文件和文本文件。文本文件以字节为单位，每字节为一ASCII码，代表一个字符，故又称字符文件：二进制文件又称内部文件或字节文件，是把内存中的数据按其在内存中的存储形式原样输出到磁盘上存放。在输入输出的过程中，文本文件需要进行转换，而二进制文件不需要进行转换。在文件操作时，需要引用头文件fstream。

#### 打开/关闭文件

```cpp title="打开/关闭文件"
定义文件流对象：
打开模式 文件流对象
打开文件：
文件流对象.open(路径,输入输出模式)
关闭文件：
文件流对象.close()
```

|打开模式|说明|
|-|-|
|ifstream|文件输入流对象（只读）|
|ofstream|文件输出流对象（只写）|
|fstream|文件输入输出流对象（读写）|

|输入输出模式|说明|
|-|-|
|ios::in|以读方式打开文件，若文件不存在，则自动建立新文件（输入流默认模式）|
|ios::out|以写方式打开文件，若文件已存在，则先删空文件中数据，然后再向文件写入数据；若文件不存在，则自动建立新文件（输出流默认模式）|
|ios::app|按写方式打开文件。写入的数据添加在文件尾。若文件不存在，则自动建立新文件|
|ios::binay|打开二进制文件，若不指定则打开文本文件|
|ios::trunc|打开文件并删除文件中原有内容|

#### 文本文件读写

输入两个文本文件路径，将源文件复制到目的文件。

```cpp
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main() {
    string f1, f2;
    cout << "输入源文件名：";
    cin >> f1;
    cout << "输入目标文件名： ";
    cin >> f2;
    ifstream infile(f1, ios::in);
    if (!infile) {
        cerr << "源文件不存在！" << endl;
        return 1;
    }
    ofstream outfile(f2, ios::out);
    char ch;
    while (infile.get(ch))outfile.put(ch);
    infile.close();
    outfile.close();
    cout << "文件成功复制！" << endl;
    return 0;
}
```

```cpp title="文本文件读写"
提取文件内容：
文件流对象.get(欲要提取到的字符)
文件流对象>>欲要提取到的字符
写入文件内容：
文件流对象.put(欲要写入的字符)
文件流对象<<欲要写入到的字符
```

#### 二进制文件读写

输入两个二进制文件路径，将源文件复制到目的文件。

```cpp
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main() {
    string f1, f2;
    char buff[4096];
    cout << "输入源文件名：";
    cin >> f1;
    cout << "输入目标文件名： ";
    cin >> f2;
    ifstream infile(f1, ios::out | ios::binary);
    if (!infile) {
        cerr << "源文件不存在！" << endl;
        return 1;
    }
    ofstream outfile(f2, ios::out | ios::binary);
    int n;
    while (!infile.eof()) {
        infile.read(buff, 4096);
        n = infile.gcount();
        outfile.write(buff, n);
    }
    infile.close();
    outfile.close();
    cout << "文件成功复制！" << endl;
    return 0;
}
```

```cpp title="二进制文件读写"
写入文件内容：
文件流对象.write(字符数组或字符指针,字节数)
读取文件内容：
文件流对象.read(字符数组或字符指针,字节数)
测试文件结束：
文件流对象.eof()
如果文件结束返回0，否则返回非0值
返回读入数据长度：
文件流对象.gcount()
返回最近一次输入所读入的字节数
```

#### 文件其它操作

输入学生信息，包括学号、姓名和成绩，以及文件相关的保存、查询和修改操作。

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
struct Student {
    string name;
    int id;
    float score;
};
void writeStudentInfo(const string& filePath, const Student& student) {
    ofstream outFile(filePath, ios::binary | ios::app);
    if (outFile.is_open()) {
        outFile.write(reinterpret_cast<const char*>(&student), sizeof(Student));
        outFile.close();
        cout << "学生信息已成功写入文件" << endl;
    }
    else {
        cout << "无法打开文件" << endl;
    }
}
void readStudentInfo(const string& filePath, int targetId) {
    ifstream inFile(filePath, ios::binary);
    if (inFile.is_open()) {
        Student student;
        bool found = false;
        while (inFile.read(reinterpret_cast<char*>(&student), sizeof(Student))) {
            if (student.id == targetId) {
                found = true;
                cout << "找到学生信息：" << endl;
                cout << "姓名: " << student.name << endl;
                cout << "学号: " << student.id << endl;
                cout << "分数: " << student.score << endl;
                break;
            }
        }
        if (!found) cout << "未找到学号为 " << targetId << " 的学生信息" << endl;
        inFile.close();
    }
    else {
        cout << "无法打开文件" << endl;
    }
}
void modifyStudentInfo(const string& filePath, int targetId, const Student& newInfo) {
    fstream file(filePath, ios::binary | ios::in | ios::out);
    if (file.is_open()) {
        Student student;
        bool found = false;
        while (file.read(reinterpret_cast<char*>(&student), sizeof(Student))) {
            if (student.id == targetId) {
                found = true;
                file.seekp(-static_cast<int>(sizeof(Student)), ios::cur);
                file.write(reinterpret_cast<const char*>(&newInfo), sizeof(Student));
                cout << "学生信息已成功修改" << endl;
                break;
            }
        }
        if (!found)cout << "未找到学号为 " << targetId << " 的学生信息" << endl;
        file.close();
    }
    else {
        cout << "无法打开文件" << endl;
    }
}
int main() {
    string filePath;
    cout << "请输入文件路径：";
    cin >> filePath;
    int f = 1, code;
    Student newStudent, modifiedStudent;
    while (f) {
        cout << "请输入命令（1.添加信息、2.查找信息、3.删除信息、0.退出:";
        cin >> code;
        switch (code) {
        case 1:
            cout << "请输入学生信息：" << endl;
            cout << "姓名: ";
            cin >> newStudent.name;
            cout << "学号: ";
            cin >> newStudent.id;
            cout << "分数: ";
            cin >> newStudent.score;
            writeStudentInfo(filePath, newStudent);
            break;
        case 2:
            int searchId;
            cout << "请输入要查找的学号: ";
            cin >> searchId;
            readStudentInfo(filePath, searchId);
            break;
        case 3:
            int modifyId;
            cout << "请输入要修改的学号: ";
            cin >> modifyId;
            cout << "请输入修改后的学生信息：" << endl;
            cout << "姓名: ";
            cin >> modifiedStudent.name;
            cout << "分数: ";
            cin >> modifiedStudent.score;
            modifyStudentInfo(filePath, modifyId, modifiedStudent);
            break;
        case 0:
            f = code;
            break;
        default:
            cout << "错误！" << endl;
        }
    }
    return 0;
}
```

```cpp title="文件相关操作"
读操作定位：
文件流对象.seekg(位移量,*参照位置*)
写操作定位：
文件流对象.seekp(位移量,*参照位置*)
输入文件中当前指针位置：
文件流对象.tellg()    返回类型为streampos
输出文件中当前指针位置：
文件流对象.tellp()    返回类型为streampos
忽略字符：
ignore(字符数，终止字符)
```

|参照位置符|说明|
|-|-|
|io3::beg或0|文件头|
|io3::cur或1|指针当前位置|
|io3::end或2|文件尾|

### 字符串流

字符串流是以内存中用户自定义的字符数组（字符串）为输入输出的对象，因此字符串流又称为内存流，其头文件为strstream。

```
定义字符串流对象：
打开模式 字符串流对象(字符数组,缓冲区大小)
已插入字符个数：
字符串流对象.pcount()
存储在字符数组中的字符串
字符串流对象.str()
```

|打开模式|说明|
|-|-|
|istrstream|字符串输入流对象（只读）|
|ostrstream|字符串输出流对象（只写）|
|strstream|字符串输入输出流对象（读写）|
