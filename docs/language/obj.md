---
title: C/C++开发与构建
subtitle: MakeFile/CMake/Lib/Dll
description: 集合与线性结构
---

# 开发应用

这里介绍C/C++进行实际项目开发时会进行应用的一些内容。包括构建工具CMake、静态库lib、动态链接库dll等。

## CMake

### 环境部署

CMake是一个用于管理源代码构建的工具，广泛用于C和C++语言，也可用于也可以构建其他语言的源代码。在其官网[CMake](https://cmake.org/download/)可以下载其安装包。下载安装包后，根据指引进行安装即可。

[官方文档](https://cmake.org/cmake/help/latest/)

### 使用

如果你使用过gcc/g++，对于的文件的编译是比较容易的，但是对于文件众多，结构复杂的项目而言，若是再使用gcc/g++，是极其痛苦的，因此可以使用CMake，其方便易用，而且移植性强。

现有一个学生管理系统程序，其中包含main.cpp主程序、student.h头文件和student.cpp源文件，还有一个图标logo.ico。我们将使用这个程序进行演示。点击此处下载程序[student](../file/student.zip)。

#### 基本

在项目文件夹创建CMake配置文件：CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.10)
project(Student)
add_executable(Student main.cpp student.h student.cpp)
```

这是一个最简单的CMake配置。接下来我们进行构建项目：

```powershell
cmake -B build -S .
```

这里`-B`参数指定构建文件夹，`-S`指定源文件夹，如果不指定，均默认为当前文件夹。

然后是编译/链接项目：

```powershell
cmake --build build
```

运行程序：

```powershell
.\build\Debug\Student.exe
```

#### 版本

但是我们需要指定项目、C及C++版本，可以修改CMake配置文件：

```cmake
cmake_minimum_required(VERSION 3.10)

project(Student VERSION 1.0)
add_executable(Student main.cpp student.h student.cpp)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED True)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
```

可以将项目版本打印出来，如果你使用过python，那么你知道使用`python --version`可以打印出python的版本。我们实现类似的效果。

修改CMake配置文件：

```cmake
cmake_minimum_required(VERSION 3.10)

project(Student VERSION 1.0)
add_executable(Student main.cpp student.h student.cpp)
configure_file(main.h.in main.h)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED True)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

target_include_directories(Student PUBLIC
                           "${PROJECT_BINARY_DIR}"
                           )
```

在项目目录新建文件`main.h.in`，其内容为：

```cpp
#define Student_VERSION_MAJOR @Student_VERSION_MAJOR@
#define Student_VERSION_MINOR @Student_VERSION_MINOR@
```

在项目主文件添加：

```cpp
#include "main.h"
......
int main() {
	std::cout << "StudentSystem Version " << Student_VERSION_MAJOR << "."
              << Student_VERSION_MINOR << std::endl;
	......
}
```

最后编译项目，运行，能够观察到打印了版本号。这样一来，只需要在CMake配置文件修改版本号，使得项目版本控制更清晰。

上面这段操作的具有过程是CMake有内置变量：PROJECT_VERSION_MAJOR（主要版本）和PROJECT_VERSION_MINOR（次要版本），当你定义了project(Student VERSION 1.0)后，这两个内置变量分别为1和0，configure_file(main.h.in main.h)操作将文件main.h.in内的对应变量名进行替换并且修改文件名为main.h，然后你在main.cpp引入头文件使用宏定义即可。当然，不一定是宏定义，其他方式也是可以的。

CMake最多支持四位版本号，这也和版本规范是契合的，依次是PROJECT_VERSION_MAJOR（主要版本）、PROJECT_VERSION_MINOR（次要版本）、PROJECT_VERSION_PATCH（修订版本）、PROJECT_VERSION_TWEAK（调整版本）。例如定义project(Student VERSION 1.5.4.8)可以分别对应这四个变量。

#### 自定义库和资源文件

在项目中，我们常常使用到自定义库，我们把student.h和student.cpp文件放到当前项目目录的stulib下，并且在stulib创建cmake配置文件，其内容为：

```cmake
add_library(stulib student.h student.cpp)
```

在主程序所在目录的cmake配置文件修改为：

```cmake
cmake_minimum_required(VERSION 3.10)

