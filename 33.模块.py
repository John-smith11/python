'''
1.什么是模块
    模块就是一系列功能的集合体，分为三大类：
    I：内置模块
    II：第三方模块
    III：自定义模块
        一个python文件本身就可以作为一个模块，文件名m.py,模块名m

    模块的四种形式：
        1.使用python编写的.py文件

        2.已被编译为共享库或DLL的C或C++扩展

        3.把一系列文件组织到一起的文件夹（注：文件夹下面有一个__init__.py文件，该文件称之为包）

        4.使用C编写并链接到python解释器的内置模块

2.为何要用模块
    I:内置和第三方模块拿来就用，无需定义，这种拿来主义，可以极大地提升开发效率
    II：自定义的模块
        可以将程序的各部分功能提取出来放到一个模块中为大家共享使用
        好处是减少了代码冗余，程序组织结构更加清晰

3.如何使用模块
'''
# 一.import导入模块

x=1111
import foo
# 首次导入模块会发生3件事
# 1.执行foo.py
# 2.产生foo.py的名称空间，将foo.py运行过程中产生的名字都丢到foo的名称空间中
# 3..在当前文件中的名称空间中产生一个名字foo，该名字指向2中产生的名称空间

# 之后如果再导入，都是直接引用首次导入产生的foo.py的名称空间，不会重复执行代码
# import foo
# import foo

# 2.引用
print(foo.x)
foo.get()
print(foo.get)
print(foo.get())
# 强调1：用 模块名.名字，是指名道姓的文某个模块要名字对应的值，不会与当前名称空间中的名字发生冲突
# 强调2：无论查看还是修改都是对原模块操作的，与调用位置无关

# 可以以逗号为分隔符在一行导入多个模块,但不建议使用这种方式
import timer,numpy,scipy,matplotlib,foo

# 3.导入模块的规范：
#1st. python内置模块
#2nd. 第三方模块
#3rd. 程序员自定义模块
#
# import timer
# import sys
#
# import torch
# import torchaudio
#
# import foo

# 4.import xxx as xxx

# 5.模块是第一类对象

# 6.python3中自定义模块命名规范：纯小写+下划线

# 7.可以在函数内导入模块
def func():
    import foo


# 二.from...import...导入模块中的名字

# import导入模块在使用时必须加前缀“模块.”
# 优点：肯定不会与当前名称空间中的名字冲突
# 缺点：加前缀显得麻烦

# from...import...导入也发生了三件事
# 1.执行foo.py
# 2.产生foo.py的名称空间，将foo.py运行过程中产生的名字都丢到foo的名称空间中
# 3.在当前文件中的名称空间中得到一个名字，该名字指向2中产生的名称空间对应名字的内存地址
from foo import x
from foo import get
from foo import change

print(x)  # 1
print(get)  # <function get at 0x000001C597EFC0D0>
print(change)  # <function change at 0x000001C597EFC160>

get()  # 1
change()
get()  # 0

print(x) # 1
from foo import x
print(x) # 0

# from...import...导入模块使用时不加前缀
# 优点：代码更精简
# 缺点：容易与当前名称空间中的名字混淆

# 一行导入多个名字(不推荐）
from foo import x,get,change

# *：导入模块中的所有名字（极少使用）
from foo import *

# 了解：__all__控制*包含的名字有哪些
from foo import *
# change()  # 报错

# 起别名
from foo import get as g

# 注意：应避免出现模块的循环导入


# 三、模块的搜索路径优先级
# 无论是import还是from...import...在导入模块时都涉及文件路径查找
# 优先级：
# first：内存（内置模块）
# second：硬盘，按照sys.path中存放的文件夹路径顺序依次查找要导入的模块

import sys
# 值为一个列表，存放了一系列的文件夹
# 其中第一个文件夹是当前执行文件所在的文件夹
# 环境变量是以执行文件为准的，所有被导入的模块或者说后续其他文件引用的sys.path都是参照执行文件的sys.path
print(sys.path)

# 了解：sys.modules查看已经加载到内存中的模块
import sys
import foo
del foo  # 删不掉，python优化机制，减少IO操作

print(sys.modules)
print('foo' in sys.modules)  # True

# 当导入模块出错
import sys
# 找foo.py就把foo.py的文件路径添加到环境变量中
sys.path.append(r'绝对路径')
import foo

# 编写一个规范的模块

"The module is used to..." #模块的文档描述

import sys #导入模块

x=1 #定义全局变量,如果非必须,则最好使用局部变量,这样可以提高代码的易维护性,并且可以节省内存提高性能

class Foo: #定义类,并写好类的注释
    'Class Foo is used to...'
    pass

def test(): #定义函数,并写好函数的注释
    'Function test is used to…'
    pass

if __name__ == '__main__': #主程序
    test() #在被当做脚本执行时,执行此处的代码


