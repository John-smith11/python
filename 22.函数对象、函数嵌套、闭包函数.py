# 精髓：可以把函数当做变量去用
# func = 内存地址
def func():
    print('凉宫春日')

# 1.可以赋值
# f=func  # 得到函数的内存地址
# print(f,func)  # <function func at 0x000001A86C2E61F0> <function func at 0x000001A86C2E61F0>
# f()  # 凉宫春日

# 2.可以当做函数的参数传入
# def foo(x):
#     print(x)
#
# foo(func)  # foo(func的内存地址):<function func at 0x000001FE984461F0>

# 3.可以把函数当做另外一个函数的返回值
# def foo(x):
#     return x
#
# res = foo(func)
# print(res)  # <function func at 0x0000016A94F561F0>
# res()  # 凉宫春日

# 4.可以当做容器类型的一个元素
# l=[func,]
# print(l)
# l[0]()
#
# dic={'k1':func}
# print(dic)
# dic['k1']()

# 案例
# def login():
#     print('登录')
#
# def transfer():
#     print('转账')
#
# def check_balance():
#     print('查询余额')
#
# def withdraw():
#     print('取款')
#
# func_dic={
#     '1':(login,'登录'),
#     '2':(transfer,'转账'),
#     '3':(check_balance,'查询余额'),
#     '4':(withdraw,'取款')
# }
#
# while True:
#     for k in func_dic:
#         print(k,func_dic[k][1])
#
#     choice = input('请输入命令编号：').strip()
#     if not choice.isdigit():
#         print('请输入编号')
#         continue
#
#     if choice == '0':
#         break
#
#     if choice in func_dic:
#         func_dic[choice][0]()
#
#     else:
#         print('输入的指令不存在')

# 函数嵌套
# 1、函数的嵌套调用：在调用一个函数的过程中又调用其他函数
# def func1():
#     ...
#
# def func2():
#     ...
#
# def func3():
#     ...
#
# def func():
#     func1()
#     func2()
#     func3()

# 2.函数嵌套的定义：在函数内定义其他函数
# def f1():
#     def f2():
#         pass

# 闭包函数=名称空间与作用域+函数嵌套+函数对象
# 核心点：名字的查找关系是以函数定义阶段为准

# 一：什么是闭包函数
# “闭”函数指的是该函数是内嵌函数
# “包”函数指的是该函数包含对其外层函数作用域（不是对全局作用域）名字的引用
# 闭包函数：名称空间与作用域+函数嵌套，无论在哪调用,老婆始终要在包里找
def f1():
    老婆 = '凉宫春日'
    def f2():
        print(老婆)
    f2()

# 闭包函数：函数对象
# def f1():
#     老婆 = '凉宫春日'
#     def f2():
#         print('函数2',老婆)
#     return f2
#
# res = f1()
# res()

# 二、为何要有闭包函数，即闭包函数的应用
# 两种为函数体传参的方式
# 方式一：直接把函数体需要的参数定义成形参
# def f2(x):
#     print(x)
#
# f2('凉宫春日')
# f2('长门有希')

# 方式二：
# def f1(x):
#     def f2():
#         print(x)
#     return f2
#
# x = f1('凉宫春日')
# x()  # 凉宫春日
#
# y = f1('长门有希')
# y()  # 长门有希
#
# f2 = f1('朝比奈实玖瑠')
# f2()  # 朝比奈实玖瑠