project(Student VERSION 1.0)
add_executable(Student main.cpp)
add_subdirectory(stulib)
configure_file(main.h.in main.h)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED True)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(RESOURCE_FILES "student.rc")

target_link_libraries(Student PUBLIC stulib)
target_include_directories(Student PUBLIC
                          "${PROJECT_BINARY_DIR}"
                          "${PROJECT_SOURCE_DIR}/stulib"
                          )
target_sources(Student PRIVATE ${RESOURCE_FILES})
```

其中student.rc是绑定的资源文件，其内容为：

```cpp title="rc"
#include "windows.h"

IDI_ICON1 ICON "logo.ico"
```

这样为生成的项目指定了图标。

#### 编译预处理

在编写代码时，我们常常用到编译预处理，例如条件编译#ifdef...#else...#endif，现在说明如何使用CMake指定定义选项。我们现在main.cpp文件中加入一段条件编译。

```cpp
#ifdef VERSIONSHOW
	std::cout << "StudentSystem Version " << Student_VERSION_MAJOR << "."
              << Student_VERSION_MINOR << std::endl;
#else
	std::cout << "StudentSystem" << std::endl;
#endif
```

并且修改CMake配置文件：

```cmake
cmake_minimum_required(VERSION 3.10)

project(Student VERSION 1.0)
add_executable(Student main.cpp)
add_subdirectory(stulib)
configure_file(main.h.in main.h)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED True)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(RESOURCE_FILES "student.rc")

option(VERSIONSHOW "Show StudentSystem version." ON)
if (VERSIONSHOW)
  target_compile_definitions(Student PRIVATE "VERSIONSHOW")
endif()

target_link_libraries(Student PUBLIC stulib)
target_include_directories(Student PUBLIC
                          "${PROJECT_BINARY_DIR}"
                          "${PROJECT_SOURCE_DIR}/stulib"
                          )
target_sources(Student PRIVATE ${RESOURCE_FILES})
```

如果直接编译，还是能够正常展示版本号，因为默认设置时开启的，当然，我们可以在CMake配置文件中修改ON为OFF，也可以在构建时修改：

```ps
cmake -DVERSIONSHOW=OFF -B build -S .
```

此时运行程序，会看到版本号不再展示。

#### 标准化

为了规范开发，在指定目录时希望能够清晰准确，我们在CMake配置文件有下面内容：

```cmake
target_include_directories(Student PUBLIC
                          "${PROJECT_BINARY_DIR}"
                          "${PROJECT_SOURCE_DIR}/stulib"
                          )
```

这是为了指定编译的库目录增加的，但是项目开发会涉及多个库的不同使用情况，因此，这样的配置并不好，可能会出现不必要的麻烦，所有可以用下面方式替代：

```cmake
target_include_directories(stulib
                           INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
                           )
```

这段代码写在库的CMake配置文件里。

在前面的编译中，代码只有在出现错误时进行报告，而警告内容是被忽略的，但是实际开发中，警告通常是需要的，可以在CMake配置文件中加入以下内容以显示警告：

```cmake
cmake_minimum_required(VERSION 3.15) #替换CMake版本为3.15

project(Student VERSION 1.0)
add_executable(Student main.cpp)
add_subdirectory(stulib)
configure_file(main.h.in main.h)

add_library(Student_compiler_flags INTERFACE)
target_compile_features(Student_compiler_flags INTERFACE cxx_std_11)

set(RESOURCE_FILES "student.rc")
set(gcc_like_cxx "$<COMPILE_LANG_AND_ID:CXX,ARMClang,AppleClang,Clang,GNU,LCC>")
set(msvc_cxx "$<COMPILE_LANG_AND_ID:CXX,MSVC>")

option(VERSIONSHOW "Show StudentSystem version." ON)
if (VERSIONSHOW)
  target_compile_definitions(Student PRIVATE "VERSIONSHOW")
endif()

target_link_libraries(Student PUBLIC stulib Student_compiler_flags)
target_include_directories(Student PUBLIC
                          "${PROJECT_BINARY_DIR}"
                          "${PROJECT_SOURCE_DIR}/stulib"
                          )
