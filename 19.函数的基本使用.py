'''
1.什么是函数
    函数就相当于具备某一功能的工具
    函数的使用必须遵循一个原则：
        先定义
        后调用
2.为何要用函数，可以避免：
    1.组织结构不清楚，可读性差
    2.代码冗余
    3.可维护性、扩展性差

3.如何使用函数
    先定义
        三种定义方式
    后调用
        三种调用方式
    返回值
        三种返回值形式
'''

# 一.先定义
# 函数的语法
'''
def 函数名(参数1,参数2,...):
    """文档描述"""
    函数体
    return 值
'''

# 形式一：无参函数
def func():
    print('凉宫春日')
    print('长门有希')
    print('朝比奈实玖瑠')

# 定义函数发生的事情
# 1.申请内存空间保存函数体代码
# 2.将上述内存地址绑定函数名
# 3.定义函数不会执行函数体代码，但是会检测函数体语法

# 调用函数发生的事情
# print(func)  # 函数体内存地址，<function func at 0x000001A9ABD461F0>
# func()  # 实际就是内存地址后面加括号
# 1.通过函数名找到函数的内存地址
# 2.然后加阔号就是在触发函数体代码的执行

# 形式二：有参函数
def func(x, y):
    print(x, y)

func('凉宫春日', '长门有希')

# 形式三：空函数，函数体代码为pass
def func():
    pass

# 应用场景
# 无参函数：函数体执行不需要额外传入参数
# 有参函数：函数体执行需要额外传入参数
# 空函数：因为在程序设计的开始，往往是先想好程序都需要完成什么功能，然后把所有功能都列举出来用pass充当函数体，
#       这将使得程序的体系结构立见，清晰且可读性强
# 示例：
# def auth_user():
#     """user authentication function"""
#     pass
#
# def download_file():
#     """download file function"""
#     pass
#
# def upload_file():
#     """upload file function"""
#     pass
#
# def ls():
#     """list contents function"""
#     pass
#
# def cd():
#     """change directory"""
#     pass

# 二、调用函数
def func(x, y):
    res=x+y

# 1.语句形式：只加括号调用函数
# func()
# 2.表达式形式：
# res = func()
# res = func()*3
# 3.函数调用可以当做参数
# func(func(),'凉宫春日')

# 三、函数的返回值
# return是函数结束的标志，即函数体代码一旦运行到return会立刻终止函数的运行，并返回return后的结果
# 1.返回None：函数体内没有return
#           return
#           return None

# 2.返回一个值： return 返回值
# def func()：
#     return 158
#
# res = func()
# print(res)

# 3.返回多个值：用逗号分隔开多个值，会被return返回成元组
def func():
    return 158, '凉宫春日', ['女朋友','老婆']

res = func()
print(res,type(res))  # (158, '凉宫春日', ['女朋友', '老婆']) <class 'tuple'>