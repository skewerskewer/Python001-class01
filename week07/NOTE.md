一切皆是对象

py3以后新式类，所有类继承于object

类：属性，方法

属性：类属性（内存里只保存一份），对象属性（每一个对象，不同的内存）


class Human(object):
    Live = True

    def __init__(self, name):
        self.name = name

man = Human('Adam')
woman = Human ('Eve')


>>> dir(Human)
['Live', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


>>> Human.__dict__
mappingproxy({'__module__': '__main__', 'Live': True, '__init__': <function Human.__init__ at 0x7fdd482541f0>, '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>, '__doc__': None})

Human.__dict__

>>> man.__dict__
{'name': 'Adam', 'Live': False}
#实例化以后， man有了Live的实例里的字段
>>> woman.__dict__
{'name': 'Eve'}
>>> 


>>> id(man)
140588374808848
>>> id(woman)
140588374867200

>>> man.__class__
<class '__main__.Human'>
>>> man.__class__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 1 required positional argument: 'name'
>>> man.__class__('Adam')
<__main__.Human object at 0x7fdd4824b760>
>>> man.__class__('Adam2')
<__main__.Human object at 0x7fdd4819ff40>
  
 
>>> type(man)
<class '__main__.Human'>
>>> type(Human)
<class 'type'>
>>> type(object)
<class 'type'>
>>> object.mro()
[<class 'object'>]




>>> setattr(Human, 'newattr2', '20')

>>> dir(Human)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'live', 'newattr', 'newattr2']


###############################################################################################################################################################

class Human2(object):
    # 人为约定不可修改
    _age = 0

    # 私有属性 改名为 _Human2__fly
    __fly = False

    # 魔术方法，不会自动改名
    # 如 __init__
>>> Human2.__dict__
mappingproxy({'__module__': '__main__', '_age': 0, '_Human2__fly': False, '__dict__': <attribute '__dict__' of 'Human2' objects>, '__weakref__': <attribute '__weakref__' of 'Human2' objects>, '__doc__': None})


# 显示object类的所有子类
print( ().__class__.__bases__[0].__subclasses__() )


>>> type(())
<class 'tuple'>
>>> ().__class__
<class 'tuple'>
>>> ().__class__.__bases__
(<class 'object'>,)
>>> ().__class__.__bases__[0]
<class 'object'>
>>> ().__class__.__bases__[0].__subclasses__
<built-in method __subclasses__ of type object at 0x105cb69c0>
>>> ().__class__.__bases__[0].__subclasses__()
[<class 'type'>, <class 'weakref'>, <class 'weakcallableproxy'>, <class 'weakproxy'>, ....
>>> 


###############################################################################################################################################################
类方法

# 让实例的方法成为类的方法
class Kls1(object):
    bar = 1
    def foo(self):
        print('in foo')
    # 使用类属性、方法
    @classmethod
    def class_foo(cls):
        print(cls.bar)
        print(cls.__name__)
        cls().foo()

Kls1.class_foo()

>>> Kls1.class_foo()
1
Kls1
in foo



class Story(object):
    snake = 'Python'
    def __init__(self, name):
        self.name = name
    # 类的方法
    @classmethod
    def get_apple_to_eve(cls):
        return cls.snake
    

s = Story('anyone')
# get_apple_to_eve 是bound方法，查找顺序是先找s的__dict__是否有get_apple_to_eve,如果没有，查类Story
print(s.get_apple_to_eve)

>>> print(s.get_apple_to_eve)
<bound method Story.get_apple_to_eve of <class '__main__.Story'>>

>>> print(s.get_apple_to_eve())
Python
>>> print(Story.get_apple_to_eve())
Python

>>> print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)))
<bound method Story.get_apple_to_eve of <class '__main__.Story'>>
>>> print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)) == s.get_apple_to_eve)
True


类方法解决的一个问题,类方法作为构造函数

class Kls2():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')

me = Kls2('wilson','yin')
me.print_name()

# 输入改为  wilson-yin

解决方法1: 修改 __init__()
解决方法2: 增加 __new__() 构造函数
解决方法3: 增加 提前处理的函数


class Kls3():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    @classmethod
    def pre_name(cls,name):
        fname, lname = name.split('-')
        return cls(fname, lname)
    
    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')

me3 = Kls3.pre_name('wilson-yin')
me3.print_name()

>>> dir(me3)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'fname', 'lname', 'pre_name', 'print_name']
>>> type(me3)
<class '__main__.Kls3'>
>>> me3.__dict__
{'fname': 'wilson', 'lname': 'yin'}
>>> Kls3.__dict__
mappingproxy({'__module__': '__main__', '__init__': <function Kls3.__init__ at 0x7fdc800d03a0>, 'pre_name': <classmethod object at 0x7fdc800a9130>, 'print_name': <function Kls3.print_name at 0x7fdc800d0430>, '__dict__': <attribute '__dict__' of 'Kls3' objects>, '__weakref__': <attribute '__weakref__' of 'Kls3' objects>, '__doc__': None})

###############################################################################################################################################################


###############################################################################################################################################################
