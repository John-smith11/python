'''
1.什么是迭代器
    迭代器指的是迭代取值的工具，迭代是一个重复的过程，
    每次重复都是基于上一次的结果而继续的，单纯的重复并不是迭代。

2.为何要有迭代
    迭代器是用来迭代取值的工具，而涉及到把多个值循环取出来的类型
    有：列表、字符串、元组、字典、集合、打开文件
    如：
    l=['凉宫春日','长门有希','朝比奈实玖瑠']
    i=0
    while i < len(l):
        print(l[i])
        i += 1

    上述迭代取值的方式只适用于有索引的数据类型：列表、字符串、元组
    为了解决基于索引迭代器取值的局限性
    python必须提供一种能够不依赖索引的取值方式，这就是迭代器

3.如何用迭代器
'''
# 可迭代对象：但凡内置有__iter__()方法的都称为可迭代对象
# s1=''
# s1.__iter__()
#
# l=[]
# l.__iter__()
#
# t=(1,)
# t.__iter__()
#
# d={'k1':11}
# d.__iter__()
#
# set1={1,2,3}
# set1.__iter__()
#
# with open('a.txt',mode=wt) as f:
#     f.__iter__()

# 调用可迭代对象下的__iter__()方法会将其转换成迭代器对象
d={'k1':'凉宫春日','k2':'长门有希','k3':'朝比奈实玖瑠'}
res = d.__iter__()
# print(res)  # <dict_keyiterator object at 0x00000135CF1E8AE0>

# print(res.__next__())  # k1
# print(res.__next__())  # k2
# print(res.__next__())  # k3
# print(res.__next__())  # 抛出异常 StopIteration

# k1
# k2
# k3
# while True:
#     try:
#         print(res.__next__())
#     except StopIteration:
#         break

# 一个迭代器只能循环遍历一遍，再次遍历结果为空
# while True:
#     try:
#         print(res.__next__())
#     except StopIteration:
#         break

# 可迭代对象与迭代器对象详解
# 1.可迭代对象（可以转换成迭代器的对象）：内置有__iter__()方法的对象
#            可迭代对象.__iter__():得到迭代器对象

# 2.迭代器对象：内置有__next__方法并且内置有__iter__方法的对象
#            迭代器对象.__next__():得到迭代器的下一个值
#            迭代器对象.__iter__():得到迭代器的本身，说白了调了跟没调一个样子
d={'k1':'凉宫春日','k2':'长门有希','k3':'朝比奈实玖瑠'}
d_iterator = d.__iter__()
print(d_iterator is d_iterator.__iter__())  # True

# 可迭代对象：字符串、列表、元组、字典、集合、文件对象
# 迭代器对象：文件对象
# s1=''
# s1.__iter__()
#
# l=[]
# l.__iter__()
#
# t=(1,)
# t.__iter__()
#
# d={'k1':11}
# d.__iter__()
#
# set1={1,2,3}
# set1.__iter__()
#
# with open('a.txt',mode=wt) as f:
#     f.__iter__()
#     f.__next__()

# for循环的工作原理:for循环又称为迭代器循环
d={'k1':'凉宫春日','k2':'长门有希','k3':'朝比奈实玖瑠'}
# 1 d.__iter__()得到一个迭代器对象
# 2 迭代器对象.__next__()得到一个返回值，然后将该返回值赋给k
# 3 循环往复步骤2，直到抛出StopIteration异常for循环会捕捉到异常然后结束循环
for k in d:
    print(k)

# d_iterator = d.__iter__()
# while True:
#     try:
#         print(d_iterator.__next__())
#     except StopIteration:
#         break

with open('The story about suzumiya haruhi and me',mode='rt',encoding='utf-8') as f:
    for line in f:
        print(line)
# 迭代器的优缺点
# 优点：
#   1、为序列和非序列类型提供了一种统一的迭代取值方式。
#   2、惰性计算：迭代器对象表示的是一个数据流，可以只在需要时才去调用next来计算出一个值，
#   就迭代器本身来说，同一时刻在内存中只有一个值，因而可以存放无限大的数据流，而对于其他容器类型，
#   如列表，需要把所有的元素都存放于内存中，受内存大小的限制，可以存放的值的个数是有限的。
# 缺点：
#   1、除非取尽，否则无法获取迭代器的长度
#   2、只能取下一个值，不能回到开始，更像是‘一次性的’，迭代器产生后的唯一目标就是重复执行next方法直到值取尽，
#   否则就会停留在某个位置，等待下一次调用next；若是要再次迭代同个对象，你只能重新调用iter方法去创建一个新的迭代器对象，
#   如果有两个或者多个循环使用同一个迭代器，必然只会有一个循环能取到值。