target_sources(Student PRIVATE ${RESOURCE_FILES})
target_compile_options(Student_compiler_flags INTERFACE
  "$<${gcc_like_cxx}:$<BUILD_INTERFACE:-Wall;-Wextra;-Wshadow;-Wformat=2;-Wunused>>"
  "$<${msvc_cxx}:$<BUILD_INTERFACE:-W3>>"
)

```

包括库的CMake配置也需要修改：

```cmake
add_library(stulib student.h student.cpp)
target_link_libraries(stulib PUBLIC Student_compiler_flags)
target_include_directories(stulib
                           INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
                           )
```

[最终文件](../file/studentend.zip)

#### CTest



## 静态库

库是写好的现有的，成熟的，可以复用的代码。现实中每个程序都要依赖很多基础的底层库，不可能每个人的代码都从零开始，因此库的存在意义非同寻常。

本质上来说库是一种可执行代码的二进制形式，可以被操作系统载入内存执行。库有两种：静态库（.a、.lib）和动态库（.so、.dll）。所谓静态、动态是指链接。

静态库是在链接阶段，会将汇编生成的目标文件.o与引用到的库一起链接打包到可执行文件中。因此对应的链接方式称为静态链接。

试想一下，静态库与汇编生成的目标文件一起链接为可执行文件，那么静态库必定跟.o文件格式相似。其实一个静态库可以简单看成是一组目标文件（.o/.obj文件）的集合，即很多目标文件经过压缩打包后形成的一个文件。静态库特点总结：

- 静态库对函数库的链接是放在编译时期完成的。
- 程序在运行时与函数库再无瓜葛，移植方便。
- 浪费空间和资源，因为所有相关的目标文件与牵涉到的函数库被链接合成一个可执行文件。

### 使用gcc/g++构建

首先我们介绍如何使用gcc/g++构建和使用静态库。

假设我们有一个简单的C文件`example.c`：

```c
#include <stdio.h>
void hello() {
    printf("Hello, world!\n");
}
```

使用`gcc`编译`example.c`为目标文件`example.o`：

```sh
gcc -c example.c -o example.o
```

使用`ar`命令将目标文件`example.o`打包成静态库`libexample.a`：

```sh
ar rcs libexample.a example.o
```

创建一个新的C文件`main.c`来使用这个静态库：

```c
void hello();

int main() {
    hello();
    return 0;
}
```

编译并链接`main.c`和静态库`libexample.a`：

```sh
gcc main.c -L. -lexample -o main
```

在上述命令中：

- `-L.`：表示链接库所在的目录为当前目录。
- `-lexample`：表示链接库的名称为`libexample.a`（`-l`后面跟的是库名，不包括前缀`lib`和后缀`.a`）。

执行生成的可执行文件：

```sh
./main
```

C++过程与C语言类似，只是使用`g++`来编译源文件。

### 使用CMake构建

假设我们有一个简单的C文件`example.c`：

```c
// example.c
#include <stdio.h>

void hello() {
    printf("Hello, world!\n");
}
```

创建一个`CMakeLists.txt`文件来配置CMake项目：

```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.10)
project(ExampleLibrary)

# 设置生成静态库
add_library(example STATIC example.c)

# 安装库文件
install(TARGETS example DESTINATION lib)

# 安装头文件
install(FILES example.h DESTINATION include)
```

如果有头文件`example.h`，内容如下：

```c
// example.h
#ifndef EXAMPLE_H
#define EXAMPLE_H

void hello();

#endif // EXAMPLE_H
```


创建一个目录来生成构建系统，并进入该目录：

```sh
mkdir build
cd build
cmake ..
cmake --build .
```

创建一个新的C文件`main.c`来使用这个静态库：

```c
// main.c
#include "example.h"

int main() {
    hello();
    return 0;
}
```

为这个新的程序创建一个CMakeLists.txt文件：

```cmake
# CMakeLists.txt for main program
cmake_minimum_required(VERSION 3.10)
project(ExampleProgram)

# 添加库的查找路径
link_directories(${CMAKE_SOURCE_DIR}/../build)

# 查找包含路径
include_directories(${CMAKE_SOURCE_DIR}/../include)

