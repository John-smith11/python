# 一、名称空间namespaces：存放名字的地方，是对栈区的划分
# 有了名称空间之后，就可以在栈区中存放相同的名字，详细的，名称空间分为三种
# 1.1 内置名称空间
# 存放的名字：存放的是python解释器内置的名字
'''
>>> input
<built-in function input>
>>> print
<built-in function print>
'''
# 存活周期：python解释器启动则产生，python解释器关闭则销毁

# 1.2 全局名称空间
# 存放的名字：运行顶级代码所产生的名字，或者说不是函数内定义、也不是内置的，这样的名字
'''
import os
x=11
if True:
    y=22
def func():  # func()==>函数的内存地址
    pass
class Foo():  # Foo()==>类的内存地址
    pass
'''
# 存活周期：python文件运行则产生，python文件运行完毕后销毁

# 1.3 局部名称空间
# 存放的名字：在调用函数时，运行函数体代码过程中产生的函数体内的名字
# 存活周期：在调用函数时存活，函数调用完毕后则销毁
# def func(x,y):
#     ...
#
# func(1,2)
# func(1,3)
# func(2,3)

# 1.4 名称空间的加载顺序
# 内置名称空间>全局名称空间>局部名称空间

# 1.5 销毁顺序
# 局部名称空间>全局名称空间>内置名称空间

# 1.6 名字的查找优先级：当前所在位置向上一层一层查找
# 层级查找顺序以函数定义阶段确定：局部->全局->内置

# 示范:名称空间的“嵌套”关系在函数定义阶段就确定好的，与调用位置无关
# x=1
# def func():
#     print(x)
#
# def foo:
#     x=222
#     func()
# foo()  # 1

# 二：作用域，即作用范围
# 全局作用域：内置名称空间 & 全局名称空间
# 1.全局存活
# 2.全局有效

# 局部作用域：局部名称空间
# 1.临时存活
# 2.局部有效：函数内有效

# 三、global和nonlocal
# 示范1
# x = 11
#
# def func():
#     x = 22
#
# func()
# print(x)  # 11,不变，在局部名称空间创建变量不影响全局空间的变量

# 示范2:如果在局部想要修改全局的名字对应的值(不可变类型),需要用global
# x = 11
#
# def func():
#     global x  # 声明x是全局的名字，不要再造新的名字了
#     x = 22

func()
print(x)  # 22,全局变量改了

# 示范3：对于不可变类型
# l = [11,]
#
# def func():
#     l.append(22)
#
# func()
# print(l)  # [11, 22]

# nonlocal:修改函数外层函数包含的名字对应的值（不可变类型）
# x = 0
# def f1():
#     x=11
#     def f2():
#         nonlocal x
#         x=22
#     f2()
#     print('x in f1',x)
#
# f1()  # x in f1 22
