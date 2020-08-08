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