# 添加可执行文件
add_executable(main main.c)

# 链接静态库
target_link_libraries(main example)
```

然后生成构建系统并编译：

```sh
mkdir build
cd build
cmake ..
cmake --build .
```

运行程序：

```sh
./main
```

## 动态库

动态链接库（Dynamic Link Library，简称dll）是存储在一个独立文件中的一组函数和数据，这些函数和数据可以在多个应用程序之间共享。动态链接库的使用不仅节省了内存和磁盘空间，还简化了程序的维护和升级。

动态库特点总结：

-  动态库把对一些库函数的链接载入推迟到程序运行的时期。
-  可以实现进程之间的资源共享。（因此动态库也称为共享库）
-  将一些程序升级变得简单。
-  甚至可以真正做到链接载入完全由程序员在程序代码中控制（显示调用）。

### 使用gcc/g++构建

假设我们有一个简单的C文件`example.c`：

```c
// example.c
#include <stdio.h>

void hello() {
    printf("Hello, world!\n");
}
```

使用`gcc`编译`example.c`为目标文件`example.o`：

```sh
gcc -c -fPIC example.c -o example.o
```

其中，`-fPIC`选项表示生成位置无关代码（Position Independent Code），这是创建动态链接库所必须的。

使用`gcc`将目标文件`example.o`链接成动态链接库`libexample.so`：

```sh
gcc -shared example.o -o libexample.so
```

创建一个新的C文件`main.c`来使用这个动态链接库：

```c
// main.c
#include "example.h"

int main() {
    hello();
    return 0;
}
```

假设我们有头文件`example.h`，内容如下：

```c
// example.h
#ifndef EXAMPLE_H
#define EXAMPLE_H

void hello();

#endif // EXAMPLE_H
```

编译并链接`main.c`和动态链接库`libexample.so`：

```sh
gcc main.c -L. -lexample -o main
```

在上述命令中：
- `-L.`：表示链接库所在的目录为当前目录。
- `-lexample`：表示链接库的名称为`libexample.so`（`-l`后面跟的是库名，不包括前缀`lib`和后缀`.so`）。


运行程序前，需要设置库路径，使系统能够找到动态链接库。可以使用`LD_LIBRARY_PATH`环境变量：

```sh
export LD_LIBRARY_PATH=.
./main
```

```
Hello, world!
```

C++过程与C语言类似，只是使用`g++`来编译源文件。

### 使用CMake构建

假设我们有一个简单的C文件`example.c`：

```c
// example.c
#include <stdio.h>

void hello() {
    printf("Hello, world!\n");
}
```

创建一个`CMakeLists.txt`文件来配置CMake项目以生成动态链接库：

```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.10)
project(ExampleLibrary)

# 设置生成动态库
add_library(example SHARED example.c)

# 安装库文件
install(TARGETS example DESTINATION lib)

# 安装头文件
install(FILES example.h DESTINATION include)
```

如果有头文件`example.h`，内容如下：

```c
// example.h
#ifndef EXAMPLE_H
#define EXAMPLE_H

void hello();

#endif // EXAMPLE_H
```

创建一个目录来生成构建系统，并进入该目录：

```sh
mkdir build
cd build
cmake ..
```

在生成的构建系统目录中运行编译命令：

```sh
cmake --build .
```

这会生成动态链接库`libexample.so`（在Windows上是`example.dll`）。

创建一个新的C文件`main.c`来使用这个动态链接库：

```c
// main.c
#include "example.h"

int main() {
    hello();
    return 0;
}
```

为这个新的程序创建一个CMakeLists.txt文件：

```cmake
# CMakeLists.txt for main program
cmake_minimum_required(VERSION 3.10)
project(ExampleProgram)

# 添加库的查找路径
link_directories(${CMAKE_SOURCE_DIR}/../build)

# 查找包含路径
include_directories(${CMAKE_SOURCE_DIR}/../include)

# 添加可执行文件
add_executable(main main.c)

# 链接动态库
target_link_libraries(main example)
```

生成构建系统并编译：

```sh
mkdir build
cd build
cmake ..
cmake --build .
```

运行程序：

```sh
./main
```
