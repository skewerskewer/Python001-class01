学习笔记

```
# 变量赋值：

赋值时传递对象本身：
(静态）不可变数据类型:int, float, string, tuple


# 问题1: a、b、c三个id是否相同
a = 123
b = 123
c = a
print(id(a))
print(id(b))
print(id(c))



# 问题2: a、b、c的值分别是多少
a = 456
print(id(a))
c = 789
c = b = a


赋值时传递对象的引用（对象的地址）：
（动态）可变数据类型：list, dict


# 问题3: x、y的值分别是什么
x = [1,2,3]
y = x
x.append(4)
print(x)
print(y)


# 问题4: a、b的值分别是多少
a = [1, 2, 3]
b = a
a = [4, 5, 6]


# 问题5: a、b的值分别是多少
a = [1, 2, 3]
b = a
a[0],a[1],a[2] = 4, 5, 6

```

序列分类
• 容器序列：list、tuple、collections.deque 等，能存放不同类型的数据 容器序列可以存
放不同类型的数据。
• 扁平序列：str、bytes、bytearray、memoryview (内存视图)、array.array 等，存放的
是相同类型的数据 扁平序列只能容纳一种类型。

另一种分类方式
• 可变序列 list、bytearray、array.array、collections.deque 和 memoryview。
• 不可变序列 tuple、str 和 bytes。

```
list操作
>>> old_list = [ i for i in range(1, 11)]
>>> new_list1 = old_list
>>> new_list2 = list(old_list)
>>> new_list1 == new_list2
True
>>> new_list1 is  new_list2
False

切片操作
>>> new_list3 = old_list[:]
>>> new_list1 is  new_list3
False
>>> new_list1 == new_list3
True

```

容器序列存在深拷贝、浅拷贝问题
• 注意：非容器（数字、字符串、元组）类型没有拷贝问题
import copy
copy.copy(object)
copy.deepcopy(object)

```
>>> import copy
>>> old_list = [ i for i in range(1, 11)]
>>> old_list.append([11, 12])
>>> new_list4 = copy.copy(old_list)
>>> new_list5 = copy.deepcopy(old_list)
>>> new_list4
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]
>>> new_list5
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]
>>> new_list4 is new_list5
False
>>> old_list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]
>>> old_list[10][0] = 13
>>> old_list
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [13, 12]]
>>> new_list4
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [13, 12]]
>>> new_list5
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12]]

```
字典的key值，只能用静态的数据来做


函数需要关注什么
1. • 调用


func， func()的区别: 

func 调用函数对象
func() 调用函数的返回值


```

>>> def func2():
...     return 123
... 
>>> func2
<function func2 at 0x7fdc80498160>
>>> func2()
123
>>> type(func2)
<class 'function'>
>>> type(func2())
<class 'int'>
>>> b = func2
>>> b
<function func2 at 0x7fdc80498160>
>>> b()
123


>>> class Kls1:
...     def __call__(self):
...             return 123
... 
>>> inst1 = Kls1()
>>> type(inst1)
<class '__main__.Kls1'>
>>> inst1()
123
>>> type(inst1())
<class 'int'>

```



2 • 作用域


高级语言对变量的使用：
• 变量声明
• 定义类型（分配内存空间大小）
• 初始化（赋值、填充内存）
• 引用（通过对象名称调用对象内存数据）
Python 和高级语言有很大差别，在模块、类、函数中定义，才有作用域的概念


Python 作用域遵循 LEGB 规则。
LEGB 含义解释：
• L-Local(function)；函数内的名字空间
• E-Enclosing function locals；外部嵌套函数的名字空间（例如closure）
• G-Global(module)；函数定义所在模块（文件）的名字空间
• B-Builtin(Python)；Python 内置模块的名字空间

```python
def func():
    var = 100
func()
print(var)
#外部找不到内部定义的var
>>> print(var)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'var' is not defined


def func():
    print(var)
func()
var = 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in func
NameError: name 'var' is not defined

#var定义在函数之后

# L G
x = 'Global'
def func2():
    x = 'Enclosing'

    def func3():
        x = 'Local'

        print (x)
    func3()
print(x)
func2()
>>> print(x)
Global
>>> func2()
Local
>>>  


# E
x = 'Global'
def func4():
    x = 'Enclosing'
    def func5():
        return x
    return func5  #注意，这里返回的是func5的对象

var = func4()
print( var() )

>>> func4()
<function func4.<locals>.func5 at 0x7fb8041cf700>
>>> func4
<function func4 at 0x7fb8041cf3a0>
>>> var = func4()
>>> print(var)
<function func4.<locals>.func5 at 0x7fb8041cf700>
>>> var()
'Enclosing'


# B
print (dir (__builtins__) )

```
