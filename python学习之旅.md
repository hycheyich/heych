

# Python之旅

## python软件安装

### 导入篇

1. 计算机原理

    ​	主板：集成电路。连接外围设备

    ​	CPU：核心运算单元

    ​	硬盘：断电可保存,读写速度慢

    ​	内存：断电不保存，读写速度很快

    ​	外设：外围设备，包括键盘鼠标，显示器。

2. 什么是编程语言？人与计算机可以沟通的语言。

3. 解释器和编译器

    ​	解释器：只在程序被执行时，才会把程序一条一条的解释成机器识别的字节码

    ​	编译器：一次性编译成二进制文件，计算机可以直接运行此二进制文件，执行速度快。

### python解释器安装

1. python解释器下载，安装

    ​	官网网站：http://www.python.org

2. pycharm编辑器下载

    ​	官网：<http://www.jetbrains.com/>

    安装完成后破解，可采用此教程链接破解。<https://www.jianshu.com/p/e8215dfafd3c>

3. pycharm 编辑器添加python解释器

    ​	文件->settings->project->project interpreter ->添加python解释器的下载路径。切记是python.exe

### git安装

1. git的安装：

    官网链接：[git](https://git-scm.com/)

### 码云

2. 码云的注册：

    - [码云](https://gitee.com/)

    - 登陆

    - 新建仓库---仓库名称  -路径 -介绍

        ![1564558807754](python学习之旅.assets/1564558807754.png)

    - 创建完成后在本地创建仓库并使用git打开。

        ![1564558820237](python学习之旅.assets/1564558820237.png)

    - 例如：

        ![1564558832780](python学习之旅.assets/1564558832780.png)

    - 在git上面输入  

        ```python
        git init    #初始化
        git add  .
        git commit -m "第一次上传" 
        git remote -m add origin  https://gitee.com/oldboy_python_full_stack_S25/19072625007  #需要输入码云的账号密码
        git push -u origin master 
        ```

        

    - 若成功的话会出现

        ![1564558844938](python学习之旅.assets/1564558844938.png)

    - 成功后即可在码云上面查看自己上传的文件。

         

#### 1.失败解析：

1. 输入码云密码错误的解决办法：

    - 在控制面板-> 用户账号->凭据管理->windows凭据->普通凭据->即可查看和编辑密码

        ![1564558859651](python学习之旅.assets/1564558859651.png)

    - 修改完成后即可上传.

2. 如果更改本地文件仓库，或者创建新的文件仓库出现的问题:

    ![1564558872565](python学习之旅.assets/1564558872565.png)

3. 删除码云/github上的文件

    ```python
    git  rm  -r   --cached filename #（要删除的文件）
    git commit -m "删除文件"  #无论上传还是下载都需要打标签
    git push origin master  #推送到码云上面
    ```

4. git commit 没有添加-m

    ![1564558884282](python学习之旅.assets/1564558884282.png)

    ```
    解释：
    	没有设置 -m 选项，Git 会尝试为你打开一个编辑器以填写提交信息。 如果 Git 在你对它的配置中找不到相关信息，默认会打开 vim。屏幕会像这样：
    ```

5. git绑定码云的教程

    ![1564558898908](python学习之旅.assets/1564558898908.png)

     

#### 2.git进阶教程

​	官网链接：[git](<https://www.runoob.com/git/git-tutorial.html>)

1. 克隆仓库

    ```python
    git clone <repo>  <directory>  #repo:Git仓库  directory:本地目录
    ```

    ![1564558943377](python学习之旅.assets/1564558943377.png)

2. 查看项目当前状态

    ```python
    git add #将文件添加到缓存中
    git status #查看项目当前状态
    ```

3. 查看提交历史

    ```python
    git log
    git log --oneline #查看历史记录
    git log  --graph   #查看分支
    git log  --reverse #逆向显示所有日志    eg: git log --reverse --oneline
    git log  --author  #查找知定用户提交日志    eg:git log --author=Linus --oneline -5
    
    ```

    ![1564558953793](python学习之旅.assets/1564558953793.png)

4. Git标签

    ```python
    git tag -a v1.0 
    ```

## python学习

#### 1.python的历史

​	2004年  Django 框架诞生了。web框架。

#### 2.python2，3对比

​	1.1 python2：

​			源码不统一，有重复的功能代码（由不同的开发人员实现功能）

​	1.2 python3：

​			源码统一，没有重复的功能代码

#### 3.python是什么？

​		首先讲解什么是编程语言，编程语言就是人与计算机通过的语言。

​		编程语言主要从以下几个角度进行分类：编译型，解释型，静态语言和动态语言，强类型定义语言，弱类型定义语言。

1. 编译型与解释型

  - **编译型**是把源程序的每一条语句都编译成机器语言，并保存成二进制文件，这样运行时，计算机可以直接以机器语言来运行此程序，速度很快。（只翻译一次，执行速度快，开发速度慢）
  - **解释型**是直在执行程序时，才一条一条的解释成机器语言给计算机来执行，所以运行速度时不如编译后的程序运行的快。（逐行翻译，执行速度慢，开发速度快）

2. python是什么语言

![1564559153753](python学习之旅.assets/1564559153753.png)

| 编译型   | 解释型     | 混合型 |
| -------- | ---------- | ------ |
| C        | Javascript | java   |
| C++      | python     | c#     |
| GO       | ruby       |        |
| Swift    | PHP        |        |
| Obiect-C | perl       |        |

3. python的种类
    - cpython：python的官方版本，使用C语言实现，使用最为广泛，CPYTHON实现会将源文件（py文件）转换成字节码文件（pyc文件），然后运行在python虚拟机上。
    - jyhton：python的java实现，jython会将python代码动态编译成java字节码，然后再JVM上运行
    - lronpython：python的C#实现，lronPython会将python代码编译成C#字节码，然后再CLR上运行。
    - pypy：python实现python，将python的字节码再编译成机器码

## 第一章    Python基础数据类型

### 1.变量

#### 	1.1  什么是变量

​		Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。

​		在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

1. 变量--输出
2. 变量就是将一个临时的值存储在内存中
3. 变量可以多次重复使用。

```python
a = 1 #声明变量
a #变量的名字
= # 赋值
1 # 值

```

#### 1.2  变量的命名规则

#变量定义规则：

1. 变量名由数字，字母，下划线组成
2. 不能以数字开头，不能使用python中关键字
3. 不能使用中文和拼音
4. 区分大小写
5. 变量名要具有描述性
6. 推荐写法
7. 驼峰体
8. 下划线（官方推荐）

#### 1.3 常量

<!--常量-->

常量

1. <!--什么是常量，常年不变更的量-->
2. <!--python语言中没有常量。-->
3. <!--常量在配置文件中声明使用-->

### 2. 标准数据类型

#### 2.1 整型

- 数字 ——int
- 用于计算，进行比较大小# 在赋值的时候先执行等号右侧内容；在执行等号左侧的
- a = 10 + 2  b = 10 / 2  print(a,b)
- Pyrhon 3 除法的时候返回的是小数（浮点型）
- Python 2 除法的时候返回的是整数（向下取整）
- 字符串之间可以加 字符串可以和数字之间相乘

#### 2.2 字符型

- 字符串 数字（整型）布尔值 列表 元组 字典 集合
- 字符串 ——str
- 字符串用于存储一些数据，在Python中只要用""内的都看作字符串
- """ """ 内的是字符串 不赋值不运行，占据内存空间

#### 2.3 布尔型

- 布尔值——bool
- 用于逻辑判断
- True与False

#### 2.4 python的数据类型

Python3 中有六个标准的数据类型：

- Number（数字）
- String（字符串）
- List（列表）
- Tuple（元组）
- Set（集合）
- Dictionary（字典）

Python3 的六个标准数据类型中：

- **不可变数据（3 个）：**Number（数字）、String（字符串）、Tuple（元组）；
- **可变数据（3 个）：**List（列表）、Dictionary（字典）、Set（集合）。

### 3 控制流语句

- if 条件:

- ​    缩进 官方推荐4个空格，Tab    

- 且 空格和Tab不能混合使用 

- if else 二选一

- if 条件:

- ​    结果

- else:

- ​    结果

    

- if elif elif 多选或者不选

- elif--再如果

    

- if elif elif else 多选一必选else 放在最后

    

- if if if 多个条件选择多个

- if 条件

- ​    结果

- if 条件

- ​    结果

- if 条件

- ​    结果

### 4.while循环

```python
while True:
    print(1111)
    print(222)
    print(4344)
    
数字中非0的都为True

while False:
    print(1111)
    print(222)
else:
    print(4344)
```

break 终止当前循环；

continue 跳出当前循环继续下次循环

break和continue的相同之处是以下的代码都不执行

### 5. 字符串格式化

​    字符串格式化三种 ：    %s是占的字符串类型的位置。

```python
s = """
你的姓名：%s
你的年龄：%s
"""
name = input("name")
age = input("age")
print(s%(name,age))
#变种1
name = "好嗨哦"
s = f"今天下雨了{name}"
print(s)
#变种2
name = input(">>>")
s = f"今天下雨了{name}"
print(s)
#变种3
s = f"今天下雨了{input('>>>')}"
print(s)
#format格式化输出
#第一种方式
s = '我叫{}，今年{}，性别{}'.format('赫翊辰',25,'男')
print(s)
#第二种方式

s1= '我叫{0}，今年{1}，性别{2}'.format('赫翊辰',25,'男')
print(s1)
#第三种方式
s1= '我叫{name}，今年{age}，性别{sex},我依然叫{name}'.format(name = '赫翊辰',age = 25,sex = '男')
print(s1)

```

f只在python3.6以上才可以使用

### 6.运算符

#### 	6.1 算术运算符 

- ​		+   -     *    /       //(整除)    **  幂（次方）  %（求模  取余）
- ​		python3:    5/2 = 2.5     python2   5/2=2

#### 	6.2 比较运算符

​		 >    <    ==   !=   >=  <=

#### 	6.3 赋值运算符

 	=   += (自加)   -=（自减）   *=（自乘）   /=（自除）  **= （幂等于）  //=（整除等于）  	%=（模等于）

#### 	6.4 逻辑运算符

- ​		and（与）   or（或） not（非） 
- ​		and 都为真时，取and的后面的值，and都为假的时候取and的前面的值，and一真一假时，取假的。
- ​	**0、’ ‘、[]、()、{}、None、False在布尔上下文中为假；其它任何东西都为真**		
- ​	or 都为真的时候取or前面的值，or都为假的时候取or后面的，or  一真一假时取真的。

- ​	优先级：（）>not>and>or

```python
print( 9 and 0 or not False and 8 or  0 and 7 and False)
```

#### 	6.4 成员运算符

- ​		in  存在
-  		not  in  不存在

```python
#存在返回True
s = "sbsd"
print("sb" in s)
#不存在返回False
s = "sbsd"
if "sb" not in s:
    print("True")
else:
    print("False")
```

### 7. 编码

python2中默认用ASCII   不支持中文  使用7位，预留一位扩展位  （美国）。

#### 7.1 Ascii

- Ascii 主要存英文，不支持中文
- Ascii 占一个字节

#### 7.2 Gbk

- Gbk 存有包存中文，英文 包含Ascii
- 中文占用两个字节 英文一个字节

#### 7.3 Utf-8

- utf-8 当下最流行的编码集，全兼容
- utf-8 英文一个字节 欧洲两个字节 亚洲三个字节
- unicode 中英文和中文都占用四个字节
- win - 编码 gbk
- linux - 编码 utf-8
- mac - 编码 utf-8

#### 7.4 单位转换

​	1字节= 8个二进制位

​	1Bytes  = 8 bit

​    1024 KBytes = 1MB

​    1024MBytes  =  1GB

​	1024GBytes  = 1TB   常用

​	1024TBytes   = 1PB

​	1024PBytes  = 1EB

---

### 8.基础数据类型详讲

#### 8.1  Number（数字）

1. **Python3 支持 int、float、bool、complex（复数）。**
2. **在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long**
3. **内置的 type() 函数可以用来查询变量所指的对象类型。**

```python
>>> a, b, c, d = 20, 5.5, True, 4+3j
>>> print(type(a), type(b), type(c), type(d))
<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
```

**注意：*** 在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。*

#### 8.2  字符串

在python中引号引起来的就是字符串，字符串是用来存储少量输

str = "heyichen"

str[4] 索引值不能超过字符串的范围

##### 8.2.1  字符串切片

str[0:6:1]   0 表示起始位置   6表示终止位置   1步长  默认步长为1 

从左向右  0 1 2 3 4 

从右向左-4  -3  -2  -1

1表示从左向右   -1表示从右向左

还可以这样表示： 

```python
# str = "niaho"# print(str[0:-1:1])
```

切片时，终止位置和起始位置可以超过索引范围

##### 8.2.2 字符串的方法

字符串是不可变的数据类型，字符串是有序的

- 变量+ .upper（） 全部大写

- 变量+ .lower（） 钱全部大写

- 变量+ .startswith( ‘  ’) 引号内用字符串，以什么为开头，支持切片，返回布尔值

- 变量+ .endswith（‘ ’）引号内用字符串，以什么为结尾，支持切片，返回布尔值

- 变量+ .count（‘ ’）引号内用字符串，统计某个字符串在变量内出现的次数

- 变量+ .strip（）/( ' ')     没有用‘ ‘ 时脱去字符串两端的空格，当引号内有容时，去除头尾两端的指定内容

- 变量 +.split（）/（’ ‘） 默认是用空格 ，换行符，制表符分割 生成列表。

    引号内有内容时，以内容分割，不保留分割内筒。引号后加数字可以控制分割字数默认时全部分割。

- 变量+ .replace（’ ‘，’ ‘） 替换功能 ，第一个引号内要放被替换的内容，第二个放替换后的内容，默认全部替换。后面加数字可以控制替换的次数。

- 变量  + .format（’ ‘） 格式化输出 可以在{} {} 内按顺序填充

    亦可以按照索引填充，也可以指定填充

- 变量+ .isdigit（）判断字符串内容是否全是数字，但是会将圈数字也看作数字

- 变量+ .isdecimal（） 判断字符串内是否是10进制

- 变量+ . isalnum（） 判断是不是由数字，字母，中文

- 变量+ .isalpha（） 判断是不是字母，中文。

- str . capitalize( ) 首字母大写

- str . title () 每个单词首字母大写

- str . swapcase() 大小写转换

- str . center(数字,"*") 居中 及填充

- str .find(x) 通过元素查找索引 查找不到是返回-1

- str.index(x) 通过元素查找索引 查不到时报错

- 连接符 . join（str） 拼接 可以将列表转换成字符串

- 字符串的加 乘的操作都是开辟新的空间

```python
"""
print(s.upper()) #全部为大写
print(s.lower()) #全部为小写
s.startswith("a",2,6)  #2是索引位置 6终止位置  以什么开头
s.endswith("n",3,7)   #以什么结尾
s.count()   #统计相同元素个数
脱： 
  字符串头尾两端的空格和换行符以及制表符  去掉头尾两端的空格和换行符以及制表符
  s.strip()
分割：
s.split()
替换：
	s.replace()

"""
#以什么结尾
s = "heychen"
s1 = s.endswith("n",3,7)
print(s1)
#脱
s = "       heych       "   
if s.strip() =="heych":   
    print("1")
else:
    print(2)              #输出    1
 #分割
s = "h e y c h"
#分割：以空格和换行符以及制表符进行分割
s1 = s.split()
print(s1)      #输出： ['h', 'e', 'y', 'c', 'h']

s1 = s.split("l",maxsplit=1)   maxsplit 表示最大切几刀   可以通过指定方式进行切割
```

capitalize()首字母大写、

```python
str = "sanjsanjan+dsa+asA+SSDduisad"
print(str.capitalize())
```

swapcase()大小写反转

```python
str = "sanjsanjan+dsa+asA+SSDduisad"print(str.swapcase())
D:\python解释器\python.exe D:/pycharm_program/venv/第一天作业/每日练习.py
SANJSANJAN+DSA+ASa+ssdDUISAD

Process finished with exit code 0
```

center（）返回一个源字符串居中，并使用空格填充至长度width的新字符串。默认填充的字符为空格。

title()  非字母隔开单词首字母大写

```python
str = "sanjs  anjan+dsa+a sA+SS Ddu isad"
print(str.title())


D:\python解释器\python.exe D:/pycharm_program/venv/第一天作业/每日练习.py
Sanjs  Anjan+Dsa+A Sa+Ss Ddu Isad

Process finished with exit code 0

```

##### 8.2.3 is系列

```python
#  isalnum  判断是不是字母，数字，中文
s = "alse"
print(s.isalnum)
# isalpha 判断是不是字母，中文
print(s.isalpha())
#isdigit   判断字符串中是不是全都是阿拉伯数字
print(s.isdigit())
# 字符串.isalnum()    所有字符都是数字或者字母，为真返回 Ture，否则返回 False。
# 字符串.isalpha()     所有字符都是字母，为真返回 Ture，否则返回 False。
# 字符串.isdigit()     所有字符都是数字，为真返回 Ture，否则返回 False。
# 字符串.islower()    所有字符都是小写，为真返回 Ture，否则返回 False。
# 字符串.isupper()    所有字符都是大写，为真返回 Ture，否则返回 False。
# 字符串.istitle()     所有单词都是首字母大写，为真返回 Ture，否则返回 False。
# 字符串.isspace()    所有字符都是空白字符，为真返回 Ture，否则返回 False。
# 字符串.isdecimal()   判断是不是十进制，为真返回True ，否则返回False。
s = " "
print(s.isspace())
"""
len()函数：
len() 方法返回对象（字符、列表、元组等）长度或项目个数。
"""
```

#### 8.3 列表

- 列表可以存储数据，数据存储量大，且可以存储不同类型的数据
- 定义一个列表 Lst = 【1，2，“alex”，True】
- 列表可以看做一个容器
- 列表内可以存放列表
- 在其他语言中称作数组
- 列表是一种有序的容器，支持索引，列表是一种可变的数据类型修改时不会开辟新空间，原地修改
- 列表是可变操作类型，查看动作为空
- 字符串中只要占用一个位置的就是一个元素
- 列表中只要用逗号分隔的就是一个元素
- 列表  + .append（） 追加 在最末尾的地方进行添加，（）内填写追加的内容
- 列表 + .insert（位置，“内容”） 插入，在指定的位置进行添加，尽量少使用。
- 列表 +.extend（）迭代添加 及一个一个添加 （ 比如把字符串拆分成一个一个添加）整型和bool是不可迭代对象/也可以用for循环实现
- 列表 +.remove（）括号内写需要删除的内容/不是索引，从左向右，只能删除符合条件的第一个元素
- 列表 +.pop（） 删除类表内的最后一位/默认，pop拥有返回值，返回的值是删除的内容。括号内也可以添加索引，用**print（repr（））可以查看内容的原生态**
- 列表 +.clear（） 清空类表的内容，无返回值
- del + 列表【】 直接从内存中删除，可以删除整个列表，也可以按照索引删除指定的元素，可以删除切片，也可以按步长删
- 列表的修改通过索引进行指定的修改 列表[ ]=' ' 在内存中新开辟空间，只是修改的地址
- 也可以通过切片进行修改，当切片替换是迭代替换，可以多替换，也可以少替换，不能使用整型和bool
- 通过步长（不为1）进行修改时，必须要一一对应，不能够超出
- 列表的查 for循环 索引
- 列表的嵌套，需要将列表内的列表整体看做一个元素
- lis （‘12345’） 迭代定义
- lis.index ( ) 通过元素查找索引
- lis . sort   排序  默认升序
- lis . sort( reverse = True) 排序 降序
- lis .reverse( ) 反转 
- 【：：-1】反转不修改原数据
- 列表的加 【1,2】+【1,2】=【1,2,1,2】
- 列表的乘 【1,2】* 2  = 【1,2,1,2】 且 Id是相同的
- 列表在进行乘法的时候元素是公用id的

##### 8.3.1 列表定义

- 有序

- 可变

- 支持索引

    ```
    列表：支持的数据类型较多，存储数据，字符串，数字，布尔值，列表，集合，元祖，字典
    python 32位的限制是536870912个元素
    python 64位的限制是1152921504606846975个元素
    ```

    ```python
    #定义一个列表
    lst = ["alex",123,True]   #用逗号分割开来就是一个元素
    id（）获取对象的内存地址
    isinstance （）来判断一个对象是否是一个已知的类型
    ```

    ```python
    isinstance() 与 type() 区别：
    
    type() 不会认为子类是一种父类类型，不考虑继承关系。
    
    isinstance() 会认为子类是一种父类类型，考虑继承关系。
    
    如果要判断两个类型是否相同推荐使用 isinstance()。
    ```

##### 8.3.2 列表的内存分配

![1564705352705](../python%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/day03.assets/1564705352705.png)

列表可以进行修改，和字符串不同。

##### 8.3.3    列表索引

```python
lst = ["nihao","zhourunfa","zhoujielun"]
print(lst[0])
print(lst[1])
#注意:列表是可以进行修改的,这里和字符串不一样
lst[2] = "王健林"
print(lst)
```

字符串修改   （重点：字符串不允许修改）

```python
s = "王思聪"
s[0] = "李"
print（s）
"""
  File "D:/pycharm_program/venv/day01/day01.py", line 479
    print（s）
           ^
SyntaxError: invalid character in identifier

"""
```

##### 8.3.4 列表的切片

```python
lst = ["麻花藤", "王剑林", "马芸", "周鸿医", "向华强"] 
print(lst[0:3])
print(lst[:3])
print(1::2)
print(lst[2::-1])   # -1表示从右向左打印输出    1，表示从左向右打印输出。不输入时，默认为1
print(lst[-1::-1])
从左往右是  0 1 2  
从右往左是  -1 -2 -3
```

```python
练习：
"""
li = [1, 3, 2, "a", 4, "b", 5,"c"]
通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
通过对li列表的切片形成新的列表l5,l5 = ["c"]
通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
"""
li = li = [1, 3, 2, "a", 4, "b", 5,"c"]
print(li[0:3])
print(li[3:6])       <=起始位置   <终止位置
print(li[1::2])
print(li[-1])
print(li[-3::-2])
```

##### 8.3.5列表的增删改查

###### 8.3.5.1 增

注意：list和str是不一样

追加模式：

```python
lst = ["麻花藤", "林俊杰", "周润发", "周芷若"] 
lst.append("123")
print(lst)
```

```python
练习：输入用户信息,添加到列表中
lst = []
while True:
    content = input("输入信息")
    if content.upper()=="Q":
        break
    lst.append(content)
print(lst)
```

插入模式

```pytho
lst = ["麻花藤", "张德忠", "孔德福"]
lst.insert(0,"heyichen")
print(lst)
##表示在首位插入字符串   insert  第一个参数表示位置，及索引下标位
```

迭代添加

```python
#extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
lst = ["王志文", "张一山", "苦海无涯"]   #简单来讲就是两个列表的拼接，在原有列表的基础上，追加另外一个列表
lst.extend(["nihao","nishishei"])
print(lst)
```

###### 8.3.5.2 删除

```python
pop 通过下标删除元素(默认删除最后一个)

lst = ["麻花藤", "王剑林林", "李李嘉诚", "王富贵"]   pop返回被删除的值
print(lst)
lst.pop()
lst.pop(2)   通过下标进行删除


remove 通过元素进行删除             返回none
lst.remove("王富贵")
###如果删除不存在的字符串，会报错。

补充：
del 删除从第二个元素开始，到第4个为止的元素（不包括尾部的元素）
str = [0,1,2,3,4,5,6]
del str[2:4]
print(str)

del 可以删除整个数据对象（列表。集合）
删除后，找不到对象
"""
注意：del是删除引用(变量)而不是删除对象(数据)，对象由自动垃圾回收机制（GC）删除
"""

```

清空

```python
clear()
lst = ["麻花藤", "王剑林", "李嘉诚", "王富贵"]
lst.clear()
print(lst)

结果:
[]

```

```python
###练习

"""
写代码，有如下列表，按照要求实现每一个功能
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
请删除列表中的元素"ritian",并输出添加后的列表
请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
请删除列表中的第2至4个元素，并输出删除元素后的列表
"""
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
print(li.extend(["ritian"]))
print(li.insert(-1,"ritian"))
print(li)

print(li.pop(1))
print(li)


print(lst.pop(2:4))
del li[1:5]
print(li)


```

###### 8.3.5.3 修改

索引切片修改

```python
# 修改 
lst = ["太白", "太黑", "五色", "银王", "⽇天"] 
lst[1] = "太污"   # 把1号元素修改成太污 print(lst) 
lst[1:4:3] = ["麻花藤", "哇靠"]     # 切片修改也OK. 如果步长不是1, 要注意元素的数 
print(lst) 
lst[1:4] = ["我是哪个村的村长王富贵"]  # 如果切片没有步长或者步长是1. 则不用关心个数 
print(lst)

```

###### 8.3.5.4 查询

列表是一个迭代对象，所以可以进行for循环

```python
lst = ["麻花藤", "王剑林", "李嘉诚", "王富贵"]
for i in lst：
	print(i)

```

```python
#练习
"""
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
将列表li中第三个元素修改成'taibai'
将列表li中第四个元素修改成'女神'
将列表li中前三个元素修改成'alex1,alex2,alex3'
"""

li[2] = "taibai"
li[3] = "女神"
li[0:3] = "alex1,alex2,alex3"
```

##### 8.3.6 列表嵌套

注意:采用降维操作,一层一层的看就好

```python
lst = [1,'太白','wusir',['麻花疼',['可口可乐'],'王健林']]
#找到太白的白字
print(lst[1][1])
#将wusir拿到,然后首字母大写 在扔回去
lst[2] = lst[2].capitalize()
print(lst)
lst[1]=lst[1].replace("白，黑")
# 把麻花疼换成麻花不疼
lst[3][0] = lst[3][0].replace('疼','不疼')
print(lst)
```

#### 8.4 元祖

- 定义方式 tu  = （1，2，3）与类表功能相仿
- 有序，不可变的，不能进行增删改
- 支持查询，可以视为不能修改的列表
- 元组支持的方法 
- 统计和获取索引
- 元组 + .index（）查询括号内元素的索引，只查找左侧第一个
- 因为元组是不可变的，所以一般用于保存重要文件，存在配置文件中，元组也可以嵌套
- 元组的加法（1,2）+（1,2）=（1,2,1,2）
- 元组的加法（1,2）* 2 =（1,2,1,2）与列表相同

##### 8.4.1 元祖定义

1对于容器型数据类型list，无论谁都可以对其增删改查，那么有一些重要的数据放在list中是不安全的，所以需要一种容器类的数据类型存放重要的数据，创建之初只能查看而不能增删改，这种数据类型就是元祖。

元祖:俗称不可变的列表,又被成为只读列表,元祖也是python的基本数据类型之一,

用小括号括起来,里面可以放任何数据类型的数据,查询可以,循环也可以,切片也可以.但就是不能改.在python中关键字是tuple

```python
tu = ('我','怎么','这么','可爱')
tu1 = tu[0]
print(tu1)

for i in tu:   #循环访问
  print(i)
 

tu2 = tu[0:3]
print(tu2)   #切片


###元祖不可以修改
eg:
  
tu[0] = "ni"
print(tu)

Traceback (most recent call last):
  File "D:/pycharm_program/venv/day01/day01.py", line 535, in <module>
    tu[0] = "ni"
TypeError: 'tuple' object does not support item assignment
  

```

关于不可变, 注意: 这里元组的不可变的意思是子元素不可变. 而子元素内部的子元素是可以变, 这取决于子元素是否是可变对象.

元组中如果只有一个元素. 一定要添加一个逗号, 否则就不是元组

```python
#若子元素是列表的话，访问子元素中的值，相当于访问列表，可以改变，如果子元素是元祖，则不可以改变
tu = ('我','怎么','这么','可爱',["nihao","123"])
print(tu)
tu[4][1]="你好"
元祖的访问和列表类似，只不过不可以随意更改元祖的值

tu = tuple()	空元祖	
tu = (1)	不是元祖
tu = (1, )	是元祖	只有一个元素不是元祖, 加一个逗号就是了

"""
tu.index(): 通过元素找索引,可以切片,找到该元素则返回第一个元素索引值,找不到则报错
tu.count(): 统计某个元素在元祖中出现的次数
len(tu): 计算元祖元素的个数
max（tuple）返回元祖中元素最大值
min(tuple) 返回元祖中元素最小值
tuple（seq）将列表转换为元祖
"""
tu = (1,2,3,['a','b',1],'str',2,2) 
print(tu.count(2))  #3

tu = (1,2,3,['a','b',1],'str',2,2) 
print(len(tu))  #7

```

```python
#在python2中
无关闭分隔符
任意无符号的对象，以逗号隔开，默认为元组，如下实例：
 
print 'abc', -4.24e93, 18+6.6j, 'xyz'
x, y = 1, 2
print "Value of x , y : ", x,y

```

##### 8.4.2 元祖使用

​	将一些非常重要的不可让人改动的数据放在元祖中，只供查看

#### 8.5 dict 字典

- 定义 dic = {“key”：“value” }
- 作用：存储数据，数据量大，将数据和数据之间起到关联作用
- 字典中所有操作都是通过键（key）
- 键 必须是不可变的数据类型（可哈希），且唯一。
    - 不可变数据类型包括。整形 字符串 元组 布尔值
- 值 任意。不可哈希的就是可变的数据类型
- 字典是可变 无序的数据类型
- get 获取 dic.get("key")  可以获取值
- dic 【“key"】 = value(值) 添加的是一个键值对/一定会增加
- dic.setdefault （“key”，“value”）【有则不添加，无则添加】由键来决定
- dic.setdefault 添加分为两步
    - 第一步先去字典内查询是否有这个键
    - 第二部如果返回的是值，不添加。如果是None则添加
- dic.pop（“key”） 通过键来删除，有返回值，返回的是被删除键的值
- dic.clear 清空
- del dic 删除整个容器
- del dic 【“key”】通过键来删除
- **字典中没有 remove**
- dic【“key”】 = “value”  有则改无则加
- dic . update（{“key”：“value”}）有则改无则加 括号内的字典级别高于上一级别
- dic . popitems 随机删除 / Python 3.6默认删除最后一个 有返回值，为被删除的键值对
- dic .fromkeys（“变量”，【】）批量创建键值对 新开辟空间
- 迭代创建键值对，键是迭代的，值是共用的值是可变数数据类型就容易有坑
- 字典和集合在遍历时不能修改长度
- get 获取 dic.get("key")  可以获取值  不在返回None
- dic.setdefault （“key”） 查询不到返回None 不能迭代查询
- print（dic【‘key’】）  查询不到报错
- for i in dic  
    - print（i） 获取的是每一个键
    - print(dic.get(i)) 获取每个值
- dic.keys（） 获取到是键的一个高仿列表
- dic.values（）获取到值的一个高仿列表 
- 高仿列表支持迭代，不支持索引
- dic.items（）  获得的是一个键与值关联的高仿列表，内容为元祖
- 字典不能够当做字典的键，只能当做自己的值
- 字典的查找的时候按照键层来查找

列表可以存储大量的数据类型，但是只能按照顺序存储，数据与数据之间关联性不强。

所以咱们需要引入一种容器型的数据类型，解决上面的问题，这就需要dict字典。

字典(dict)是python中唯⼀的⼀个映射类型.他是以{ }括起来的键值对组成.

在dict中key是 唯⼀的.在保存的时候, 根据key来计算出⼀个内存地址. 然后将key-value保存在这个地址中.

这种算法被称为hash算法, 所以, 切记, 在dict中存储的key-value中的key必须是可hash的

可以改变的都是不可哈希的, 那么可哈希就意味着不可变. 这个是为了能准确的计算内存地址⽽规定的.

##### 8.5.1 字典的定义

**已知的可哈希(不可变)的数据类型: int, str, tuple, bool 不可哈希(可变)的数据类型: list, dict, set**

**语法：** 

```python
#语法：
{"key1":1,"key2":2,"key3":3}

"""
注意：
key必须是不可变（可哈希）的，value 没有要求，可以保存任意类型的数据
"""

```

```python
#例子
dic = {123:456,True:999,"id":1,(1,2,3):"麻花藤"，"tu":[1,2,3]}
print(dic[123])
print(dic["id"])
print(dic[(1,2,3)])
# 不合法
# dic = {[1, 2, 3]: '周杰伦'} # list是可变的. 不能作为key
# dic = {{1: 2}: "哈哈哈"} # dict是可变的. 不能作为key
dic = {{1, 2, 3}: '呵呵呵'} # set是可变的, 不能作为key

```

注意：

```
dict保存的数据不是按照我们添加进去的顺序保存的. 是按照hash表的顺序保存的. ⽽hash表 不是连续的. 所以不能进⾏切片⼯作. 它只能通过key来获取dict中的数据
```

##### 8.5.2 字典的增删改查

###### 8.5.2.1 增

增加有两种：

一种是  赋值：

另一种是 setdefault  

```python
#定义字典
dic = {}
dic["name"]="heyichen"
dic["age"]=19
print(dic)
#如果没有出现过key-value则采用setdefault
s1 = dic.setdefault("王菲")
print(s1)
print(dic)
结果：
"""
{'name': 'heyichen', 'age': 19}
None
{'name': 'heyichen', 'age': 19, '王菲': None}
# 我们使用setdefault这个方法 里边放的这个内容是我们字典的健,这样我们添加出来的结果
就是值是一个None

"""
### 字典中的值无法修改
s1 = dic.setdefault("王菲")
print(s1)
print(dic)
s2 = dic.setdefault("王菲","258")
print(dic)
结果：
"""
{'name': 'heyichen', 'age': 19, '王菲': None}
{'name': 'heyichen', 'age': 19, '王菲': None}
# 这样就是不会进行添加操作了,因为王菲在dic这个字典中存在
# 总结: 当setdefault中第一个参数存在这个字典中就就不进行添加操作,否则就添加
"""
```

###### 8.5.2.2 删

删除中有两种：

一种是  pop  删除键，返回删除键对应的值   

另一种： popitem   python2中是随机删除，python3.6以上是默认删除最后一个

还有一种是clear  清空字典

```python
dic = {} 
dic["name"]="heyichen"
dic["age"]=19
print(dic)
#如果没有出现过key-value则采用setdefault
s1 = dic.setdefault("王菲")
print(dic)
s = dic.pop("王菲")
print(s)
print(dic)
 # pop删除有返回值,返回的是被删的值

dic.popitem()  # 随机删除  python3.6是删除最后一个
print(dic)
  
```

###### 8.5.2.3 改

有两种方法可以更改字典中值：

1. 赋值
2. update  没有dic中键值对就添加到dic字典中，如果有，则修改键对应的值

```python
dic = ["剑圣":"hello","hellowold":123]
dic["剑圣"]="剪辑"
print(dic)
dic.update({"key":"V","剑圣":"123"}) 
# 当update中的字典里没有dic中键值对就添加到dic字典中,如果有就修改里边的对应的值
print(dic)
```

###### 8.5.2.4 查

查找的两种方式：

1. 通过访问键，得到值  dic[”剑圣“]
2. 通过get函数  get("键",”自定义返回值“)  没有键或者值，则默认返回none

```python
dic = ["剑圣":"hello","hellowold":123]
s = dic["剑圣"]
print(s)

print(dic["剑圣"])
##通过健来查看,如果这个健不在这个字典中.就会返回None
print(dic.get("123","没有你还查"))
 # 我们可以在get查找的时候自己定义返回的结果

```

```python
#练习：
"""
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
请在k3对应的值中追加一个元素 44，输出修改后的字典
请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
"""
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# dic["k4"] = "v4"
# print(dic)
方法二：
# dic.setdefault("k4","v4")
# print(dic)

第二题：
# dic.update({"k1":"alex"})
# # dic['k1'] = "alex"
# print(dic)
第三题：
dic["k3"].append(44)
print(dic)
#方法二：
dic.get("k3").append(55)
print(dic)
第四题：
dic["k3"].insert(0,18)
print(dic)
#方法二：
dic.get("k3").insert(55)
print(dic)

```

##### 8.5.3 字典的其他操作

 获取字典所有键

```python
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
print(dic.keys())
# 一个高仿列表,存放的都是字典中的key
```

获取字典所有值

```python
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
#slt = dic.keys()
#print(slt)
cl = dic.values()
print(cl)
#一个高仿列表,存放都是字典中的value
```

获取字典的键值对

```python
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
tm = dic.items()
print(tm)
# 一个高仿列表,存放是多个元祖,元祖中第一个是字典中的键,第二个是字典中的值


```

循环打印所有键：

```python
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
#方法一：
for i in dic:
    print(i)
#方法二：
for i in dic.keys():
    print(i)
```

循环打印所有值

```python
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
#方法一：
for i in dic.values():
    print(i)
#方法二：
for i in dic:
    print(dic[i])

```

循环打印所有键值对

```python
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
for i in dic.items():
    print(i)
```

##### 8.5.4 字典嵌套

```python
dic = {
    'name':'汪峰',
    'age':48,
    'wife':[{'name':'国际章','age':38}],
    'children':['第一个熊孩子','第二个熊孩子']
}
#获取汪峰妻子的名字
print(dic['wife'][0]["name"])
#获取汪峰的孩子
print(dic['children'])
#获取汪峰的第一个孩子
print(dic['children'][0])
```

练习：

```python
"""
dic1 = {
 'name':['alex',2,3,5],
 'job':'teacher',
 'oldboy':{'alex':['python1','python2',100]}
 }
1，将name对应的列表追加⼀个元素’wusir’。
2，将name对应的列表中的alex⾸字⺟⼤写。
3，oldboy对应的字典加⼀个键值对’⽼男孩’,’linux’。
4，将oldboy对应的字典中的alex对应的列表中的python2删除
"""
#1
dic1['name'].append("wusir")
#2
dic1['name'][0]= dic1['name'][0].capitalize()
print(dic1)
#3
dic1['oldboy'].setdefault("老男孩","linux")
print(dic1)
#4
dic1['oldboy']["alex"].pop(1)
print(dic1)
```

#### 8.6 集合/set

- Python中数据类型之一
- 定义方法 s = set （）
- 集合就是一个没有值的字典，所以集合内的值都是可哈希/不可变的。
- 无序 可变
- 集合自动去重（因为字典内的键是唯一的）
- 定义 s = {} 时默认是字典
- s.add (" ")   一次性增加
- s.update （“ ”） 迭代添加
- s = set（“ ”）迭代添加
- s.remove（“ ”）根据元素删除
- s.clear（） 清空
- s.pop（） 随机删除（删除最小）
- 先删除后增加
- for 循环遍历
- s - s1 去除s内与s1一样的元素
- 求差集

没有值的字典   无序 ---不支持索引

天然去重

s = {1，“alex”,False,(1,2,3)}



面试题

```python
lst = [1,2,3,4,3,2,1]
print(list(set(lst)))   #去重
```

##### 8.6.1 添加

add   只能添加一个

update   迭代添加

##### 8.6.2 删除

pop  随机删除，有返回值

remove（）指定元素删除

clear（）  清空   返回：空集合

##### 8.6.3 改：

先删再加

##### 8.6.4 查：

```
# for i in {1,2,3}:
#     print(i)
```

其他操作：

##### 8.6.5 集合运算：

交集：

```python
s1 = {1,2,3,4}
s2 = {1,2,3,4,5,6,7}
print(s1&s2)
```

并集：

```
s1 = {1,2,3,4}
s2 = {1,2,3,4,5,6,7}
print(s1|s2)
```

差集：

```python
s1 = {1,2,3,4}
s2 = {1,2,3,4,5,6,7}
print(s2-s1)
```

对称差集：{反交集}

```
s1 = {1,2,3,4}
s2 = {1,2,3,4,5,6,7}
print(s2^s1)
```

父集（超集）

```python
print(s1<s2)
```

子集：

```
print(s1>s2) 子集
```

冻结集合：

frozenset(s1)  当作字典的键  将集合冻住，不可变了

#### 8.7 数据类型的转换

- 可变:list 、dict 、set

- 不可变:int 、str 、bool 、tuple

- 有序: list 、tuple 、str

- 无序： dict 、 set

- str -- int 、int -- str

- str -- bool 、 bool -- str

- int  -- bool 、 bool -- int

- list -- tuple
    lst = [1,23,5,4]
    print(tuple(lst))

    tuple -- list
    tu = (1,23,5,4)
    print(list(tu))

    list -- set
    lst = [1,23,12,31,23]
    print(set(lst))

    set -- list

    tuple -- set
    tu = (1,2,3,4,5)
    print(set(tu))

    set -- tuple

    ```
    list -- str
    lst = ["1","2","3"]
    print("".join(lst))
    
    str -- list
    s = "alex wusir 太白"
    print(s.split())
    ```

     目前字典转换,自己实现方法

- list -- tuple  lst = [1,23,5,4]

- tuple -- list  tu = (1,23,5,4)

- list -- set  lst = [1,23,12,31,23]

- tuple -- set 、 tu = (1,2,3,4,5)

    重要: 

    ```
    # list -- str
    # lst = ["1","2","3"]
    # print("".join(lst))
    
    # str -- list
    # s = "alex wusir 太白"
    # print(s.split())
    ```

    目前字典转换,自己实现方法

#### 8.8内存占用

```python
import sys
print(sys.getsizeof([]))
空列表内存占用   64B
空元祖内存占用   48B
空字典内存占用    240B
空集合内存占用    224 B
空整形内存占用  24B
空字符串内存占用  49B
```

### 9.  for循环

#### 9.1 for循环

- for * in 变量
    - for 关键字
    - *为变量名
    - 循环内可以加pass作为站位

#### 9.2 range 范围

- range（1，10） 顾头不顾尾，为了解决不能循环的数字
- 如range（10） 代表终止位置为10 开始位置默认为0
- 也拥有步长的操作

#### 9.3 解构

- a，b =  10， 20  可以用列表 元组   字符串 可迭代的都可以    字典也可以，但是只获取键
- a = 10， 20  print ( a ) 打印出的是元组
- *是万能接收，集合
- Python的格式要求Pep8

```python
a,b = 1,2
print(a,b)
结果:
1 2

a,b = ('你好','世界')
print(a,b)
结果:
你好 世界

a,b = ['你好','大飞哥']
print(a,b)
结果:
你好 世界

a,b = {'汪峰':'北京北京','王菲':'天后'}
print(a,b)
结果:
汪峰 王菲
```

解构可以将内容分别赋值到变量当中,我们使用解构就能够快速的将值使用

循环字典获取键和值

```python
dic =  {'汪峰':'北京北京','王菲':'天后'}
for a ,b in dic.items():
    print(a)
    print(b)
#输出结果：
汪峰
北京北京
王菲
天后

```

### 10. 小数据池

#### 10.1小数据池

- 小数据池支持 int str bool

    - int ： -5  ~  256

    - str ： 当字符串（字母，数字）进行乘法时总长度不能超过20

        ​		定义字符串（字母，数字）的时候可以进行任意长度

        ​		特殊符号（中文、符号）进行乘法时 ，只能乘0.

    - 布尔值： 只有True 和 False

- == 判断两个值是否相等

- is 是通过内存地址来进行判断

- id（变量） 就可以查询变量的内存地址

#### 10.2 代码块

- 一个Py文件 ，一个函数，一个模块，终端中每一行都是代码块

- 代码块支持int str bool

    - int -5 ~ 正无穷.

    - str ：当字符串（字母，数字）进行乘法时总长度不能超过20		

        ​	定义字符串的时候可以进行任意长度

        ​	特殊符号（中文、符号）进行乘法时 ，只能乘0，1.

        ​	布尔值： 只有True 和 False

- 小数据池，代码块同在的情况下先执行代码块（在Python中）

- 在cmd中因为每一行是一个代码块 所以会先走小数据池

- 驻留机制：节省内存空间,提示效率（减少了开辟空间的耗时）

### 11. 深浅拷贝

- 以后避免坑
- 面试逼问

#### 11.1 赋值

- b = a
- 将相同的空间地址赋给b（多个变量指向同一个空间地址）
- 数字和字符串在内存当中用的都是同一块地址

赋值：

```python
lst = [1,2,3,4,5,6,[1,2,3]]
lst1 = lst
lst[-1].append(8)
print(lst)
print(lst1)


```

#### 11.2 浅拷贝

- 浅拷贝：只拷贝第一次元素的地址，只有修改第一层（不可变类型）的时候不进行改变，
- b = a [ : ]  切边——浅拷贝
- 元素Id一样 整体id不一样

```python
lst = [1,2,3,4,5,6,[1,2,3]]
lst1 = lst.copy()    #新开辟一块空间给lst1
print(id(lst))
print(id(lst1))
```

![1565095089633](../python%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/day03.assets/1565095089633.png)

```python
lst = [1,2,3,4,5,6,[1,2,3]]
lst1 = lst.copy()
print(id(lst[-1]))   表示lst1后面的指向lst的地址
print(id(lst1[-1]))
"""
D:\python解释器\python.exe D:/pycharm_program/venv/第一天作业/每日练习.py
1618631044296
1618631044296

Process finished with exit code 0
"""
```

```python
lst = [1,2,3,4,5,6,[1,2,3]]
lst1 = lst.copy()
lst[0]=11
print(lst)
print(lst1)
"""
[11, 2, 3, 4, 5, 6, [1, 2, 3]]
[1, 2, 3, 4, 5, 6, [1, 2, 3]]
"""
```

![1565095897028](../python%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/day03.assets/1565095897028.png)

总结：

```
浅拷贝的时候，只会开辟一个新的容器列表，其他的元素使用的都是原列表中的元素。

修改新拷贝的列表中不可变元素的时，原列表不进行改变

修改新拷贝的列表中可变元素的时，原列表不进行改变

在给可变数据类型添加增删改的时候，原列表进行改变
```

```
浅拷贝的时候，只拷贝第一层元素

浅拷贝在修改第一层元素的时候（不可变数据类型），拷贝出来的新列表不进行改变。

浅拷贝在替换第一层元素的时候（可变数据类型），拷贝出来的新列表进行改变。

浅拷贝在修改第一层元素中的元素（第二层）的时候，拷贝出来的新列表进行改变，
```

#### 11.3 深拷贝

- import copy # 导入拷贝模块
- 不可变数据类型内存地址共用，可变数据类型单独开辟
    - 即不可变的地址一样，可变的地址不一样

![1565097850963](../python%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/day03.assets/1565097850963.png)

开辟一个容器空间（列表）不可变数据公用，可变数据类型（再次开辟一个新的空间，）

空间里面的值使用的是公用的。可变数据类型再次开辟空间

#### 11.4 总结

```
赋值：将多个变量指向同一个内存地址。

浅拷贝：

1. 只拷贝第一层元素的地址，只有修改第一层的时候原数据不受影响。
2. 给可变数据类型进行添加的时候原数据会受影响

深拷贝：

​	不可变数据类型共用，可变数据类型新开辟一片空间
```



## 第二章 函数

### 1.文件操作

- open（） 通过Python控制操作系统，打开文件
- file 文件路径
- mode 默认不写就是r
- encouding 选择编码格式
- f 文件句柄
- 文件只能读取一次
- r - read (读)
- f.read（） 全部读取
- f.read（11）按照字符读取
- f.readline（）按行读取，默认尾部有一个\n
- f.readlines（）一行一行读取。全部存在列表中
- rb - 读字节
- 在进行字节操作的时候不能指定encoding
- f.read（11） 按照字节读取
- read 和 readlines 在读取较大文件时，会出现内存溢出
    - 解决办法
    - for 循环 一行一行读取（相似于readline）

- \ \ 路径转义

- 在文件名前加一个r  -- 推荐使用

- 有后缀名加后缀名，没有后缀名不要增加

- w - write(写)

- 也需要open（）

- 当模式为 w 和 a时，有文件就使用当前文件，无文件就创建文件

- write的内容必须是字符串

- w -- 清空写 先清空文件（打开文件时清空），在写入内容

- wb - 清空写 ，写字节 不能指定编码

- a - add ( 追加) 写文本

- 不清空在文件后继续行

- a+ 无论怎么移动光标，都是在文件的最后添加

- ab -- 追加写字节

- 路径

    - 绝对路径 ： 从磁盘根部开始查找
    - 相对路径 ： 相对于某个文件进行查找

- *# seek() 移动光标* 

    *# f.seek(0,0)  # 移动光标到文件的头部* 

    *# f.seek(0,1)  # 移动光标到当前位置* 

    *# f.seek(0,2)  # 移动光标到文件末尾* 

    *# f.seek(6)   # 光标是按照字节移动* 

    

- tell 查看光标位置，按字节查询

*# import os  # 操作系统交互的接口* 

*# f = open('a2',"r",encoding="utf-8")* 

*# f1 = open("a1","w",encoding="utf-8")* 

*# for i in f:* 

*#     i = i.replace("日","天")* 

*#     f1.write(i)* 

*# f.close()* 

*# f1.close()* 

*# os.remove("a2")   # 删除不能找回* 

*# os.rename("a1","a2")*

*# import os  # 操作系统交互的接口* 

*# f = open('a2',"r",encoding="utf-8")* 

*# f1 = open("a1","w",encoding="utf-8")* 

*# for i in f:* 

*#     i = i.replace("天","日")* 

*#     f1.write(i)* 

*# f.close()* 

*# f1.close()* 

*# os.rename("a2","a3")* 

*# os.rename("a1","a2")* 

*# import os  # 操作系统交互的接口* 

*# f = open('a2',"r",encoding="utf-8")* 

*# f1 = open("a1","w",encoding="utf-8")* 

*# i = f1.read().replace("天","日")    # 将文件中全部内容读取 容易导致内存溢出* 

*# f1.write(i)*

*# f.close()* 

*# f1.close()* 

*# os.rename("a2","a3")* 

*# os.rename("a1","a2")* 

*# with open("a3","r",encoding="utf-8")as f,\* 

*#         open('a2',"r",encoding="utf-8")as f1:* 

*#     print(f.read())* 

*#     print(f1.read())* 

*# 1.自动关闭文件* 

*# 2.同一时间操作多个文件* 

*# 文件操作的目的:* 

*#     1.持久化: 永久存储*

#### 1.1  open

open（）函数打开一个文件，获取到文件句柄

只读操作（r,rb）

encoding 表示编码集

1. rb读取出阿里的数据是Bytes类型，在rb模式下，不能选择encoding字符集
2. rb的作用：在读取非文本文件的时候，例如（MP3，图像，视频）

绝对路径，相对路径：

绝对路径：从磁盘根目录开始一直到文件名

相对路径：同一个文件夹下的文件。相对于当前这个程序所在的文件夹

#### 1.2 读取文件方式

1. read() 将文件中内容全部读取出来，弊端：占内存，如果文件过大，容易导致内存奔溃

2. read（n）读取n个字符，需要注意的是：如果再次读取，那么会在当前位置继续去读而不是从头读，如果使用的是rb模式，则读取出来的是n个字节

3. readline（）一次读取一行数据  注意：readline（）结尾，注意每次读取出来的数据都会又一个\n  所以，需要我们使用strip方法去掉\n或者是空格

4. readlines（）将每一行形成一个元素，放到一个列表中，将所有的内容都读取出来，所以，容易出现内存崩溃的问题。

5. 循环读取，这种方式是最好的，每次读取一行内容，不会产生内存溢出的问题。

    ```python
    f = open()
    
    for i in f:
    
    print(i.strip())
    ```

##### 1.2.1 写模式：（w,wb）：

```
写文件时，如果没有文件，则会创建，如果文件存在，则将原件中的原来的内容删除，再写入新内容。

w模式，打开文件的时候，会清空文件。open（）时，会清空文件。
```

##### 1.2.2 追加模式（a,ab）：

```
在追加模式下，写入的内容会追加在文件的结尾。
```

##### 1.2.3 读写模式（r+,r+b）

```
读写模式，必须是先读，因为默认光标是在开头，准备读取时，当读完了之后再进行写入。
```

##### 1.2.4 写读模式：（w+，w+b）

```
先将所有的内容清空，然后写入，最后读取，但是读取的内容是空的
```

##### 1.2.5 追加读（a+）

```
a+模式下，不论先读还是后读，都是读取不到数据的
```

##### 1.2.6 其他操作：

seek()

```
seek(n)  光标移动到n位置，注意，移动的单位是Byte，所以，如果是UTF-8的中文部分要是3的倍数

seek（0，0） 移动光标到开头

seek（0，1）移动光标到当前位置

seek（0，2）移动光标到结尾。

tell（） 使用tell可以帮我们获取到当前光标的位置，按照字节进行计算
```

trunecate（）截断文件

深坑：

```
在r+模式下，如果读取了内容，不论读取内容多少，光标显示的是多少，再写入或者操作文件的时候都是再结果进行的操作。

先挪动光标，挪动带你想要阶段的位置，然后再进行截断。

truncate（n）表示从开头进行阶段，如果不给，则表示当前位置截断，后面内容将会被删除
```

### 2.函数

#### 2.1 函数定义：

什么是函数?

​	将某个功能封装到一个空间中就是一个函数

​	减少重复代码

定义函数：

def   python关键字

```
len  函数名    --变量名一模一样
（）   必须要写   格式规范
：  语句结束
```

#### 2.2 函数调用：

函数名+（）就是在调用函数

1. 面向过程
2. 面向函数
3. 面向对象

函数返回值：

​	函数的返回值，返回给函数的调用者

return  :

1. 可以返回任意类型数据
2. return返回多个内容是元祖形式
3. return下方不执行，并且会终止当前这个函数
4. return 不屑或者是写了return后面不写值都返回none

```
def   yue（app1）  #形参
yue（10）   #实参
```

传参：将实参传递给形参的过程

```python
def len():
  a = "alexdsb"
  count = 0
  for i in a:
      count += 1
  print(count)

len()  # 函数的调用
```

调用执行的时候,才会执行func这个空间里的代码,执行的时候在开辟空间,这次是在func里边开辟的空间.

![1566613374886](python学习之旅.assets/1566613374886.png)

#### 2.3 函数的参数：

```
1.形参
　　　　写在函数声明的位置的变量叫形参,形式上的一个完整.表示这个函数需要xxx
2.实参
　　　　在函数调用的时候给函数传递的值.加实参,实际执行的时候给函数传递的信息.表示给函数xxx
3.传参
　　　　从调用函数的时候将值传递到定义函数的过程叫做传参
```

```
形参：位置参数：

- ​	一一对应

默认参数：函数定义的时，括号写的就是默认参数
				位置参数必须放在默认参数前面
位置参数和默认参数不能同名
位置参数>默认参数
实参：
位置参数：
		一一对应
关键字参数：
		指名道姓
混合传参：
位置参数和关键字参数混合参数
形参就是一个变量名,实参就是值 传参就是在赋值

```

#### 2.4 函数的内存空间：

函数的定义在内存空间，内存开辟了一个空间,但是里边存放是代码

![1566613264604](python学习之旅.assets/1566613264604.png)

三目运算：  （没有elif）

条件成立的结果   条件     条件不成立的结果

#### 2.5 函数的动态参数：

动态参数：

​	形参：

```python
#动态位置参数
def  eatO(*args):   #函数的定义阶段   *聚合（打包）
  print(args)				#打包后的是元祖
  print(*args)         #函数体中的*   打散（解包）
 

位置参数>动态位置参数>默认参数>动态默认参数
**kwargs   动态关键字参数

```

```
函数定义时，
函数体中  *就是打散  *args字符串
def  fun(*args,**kwargs):  万能传参
在形参的位置上的*表示把接受到的参数组合成一个元祖
如果是一个字典，那么也可以打散，不过需要两个
```

#### 2.6  函数的注释：

（写函数必须写注释）

```python
def myfun():
    """
    
    :return: 
    """
    
 #函数注释
def myfun():
    """

    :return:
    """
    print(myfun.__name__)               #查看函数名
    print(myfun.__doc__)                #查看函数注释
myfun()
```

#### 2.7 命名空间:

```
在python解释器开始执行之后, 就会在内存中开辟一个空间, 每当遇到一个变量的时候, 就把变量名和值之间的关系记录下来, 但是当遇到函数定义的时候, 解释器只是把函数名读入内存, 表示这个函数存在了, 至于函数内部的变量和逻辑, 解释器是不关心的. 也就是说一开始的时候函数只是加载进来, 仅此而已, 只有当函数被调用和访问的时候, 解释器才会根据函数内部声明的变量来进行开辟变量的内部空间. 随着函数执行完毕, 这些函数内部变量占用的空间也会随着函数执行完毕而被清空.
```

##### 2.7.1 命名空间分类：

1. 全局命名空间 ->我们直接在py文件中，函数外声明的变量都属于全局命名空间
2. 局部命名空间->在函数中声明的变量会放在局部命名空间
3. 内置命名空间->存放python解释器为我们提供的名字，list，tuple，str, int 这些都是内置命名空间

##### 2.7.2 加载顺序：

```
内置命名空间 ->全局命名空间->局部命名空间（函数被执行的时候）
```

##### 2.7.3  取值顺序：

```
局部命名空间->全局命名空间->内置命名空间
```

##### 2.7.4 作用域：

作用域就是作用范围，按照生效范围来看分为  全局作用域和局部作用域

1. 全局作用域：全局命名空间+内置命名空间
2. 局部作用域：局部命名空间

可以使用globals（）函数查看全部作用域中的内容，也可以通过locals（）查看局部作用域中的变量和函数信息

```python
a  = 20

def fun():
    a = 40
    b = 20
    def abc():
        print("hh")
    print(a,b)
    print(globals())
    print("-----------------------------------------------")
    print(locals())
fun()
打印结果：
D:\python解释器\python.exe D:/pycharm_program/venv/第一天作业/test.py
40 20
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002F62F92D198>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:/pycharm_program/venv/第一天作业/test.py', '__cached__': None, 'a': 20, 'fun': <function fun at 0x000002F62FB93EA0>}
-----------------------------------------------
{'abc': <function fun.<locals>.abc at 0x000002F636C7F1E0>, 'b': 20, 'a': 40}
```

##### 2.7.4 函数的执行顺序

关键字global 和nonlocal

global   : 只修改全局

nonlocal: 只修改局部，修改离nonlocal最近的一层，上一层没有继续向上上层查找只限在局部

函数可以同名，只不过在同一个作用域中，后面定义的函数会覆盖之前的定义的函数.

函数也分为全局作用域和局部作用域,当局部没有时,会到全局中查找.

#### 2.8 函数嵌套：

只要遇见了（）就是函数的调用，如果没有（）就不是函数的调用

#### 2.9 函数名第一类对象：

##### 2.9.1 当作值，赋值给变量

```python
## def fun():
#    print(1)
# print(fun)  
#函数的内存地址
## a  = fun
# print(a)
# a()
```

##### 2.9.2 当作容器中的元素

```python
lst = []
dic = {}


def fun():
    print(1)


def foo():
    print(2)
#放在列表中
lst.append(fun)
lst.append(foo)
print(lst)
for i in lst:
    print(i)
    i()
#放在字典中


def login():
    print("这是登陆")


def regin():
    print("这是注册")


dic = {"1": login, "2": regin}

msg = """
1、登陆
2、注册
"""
choose = input(msg)
if choose.isdecimal():
    if dic.get(choose):
        dic[choose]()
    else:
        print("请正确输入")
```

##### 2.9.3 函数名当作函数的参数

```python
def fun(a):
    a()
    print(111)

def foo():
    print(222)
    def f1():
        print(333)
    fun(f1)

foo()
```

##### 2.9.4 函数名可以当作函数的返回值

```python
def fun():
    def foo():
        print(111)
    return foo
fun()()   #foo()
```

##### 2.9.5 总结

```
函数名的第一类对象的使用方式如下：
1、可以当作值，赋值给变量
2、可以当作容器中的元素
3、可以当作函数的参数
4、可以当作函数的返回值
```

```python
#练习：
def foo():
    def func():
        def f1():
            print(123)
        return f1()
    return func()
print(foo())

```

### 3.迭代器

**在python中，但凡内部含有iter方法的对象，都是可迭代对象**。

#### 3.1 查看对象内部方法

 该对象内部含有什么方法除了看源码还有什么其他的解决方式么？当然有了， 可以通过dir() 去判断一个对象具有什么方法

```
s1 = 'alex'
print(dir(s1))
```

dir()会返回一个列表，这个列表中含有该对象的以字符串的形式所有方法名。这样我们就可以判断python中的一个对象是不是可迭代对象了：

```python
s1 = 'alex'
i = 100
print('__iter__' in dir(i))  # False
print('__iter__' in dir(s1))  # True
```

#### 3.2 小结

 从字面意思来说：可迭代对象就是一个可以重复取值的实实在在的东西。

 从专业角度来说：但凡内部含有__iter__方法的对象，都是可迭代对象。

 可迭代对象可以通过判断该对象是否有__iter__方法来判断。

 可迭代对象的优点：

 可以直观的查看里面的数据。

 可迭代对象的缺点：

 1.占用内存。

 2.可迭代对象不能迭代取值（除去索引，key以外）。

 那么这个缺点有人就提出质疑了，即使抛去索引,key以外，这些我可以通过for循环进行取值呀！对，他们都可以通过for循环进行取值，其实for循环在底层做了一个小小的转化，就是先将可迭代对象转化成迭代器，然后在进行取值的。那么接下来，我们就看看迭代器是个什么鬼。

#### 3.3 迭代器

##### **3.3.1  迭代器的定义**

 从字面意思来说迭代器，是一个可以迭代取值的工具，器：在这里当做工具比较合适。

 从专业角度来说：迭代器是这样的对象：实现了无参数的__next__方法，返回序列中的下一个元素，如果没有元素了，那么抛出StopIteration异常.python中的迭代器还实现了__iter__方法，因此迭代器也可以迭代。 出自《流畅的python》

 那么对于上面的解释有一些超前，和难以理解，不用过于纠结，我们简单来说：**在python中，内部含有__Iter__方法并且含有__next__方法的对象就是迭代器。**

##### **3.3.2 如何判断该对象是否是迭代器**

 ok，那么我们有了这个定义，我们就可以判断一些对象是不是迭代器或者可迭代对象了了，请判断这些对象：str list tuple dict set range 文件句柄 哪个是迭代器，哪个是可迭代对象：

```python
o1 = 'alex'
o2 = [1, 2, 3]
o3 = (1, 2, 3)
o4 = {'name': '太白','age': 18}
o5 = {1, 2, 3}
f = open('file',encoding='utf-8', mode='w')
print('__iter__' in dir(o1))  # True
print('__iter__' in dir(o2))  # True
print('__iter__' in dir(o3))  # True
print('__iter__' in dir(o4))  # True
print('__iter__' in dir(o5))  # True
print('__iter__' in dir(f))  # True

print('__next__' in dir(o1))  # False
print('__next__' in dir(o2))  # False
print('__next__' in dir(o3))  # False
print('__next__' in dir(o4))  # False
print('__next__' in dir(o5))  # False
print('__next__' in dir(f))  # True
f.close()
```

通过以上代码可以验证，之前我们学过的这些对象，只有文件句柄是迭代器，剩下的那些数据类型都是可迭代对象。

##### **3.3.3 可迭代对象如何转化成迭代器：**

```python
l1 = [1, 2, 3, 4, 5, 6]
obj = l1.__iter__()
# <list_iterator object at 0x000002057FE1A3C8>
# 或
obj = iter(l1)
print(obj)
# <list_iterator object at 0x102cc67f0>
```

##### **3.3.4 迭代器取值：**

 可迭代对象是不可以一直迭代取值的（除去用索引，切片以及Key），但是转化成迭代器就可以了，迭代器是利用__next__()进行取值：

```python
l1 = [1, 2, 3,]
obj = l1.__iter__()  # 或者 iter(l1)
# print(obj)  # <list_iterator object at 0x000002057FE1A3C8>
ret = obj.__next__()
print(ret)
ret = obj.__next__()
print(ret)
ret = obj.__next__()
print(ret)
ret = obj.__next__()  # StopIteration
print(ret)
# 迭代器利用next取值：一个next取对应的一个值，如果迭代器里面的值取完了，还要next，
# 那么就报StopIteration的错误。
```

##### **3.3.5 while模拟for的内部循环机制：**

 刚才我们提到了，for循环的循环对象一定要是可迭代对象，但是这不意味着可迭代对象就可以取值，因为for循环的内部机制是：将可迭代对象转换成迭代器，然后利用next进行取值，最后利用异常处理处理StopIteration抛出的异常。

```
l1 = [1, 2, 3, 4, 5, 6]
# 1 将可迭代对象转化成迭代器
obj = iter(l1)
# 2,利用while循环，next进行取值
while 1:
    # 3,利用异常处理终止循环
    try:
        print(next(obj))
    except StopIteration:
        break
```

##### **3.3.6 小结：**

 从字面意思来说：迭代器就是可以迭代取值的工具。

 从专业角度来说：在python中，内部含有__Iter__方法并且含有__next__方法的对象就是迭代器。

 迭代器的优点：

 节省内存。  迭代器在内存中相当于只占一个数据的空间：因为每次取值都上一条数据会在内存释放，加载当前的此条数据。

 惰性机制。  next一次，取一个值，绝不过多取值。

 有一个迭代器模式可以很好的解释上面这两条：迭代是数据处理的基石。扫描内存中放不下的数据集时，我们要找到一种惰性获取数据项的方式，即按需一次获取一个数据项。这就是迭代器模式。

#####  3.3.7 迭代器的缺点：

 不能直观的查看里面的数据。

 取值时不走回头路，只能一直向下取值。

```python
l1 = [1, 2, 3, 4, 5, 6]
obj = iter(l1)

for i in range(2):
    print(next(obj))

for i in range(2):
    print(next(obj))
```

#### 3.4 可迭代对象与迭代器对比

 我们今天比较深入的了解了可迭代对象与迭代器，接下来我们说一下这两者之间比较与应用：

#####  3.4.1 **可迭代对象：**

 是一个私有的方法比较多，操作灵活（比如列表，字典的增删改查，字符串的常用操作方法等）,比较直观，但是占用内存，而且不能直接通过循环迭代取值的这么一个数据集。

 **应用**：当你侧重于对于数据可以灵活处理，并且内存空间足够，将数据集设置为可迭代对象是明确的选择。

#####  3.4.2 **迭代器：**

 是一个非常节省内存，可以记录取值位置，可以直接通过循环+next方法取值，但是不直观，操作方法比较单一的数据集。

 **应用**：当你的数据量过大，大到足以撑爆你的内存或者你以节省内存为首选因素时，将数据集设置为迭代器是一个不错的选择。（可参考为什么python把文件句柄设置成迭代器）。

##### 3.4.3 迭代器方法在py3和py2中的区别

- Python3：--iter--() 和 iter() 都有

    ​                --next--() 和next() 都有

- python2： 只有--iter--()

    ​                 只有--next--()

##### 3.3.4 迭代器的优缺点

1. 优点：

​        惰性机制(节省空间)

2. 缺点：
    - 不能直接查看值，迭代器查看到的是一个迭代器内存地址
    - 是一次性的，用完就没了
    - 不能逆行（后退）

##### 3.3.5  空间与时间之间的转换：

- 空间换时间：

    ​	容量存储大量的元素时，取值时直接调	取，时间就会缩短，但是容器占用空间 	大

- 时间换空间：

    ​	迭代器就是为了节省空间，但是取值时	间较长

### 4.生成器

生成器的本质：本质就是一个迭代器

生成器的编写方式：

1. 基于函数编写
2. 基于推导式方式编写

```python
def func():
	print("这是一个生成器")
	yield"生成器"    # 申明要生成一个生成器
func()   # 生成一个生成器
print(func().__next__())    #启动生成器
# generator -- 生成器
# print(func())  #获取到的是生成器的内存地址
```

#### 4.1 yield与return的比较

- 相同点：

    （1）都是返回内容

    （2）都可以返回多个，但是return写多个只会返回执行一个

- 不同点：

    （1）return终止函数，yield是暂停生成器

    （2）yield能够记录当前执行位置

    （3）一个yield只能对应一个next

#### 4.2 可迭代对象、迭代器、生成器的优缺点

##### 4.2.1  可迭代对象的优缺点

- 优点：节省时间，取值方便，使用灵活
- 缺点：消耗空间内存

##### 4.2.2  迭代器的优缺点

- 优点：节省时间
- 缺点：不能直接查看值，只能查看内存地址，使用不灵活，消耗时间，一次性（用完就没了），不可逆行

##### 4.2.3 生成器的优缺点

- 节省空间，可扩展
- 缺点：不能直接查看值，只能查看内存地址，使用不灵活，消耗时间，一次性（用完就没了），不可逆行

##### 4.2.4 使用场景

当文件或容器中数据较大时，建议使用生成器

#### 4.3  怎么区分生成器与迭代器

##### 4.3.1看内存地址显示

- 迭代器：iterator
- 生成器：generator

##### 4.3.2 send方法

- 没有send()方法就是一个迭代器，反之，有send()方法就是生成器

相同点：

- send 和 next()都可以让生成器对应的yield向下执行一次。
- 都可以获取到yield生成的值。

 不同点：

- 第一次获取yield值只能用next不能用send（可以用send(None)）。
- send可以给上一个yield置传递值。

#### 4.4 yield与yield from的区别

- yield将可迭代对象一次性返回
- yield form 是将可迭代对象整个返回

在python3中提供一种可以直接把可迭代对象中的每一个数据作为生成器的结果进行返回

```python

def  fun():
    lst = [12,3,4,5,6]
    yield lst
g =fun()
print(next(g))
结果是：列表  [12,3,4,5,6]


def  fun():
    lst = [12,3,4,5,6]
    yield from  lst
g =fun()
print(next(g))
结果是：12
#他会将这个可迭代对象(列表)的每个元素当成迭代器的每个结果进行返回。
```

yield from 坑

```python
def fun():
    lst1 = [1,2,3,4,5]
    lst2=[5,6,7,8,12,3,45]
    yield lst1
    yield lst2

g = fun()
for i in g:
    print(i)
   # 返回的结果是将第一个列表的元素全部返回后,在返回第二个列表
```

#### 4.5 补充

- 数据类型 (python3中的range,python2中的xrange)都是可迭代对象，具有__iter__()
- 文件句柄是迭代器__iter__()、__next__()

### 5.推导式

#### 5.1 种类

- 普通循环
- 筛选循环

#### 5.2 列表推导式

- 普通循环

```
print([i for i in range(10)])
    # [变量 for循环 ] 
```

- 筛选循环 

```
print([i for i in range(10) if i % 2 == 0])
print([i for i in range(10) if i > 2])
[加工后的变量  for循环  加工条件]
```

#### 5.3 字典推导式

- 普通循环

```
print({i : i+1 for i in range(10) })
[{加工后的值：值  for循环 加工条件}]
```

- 筛选循环

```
print({i:i+1 for i in range(10) if i % 2 == 0})
{加工后的键：值 for循环 加工条件}
```

#### 5.4 集合推导式

- 普通循环

```
print({i for i in  range(10)})
{加工后的变量  for循环 加工条件}
```

- 筛选循环

```
print({i for i in range(10) if i % 2 == 0})
{加工后的变量 for循环 加工条件}
```

#### 5.5 生成器推导式

- 普通循环

```
tu = (i for i in range(10))
     (变量 for循环)
```

- 筛选循环

```
tu = (i for i in range(10) if i > 5)
    (加工后的变量 for循环 加工条件)
```

### 6. 匿名函数：

== 没有名字的函数     一行函数

匿名函数的名字叫做lambda

```python
#原先定义函数
def fun():
    return 6
print(fun())
#匿名函数
print((lambda :6)())   #输出6
print(lambda :6)   #返回匿名函数的内存地址
```

lambda   ==def  ==  关键字

x  是普通函数的形参（位置，关键字。。。） 可以不接受参数（x:可以不写）

： 后面x是普通函数的函数值（只能返回一个数据类型）（：x返回值必须写）

```python
print((lambda x:x+6)(5))

f = lambda x:x+6
print(f.__name__)
打印结果：<lambda>


#重点：
f = lambda x,y,z,b=1:x,y,z,b
print(f(1,2,3))   #报错
lambda  返回是一个元素

f = lambda x,y,z,b=1:(x,y,z,b)
print(f(1,2,3))  #返回一个元祖

```

```python
#面试题
lst  = [lambda  : i for i in range(5)]
print(lst[0]())
 
  lambda 中的 i是自由变量，每次匿名函数的返回值指向同一块的内存地址i，所以打印结果会是最后一次i的值。

```

```python
tu = (lambda :i for i in range(3))
print(next(tu)())
print(next(tu)())
print(next(tu)())
lambda加括号是生成器，tu是生成器的内存地址。
next（tu）打印结果是lambda的内存地址。后面加括号表示启动lambda函数。
```

函数体中存放的是代码，生成器中存放的也是代码

就是yield导致函数和生成器的执行结果不一致。

```python
lst = [lambda :i for i in range(3)]
print([i() for i in lst])
#结果是;[2,2,2]

lst = (lambda :i for i in range(3))
print([i() for i in lst])
#结果是【0，1，2】
yield 暂停执行。
```

### 7.内置函数

##### 7.1 内置函数一

| 函数     | 使用                                                         |
| :------- | ------------------------------------------------------------ |
| eval：   | 执行字符串类型的代码，并返回最终结果      工作中禁止使用**   |
| exec     | 执行字符串类型的代码。                                   工作中禁止使用** |
| hash     | 获取一个对象（可哈希对象：int，str，Bool，tuple）的哈希值。  |
| help     | 函数用于查看函数或模块用途的详细说明。                       |
| callable | 函数用于检查一个对象是否是可调用的。如果返回True，仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功。 |
| int      | 函数用于将一个字符串或数字转换为整型。                       |
| float    | 函数用于将整数和字符串转换成浮点数。                         |
| bin      | 将十进制转换成二进制并返回。                                 |
| oct      | 将十进制转化成八进制字符串并返回。                           |
| hex      | 将十进制转化成十六进制字符串并返回。                         |
| divmod   | 计算除数与被除数的结果，返回一个包含商和余数的元组(a // b, a % b)。 |
| round    | 保留浮点数的小数位数，默认保留整数。                         |
| pow      | 求x**y次幂。（三个参数为x**y的结果对z取余）                  |
| bytes    | 用于不同编码之间的转化。                                     |
| ord      | 输入字符找当前字符编码的位置                                 |
| chr      | 输入当前编码的位置数字找出其对应的字符                       |
| repr     | 返回一个对象的string形式（原形毕露）                         |
| all      | 可迭代对象中，全都是True才是True                             |
| any      | 可迭代对象中，有一个True 就是True                            |

```python
# all  可迭代对象中，全都是True才是True
# any  可迭代对象中，有一个True 就是True
# print(all([1,2,True,0]))
# print(any([1,'',0]))
```

##### 7.2 内置函数二

str()  将字节转换成字符串

list() 将可迭代对象转换成列表

tuple（）将可迭代对象转换为元祖

dict（）将元祖和列表转换成字典

```python
#将两个字典合为一个字典
dic1 = {"key1":1,"key":2}
dic2 = {"key3":3,"key4":4}
print(dict(**dic1,**dic2))
#方法2：
update
dic1 = {"key1":1,"key":2}
dic2 = {"key3":3,"key4":4}
dic1.update(dic2)
print(dic1)
#方法三：
print(dict([(1,2),(3,4)]))
#函数内部实现方式:
dic = dict()
for x,y in [(1,2),(3,4)]:
    dic[x] = y
print(dic)

```

set()将可迭代对象转换成一个集合

print（）屏幕输出

```python
''' 源码分析
def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    file:  默认是输出到屏幕，如果设置为文件句柄，输出到文件
    sep:   打印多个值之间的分隔符，默认为空格
    end:   每一次打印的结尾，默认为换行符
    flush: 立即把内容输出到流文件，不作缓存
    """
'''
print(111,222,333,sep='*')  # 111*222*333
print(111,end='')
print(222)  #两行的结果 111222

f = open('log','w',encoding='utf-8')
print('写入文件',fle=f,flush=True)


使用print写入文件
print(1,2,3,4,file = open("test.txt","w",encoding="utf-8"))

```

sum()求和，求和必须是可迭代对象，对象中元素必须是整型，字符串类型不能使用

```python
print(sum([1,2,3]))
print(sum([1,2,3],100))  100是起始值,就是从100开始进行求和
```

abs（）返回绝对值

```python
i = -5
print(abs(i))  # 5
```

dir（）查看当前对象具体什么方法

```Python
print(dir(list))
```

zip（）拉链方法。函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组,

然后返回由这些元祖组成的内容,如果各个迭代器的元素个数不一致,则按照长度最短的返回

```python
lst1 = [1,2,3]
lst2 = ['a','b','c','d']
lst3 = (11,12,13,14,15)
for i in zip(lst1,lst2,lst3):
    print(i)

结果:
(1, 'a', 11)
(2, 'b', 12)
(3, 'c', 13)
```

format()格式转换

```python
# 对齐方式:
print(format(122,">20"))   右对齐
print(format(122,"<20"))    左对齐
print(format(122,"^20"))    居中

# 进制转换:
将十进制转换成二进制
print(format(12,"b"))
print(format(12,"08b"))

将十进制转换成八进制
print(format(12,"o"))
print(format(12,"08o"))

将二进制转换成十进制
print(format(0b11001,"d"))

将十进制转换成十六进制
print(format(17,"x"))
print(format(17,"08x"))
```

reversed（）将一个序列翻转，返回反转序列的迭代器reversed

```python
l = reversed('你好')  # l 获取到的是一个生成器
print(list(l))
ret = reversed([1, 4, 3, 7, 9])
print(list(ret))  # [9, 7, 3, 4, 1]
```

##### 7.3 高阶函数

filter 筛选过滤：

```python
语法: filter(function,iterable)

function: 用来筛选的函数,在filter中会自动的把iterable中的元素传递给function,然后根据function返回的True或者False来判断是否保留此项数据
  iterable:可迭代对象

lst = [{'id':1,'name':'alex','age':18},
        {'id':1,'name':'wusir','age':17},
        {'id':1,'name':'taibai','age':16},]

ls = filter(lambda e:e['age'] > 16,lst)

print(list(ls))

结果:
[{'id': 1, 'name': 'alex', 'age': 18},
 {'id': 1, 'name': 'wusir', 'age': 17}]


# lst = [1,2,3,4,5,6]
# def func(a):
#     return a>1
#
# print(list(filter(func,lst)))
# print(list(filter(lambda x:x>1,lst)))

# lst = [1,2,3,4,5,6]
# def f(func,args):
#     new_lst = []
#     for i in args:
#         if func(i):
#             new_lst.append(i)
#     return new_lst
#
# def func(a):
#     return a>1
#
# print(f(func,lst))

# print(list(filter(lambda x:x>2,[1,2,3,4,5])))
# lst = [{'id':1,'name':'alex','age':18},
#         {'id':1,'name':'wusir','age':17},
#         {'id':1,'name':'taibai','age':16},]
#
# print(list(filter(lambda x:x['age']>16,lst)))

```

map映射：

```python
映射函数

语法: map(function,iterable) 可以对可迭代对象中的每一个元素进映射,分别取执行function

计算列表中每个元素的平方,返回新列表

lst = [1,2,3,4,5]

def func(s):

    return  s*s

mp = map(func,lst)

print(mp)

print(list(mp))




改写成lambda

lst = [1,2,3,4,5]

print(list(map(lambda s:s*s,lst)))

计算两个列表中相同位置的数据的和

lst1 = [1, 2, 3, 4, 5]

lst2 = [2, 4, 6, 8, 10]

print(list(map(lambda x, y: x+y, lst1, lst2)))

结果:

[3, 6, 9, 12, 15]
```

sorted 排序函数

```python
语法:sorted(iterable,key=None,reverse=False)

iterable : 可迭代对象

key: 排序规则(排序函数),在sorted内部会将可迭代对象中的每一个元素传递给这个函数的参数.根据函数运算的结果进行排序

reverse :是否是倒序,True 倒序 False 正序

lst = [1,3,2,5,4]
lst2 = sorted(lst)
print(lst)    #原列表不会改变
print(lst2)   #返回的新列表是经过排序的


lst3 = sorted(lst,reverse=True)
print(lst3)   #倒叙

结果:
[1, 3, 2, 5, 4]
[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]

字典使用sorted排序

dic = {1:'a',3:'c',2:'b'}
print(sorted(dic))   # 字典排序返回的就是排序后的key

结果:
[1,2,3]


和函数组合使用

# 定义一个列表,然后根据一元素的长度排序
lst = ['天龙八部','西游记','红楼梦','三国演义']

# 计算字符串的长度
def func(s):
    return len(s)
print(sorted(lst,key=func))

# 结果:
# ['西游记', '红楼梦', '天龙八部', '三国演义']


和lambda组合使用

lst = ['天龙八部','西游记','红楼梦','三国演义']

print(sorted(lst,key=lambda s:len(s)))

结果:
['西游记', '红楼梦', '天龙八部', '三国演义']


lst = [{'id':1,'name':'alex','age':18},
    {'id':2,'name':'wusir','age':17},
    {'id':3,'name':'taibai','age':16},]

# 按照年龄对学生信息进行排序

print(sorted(lst,key=lambda e:e['age']))

结果:
[{'id': 3, 'name': 'taibai', 'age': 16}, {'id': 2, 'name': 'wusir', 'age': 17}, {'id': 1, 'name': 'alex', 'age': 18}]
```

max()最大值与最小值

min 求最小值：

```
print(min([1,2,3]))  # 返回此序列最小值

 max()  -- 最大值
# print(max(10,12,13,15,16))
# print(max([10,12,13,15,-16],key=abs))
ret = min([1,2,-5,],key=abs)  # 按照绝对值的大小，返回此序列最小值

print(ret)
# 加key是可以加函数名，min自动会获取传入函数中的参数的每个元素，然后通过你设定的返回值比较大小，返回最小的传入的那个参数。
print(min(1,2,-5,6,-3,key=lambda x:abs(x)))  # 可以设置很多参数比较大小
dic = {'a':3,'b':2,'c':1}
print(min(dic,key=lambda x:dic[x]))

# x为dic的key，lambda的返回值（即dic的值进行比较）返回最小的值对应的键
```

**reduce 累计算**

```python
from functools import reduce
def func(x,y):
    return x + y

# reduce 的使用方式:
# reduce(函数名,可迭代对象)  # 这两个参数必须都要有,缺一个不行

ret = reduce(func,[3,4,5,6,7])
print(ret)  # 结果 25
reduce的作用是先把列表中的前俩个元素取出计算出一个值然后临时保存着,
接下来用这个临时保存的值和列表中第三个元素进行计算,求出一个新的值将最开始
临时保存的值覆盖掉,然后在用这个新的临时值和列表中第四个元素计算.依次类推

注意:我们放进去的可迭代对象没有更改
以上这个例子我们使用sum就可以完全的实现了.我现在有[1,2,3,4]想让列表中的数变成1234,就要用到reduce了.
普通函数版
from functools import reduce

def func(x,y):

    return x * 10 + y
    # 第一次的时候 x是1 y是2  x乘以10就是10,然后加上y也就是2最终结果是12然后临时存储起来了
    # 第二次的时候x是临时存储的值12 x乘以10就是 120 然后加上y也就是3最终结果是123临时存储起来了
    # 第三次的时候x是临时存储的值123 x乘以10就是 1230 然后加上y也就是4最终结果是1234然后返回了

l = reduce(func,[1,2,3,4])
print(l)


匿名函数版
l = reduce(lambda x,y:x*10+y,[1,2,3,4])
print(l)
函数参数必须传入两个参数，否则报错

在Python2.x版本中recude是直接 import就可以的, Python3.x版本中需要从functools这个包中导入

```

面试题字典

```python
    # dict(k=1)
    # dict([(1,2)])
    # dict(**dic1,**dic2)
    dict(zip(list1,list2))
```

### 8.闭包

什么是闭包？

1、在嵌套函数内，使用（非本层变量）和非全局变量就是闭包

```
# 闭包的作用:
# 1.保护数据的安全性
# 2.装饰器
```

为什么叫做保护数据的安全性呢?

如果使用全局变量，只要是全局作用域的任何地方，都可能对这个变量或者列表进行改变，

如果使用局部变量。执行函数，会开启一个临时的名称空间，随着函数的结束而消失，所以你每次执行函数的时候，都是重新创建这个列表，

```python
# 例一：
def wrapper():
    a = 1
    def inner():
        print(a)
    return inner
ret = wrapper()
#闭包

# 例二：
a = 2
def wrapper():
    def inner():
        print(a)
    return inner
ret = wrapper()

#不是闭包
# 例三：

def wrapper(a,b):
    def inner():
        print(a)
        print(b)
    return inner
a = 2
b = 3
ret = wrapper(a,b)    
传参的过程相当于赋值
def wrapper(a,b):
  	a = 2
    b = 3
    def inner():
        print(a)
        print(b)
    return inner
a = 2
b = 3
ret = wrapper(a,b)      #闭包
```

**闭包的应用**：

1. 可以保存一些非全局变量但是不易被销毁、改变的数据。
2. 装饰器。

### 9.装饰器

#### 9.1开放封闭原则：

【在不修改源代码及调用方式，对功能进行额外添加就是开放封闭原则】

1、代码扩展进行开放

2、修改源代码是封闭

装饰器是以功能为导向，就是一个函数

```python

def foo():
    print("被装饰的函数")
def warpper(func):
    def inner():
        print("内置函数")
        func()
        print("函数调用")
    return inner()      
foo = warpper(foo)
foo()
# 注意：在函数体中函数调用不能加()


#标准版装饰器


def foo():
    print("被装饰的函数")
def warpper(func):
    def inner():
        print("内置函数")
        func()
        print("函数调用")
    return inner
foo = warpper(foo)
foo()

语法糖:写在被装饰的函数正上方

def warpper(f):
    def inner(*args,**kwargs):
        print("被装饰函数执行前")
        ret = f(*args,**kwargs)
        print("被装饰函数执行后")
        return ret
    return inner

@warpper
def func(*args,**kwargs):
    print(f"被装饰的{args,kwargs}")
    return "我是func函数"
print(func(1,2,3,4,5,6,7,8,a=1))


def warpper(f):
    def inner(*args,**kwargs):
        f(*args,**kwargs)
    return inner

@warpper
def func():
    print(111)

```

#### 9.2 装饰器进阶：

##### 9.2.1 有参装饰器

```python
def  fun(ll):
    def wrapper(func):
        def inner():
            print(ll)
            func()
        print("++++",inner)
        return inner
    print("-----",wrapper)
    return wrapper

@fun("qqqq")
def func():
    print("1111")
print("------++++=+",func)
func()
理解：
----- <function fun.<locals>.wrapper at 0x000002D03E0E01E0>
++++ <function fun.<locals>.wrapper.<locals>.inner at 0x000002D03E0E02F0>
------++++=+ <function fun.<locals>.wrapper.<locals>.inner at 0x000002D03E0E02F0>
qqqq
1111

【总结：
@fun('qqqq') :分两步：

​ 第一步先执行fun('qqqq')函数，得到返回值wrapper

​ 第二步@与wrapper结合，形成装饰器@wrapper 然后在依次执行。】

相当于有两个装饰器嵌套。
```

##### 9.2.2 多个装饰器装饰一个函数

多个装饰器装饰一个函数时,先执行离被装饰函数最近的装饰器

```python
# def auth(func): # wrapper1装饰器里的 inner
#     def inner(*args,**kwargs):
#         print("额外增加了一道 锅包肉")
#         func(*args,**kwargs)
#         print("锅包肉 38元")
#     return inner
#
# def wrapper1(func): # warpper2装饰器里的 inner
#     def inner(*args,**kwargs):
#         print("额外增加了一道 日魔刺生")
#         func(*args,**kwargs)
#         print("日魔刺生 白吃")
#     return inner
#
# def wrapper2(func):  # 被装饰的函数foo
#     def inner(*args,**kwargs):
#         print("额外增加了一道 麻辣三哥")
#         func(*args,**kwargs)
#         print("难以下嘴")
#     return inner
#
# @auth        # 1           7
# @wrapper1    #   2       6
# @wrapper2    #    3    5
# def foo():   #      4
#     print("这是一个元宝虾饭店")


# foo = wrapper2(foo) # inner = wrapper2(foo)
# foo = wrapper1(foo) # inner = wrapper1(inner)
# foo = auth(foo)     # inner = auth(inner)
# foo()               # auth里边的inner()
```



##### 9.2.3.装饰器补充

```
from functools import wraps

def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        # 之前
        ret = func(*args, **kwargs)
        # 之后
        return ret

    return inner
```

为什么要使用wraps

原因：

```python
def wrapper(func):
    def inner(*args, **kwargs):
        # 之前
        ret = func(*args, **kwargs)
        # 之后
        return ret

    return inner


@wrapper
def fun():
    print(111)

@wrapper
def fun1():
    print(111)

print(fun.__name__,fun1.__name__)

__name__
__doc__
结果
"""
inner  inner
none  none
"""
分析：
"""
因为此时fun 以及fun1 实际变成了装饰器中inner函数
为了解决此问题，使用wraps装饰
"""
```

![1572436558694](../python%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/django/django02.assets/1572436558694.png)

![1572436668530](../python%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/django/django02.assets/1572436668530.png)



加入warps后

```python
from functools import wraps


def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        # 之前
        ret = func(*args, **kwargs)
        # 之后
        return ret

    return inner


@wrapper
def fun():
    """
    这是一个fun函数
    :return:
    """
    print(111)

@wrapper
def fun1():
    """
    这是一个fun1函数
    :return:
    """
    print(111)

print(fun.__name__,fun1.__name__)
print(fun.__doc__,fun1.__doc__)

结果:
"""
D:\python解释器\python.exe D:/django_programe/library/test.py
fun fun1

    这是一个fun函数
    :return:
     
    这是一个fn1函数
    :return:
    
进程已结束，退出代码 0
"""

```

##### 9.2.4类装饰器

```python
def newEat(newCls):
    class newEatCls():
        def __init__(self, food, water):
            print(newCls)
            self.new = newCls(food)
            self.water = water
        def display(self):
            print("my lunch is " + self.new.food + ' and ' + self.water)
    return newEatCls

@newEat
class eat:
    def __init__(self, food):
        self.food = food

    def display(self):
        print('my lunch is' + self.food)


t = eat('米饭','红烧肉')
print(t)
t.display()
print(eat.__name__)

"""
D:\python解释器\python.exe D:/django_programe/library/test.py
<class '__main__.eat'>
<__main__.newEat.<locals>.newEatCls object at 0x000001320DFA4780>
my lunch is 米饭 and 红烧肉
newEatCls

进程已结束，退出代码 0

"""
第一步：@newEat将eat当作参数传递到函数newEat中，此时newCls = eat
返回 newEatCls类的内存地址，
第二步：实例化对象，实际是实例化newEatCls类，所以，传入两个参数正好传到了def __init__(self, food, water)函数中。
第三步：调用的display也是调用的是newEatCls类中的方法

```

### 10.递归

递归：

递：一直传参

归：返回

1、不断调用自己本身（无效递归）

2、有明确的终止条件

```python
# 1.不断调用自己本身   (无效递归 -- 死递归)

    # def func():
    #     print(1)
    #     func()
    # func()
# 递归的最大深度(层次) 官方说明1000  实际测试 998/997

```

### 11.模块

#### 11.1 模块的了解

#### 11.2  作用

- 文件化管理：提高可读性，避免代码重复
- 拿来就用主义：  避免重复造轮子，减少时间

#### 11.3 定义

一个文件（py文件）就是一个模块（能被调用的工具箱（工具：函数）

#### 11.4  import

- 将test.py文件中所有代码读取到当前文件的内存中
- 给当前文件开辟空间
- 等待被调用

#### 11.5  import 调用工具

- import test       # 导入test模块 （打开工具箱，只能将整个工

    ​                            具箱拿来）                               

- 函数（功能调用）

    test.t1()  

    test.t2()

    print(test.tt)

#### 11.6  起别名  as

- 给函数起别名

    a = test.t1        # 将t1函数更改简短的变量为a

- 给工具箱改名

    import  test  as t       # 工具箱名字过长可以起别名

    ```
    import test        # 导入模块不能加后缀名
    ```

#### 11.7 form 

```
form test import t1    # 从test工具箱中将t1这个工具拿过来
```

```
def t1():
	print("高级工程师")
form test import t1 as t
t1()

# 打印结果：十字螺丝钉
           高级工程师
           （后面的t1将前面的t1覆盖）
```

```
form test import t1 as t 
	def t1():
	print("高级工程师")
t1()                     # 高级工程师
t()                      # 十字螺丝钉
```

#### 11.8   form 与import的区别

- from只能执行导入的函数（功能）
- import能够执行整个模块中所有的功能
- form容易将当前文件中定义的功能覆盖
- import只能导入当前文件夹下的模块
- import后面不能进行加点操作
- import和form都是使用相对路径

```
form day15 import ttt.t1 (错误)
# import 后面不能进行加点操作
form  day15.ttt import t1 (正确)
```

#### 11.9  sys模块

```
import sys
print(sys.path)
sys.path.append(r"C:\Users\oldboy\Desktop")

```

sys 模块    

与python解释器做交互

sys.path()模块导入的路径    列表数据类型，   模块查找的顺序   ***

sys.argv()   在pycharm  运行显示文件的绝对路径    只能在终端运行才能发挥作用，可以加参数

sys.modules()   查看加载到内存的模块

sys.platform()    查看当前操作系统平台   

sys.version （）  查看python解释器版本

##### 11.9.1 模块导入顺序

- sys.path.append(r"C:\Users\oldboy\Desktop")

    内存 > 内置 > 第三方 > 自定义

- sys.path.insert(0,r"C:\Users\oldboy\Desktop")

    内存 > 自定义  > 内置 > 第三方

##### 11.9.2 模块的两种用法

- 当做模块被导入 
- 当做脚本被执行

```
面试题
(1)  当文件被当做模块被调用时，__name__返回的是当前的的模块名
(2)  当文件被当做脚本执行时，__name__返回的是__main__
```

##### 11.9.3  以后会遇到的坑

- 注意自己定义模块的名字
- 注意自己的思路（循环导入时建议把导入模块往下放） 

- from test import *       # 拿取整个工具箱

- from test  import*

    t1()    # 指定拿取test中的t1      

    t2()     # 指定拿取test中的t2

    print(tt)    # 指定拿取tt

- 通过__all__控制要导入的内容

#### 11.10  time模块

##### 11.10.1    time.time()

```
print(time.time())    # 时间戳 浮点数 以秒读取
```

##### 11.10.2 time.sleep()

```
time.sleep(3)    # 睡眠3秒
```

##### 11.10.3  将时间戳转换成结构化时间

```
print(time.localtime(time.time()))   # 记录当前时间
#  其是命名元组，所以可以通过索引和元素查值
```

##### 11.10.4 将结构化时间转换成字符串

```
time_g = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%s",time_g))
```

##### 11.10.5将字符串转换成结构化时间

```
str_time = "2018-10-1 10:11:12"
time_g = time.strptime(str_time,"%Y-%m-%d %H:%M:%s")
```

##### 11.10/66 将结构化时间转换成时间戳

```
print(time.mktime(time_g))
```

#### 11.11  datetime() 模块

##### 11.11.1 获取当前时间

```
datetime.now()    # 获取当前时间
```

##### 11.11.2 指定时间

```
datetime(2018,10,1,10,11,12) - datetime(2011,11,1,10,11,12)
# 指定时间
```

##### 11.11.3 将对象转换成时间戳

```
(datetime.now()).timestamp()
```

##### 11.11.4 将时间戳转换成对象

```
datetime.fromtimestamp(time.time())
```

##### 11.11.5  将对象转换成字符串

```
datetime.now().strftime("%Y-%m-%d %H:%M:%s")
```

##### 11.11.6 将字符串转换成对象

```
s = "2018-12-31 10:11:12"
datetime.strptimes(s,"%Y-%m-%d %H:%M:%s")
```

##### 11.11.7 时间加减

```
datetime.now() - timedelta(days = 1) 
# 当前时间的天数-1
```

#### 11.12 random 模块

```
print(random.randit(1,50))
 # 选择1-50之间的随机整数
```

```
print(random.ndom())
# 0-1之间随机小数，不包含1
```

```
print(random.uniform(1，10))
# 1-10 之间随机小数，不包含10
```

```
print(random.choose(1,2,3,4,5,7)))
# 从容器中随机选择一个
```

```
print(random.choices(1,2,3,4,5,7),k = 3))
# 从容器中随机选择3个元素，以列表的形式输出，会出现重复元素
```

```
print(random.sapmle(1,2,3,4,5,7),k = 3)
# 从容器中随机选择3个元素，以列表的形式输出，不会出现重复元素
```

```
print(random.randrange(1,10,2))
# 随机的奇数或偶数
```

```
lst = [1,2,3,4,5,6,7]
random.shuffle(lst)
print(lst)
 # 将有序的数据打散
```

#### 11.13 序列化  json

##### 11.13.1 什么是序列化？

```
当程序运行时，所有的变量或者对象都是存储到内存中的，一旦程序调用完成，这些变量或者对象所占有的内存都会被回收。而为了实现变量和对象持久化的存储到磁盘中或在网络上进行传输，我们需要将变量或者对象转化为二进制流的方式。而将其转化为二进制流的过程就是序列化
```

##### 11.13.2 什么叫做反序列化？

```
就是说程序运行的时候不能从磁盘中进行读取，需要将序列化的对象或者变量从磁盘中转移到内存中，同时也会将二进制流转换为原来的数据格式。我们把这一过程叫做反序列化
```

两个模块实现序列化与反序列化。

1. json
2. pickle

dumps     loads             --用于网络传输

dump   load    ---用于文件存储

json：

```python
dic = {"k":1}
s = json.dumps(dic)  #将字典转换成字符串
print(repr(s))
print(json.loads(s))   #将字符串转换成字典
#将数据类型转换成字符串（序列化），将字符串转成原数据类型（反序列）
#能够序列化：字典，列表，元祖序列后自动变成列表
不可以使用str转成字符串后，使用loads再进行反序列化，因为str和dumps转换的方式不一样，存在区别。
使用str转，会报错。
import json
dic={"k1":2}
# a = json.dumps(dic)
# print(json.dumps(dic))
a = str(dic)
print(repr(a))
print(type(a))
print(type(json.loads(a)))
```

![1566561712104](../python%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/python%E4%B9%8B%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91%E8%A7%84%E8%8C%83.assets/1566561712104.png)

str和json.dumps的区别：

​	https://blog.csdn.net/weixin_34009794/article/details/88004878

```python
import json
dic={"k1":2}

print(json.dump(dic,open("aaa","w",encoding="utf-8")))   #将字典转换成字符串后，写入到文件aaa中，返回none
print(type(json.load(open("aaa","r",encoding="utf-8"))))   #将文件aaa中的内容读取出来，转换成字典。
【
import json
dic={"k1":"宝元"}

print(json.dump(dic,open("aaa","w",encoding="utf-8")))   默认使用unicode存储
print(type(json.load(open("aaa","r",encoding="utf-8"))))
文件aaa中：{"k1": "\u5b9d\u5143"}

"""
ensure_ascii:，当它为True的时候，所有非ASCII码字符显示为\uXXXX序列，只需在dump时将ensure_ascii设置为False即可，此时存入json的中文即可正常显示。
separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(,,:)；这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：”隔开。
sort_keys：将数据根据keys的值进行排序。 剩下的自己看源码研究
"""
dic = {"meet":27,"太白":30,"alex":36,"wusir":33}
print(json.dumps(dic,ensure_ascii=False,sort_keys=True))  默认从小到大排序
】
```

pickle

只有python有，几乎可以序列python中所有数据类型，匿名函数不能序列

pickle.dumps()  #将元数据类型转成类似字节的内容

pickle.loads （）#将类似字节的内容转换成原数据类型

```python
# import pickle
# def func():
#     print(1)
#
# a = pickle.dumps(func)   # 将原数据类型转换成类似字节的内容
# print(pickle.loads(a))   # 将类似字节的内容转换成原数据类型
```

**dumps、loads**

```python
import pickle
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = pickle.dumps(dic)
print(str_dic)  # bytes类型

dic2 = pickle.loads(str_dic)
print(dic2)    #字典
# 还可以序列化对象
import pickle
def func():
    print(666)

ret = pickle.dumps(func)
print(ret,type(ret))  # b'\x80\x03c__main__\nfunc\nq\x00.' <class 'bytes'>
f1 = pickle.loads(ret)  # f1得到 func函数的内存地址
f1()  # 执行func函数
```

**dump、load**

```python
dic = {(1,2):'oldboy',1:True,'set':{1,2,3}}
f = open('pick序列化',mode='wb')
pickle.dump(dic,f)
f.close()
with open('pick序列化',mode='wb') as f1:
    pickle.dump(dic,f1)
```

**pickle序列化存储多个数据到一个文件中**

```python
dic1 = {'name':'oldboy1'}
dic2 = {'name':'oldboy2'}
dic3 = {'name':'oldboy3'}

f = open('pick多数据',mode='wb')
pickle.dump(dic1,f)
pickle.dump(dic2,f)
pickle.dump(dic3,f)
f.close()

f = open('pick多数据',mode='rb')
while True:
    try:
        print(pickle.load(f))
    except EOFError:
        break
f.close()
```

#### 11.14 OS模块

import   os  #os是和操作系统做交互，给操作发指令

##### 11.14.1 工作目录相关的工作路径：

- os.getcwd    #获取当前文件工作的路径
- os.chdir()   改变当前脚本工作目录，相当于shell下的cd
- os.curdir     返回当前目录
- os.pardir   获取当前目录的父目录字符串名：

##### 11.14.2 文件夹相关：

- os.makedirs()   生成剁成递归目录 
- os.removedirs()   若目录为空，则是删除，并递归到上一级目录，如若也为空，则删除
- os.mkdir()    生成单级目录，相当于shell中mkdir   
- os.rmdir()     删除单级空目录，若目录不为空，则无法删除，报错，相当于shell  中rmdir  dirname
- os.listdir("dirname")   列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表的方式打印

##### 11.14.3文件相关：

- os.remove()   删除一个文件
- os.rename()   重命名文件
- os.stat（）      获取文件/目录信息

##### 11.14.4 路径相关：

- os.path.abspath（）  返回path规范化的绝对路径
- os.path.split()  将path分割成目录和文件名二元组返回
- os.path.dirname()  返回path目录，其实就是os.path.split()的第一个元素
- os.path.basename()  返回path最后的文件名

```python
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False  ***
os.path.isabs(path)  如果path是绝对路径，返回True  **
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False  ***
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False  ***
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略 ***
os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间  **
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间  **
os.path.getsize(path) 返回path的大小 ***
```

##### 11.14.5 操作系统相关：

```python
os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/" *
os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n" 
os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为: *
os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix' *
# 和执行系统命令相关
os.system("bash command")  运行shell命令，直接显示  **
os.popen("bash command).read()  运行shell命令，获取执行结果  **
os.environ  获取系统环境变量  **
```

os.stat('path/filename') 获取文件/目录信息

```python
stat 结构:
st_mode: inode 保护模式
st_ino: inode 节点号。
st_dev: inode 驻留的设备。
st_nlink: inode 的链接数。
st_uid: 所有者的用户ID。
st_gid: 所有者的组ID。
st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
st_atime: 上次访问的时间。
st_mtime: 最后一次修改的时间。
st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
```

### 第三章 模块进阶

#### 1.  re  正则表达式

正则就是用一些具有特殊含义的符号组合在一起。

\w |\W

```python
name = "宝元-meet_123 \n \t"
print(re.findall("\W",name))  #匹配非字母（包含中文）或数字或下划线
print(re.findall("\w",name))   #匹配字母（包含中文）或数字或下划线
```

\S|\s

```python
print(re.findall("\s",name))   #匹配任意的空白符
print(re.findall("\S",name))   #匹配任意非空白符
```

\D|\d 

```python
print(re.findall("\d",name))  #匹配数字
print(re.findall("\D",name))  #	匹配非数字
```

\A   ^

```python
print(re.findall("\A宝元",name))   #从字符串开头匹配
print(re.findall("^宝元",name))   #从字符串开头匹配
```

\z  $

```python
name = "宝元-meet_123 "
print(re.findall("123 \Z",name))  #匹配字符串的结束，如果是换行，只匹配到换行前的结果
print(re.findall("123 $",name))   #匹配字符串的结束，如果是换行，只匹配到换行前的结果  
```

\n  匹配一个换行符

\t  匹配一个制表符

```python
print(re.findall("\n",name))
print(re.findall("\t",name))
```

.  匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。

```python
name = "宝元-meet_123 "
print(re.findall(".",name))
print(re.findall(".",name,re.DOTALL))
['宝', '元', '-', 'm', 'e', 'e', 't', '_', '1', '2', '3', ' ']
['宝', '元', '-', 'm', 'e', 'e', 't', '_', '1', '2', '3', ' ']
```

*匹配 *前面的字符个数是0个或者多个左边字符

```python
name = "m-e-me-meet-meet_123\t \nmeeeeeet mtttt"
print(re.findall("me*",name))
['m', 'me', 'mee', 'mee', 'meeeeee', 'm']
```

+匹配+前面的字符一个或者多个左边的字符。

```python
name = "m-e-me-meet-meet_123\t \nmeeeeeet mtttt"
print(re.findall("me+",name))
['me', 'mee', 'mee', 'meeeeee']
```

? 匹配前面的字符0个或者1个左边的字符，非贪婪方式。

```python
name = "m-e-me-meet-meet_123\t \nmeeeeeet mtttt"
print(re.findall("me?",name))  #表示？前面的e允许没有或着有一个存在
['m', 'me', 'me', 'me', 'me', 'm']
```

{n  }精准匹配n个前面的表达式。

{n,m} 匹配n到m次由前面的正则表达式定义的片段，贪婪方式

```python
name = "m-e-me-meet-meet_123\t \nmeeeeeet mtttt"
print(re.findall("e{1,4}",name))
```

ab  匹配a或者b



()匹配括号内的表达式，也表示一个组

**()** 分组 定制一个匹配规则

```python
import re
print(re.findall('(.*?)_sb', 'alex_sb wusir_sb 日天_sb'))
# 结果
['alex', ' wusir', ' 日天']

# 应用举例:
print(re.findall('href="(.*?)"','<a href="http://www.baidu.com">点击</a>')
# 结果
['http://www.baidu.com']
```

**.\*** 任意内容0个或多个

```python
import re
name = "m-e-me-meet-meet_123\t \n"
print(re.findall(".*",name))
# 结果
['m-e-me-meet-meet_123', '']
```

**.\*?** 任意内容0个或1个

```python
import re
name = "m-e-me-meet-meet_123"
print(re.findall("m.*?e",name))
# 结果
['m-e', 'me', 'mee', 'mee']

import re
name = "m-e-me-meet-meet_123"
print(re.findall("m.?e",name))
# 结果
['m-e', 'me', 'mee', 'mee']
```

**[]** 获取括号中的内容

```python
import re
name = "m-e-me-meet-meet_123"
print(re.findall("[1-9]",name))
# 结果
['1', '2', '3']
# []中的-是什么至什么不会匹配-

import re
name = "m-e-me-meet-meet_123"
print(re.findall("[a-z]",name))
# 结果
['m', 'e', 'm', 'e', 'm', 'e', 'e', 't', 'm', 'e', 'e', 't']

import re
name = "m-e-me-meet-meet_123"
print(re.findall("[A-z]",name))
# 结果
['m', 'e', 'm', 'e', 'm', 'e', 'e', 't', 'm', 'e', 'e', 't', '_']
# 是按照ascii码表位进行匹配的

import re
name = "m-e-me-meet-meet_123"
print(re.findall("[a-zA-Z]",name))
# 结果
['m', 'e', 'm', 'e', 'm', 'e', 'e', 't', 'm', 'e', 'e', 't']

import re
name = "m-e-me-meet-meet_123"
print(re.findall("[^A-z]",name))
# 结果
['-', '-', '-', '-', '1', '2', '3']
# [^A-z] 有上尖号就是取反,获取不是字母和特定的几个字符

如果想要匹配到-,就需要进行如下操作(将-号放到最前面)
import re
name = "m-e-me-meet-meet_123"
print(re.findall("[-+*/]",name))
# 结果
['-', '-', '-', '-']
```

**|** 匹配 左边或者右边

```python
import re
print(re.findall('alex|宝元|wusir', 'alex宝元wusiraleeeex宝宝元odlb'))
# 结果
['alex', '宝元', 'wusir', '宝元']

import re
print(re.findall('compan(day|morrow)','Work harder today than yesterday, and the day after tomorrow will be better'))
# 结果
['day', 'morrow']

import re
print(re.findall('compan(?:day|morrow)','Work harder today than yesterday, and the day after tomorrow will be better'))
# 结果
['today', 'tomorrow']
# 分组() 中加入?: 表示将整体匹配出来而不只是()里面的内容。
```

**findall** 全部找到返回一个列表

```python
import re
print(re.findall("alex","alexdsb,alex_sb,alexnb,al_ex"))
# 结果
['alex', 'alex', 'alex']
```

**search** 从字符串中任意位置进行匹配查找到一个就停止了,返回的是一个对象. 获取匹配的内容必须使用.group()进行获取

```python
import re
print(re.search("sb|nb","alexdsb,alex_sb,alexnb,al_ex").group())
# 结果
sb
```

**match** 从字符串开始位置进行匹配

```python
import re
print(re.match('meet', 'meet alex wusir 日天').group())
# 结果
meet

import re
print(re.match('alex', 'meet alex wusir 日天'))
# 结果
None
```

**split** 分隔 可按照任意分隔符进行分隔

```python
import re
print(re.split('[ ：:,;；，]','alex wusir,日天，太白;女神;肖锋：吴超'))
# 结果
['alex', 'wusir', '日天', '太白', '女神', '肖锋', '吴超']
```

**sub** 替换

```python
import re
print(re.sub('barry', 'meet', 'barry是最好的讲师，barry就是一个普通老师，请不要将barry当男神对待。'))
# 结果
meet是最好的讲师，meet就是一个普通老师，请不要将meet当男神对待。
```

**compile** 定义匹配规则

```python
import re
obj = re.compile('\d{2}')
print(obj.findall("alex12345"))
# 结果
['12', '34']

import re
['12', '34']
obj = re.compile('\d{2}')
print(obj.search("alex12345").group())
# 结果
12
```

**finditer** 返回一个迭代器

```python
import re
g = re.finditer('al',"alex_alsb,al22,aladf")
print(next(g).group())
print([i.group() for i in g])
# 结果
al
['al','al','al']
```

给分组起名字

```python
import re
ret = re.search("<(?P<tag_name>\w+)>\w+</\w+>","<h1>hello</h1>")
print(ret.group("tag_name"))
print(ret.group())
# 结果
h1
<h1>hello</h1>

import re
ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
print(ret.group(1))
print(ret.group())
```

```python
#练习
1.2 匹配所有的数字（包含小数）
print(re.findall(r'\d+\.?\d*|\d*\.?\d+', "1-2*(60+(-40.35/5)-(-4*3))"))

s1 = '''
时间就是1995-04-27,2005-04-27
1999-04-27 老男孩教育创始人
老男孩老师 alex 1980-04-27:1980-04-27
2018-12-08
'''
print(re.findall('\d{4}-\d{2}-\d{2}', s1))

4 匹配 一个浮点数
print(re.findall('\d+\.\d*','1.17'))

5 匹配qq号：腾讯从10000开始：
print(re.findall('[1-9][0-9]{4,}', '2413545136'))

s1 = '''
<div id="cnblogs_post_body" class="blogpost-body"><h3><span style="font-family: 楷体;">python基础篇</span></h3>
<p><span style="font-family: 楷体;">&nbsp; &nbsp;<strong><a href="http://www.cnblogs.com/guobaoyuan/p/6847032.html" target="_blank">python 基础知识</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/p/6627631.html" target="_blank">python 初始python</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<strong><a href="http://www.cnblogs.com/guobaoyuan/articles/7087609.html" target="_blank">python 字符编码</a></strong></strong></span></p>
<p><span style="font-family: 楷体;"><strong><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/articles/6752157.html" target="_blank">python 类型及变量</a></strong></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/p/6847663.html" target="_blank">python 字符串详解</a></strong></span></p>
<p><span style="font-family: 楷体;">&nbsp; &nbsp;<strong><a href="http://www.cnblogs.com/guobaoyuan/p/6850347.html" target="_blank">python 列表详解</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/p/6850496.html" target="_blank">python 数字元祖</a></strong></span></p>
<p><span style="font-family: 楷体;">&nbsp; &nbsp;<strong><a href="http://www.cnblogs.com/guobaoyuan/p/6851820.html" target="_blank">python 字典详解</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<strong><a href="http://www.cnblogs.com/guobaoyuan/p/6852131.html" target="_blank">python 集合详解</a></strong></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/articles/7087614.html" target="_blank">python 数据类型</a>&nbsp;</strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/p/6752169.html" target="_blank">python文件操作</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/p/8149209.html" target="_blank">python 闭包</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/articles/6705714.html" target="_blank">python 函数详解</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/articles/7087616.html" target="_blank">python 函数、装饰器、内置函数</a></strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/articles/7087629.html" target="_blank">python 迭代器 生成器</a>&nbsp;&nbsp;</strong></span></p>
<p><span style="font-family: 楷体;"><strong>&nbsp; &nbsp;<a href="http://www.cnblogs.com/guobaoyuan/articles/6757215.html" target="_blank">python匿名函数、内置函数</a></strong></span></p>
</div>
'''
1,找到所有的span标签的内容
ret = re.findall('<span(.*?)>', s1)
print(ret)

2,找到所有a标签对应的url
print(re.findall('<a href="(.*?)".*?</a>',s1))
```



#### 2. 包的写作要求

```
一
通过from和import 可以查询包中的指定方法
有两种
1.from day1.day2 import cen2
	cen2.cen2()
2.import day1.day2.cen2 as f
	f.cen2()
这两种都是绝对路径那都好使，就是用起来不灵活
还有一种省略的方法
from day1.day2.cen2 import *

通过from和import可以获取到整个包
两种
1.from day1.day2 import *
 拿到的是day2中所有的模块
 取值方式
 cen3.cen3()
2.import day1
 取值方式  
day1.day2.cen2.cen2()
需要设置__init__如# from . import day2 每个init都要配置
这里拿到的是整个包中所有的模块，但是想要使用模块中的函数换需要使用绝对路径取获取
总结：无论是想要获得模块还是包其实都是通过绝对路径
二
相对路径不能使用到最外层，上级必须是包
注意：这里如果使用相对路径只能在启动文件中执行，如果在当前文件夹引用时会报错

问题：
如果想要调用同级模块中的函数时，使用相对路径时，在本页面能运行不一定在启动文件中能用
解决：
通过i
import os
import sys
b=os.path.dirname(__file__)
sys.path.insert(0,b)
再次调用相对路径时自动获取父级的绝对路径。将代码复制到别的文件时也可以直接使用

```





#### 3. 日志

```
# logging -- 日志
# 1.记录用户的信息
# 2.记录个人流水
# 3.记录软件的运行状态
# 4.记录程序员发出的指令
# 5.用于程序员代码调试

# 日志中要记录的信息
# 默认从warning开始记录

# 手动挡
# import logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filename="test.log",
#                     filemode="a",
# )
#
#
# logging.debug("你是疯儿,我是傻") # debug 调试
# logging.info("疯疯癫癫去我家")   # info 信息
# logging.warning("缠缠绵绵到天涯")   # info 警告
# logging.error("我下不床")           # error 错误
# logging.critical("你回不了家")        # critical 危险


# 自动挡
import logging
# 初始化一个空日志
logger = logging.getLogger()   # -- 创建了一个对象
# 创建一个文件,用于记录日志信息
fh = logging.FileHandler('test.log',encoding='utf-8')
# 创建一个文件,用于记录日志信息
fh1 = logging.FileHandler('test1.log',encoding='utf-8')
# 创建一个可以在屏幕输出的东西
ch = logging.StreamHandler()
# 对要记录的信息定义格式
msg = logging.Formatter('%(asctime)s - [line:%(lineno)d] %(filename)s - %(levelname)s - %(message)s')
# 对要记录的信息定义格式
msg1 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# 设置记录等级
logger.setLevel(10) or logger.setLevel(logging.DEBUG)
# 等级对应表
'''
DEBUG - 10
INFO - 20
WARNING - 30
ERROR - 40
CRITICAL - 50
'''
# 将咱们设置好的格式绑定到文件上
fh.setFormatter(msg)
fh1.setFormatter(msg)
# 将咱们设置好的格式绑定到屏幕上
ch.setFormatter(msg1)
# 将设置存储日志信息的文件绑定到logger日志上
logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
logger.addHandler(fh1)
logger.addHandler(ch)
# 记录日志
logger.debug([1,2,3,4,])
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')

```

#### 4. hashlib

```
# 摘要算法,加密算数 ...
# 1.加密
# 2.校验

# md5,sha1,sha256,sha512
# 1.md5,加密速度快,安全系数低
# 2.sha512 加密速度慢,安全系数高

# 明文(123adsa) -- 字节 -- 密文(bs2501153023ras32rf150q23r13ar)

# 1.当要加密的内容相同时,你的密文一定是一样的
# 2.当你的明文不一样时,密文不一样
# 3.不可逆

# import hashlib
# md5 = hashlib.md5()   # 初始化
# md5.update("alex".encode("utf-8"))   # 将明文转换成字节添加到新初始化的md5中
# print(md5.hexdigest())   # 进行加密

# dic = {"534b44a19bf18d20b71ecc4eb77c572f":"alex"}

# 534b44a19bf18d20b71ecc4eb77c572f
# 9b4c00b63b24c060abd31c6cb96b7bc8

# msg = input("请输入密码")
# print(msg)

# 加盐

# 加固定盐
# import hashlib
# md5 = hashlib.md5("rimo_dsb".encode("utf-8"))   # 初始化
# md5.update("alex".encode("utf-8"))   # 将明文转换成字节添加到新初始化的md5中
# print(md5.hexdigest())   # 进行加密

# 加动态盐

# import hashlib
# user = input("username:")
# pwd = input("password:")
#
# md5 = hashlib.md5(user.encode("utf-8"))   # 初始化
# md5.update(pwd.encode("utf-8"))   # 将明文转换成字节添加到新初始化的md5中
# print(md5.hexdigest())   # 进行加密


# 1f174367fa08bf51d789a5c988f8ff1e
# d599321766c76d5ce8b9e2b53ebd5764

# 60c6d277a8bd81de7fdde19201bf9c58a3df08f4
# 35f319ca1dfc9689f5a33631c8f93ed7c3120ee7afa05b1672c7df7b71f63a6753def5fd3ac9db2eaf90ccab6bff31a486b51c7095ff958d228102b84efd7736

# import hashlib
# sha1 = hashlib.sha1()
# sha1.update("alex".encode("utf-8"))
# print(sha1.hexdigest())

# import hashlib
# sha1 = hashlib.sha1()
# sha1.update("日魔就是一个大SB".encode("utf-8"))
# print(sha1.hexdigest())
#
# sha1 = hashlib.sha1()
# sha1.update("日魔就是一个大SB".encode("gbk"))
# print(sha1.hexdigest())

# 中文内容编码不同时密文是不一致,英文的密文都是一致的

# import hashlib
# md5 = hashlib.md5()
# md5.update(b"afdadfadfadsfafasdfasfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfd")
# md5.update(b"afdadfadfadsfafasdfasfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfd")
# md5.update(b"afdadfadfadsfafasdfasfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfd")
# print(md5.hexdigest())
# efe9bb9e7e090768597517019e5716b6
# efe9bb9e7e090768597517019e5716b6

# import hashlib
# md5 = hashlib.md5()
# md5.update(b"afdadfadfadsfafasd")
# print(md5.hexdigest())

# import hashlib
# def file_check(file_path):
#     with open(file_path,mode='rb') as f1:
#         md5= hashlib.md5()
#         while True:
#             content = f1.read(1024)   # 2049 1025 1
#             if content:
#                 md5.update(content)
#             else:
#                 return md5.hexdigest()
# print(file_check('python-3.6.6-amd64.exe'))

# ftp 

```

#### 5.collections

```
# collections  -- 基于python自带的数据类型之上额外增的几个数据类型

# 命名元组:
# from collections import namedtuple
# limit = namedtuple("limit",["x","y"])
# l = limit(1,2)
# print(l.x)
# print(l[0])


# 双端队列
from collections import deque
# lst = [1,2,3,4]

# deque = [1,2,3,4]
# deque.append(1)
# deque.remove(1)
# print(deque)

# l = deque([1,2])
# l.append(3)
# l.appendleft(0)
# l.pop()
# l.popleft()
# l.remove(2)
# print(l)

# 队列: 先进先出
# 栈: 先进后出

# from collections import OrderedDict
# 有序字典(python2版本)  -- python3.6 默认是显示有序

# dic = OrderedDict(k=1,v=11,k1=111)
# print(dic)
# print(dic.get("k"))
# dic.move_to_end("k")


from collections import defaultdict
# 默认字典

# dic = defaultdict(list)
# dic[1]
# print(dic)


# lst = [11,22,33,44,55,77,88,99]
# dic = defaultdict(list)
# for i in lst:
#     if i > 66:
#         dic['key1'].append(i)
#     else:
#         dic['key2'].append(i)
# print(dict(dic))


# from collections import Counter
# 计数 返回一个字典
# lst = [1,2,112,312,312,31,1,1,1231,23,123,1,1,1,12,32]
# d = Counter(lst)
# print(list(d.elements()))
# print(dict(d))

# 重要Counter
查看数据类型是否是列表
l=[1,2,3]
print(isinstance(l,list))



```



```python
字典按照值排序：
方法一：
my_data = {'Python': 20, 'Swift':32, 'Kotlin': 43, 'Go': 25}
print(dict(sorted(my_data.items(),key=lambda t:t[1])))
方法二：
my_data = {'Python': 20, 'Swift':32, 'Kotlin': 43, 'Go': 25}
print(dict(zip(dict(sorted(zip(my_data.values(),my_data.keys()))).values(),dict(sorted(zip(my_data.values(),my_data.keys()))).keys())))
zip：可以实现字典的键和值互换
方法三：
from collections import OrderedDict
my_data = {'Python': 20, 'Swift':32, 'Kotlin': 43, 'Go': 25}
# 创建基于key排序的OrderedDict
d1 = OrderedDict(sorted(my_data.items(), key=lambda t: t[0]))
创建基于value排序的OrderedDict
d1 = OrderedDict(sorted(my_data.items(), key=lambda t: t[1]))
print(dict(d1))
""
由于 OrderedDict 是有序的，因此 Python 为之提供了如下两个方法：
popitem(last=True)：默认弹出并返回最右边（最后加入）的 key-value 对；如果将 last 参数设为 False，则弹出并返回最左边（最先加入）的 key-value 对。
move_to_end(key, last=True)：默认将指定的 key-value 对移动到最右边（最后加入）；如果将 last 改为 False，则将指定的 key-value 对移动到最左边（最先加入）。

""
```

```python
from collections import defaultdict
defaultdict 可以为不存在的 key 设置默认的 value
s = [('Python', 1), ('Swift', 2), ('Python', 3), ('Swift', 4), ('Python', 9)]
# 创建defaultdict，设置由list()函数来生成默认值
d = defaultdict(list)
for k, v in s:
    # 直接访问defaultdict中指定key对应的value即可。
    # 如果该key不存在，defaultdict会自动为该key生成默认值
    d[k].append(v)
print(dict(d))

```

### 第四章  面向对象

#### 1. 面向对象

我们现在学习到当前的这个阶段，我们能够实现很多功能了，回想一下我们其实学习了两种编程方式,今天咱们在学习一种编程方式,在开发中只有个这三种开发方式

编程方式：

- 过程式编程
- 函数式编程
- 面向对象式编程

过程式编程 vs 函数式编程

有个s1='aabbbccddeeeffffssss'使用程序统计s1字符串的长度，禁止使用len函数

```
count = 0
for i in s1：
    count += 1
print(count)
```

这样我们就成功的实现了，现在又出现了一个列表 l1 = [1,2,3,4,5,6,7,8,9,0,01,2132,321,41234],还是同样的需求不能使用len函数来统计长度

```
count = 0
for i in l1：
    count += 1
print(count)
```

这样也完美的实现了这个需求，但是将两个需求一对比发现只有可迭代对象是不同的，其他的代码都是一样的，就出现了重复代码的情况。看到这个我们瞬间就想到函数式编程，函数式编程就完美的将重复代码的现象解决掉，我们现在用函数式编程来实现一下

```
def my_count(obj):
    count = 0
    for i in obj:
        count += 1 
    print(count)
my_count(s1)
my_count(l1)
```

这样就很好的解决了,过程式编程和函数式编程没有问题后咱们来看看函数式编程和面向对象式编程

[回到顶部](https://www.cnblogs.com/guobaoyuan/p/10757460.html#_labelTop)

#### 2.函数式编程 vs 面向对象式编程

函数式编程我们一直在用,ATM机是不是就全都是用函数写的,写了一堆函数,还需要人为的进行分类,加注释 才能稍微的清晰一些,如下:

```
# 这是账户相关的逻辑

def login():
    print('这是登录函数')


def register():
    print('这是注册函数')


def check_user():
    print('这是验证用户名')


def check_password():
    print('这是验证密码')


# 这是金钱相关的逻辑
def save():
    print('这是存钱的逻辑')


def send_money():
    print('这是转账的逻辑')


def show_money():
    print('这是查看余额的逻辑')


# 这是购物相关的逻辑
def shopping():
    print('这是购物逻辑')


def show_love_goods():
    print('这是查看喜欢的商品')


def show_buy_goods():
    print('这是查看购买的商品')
```

这个九个函数我们还是写了注释,不仔细看也不知道都是什么功能,给人直观的感觉就是比较乱,我们先查看一下面向对象式编程,在给大家讲面向对象

```
class UserInfo:

    def login(self):
        pass

    def register(self):
        pass

    def show_user(self):
        pass

    def show_password(self):
        pass

class Shopping:
    
    def show_buy_goods(self):
        pass
    
    def show_love_goods(self):
        pass
    
class Money:
    
    def save(self):
        pass
    
    def send_money(self):
        pass
    
    def show_money(self):
        pass
```

面向对象式编程就从代码级别上看比较清晰,容易读. 还将一类相似的功能和属性汇总到一起,帮助咱们做到分类的功能

这其实就是面向对象的优点一:

1. 代码可读性强
2. 将相似的功能和属性汇总到一起,帮助咱们进行分类

面向对象不止这一个优点,我们先来学习面向对象,优点慢慢进行体会,首先要学习面向对象就要学习什么是类什么是对象

#### 3.什么是对象

一类事物的统称，不能实际感觉到的

定义类其实和定义函数很类似,看如下对比:

```
def func():
    print('这是一个函数')
class Dog():
    print('这是一个类')
```

两个对比之后发现,关键字不同,定义类是class 函数的名字和类的名字有点区别,是的没错 类名需要使用大驼峰,两个或多个单词以上不建议使用下划线相连

类是由两部分组成:

- 类变量(静态属性,静态字段)
- 类方法(动态属性,方法)

上边说到了类变量和类方法,我们来定义一个完整的类

```
class Pepole:
    main = '有思想'  #类变量 静态属性 静态字段

    def work(self):  #类方法 动态属性 函数
        print('正在工作')

    def eat(self):
        print(在吃东西')
```

我们来观察我们写的这个类,这个类就是一个人类,我写的类变量就是所有人都具有的,我写的类方法就是人类都具有的功能,也就是说人会做的事情.好了  你告诉我你是什么,你说你是人 ok你怎么证明?  你只要有思想会工作你就是人,我们可以根据自己的特点去总结类.你们刚开始接触面向对象不会定义类很正常,我现在先教你一个方法

简单定义类

```
我:小黄你叫什么啊?

小黄:王富贵

我:小黄你多大了?

小黄:20

我:小黄你是男的还是女的?

小黄:男

我:小黄你能干啥?

小黄:我能吃饭,睡觉,说话,工作

我:小白你叫什么啊?

小白:王老二

我:小白你多大了?

小白:25

我:小白你是男的还是女的?

小白:男的

我:小白你能干啥?

小白:我能吃饭,睡觉,说话,工作
```

通过于小黄,小白得到的信息,我们将这些信息用代码描述出来

```
# 小黄

name = '王富贵'
age = 20
sex = '男'


def eat():
    print('这是吃饭')


def sleep():
    print('这是睡觉')


def talk():
    print('这是说话')


def work():
    print('这是工作')


# 小白

name = '王老二'
age = 25
sex = '男'


def eat():
    print('这是吃饭')


def sleep():
    print('这是睡觉')


def talk():
    print('这是说话')


def work():
    print('这是工作')
```

发现小黄和小白只有名字和年龄不一样其他好像都是一样的,我们将一样的东西用类包一下

```
class People:
    
    def eat(self):
        pass
    
    def sleep(self):
        pass
    
    def talk(self):
        pass
    
    def work(self):
        pass

```

我们将他们两共同的功能放到一个类中,名字和年龄是小黄和小白的特征也是区分的地方咱们稍后在说,先说他们都有的功能,现在把他们共同的功能写到一个类中,我们先来分析一下 代码运行都干了什么

定义类发生的事情

```
print(People.__dict__)  #类名.__dict__就是查看类空间的内容

```

#### 4.万能的点

**对象可以通过点来调用方法**

- 类就是一些相似事物的统称,范围比较广
- 对象就是具体的实物,范围比较小.能够准确定位到某些东西
- 定义类 使用 `class`关键字 类名使用大驼峰
- 类名+() 是在实例化对象
- 查看类空间和对象空间使用.__dict__
- 类和对象通过.可以进行增删改查 这里的增和删相同和字典有点像
- 除去(类方法,静态方法) 建议使用对象调用类中的方法,因为Python帮我们自动把对象当最第一个参数传递给self
- self 是可以进行更改,但是不建议更改(面试可能会问)
- 一个类可以有多个对象,但是对象的空间是独立的

#### 5. 类名角度操作类

```
class People:
    mind = "有思想"  # 静态属性

    def eat(self):   # 方法
        print("在吃饭")

    def work(self):
        print("在工作")

# 查看类下所有内容
# print(People.__dict__)

# 万能的点 查看单个属性或方法
# print(People.mind)

# 增:
# People.emotion = "有情感"

# 删:
# del People.mind

# 改:
# People.mind = "无脑"
# print(People.__dict__)

# 查:
# print(People.mind)  # 单独查一个

# People.eat(1)
# 一般情况下我们不使用类名去操作方法 (类方法除外)

```

#### 6. 对象角度操作类

```
# class People:
#     mind = "有思想"  # 静态属性
#
#     def eat(self):   # 方法
#         print("self --->",self)
#         print("在吃饭")
#
#     def work(self):
#         print("在工作")

# 创建对象 -- 类名()
# p = People()  # 实例化对象
# print(p.__dict__)  # 对象的空间
# print("p---->",p)
# print(p.mind)
# p.eat()
# p.work()



class People:

    mind = "有思想"  # 静态属性

    def __init__(self,name,age,sex):   # 初始化
        # self == p
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):   # 方法
        print(self.name)
        print("在吃饭")

    def work(self):
        print("在工作")

p = People("alex",19,"男") # 实例化一个对象
p.eat()


# 类外部给对象创建属性 不建议这样使用
# p.mind = "无脑"  # 给对象创了一个空间
# print(People.__dict__)
# print(p.__dict__)




# 对象只能使用类中的属性和方法,不能进行修改

# 1. 实例化一个对象,给对象开辟空间
# 2. 自动执行__init__方法
# 3. 自动将对象的地址隐性传递给了self

```

#### 7. 类空间

```
# 1.给对象空间添加属性
# class A:
#
#     def __init__(self,name):
#         # 类里边给对象添加属性
#         self.name = name
#
#     def func(self,sex):
#         self.sex = sex
#
# a = A("meet")
# a.func("男")
# # 类外边给对象添加属性
# a.age = 18
# print(a.__dict__)

# 总结:给对象空间添加属性可以在类的内部,类的外部,类中的方法

# 2.给类空间添加属性

# class A:
#
#     def __init__(self,name):
#         # 类内部给类空间添加属性
#         A.name = name
#
#     def func(self,age):
#         # 类中的方法给类空间添加属性
#         A.age = age

# 类外部给类空间添加属性
# A.name = "alex"
# a = A('meet')
# a.func(19)
# print(A.__dict__)

# 总结:给类空间添加属性可以在类的内部,类的外部,类中的方法

# class B:
#
#     def __init__(self,name):
#         self.name = name
#
#     def index(self):
#         print(self.name,"is index")
#
# b = B("alex")
# b.index()

```

#### 8. 类与类之间的关系

```
# 1.依赖关系
# 主 -- 人
# 次 -- 冰箱

# class People:
#
#     def __init__(self,name):
#         self.name = name
#
#     def open(self,bx):
#         bx.open_door(self)
#
#     def close(self,bx):
#         bx.close_door(self)
#
#
# class Refrigerator:
#
#     def __init__(self,name):
#         self.name = name
#
#     def open_door(self,p):
#         print(f"{p.name} 打开冰箱")
#
#     def close_door(self,p):
#         print(f"{p.name} 关闭冰箱")
#
#
# r = People("日魔")
# aux = Refrigerator("奥克斯")
# r.open(aux)
# r.close(aux)


# class People:
#
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self,food,flag):
#         food.eat(self,flag)
#
#
# class Food:
#
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self,p,f):
#         if f:
#             print(f"{p.name} 吃了 {self.name}")
#         else:
#             print(f"{p.name} 消化了 {self.name}")
#
#
# p = People("日魔")
# f = Food("大煎饼")
# p.eat(f,False)


# 总结:将一个类的对象当做参数传递到另一个类中使用 -- 依赖关系

# 2.组合关系

# class Boy:
#
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self):
#         print(f"{self.name}和{self.girl} 一起吃了个烛光晚餐!")
#
#     def make_keep(self):
#         print(f"{self.name}带着{self.girl}去做俯卧撑!")
#
# b = Boy("日魔")
# b.girl = "乔bi萝"
# # b.eat()
# b.make_keep()


# class Boy:
#
#     def __init__(self,name,g):
#         self.name = name    # self = b
#         self.g = g          # g就是girl类实例化的一个对象内存地址
#
#     def eat(self):
#         print(f"{self.name}和{self.g.age}岁,且{self.g.weight}公斤的{self.g.name}py朋友.一起吃了个烛光晚餐!")
#
#     def make_keep(self):
#         self.g.live(f"{self.g.weight}公斤的{self.g.name}给{self.name}踩背")
#
#
# class Girl:
#
#     def __init__(self,name,age,sex,weight,*args):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.weight = weight
#         self.args = args
#
#     def live(self,argv):
#         print(f"直播内容:{argv}")
#
#
# g = Girl("乔毕萝",54,"女",220)
# b = Boy("太正博",g)
# b.make_keep()


#总结: 将一个类的对象封装到另一个类的对象属性中




# 1.类空间
# 给类空间和对象空间添加属性
# 类外部,内部,方法中

# 2.类关系:
# 依赖:将一个类的对象当做参数传递给另一个类的方法中
# 组合:将一个类的对象封装到另一个类实例化的对象空间中

# self.g.f.eat()  一定是组合 (组合是咱们最常用的关系)
# 依赖关系和组合关系: 会用就行

# 函数嵌套

```

#### 9.类的继承--单继承

```
# 继承  - 子承父业
# 程序中 A(B)

# A -- 子类,派生类
# B -- 父类,基类,超类

# class Human:
#
#     def __init__(self,name,age,sex):
#
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print("吃")
#
# class Dog:
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print("吃")
#
# class Cat:
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print("吃")
#
# class Pig:
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print("吃")



class Animal: # 父类
    """
    动物类
    """
    live = "活的"

    def __init__(self, name, age, sex):
        print("is __init__")
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self):  # self 是函数的位置参数
        print("吃")

class Human(Animal): # 子类
    pass

class Dog(Animal):  # 子类
    pass

# 通过子类的类名使用父类的属性和方法
# Human.eat(12)
# Human.__init__(Human,"日魔",18,"男")

# print(Human.live)
# print(Human.__dict__)

# 通过子类的对象使用父类的属性和方法
# p = Human("日魔",18,"男")
# d = Dog("rimo",1,'母')
# print(d.__dict__)
# print(p.__dict__)

# p = Human("日魔",18,"男")
# print(p.live)

# 查找顺序:
# 不可逆(就近原则)
# 通过子类,类名使用父类的属性或方法(查找顺序):当前类, 当前类的父类,当前类的父类的父类 --->
# 通过子类对象使用父类的属性或方法(查找顺序):先找对象,实例化这个对象的类,当前类的父类, --->


### 重要
# 继承: 单继承,多继承
# Python2: python2.2 之前都是经典类,python2.2之后出现了新式类,继承object就是新式类
# Python3: 只有新式类,不管你继不继承object都是新式类


# 继承的优点:
# 1.减少重复代码
# 2.结构清晰,规范
# 3.增加耦合性(不在多,在精)
```

#### 10.类的继承---多继承

多继承是继承多个父类

python2.2以前都是经典类，python2.2以后出现新式类和经典类共存，python3以后全部都是新式类

经典类：多继承是从左向右执行，（深度优先）左侧优先，一条路走到头，找不到会到分叉点向右查询

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(A):
    pass

class E(B,C):
    pass

class F(C,D):
    pass

class G(D):
    pass

class H(E,F):
    pass

class I(F,G):
    pass

class K(H,I):
    pass
 经典类继承关系：

```

![1567562694434](python学习之旅.assets/1567562694434.png)

新式类：（C3）算法 

```python
class O(object):
    # name = "宝元"
    pass
class D(O):
    # name = "日魔"
    pass

class E(O):
    # name = "太正博"
    pass

class F(O):
    # name = "alex"
    pass

class B(D,E):
    # name = "三哥"
    pass

class C(E,F):
    # name = "文刚"
    pass

class A(B,C):
    # name = "春生"
    pass

print(A.mro())
"""
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class '__main__.F'>, <class '__main__.O'>, <class 'object'>]
"""
```

*# mro(Child(Base1，Base2)) = [ Child ] + merge( mro(Base1), mro(Base2), [ Base1, Base2] )*

经典类不能使用Mro，新式类才能使用Mro

补充：

什么是C3算法：

判断mro要先确定一个线性序列，然后查找路径由由序列中类的顺序决定。所以C3算法就是生成一个线性序列。

什么是mro？

mro即 method resolution order (方法解释顺序)，主要用于在多继承时判断属性的路径(来自于哪个类)。

```python
#C3算法
def mro_C3(*cls):  
        if len(cls)==1:  
            if not cls[0].__bases__:  
                return  cls  
            else:  
                return cls+ mro_C3(*cls[0].__bases__)  
        else:  
            seqs = [list(mro_C3(C)) for C in cls ] +[list(cls)]  
            res = []  
            while True:  
              non_empty = list(filter(None, seqs))  
              if not non_empty:  
                  return tuple(res)  
              for seq in non_empty:  
                  candidate = seq[0]  
                  not_head = [s for s in non_empty if candidate in s[1:]]  
                  if not_head:  
                      candidate = None  
                  else:  
                      break  
              if not candidate:  
                  raise TypeError("inconsistent hierarchy, no C3 MRO is possible")  
              res.append(candidate)  
              for seq in non_empty:  
                  if seq[0] == candidate:  
                      del seq[0]  
```

#### 11.面向对象的三大特征：

1、继承

2、封装：将一些代码或数据存储到某个空间中（函数，对象，类）

3、多态：python默认就是多态

#### 12.使用子类和父类的方法或属性

```
class Animal: # 父类
    """
    动物类
    """
    live = "活的"

    def __init__(self, name, age, sex):
        # self = p的内存地址
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self):  # self 是函数的位置参数
        print("吃")

# 方法一: 不依赖(不需要)继承
# class Human: # 子类
#
#     def __init__(self, name, age, sex, hobby):
#         # print(Animal.live)
#         # self = p的内存地址
#         Animal.__init__(self,name,age,sex)
#         self.hobby = hobby
#
# class Dog:
#
#     def __init__(self, name, age, sex, attitude):
#         # self = p的内存地址
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#
# p = Human("日魔",18,"男","健身")
# print(p.__dict__)


# 方法二: 依赖(需要)继承

# class Dog(Animal):
#
#     def __init__(self, name, age, sex, attitude):
#         # self = p的内存地址
#         # super(Dog,self).__init__(name,age,sex)   # 完整写法
#         super().__init__(name,age,sex)   # 正常写法
#         self.attitude = attitude
#
# d = Dog("日魔",18,"男","忠诚")
# print(d.__dict__)


# def func(self):
#     self = 3
#     print(self)
#
# self = 3
# func(self)

# 1

# class Base:
#     def __init__(self, num):
#         self.num = num
#
#     def func1(self):
#         print(self.num)
#
# class Foo(Base):
#     pass
#
# obj = Foo(123)
# obj.func1()

# class Base:
#     def __init__(self, num):
#         self.num = num
#
#     def func1(self):
#         print(self.num)
#
#
# class Foo(Base):
#     def func1(self):
#         print("Foo. func1", self.num)
#
#
# obj = Foo(123)
# obj.func1()


# class Base:
#     def __init__(self, num):
#         self.num = num
#
#     def func1(self):
#         print(self.num)
#         self.func2()
#
#     def func2(self):
#         print("Base.func2")
#
#
# class Foo(Base):
#     def func2(self):
#         print("Foo.func2")
#
#
# obj = Foo(123)
# obj.func1()


# class Base:
#     def __init__(self, num):
#         self.num = num
#
#     def func1(self):
#         print(self.num)
#         self.func2()
#
#     def func2(self):
#         print(111, self.num)
#
#
# class Foo(Base):
#     def func2(self):
#         print(222, self.num)
# a = Base(1)
# b = Base(2)
# c = Foo(3)
# lst = [a, b, c]
# print(lst)
# for obj in lst:
#     obj.func2()


# class Base:
#     def __init__(self, num):
#         self.num = num
#
#     def func1(self):
#         print(self.num)
#         self.func2()
#
#     def func2(self):
#         print(111, self.num)
#
#
# class Foo(Base):
#     def func2(self):
#         print(222, self.num)
#
# 
# lst = [Base(1), Base(2), Foo(3)]
# for obj in lst:
#     obj.func1()

# 1
# 111 1
# 2
# 111 2
# 3
# 222 3
```

```
# 1.继承

# 单继承,多继承
# 经典类,新式类

# 1.子类的类名使用父类的属性和方法
# 2.子类的对象使用父类的属性和方法
# 3.既要使用子类的属性又使用父类的属性

# 方法一:不依赖(需要)继承
    # 在本类的__init__方法中,使用另一个类名的__init__方法进行初始化
    # def __init__(self,name,age,sex):
    #     A.__init__(self,name,age)
    #     self.sex = sex

# 方法二:(依赖继承) super只能继承之后使用
#     def __init__(self,name,age,sex): # 初始化方法
#         super(本类,self).__init__(name,age)
#         super().__init__(name,age)   # 重构方法
#         self.sex = sex
```

#### 13 .鸭子类型：

编程思想

什么是鸭子类型(Duck Typing)？鸭子类型可解释为，如果一只动物，走起来像鸭子或者叫起来像鸭子，就可以把它当作鸭子。

”When I see a bird that walks like a duck and swims like a duck and quackslike a duck, I call that bird a duck.” 

　　**python崇尚一种鸭子类型，类与类之间不用共同继承一个父类，只需要将它们做得像一种事物即可。**

例如，如果想编写现有对象的自定义版本。

　　1、可以继承该对象

　　2、可以创建一个外观和行为像，但与它无任何关系的全新对象(通常用于保存程序组件的松耦合度)

例1：利用标准库中定义的各种‘与文件类似’的对象，尽管这些对象的工作方式像文件，但他们没有继承内置文件对象的方法

```python
class File:
    def read(self):
        pass

    def write(self):
        pass

class Disk:
    def read(self):
        print('disk read')

    def write(self):
        print('disk write')

class Text:
    def read(self):
        print('text read')

    def write(self):
        print('text write')


disk = Disk()
text = Text()

disk.read()
disk.write()

text.read()
text.write()
"""
disk read
disk write
text read
text write
"""

像文件的类
```

例2：序列类型有多种形态：字符串，列表，元组，但他们直接没有直接的继承关系

```python
# 序列类型：列表list、元组tuple、字符串str
l = list([1, 2, 3])
t = tuple(('a', 'b'))
s = str('hello')

print(l.__len__())  # 3
print(t.__len__())  # 2
print(s.__len__())  # 5

像序列的类型
```

#### 14.类的约束：

雏形：

```Python
class WechatPay:

    def pay(self):
        print("微信支付")


class AliPay:

    def pay(self):
        print("支付宝支付")


class QQpay:

    def fuqian(self):
        print("QQ支付")

qq = QQpay()
# qq.fuqian()

wei = WechatPay()
ali = AliPay()
qq = QQpay()
#
#
# wei.pay()
# ali.pay()
# qq.fuqian()


def pay(object):
    object().pay()  具有相同功能和名字的封装成函数

pay(qq)   在qq对象中没有可调用的pay函数

"""
Traceback (most recent call last):
  File "D:/pycharm_program/venv/练习册/人工只能.py", line 130, in <module>
    pay(qq)
  File "D:/pycharm_program/venv/练习册/人工只能.py", line 128, in pay
    object().pay()
TypeError: 'QQpay' object is not callable

"""
```

雏形2：

```python
class PayClass:
    def pay(self):
        pass

class WechatPay(PayClass):

    def pay(self):
        print("微信支付")


class AliPay(PayClass):

    def pay(self):
        print("支付宝支付")


class QQpay(PayClass):

    def fuqian(self):
        print("QQ支付")


def pay(object):
    object().pay()

pay(QQpay)
QQpay继承payclass的类，此时会去父类中查找pay方法
```

方法一：（推介并且常用的方法）

raise   主动抛出异常（主动报错）

```python
# raise 主动抛出异常(主动报错)
class PayClass:
    def pay(self):
        raise Exception("你子类必须要写一个pay方法")

class WechatPay(PayClass):

    def pay(self):
        print("微信支付")


class AliPay(PayClass):

    def pay(self):
        print("支付宝支付")


class QQpay(PayClass):
    pass
    
    # def pay(self):
    #     print("QQ支付")

    # def pay(self):
    #     pass

def pay(object):
    object().pay()

pay(QQpay)
"""
Traceback (most recent call last):
  File "D:/pycharm_program/venv/练习册/人工只能.py", line 124, in <module>
    pay(QQpay)
  File "D:/pycharm_program/venv/练习册/人工只能.py", line 122, in pay
    object().pay()
  File "D:/pycharm_program/venv/练习册/人工只能.py", line 98, in pay
    raise Exception("你子类必须要写一个pay方法")
Exception: 你子类必须要写一个pay方法
"""
```

方法二：抽象类

引入抽象类的概念处理

```python
from abc import ABCMeta,abstractmethod   # 抽象类,接口类
class PayClass(metaclass=ABCMeta):  # 元类
    @abstractmethod
    def pay(self):
        raise Exception("你子类必须要写一个pay方法")

class WechatPay(PayClass):

    def pay(self):
        print("微信支付")

class AliPay(PayClass):

    def pay(self):
        print("支付宝支付")

class QQpay(PayClass):
    pass
    # def pay(self):
    #     print("QQ支付")

def pay(object):
    object().pay()

pay(WechatPay)
pay(AliPay)
pay(QQpay)

qq = QQpay()
qq.pay()
"""
微信支付
Traceback (most recent call last):
支付宝支付
  File "D:/pycharm_program/venv/练习册/人工只能.py", line 122, in <module>
    pay(QQpay)
  File "D:/pycharm_program/venv/练习册/人工只能.py", line 118, in pay
    object().pay()
TypeError: Can't instantiate abstract class QQpay with abstract methods pay
"""

# 抽象类和接口类做的事情 ：建立规范
# 制定一个类的metaclass是ABCMeta，
# 那么这个类就变成了一个抽象类(接口类)
# 这个类的主要功能就是建立一个规范
```

**总结: 约束. 其实就是⽗类对⼦类进⾏约束. ⼦类必须要写xxx⽅法. 在python中约束的⽅式和⽅法有两种:**

**1. 使⽤抽象类和抽象⽅法, 由于该⽅案来源是java和c#. 所以使⽤频率还是很少的**

**2. 使⽤⼈为抛出异常的⽅案. 并且尽量抛出的是NotImplementError. 这样比较专业, ⽽且错误比较明确.(推荐)**

#### 14.抽象类：

**什么是抽象类**

​    *与java一样，python也有抽象类的概念但是同样需要借助模块实现，**抽象类是一个特殊的类，它的特殊之处在于只能被继承，不能被实例化***

**为什么要有抽象类**

​    *如果说**类是从**一堆**对象**中抽取相同的内容而来的，那么**抽象类**就**是从**一堆**类**中抽取相同的内容而来的，内容包括数据属性和函数属性。*

　 *比如我们有香蕉的类，有苹果的类，有桃子的类，从这些类抽取相同的内容就是水果这个抽象的类，你吃水果时，要么是吃一个具体的香蕉，要么是吃一个具体的桃子。。。。。。你永远无法吃到一个叫做水果的东西。*

​    *从设计角度去看，如果类是从现实对象抽象而来的，那么抽象类就是基于类抽象而来的。*

　 *从实现角度来看，抽象类与普通类的不同之处在于：抽象类中有抽象方法，该类不能被实例化，只能被继承，且子类必须实现抽象方法。*

***在python中实现抽象类***

```python
#一切皆文件
import abc #利用abc模块实现抽象类

class All_file(metaclass=abc.ABCMeta):
    all_type='file'
    @abc.abstractmethod #定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        pass

    @abc.abstractmethod #定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass

# class Txt(All_file):
#     pass
#
# t1=Txt() #报错,子类没有定义抽象方法

class Txt(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')

class Sata(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')

class Process(All_file): #子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')

wenbenwenjian=Txt()

yingpanwenjian=Sata()

jinchengwenjian=Process()

#这样大家都是被归一化了,也就是一切皆文件的思想
wenbenwenjian.read()
yingpanwenjian.write()
jinchengwenjian.read()

print(wenbenwenjian.all_type)
print(yingpanwenjian.all_type)
print(jinchengwenjian.all_type)
```

*抽象类的本质还是类，指的是一组类的相似性，包括数据属性（如all_type）和函数属性（如read、write），而接口只强调函数属性的相似性。*

***抽象类是一个介于类和接口直接的一个概念，同时具备类和接口的部分特性，可以用来实现归一化设计***

```
1.多继承问题
在继承抽象类的过程中，我们应该尽量避免多继承；
而在继承接口的时候，我们反而鼓励你来多继承接口


2.方法的实现
在抽象类中，我们可以对一些抽象方法做出基础实现；
而在接口类中，任何方法都只是一种规范，具体的功能需要子类实现
```

#### 15 super（）方法：

```python
class D(object):

    def f1(self):
        print("这是D父类",self)

class B1(D):
    pass
    # def f1(self):
    #     print("这是B1父类",self)

class A(D):
    pass
    # def f1(self):
    #     print("这是A父类",self)


class B(B1,A):

    def f1(self):
        print ("这是子类",self)
        super(B,self).f1()   # super 按照mro进行查找

b = B()
b.f1()
print(B.mro())
"""
这是子类 <__main__.B object at 0x000001D595C0C358>
这是D父类 <__main__.B object at 0x000001D595C0C358>
[<class '__main__.B'>, <class '__main__.B1'>, <class '__main__.A'>, <class '__main__.D'>, <class 'object'>]
"""
```

```python
class A:
    def f1(self):
        print(111)

    def f2(self):
        print(2222)

class fun(A):
    def f1(self):
        super(fun,self).f2()
        print(333)

c = fun()
c.f1()
2222
333
```

```python
class A:
    def f1(self):
        print('in A')

class Foo(A):
    def f1(self):
        super().f1()
        print('in Foo')

class Bar(A):
    def f1(self):
        print('in Bar')

class Info(Foo,Bar):
    def f1(self):
        super(Foo,self).f1()
        print('in Info f1')

# [Info -- Foo -- Bar -- A]
obj = Info()
obj.f1()
"""
in Bar
in Info f1
"""
```

```python
class A:
    def f1(self):
        print('in A')

class Foo(A):
    def f1(self):
        super().f1()
        print('in Foo')

class Bar(A):
    def f1(self):
        print('in Bar')

class Info(Foo,Bar):
    def f1(self):
        # super里的类名是指定查找mro中类名的下一个类, self是指定查找时使用的mro顺序
        super(Info,self).f1()   # Foo() 对象的内存地址  # super(子类名,子类的mro列表)
        print('in Info f1')


aa = Info()  # 对象的内存地址
aa.f1()

# [Info', Foo', Bar', A', 'object']

a = Foo()
b = a
print(a)
print(b)
"""
in Bar
in Foo
in Info f1
<__main__.Foo object at 0x000001C87940EB00>
<__main__.Foo object at 0x000001C87940EB00>
"""
```

**super里的类名是指定查找mro中类名的下一个类，self是指定查找时使用的mro顺序**

**在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照MRO（Method Resolution Order）：方法解析顺序 进行的。**



```
python2中 把中文放到容器中，显示字节码

python2和python3最大区别：

python2中 bytes类型是字符串，unicode是

python3中字节是str


```

#### 16.类成员

私有：只能自己有

以__开头就是私有内容

*私有内容的目的就是保护数据的安全性*

```python
class Human:

    live = "有思想"        # 类公有的属性
    __desires = "有欲望"   # (程序级别)类私有的属性
    _desires = "有欲望"    # (程序员之间约定俗成)类私有的属性

    def __init__(self,name,age,sex,hobby):
        self.name = name
        self.age = age
        self.sex = sex        # 对象的公有属性
        self.__hobby = hobby  # 对象的私有属性

    def func(self):
        # 类内部可以查看对象的私有属性
        print(self.__hobby)

    def foo(self):            # 公有方法
        # 类内部可以查看类的私有属性
        print(self.__desires)

    def __abc(self):          # 私有方法
        print("is abc")

# print(Human.__dict__)
# print(Human._desires)


# class B(Human):
#     pass
    # def run(self):
        # print(self.__desires)
        # self._Human__abc()    # 强制继承(非常不推荐使用)

```

### 补充：Print带颜色输出

#### 书写格式：

##### 开头部分

\033[显示方式;前景色;背景色m

##### 结尾部分

\033[0m

注意：开头部分的三个参数：

- 显示方式
- 字体颜色
- 背景色

是可选参数，可以只写其中的某一个；另外由于表示三个参数不同含义的数值都是唯一的没有重复的，所以三个参数的书写先后顺序没有固定要求，系统都能识别；但是，建议按照默认的格式规范书写。

对于结尾部分，其实也可以省略，但是为了书写规范，建议\033[***开头，\033[0m结尾

| 字体颜色 | 背景颜色 | 颜色描述 |
| :------: | :------: | :------: |
|    30    |    40    |   黑色   |
|    31    |    41    |   红色   |
|    32    |    42    |   绿色   |
|    33    |    43    |   黃色   |
|    34    |    44    |   蓝色   |
|    35    |    45    |  紫红色  |
|    36    |    46    |  青蓝色  |
|    37    |    47    |   白色   |

| 显示方式 |     效果     |
| :------: | :----------: |
|    0     | 终端默认设置 |
|    1     |   高亮显示   |
|    4     |  使用下划线  |
|    5     |     闪烁     |
|    7     |   反白显示   |
|    8     |    不可见    |

**常见开头格式**： \033[0m 默认字体正常显示，不高亮 \033[32;0m 红色字体正常显示 \033[1;32;40m 显示方式: 高亮 字体前景色：绿色 背景色：黑色 \033[0;31;46m 显示方式: 正常 字体前景色：红色 背景色：青色

举例说明：

```python
print('\033[1;35;0m字体变色，但无背景色 \033[0m')  # 有高亮
print('\033[1;35m字体有色，但无背景色 \033[0m')    # 有高亮
print('\033[1;45m 字体不变色，有背景色 \033[0m')  # 有高亮
print('\033[1;35;46m 字体有色，且有背景色 \033[0m')  # 有高亮
print('\033[0;35;46m 字体有色，且有背景色 \033[0m')  # 无高亮
```

运行结果:

![image-20190901161633363](../python%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/Untitled.assets/image-20190901161633363.png)

除了以上的使用方式,还可以这用使用

```python
print('\033[0;36m骑牛远远过前村，')
print('短笛横吹隔陇闻。')
print('多少长安名利客，')
print('机关用尽不如君。\033[0m')
```

运行结果

![image-20190901162519279](Untitled.assets/image-20190901162519279.png)



### 软件开发规范-----分文件

当代码存在一个py文件中时

- 不便于管理 【修改和增加】
- 可读性差
- 加载速度慢

Django --  雏形

1. 启动文件   启动接口                start.py           目录（bin文件夹）
2. 公共文件   大家需要的功能        装饰器    日志       common.py      lib文件夹
3. 配置文件 （静态文件）变量       setting.py         conf配置文件夹
4. 主逻辑        核心              src.py                       core文件夹
5. 用户相关数据   账号密码等文件            register
6. 日志    记录重要信息，记录程序员开发人员的行为             loging.log