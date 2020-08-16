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
• 参数
先传args, 再穿kargs

def func(*args, **kargs):
    print(f'args: {args}')
    print(f'kargs:{kargs}')


func(123, 'xz', name='xvalue')

>>> func(123, 'xz', name='xvalue')
args: (123, 'xz')
kargs:{'name': 'xvalue'}
>>> func(name='xvle', 123, 'xz')
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
>>>


偏函数
functools.partial：返回一个可调用的 partial 对象
使用方法：partial(func,*args,**kw)

注意：
• func 是必须参数
至少需要一个args活kw参数

#例子1
def add(x, y):
    return x + y

import functools
add_1 = functools.partial(add, 1) # 吧函数add(x,y)中的，x固定为1， 然后命名这个偏函数为add_1，每次调用只用提供y值就行了
add_1(10)

>>> add_1(10)
11
>>> add_1(9)
10


#例子2
>>> import itertools
>>> g = itertools.count()
>>> next(g)
0
>>> auto_add_1 = functools.partial(next, g)
>>> auto_add_1()
1
>>> auto_add_1()
2





Lambda 只是表达式，不是所有的函数逻辑都能封装进去
k = lambda x:x+1
k lambd
Lambda 表达式后面只能有一个表达式
• 实现简单函数的时候可以使用 Lambda 表达式替代
• 实现简单函数的时候可以使用 Lambda 表达式
• 返回


>>> def k(x):
...     return x+1
...
>>> print(k(1))
2

>>> k = lambda x: x+1
>>> k(1)
2



高阶函数: map, reduce, filter

def square(x):
    return x**2

#map调用square
m = map(square, range(10))

>>> next(m)
0
>>> next(m)
1
>>> next(m)
4
>>> next(m)
9
>>> list(m)
[16, 25, 36, 49, 64, 81]


#推倒式的方式调用square
>>> [square(x) for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# reduce 的函数定义
# reduce(f, [x1, x2, x3]) = f(f(x1, x2), x3)
from functools import reduce
def subsctract(x, y):
    return x - y

reduce(subsctract, [1, 3, 5, 7, 9])

>>> reduce(add, [1, 3, 5, 7, 9])
-23
>>>




# filter, 定义一个函数作为过滤条件
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
>>> list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
[1, 5, 9, 15]


函数需要掌握 itertools 和 functools 两个库




函数返回值




def line_func(x):
    return 2*x + 10
print(line_func(5))


# version 1
# 函数是一个对象，所以可以作为某个函数的返回结果
def line_conf():
    def line(x):
        return 2*x+10
    return line       # return a function object

my_line = line_conf()
print(my_line(5))


# version 3

def line_conf():
    b = 10
    def line(x):
        '''如果line()的定义中引用了外部的变量'''
        return 2*x+b
    return line

b = -1
my_line = line_conf()
print(my_line(5))


# 编译后函数体保存的局部变量
print(my_line.__code__.co_varnames)
# 编译后函数体保存的自由变量
print(my_line.__code__.co_freevars)
# 自由变量真正的值
print(my_line.__closure__[0].cell_contents)


>>> # 编译后函数体保存的局部变量
>>>
>>> print(my_line.__code__.co_varnames)
('x',)
>>> # 编译后函数体保存的自由变量
>>>
>>> print(my_line.__code__.co_freevars)
('b',)
>>> # 自由变量真正的值
>>>
>>> print(my_line.__closure__[0].cell_contents)
10



#####################
# 函数和对象比较有哪些不同的属性
# 函数还有哪些属性
def func():
    pass
func_magic = dir(func)

# 常规对象有哪些属性
class ClassA():
    pass
obj = ClassA()
obj_magic = dir(obj)

# 比较函数和对象的默认属性
set(func_magic) - set(obj_magic)


>>> type(func)
<class 'function'>
>>> type(func_magic)
<class 'list'>

>>> type(obj)
<class '__main__.ClassA'>
>>> type(obj_magic)
<class 'list'>


>>> print(func_magic)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> print(obj_magic)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

>>> set(func_magic) - set(obj_magic)
{'__get__', '__name__', '__globals__', '__defaults__', '__code__', '__closure__', '__annotations__', '__kwdefaults__', '__qualname__', '__call__


# version 4
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))



# version 5
# 与line绑定的是line_conf()传入的a,b
a=100
b=200
def line_conf(a, b):
    def line(x):
        return a*x+b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))

#闭包的好处是让global的变量不会影响local里面的变量的值



# 内部函数对外部函数作用域里变量的引用（非全局变量）则称内部函数为闭包

def counter(start=0):
   count=[start]
   def incr():
       count[0]+=1
       return count[0]
   return incr

c1=counter(10)

print(c1())
# 结果：11
print(c1())
# 结果：12

# nonlocal访问外部函数的局部变量
# 注意start的位置，return的作用域和函数内的作用域不同
def counter2(start=0):
    def incr():
        nonlocal start
        start+=1
        return start
    return incr
c1=counter2(5)
print(c1())
print(c1())


装饰器:
增强而不改变原有函数
装饰器强调函数的定义态而不是运行态
装饰器在模块导入的时候自动运行


