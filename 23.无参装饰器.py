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
import time

def index(x,y):
    time.sleep(3)
    print('index %s %s' % (x,y))

index(111,222)

# 解决方案一：失败
# 问题：没有修改被装饰对象的调用方式，但是修改了其源代码
def index(x, y):
    start = time.time()
    time.sleep(3)
    print('index %s %s' % (x, y))
    stop = time.time()
    print(stop-start)

index(111, 222)

# 解决方案二：没有修改被装饰对象的调用方式，也没有修改其源代码
# 问题：代码冗余
def index(x,y):
    time.sleep(3)
    print('index %s %s' % (x,y))

start = time.time()
index(111,222)
stop = time.time()
print(stop-start)

start = time.time()
index(111,222)
stop = time.time()
print(stop-start)

start = time.time()
index(111,222)
stop = time.time()
print(stop-start)

# 解决方案三：解决了代码冗余问题
# 问题：改变了调用方式
def index(x,y):
    time.sleep(3)
    print('index %s %s' % (x,y))

def wrapper(*args,**kwargs):
    start = time.time()
    index(*args,**kwargs)
    stop = time.time()
    print(stop-start)

wrapper(111,222)

# 解决方案三：装饰器
def index(x,y):
    time.sleep(3)
    print('index %s %s' % (x,y))
    return '凉宫春日'

def outer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        stop = time.time()
        print(stop-start)
        return func(*args,**kwargs)
    return wrapper

# 偷梁换柱
index = outer(index)  # index = outer(index的内存地址)
res = index(111,222)
print(res)

# 偷梁换柱的简洁写法
# 装饰器要放在被装饰函数之前不然会报错
def outer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        stop = time.time()
        print(stop-start)
        return res
    return wrapper

# 在被装饰对象正上方单独一行写 @装饰器名字
@outer  # index = outer(index)
def index(x,y):
    time.sleep(3)
    print('index %s %s' % (x,y))
    return '凉宫春日'

res = index(111,222)
print(res)

# 叠加多个装饰器，加载顺序与运行顺序
# @deco1  #index = deco1(deco2内wrapper的内存地址)
# @deco2  #deco2内wrapper的内存地址=deco2(deco3内wrapper的内存地址)
# @deco3  #deco3内wrapper的内存地址=deco3(func)
# def func():
#     ...

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
