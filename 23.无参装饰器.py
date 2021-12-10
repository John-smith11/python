# 装饰器
'''
1.什么是装饰器
    器指的是工具，可以定义成函数
    装饰指的是为其他事物添加点缀

    合到一起解释：
        装饰器指的是定义一个函数（或类），该函数（或类）是用来为其他函数（或类）添加额外的功能

2.为何要用装饰器
    开放封闭原则
        开放：指的是对拓展功能是开放的
        封闭：指的是对修改源代码是封闭的

    装饰器就是在不修改装饰器对象源代码及其调用方式的前提下为被装饰对象添加新功能
3.如何用

'''

# 需求：在不修改index源代码以及调用方式的前提下为其添加统计运行时间的功能
# import time
#
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' % (x,y))
#
# index(111,222)

# 解决方案一：失败
# 问题：没有修改被装饰对象的调用方式，但是修改了其源代码
# def index(x, y):
#     start = time.time()
#     time.sleep(3)
#     print('index %s %s' % (x, y))
#     stop = time.time()
#     print(stop-start)
#
# index(111, 222)

# 解决方案二：没有修改被装饰对象的调用方式，也没有修改其源代码
# 问题：代码冗余
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' % (x,y))
#
# start = time.time()
# index(111,222)
# stop = time.time()
# print(stop-start)
#
# start = time.time()
# index(111,222)
# stop = time.time()
# print(stop-start)
#
# start = time.time()
# index(111,222)
# stop = time.time()
# print(stop-start)

# 解决方案三：解决了代码冗余问题
# 问题：改变了调用方式
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' % (x,y))
#
# def wrapper(*args,**kwargs):
#     start = time.time()
#     index(*args,**kwargs)
#     stop = time.time()
#     print(stop-start)
#
# wrapper(111,222)

# 解决方案三：装饰器
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' % (x,y))
#     return '凉宫春日'
#
# def outer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         func(*args,**kwargs)
#         stop = time.time()
#         print(stop-start)
#         return func(*args,**kwargs)
#     return wrapper

# 偷梁换柱：即将原函数的内存地址偷梁换柱成wrapper函数的内存地址
#       所以应该将wrapper做的跟原函数一样才行（参数、返回值、属性）
# index = outer(index)  # index = outer(index的内存地址)
# res = index(111,222)
# print(res)

# 偷梁换柱的简洁写法
# 装饰器要放在被装饰函数之前不然会报错
# def outer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         res = func(*args,**kwargs)
#         stop = time.time()
#         print(stop-start)
#         return res
#     return wrapper

# 在被装饰对象正上方单独一行写 @装饰器名字
# @outer  # index = outer(index)
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' % (x,y))
#     return '凉宫春日'
#
# res = index(111,222)
# print(res)

# 叠加多个装饰器，加载顺序与运行顺序
# @deco1  #index = deco1(deco2内wrapper的内存地址)
# @deco2  #deco2内wrapper的内存地址=deco2(deco3内wrapper的内存地址)
# @deco3  #deco3内wrapper的内存地址=deco3(func)
# def func():
#     ...
def deco1(func1):  # func1=wrapper2的内存地址
    def wrapper1(*args,**kwargs):
        print('first wrapper')
        res1=func1(*args,**kwargs)
        return res1
    return wrapper1

def deco2(func2):  # func2=wrapper3的内存地址
    def wrapper2(*args,**kwargs):
        print('second wrapper')
        res2=func2(*args,**kwargs)
        return res2
    return wrapper2

def deco3(x):
    def outter3(func3):  # func3=被装饰对象index函数的内存地址
        def wrapper3(*args,**kwargs):
            print('third wrapper')
            res3=func3(*args,**kwargs)
            return res3
        return wrapper3
    return outter3

# 加载顺序自下而上
@deco1  # index=deco1(index)即index=deco1(wrapper2的内存地址)-->index=wrapper1的内存地址
@deco2  # index=deco2(index)即index=deco2(wrapper3的内存地址)-->index=wrapper2的内存地址
@deco3(111)  #--> @outter3--> index=outter3(index) --> index=wrapper3的内存地址
def index(x,y):
    print('index %s : %s'%(x,y))

# print(index)  # <function deco1.<locals>.wrapper1 at 0x000002D6CC73C3A0>
# 执行顺序：自上而下：wrapper1-->wrapper2-->wrapper3-->index,后运行的先结束
index(1,2)
'''
first wrapper
second wrapper
third wrapper
index 1 : 2

'''


# 总结无参装饰器模板
def outter(func):
    def wrapper(*args,**kwargs):
        # 1.调用原函数
        # 2.为其增加新功能
        res = func(*args,**kwargs)
        return res
    return wrapper

@outter
def func1():
    ...

# 将原函数的属性值赋给wrapper函数
from functools import wraps

def outter(func):
    @wraps(func)  # 将原函数的属性值赋给wrapper函数
    def wrapper(*args,**kwargs):
        # 1.调用原函数
        # 2.为其增加新功能
        res = func(*args,**kwargs)
        return res
    return wrapper

@outter
def func1():
    ...