被修饰函数带参数
被修饰函数带不定长参数
被修饰函数带返回值


# 装饰器, @ 语法糖
@decorate
def func2():
    print('do sth')

# 等效于下面
def func2():
    print('do sth')
func2 = decorate(func2)



>>> def decorate(func):
...     print('running in modlue')
...     def inner():
...         return func()
...     return inner
...
>>> @decorate
... def func2():
...     pass
...
running in modlue



# 包装 wrapper
def html(func): #func 在这时是body
    def decorator():
        return f'<html>{func()}</html>'
    return decorator

def body(func): #func 在这时是content
    def decorator():
        return f'<body>{func()}</body>'
    return decorator

@html
@body
def content():
    return 'hello world'

>>> content()
'<html><body>hello world</body></html>'



# 被修饰函数带参数
def outer(func):
    def inner(a,b):
        print(f'inner: {func.__name__}')
        print(a,b)
        func(a,b)
    return inner

@outer
def foo(a,b):
    print(a+b)
    print(f'foo: {foo.__name__}')


foo(1,2)
foo.__name__


>>> foo(1,2)
inner: foo
1 2
3
foo: inner
>>> foo.__name__
'inner'


# 被修饰函数带不定长参数
def outer2(func):
    def inner2(*args,**kwargs):
        func(*args,**kwargs)
    return inner2

@outer2
def foo2(a,b,c):
    print(a+b+c)

>>> foo2(1,3,4)
8
>>> foo2.__name__
'inner2'



# 被修饰函数带返回值

def outer3(func):
    def inner3(*args,**kwargs):
        ###
        return func(*args,**kwargs)
        ###
    return inner3

@outer3
def foo3(a,b,c):
    return (a+b+c)

>>> print(foo3(1,3,5))
9
>>> foo3.__name__
'inner3'


# 装饰器带参数

def outer_arg(bar):
    def outer(func):
        def inner(*args,**kwargs):
            ret = func(*args,**kwargs)
            print(bar)
            return ret
        return inner
    return outer

# 相当于outer_arg('foo_arg')(foo)()
@outer_arg('foo_arg')
def foo(a,b,c):
    return (a+b+c)

print(foo(1,3,5))


# 类装饰器
# 其他经常用在类装饰器的python自带装饰器
# classmethod
# staticmethod
# property


from functools import wraps

class MyClass(object):
    def __init__(self, var='init_var', *args, **kwargs):
        self._v = var
        super(MyClass, self).__init__(*args, **kwargs)

    def __call__(self, func):
        # 类的函数装饰器
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            func_name = func.__name__ + " was called"
            print(func_name)
            return func(*args, **kwargs)
        return wrapped_function

>>> @MyClass(100)
... def myfunc():
...     pass
...
>>> myfunc()
myfunc was called
>>> MyClass(100)(myfunc)()
myfunc was called
myfunc was called


# 另一个示例
class Count(object):
    def __init__(self,func):
        self._func = func
        self.num_calls = 0

    def __call__(self, *args, **kargs):
        self.num_calls += 1
        print(f'num of call is {self.num_calls}')
        return self._func(*args, **kargs)

@Count
def example():
    print('hello')

example()
print(type(example))



# 装饰类
def decorator(aClass):
    class newClass(object):
        def __init__(self, args):
            self.times = 0
            self.wrapped = aClass(args)

        def display(self):
            # 将runtimes()替换为display()
            self.times += 1
            print("run times", self.times)
            self.wrapped.display()
    return newClass

@decorator
class MyClass(object):
    def __init__(self, number):
        self.number = number
    # 重写display
    def display(self):
        print("number is",self.number)

six = MyClass(6)
for i in range(5):
    six.display()


run times 1
number is 6
run times 2
number is 6
run times 3
number is 6
run times 4
number is 6
run times 5
number is 6


对象协议

Duck Typing 的概念
容器类型协议
• __str__ 打印对象时，默认输出该方法的返回值
• __getitem__、__setitem__、__delitem__ 字典索引操作
• __iter__ 迭代器
• __call__ 可调用对象协议
比较大小的协议
• __eq__ • __gt__
描述符协议和属性交互协议
• __get__ • __set__
可哈希对象
• __hash__

上下文管理器
with 上下文表达式的用法
使用 __enter__() __exit__() 实现上下文管理器



generator生成器
1. 在函数中使用yield关键字，可以实现生成器。
2. 生成器可以让函数返回可迭代对象。
3. yield和return不同，return返回后，函数状态终止，yield保持函数的执行状态，
返回后，函数回到之前保存的状态继续执行。
4. 函数被yield会暂停，局部变量也会被保存。
5. 迭代器终止时，会抛出StopIteration异常。

Iterables: 包含 __getitem__() 或 __iter__() 方法的容器对象
Iterator: 包含 next() 和 __iter__() 方法
Generator: 包含 yield 语句的函数


# yield语句

alist = [1, 2, 3, 4, 5]
hasattr( alist, '__iter__' )  # True
hasattr( alist, '__next__' )  # False

for i in  alist:
    print(i)

