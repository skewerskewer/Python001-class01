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