# 结论一  列表是可迭代对象，或称作可迭代（iterable）,
#         不是迭代器（iterator）

# __iter__方法是 iter() 函数所对应的魔法方法，
# __next__方法是 next() 函数所对应的魔法方法

###########################

g = ( i for i in range(5))
g  #<generator object>

hasattr( g, '__iter__' )  # True
hasattr( g, '__next__' )  # True

g.__next__()
next(g)
for i in g:
    print(i)

# 结论二 生成器实现完整的迭代器协议


##############################
# 类实现完整的迭代器协议

class SampleIterator:
    def __iter__(self):
        return self

    def __next__(self):
        # Not The End
        if ...:
            return ...
        # Reach The End
        else:
            raise StopIteration

# 函数实现完整的迭代器协议
def SampleGenerator():
    yield ...
    yield ...
    yield ...  # yield语句
# 只要一个函数的定义中出现了 yield 关键词，则此函数将不再是一个函数，
# 而成为一个“生成器构造函数”，调用此构造函数即可产生一个生成器对象。



###################
# check iter
def check_iterator(obj):
    if hasattr( obj, '__iter__' ):
        if hasattr( obj, '__next__' ):
            print(f'{obj} is a iterator') # 完整迭代器协议
        else:
            print(f'{obj} is a iterable') # 可迭代对象
    else:
        print(f'{obj} can not iterable') # 不可迭代

def func1():
    yield range(5)

>>> check_iterator(func1)
<function func1 at 0x7ff7201cf700> can not iterable
>>> check_iterator(func1())
<generator object func1 at 0x7ff72017eb30> is a iterator

# 结论三： 有yield的函数是迭代器，执行yield语句之后才变成生成器构造函数


# 迭代器有效性测试
>>> a_dict = {'a':1, 'b':2}
>>> a_dict_iter = iter(a_dict)
>>>
>>> next(a_dict_iter)
'a'
>>>
>>> a_dict['c']=3
>>> next(a_dict_iter)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration
# RuntimeError: 字典进行插入操作后，字典迭代器会立即失效



# 尾插入操作不会损坏指向当前元素的List迭代器,列表会自动变长
b_dict = ['a', 'b', 'c']
b_dict_iter = iter(b_dict)

next(b_dict_iter)
>>> b_dict.append('d')
>>> next(b_dict_iter)
'b'
>>> next(b_dict_iter)
'c'
>>> next(b_dict_iter)
'd'


# 迭代器一旦耗尽，永久损坏
>>> x = iter([ y for y in range(5)])
>>> for i in x:
...     i
...
0
1
2
3
4
>>> x.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration


协程和线程的区别
• 协程是异步的，线程是同步的
• 协程是非抢占式的，线程是抢占式的
• 线程是被动调度的，协程是主动调度的
• 协程可以暂停函数的执行，保留上一次调用时的状态，是增强型生成器
• 协程是用户级的任务调度，线程是内核级的任务调度
• 协程适用于 IO 密集型程序，不适用于 CPU 密集型程序的处理



# python3.4 支持事件循环的方法
import asyncio

@asyncio.coroutine
def py34_func():
    yield from sth()


##################
# python3.5 增加async await
async def py35_func():
    await sth()

# 注意： await 接收的对象必须是awaitable对象
# awaitable 对象定义了__await__()方法
# awaitable 对象有三类
# 1 协程 coroutine
# 2 任务 Task
# 3 未来对象 Future
#####################
import asyncio
async def main():
    print('hello')
    await asyncio.sleep(3)
    print('world')

# asyncio.run()运行最高层级的conroutine
asyncio.run(main())
# hello
# sleep 3 second
# world

#################
# 协程调用过程：
# 调用协程时，会被注册到ioloop，返回coroutine对象
# 用ensure_future 封装为Future对象
# 提交给ioloop

# 官方文档
# https://docs.python.org/zh-cn/3/library/asyncio-task.html



同步和异步的区别就在于是否等待IO执行的结果。好比你去麦当劳点餐，你说“来个汉堡”，服务员告诉你，对不起，汉堡要现做，需要等5分钟，于是你站在收银台前面等了5分钟，拿到汉堡再去逛商场，这是同步IO。

你说“来个汉堡”，服务员告诉你，汉堡需要等5分钟，你可以先去逛商场，等做好了，我们再通知你，这样你可以立刻去干别的事情（逛商场），这是异步IO。

很明显，使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。想想看，你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。如果是服务员跑过来找到你，这是回调模式，如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。总之，异步IO的复杂度远远高于同步IO。


import math

def point_move(x, y, step, angle):
    point_x = x + step * math.cos(angle)
    point_y = y + step * math.sin(angle)
    return point_x, point_y

>>> type(point_move)
<class 'function'>
>>> a, b = point_move(2, 3, 200, 10)
>>> print(a, b)
-165.81430581529048 -105.80422217787398
>>> type(a)
<class 'float'>
>>> type(b)
<class 'float'>
>>> result = point_move(2, 3, 200, 10)
>>> type(result)
<class 'tuple'>
>>> print(result)
(-165.81430581529048, -105.80422217787398)

在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。


```
