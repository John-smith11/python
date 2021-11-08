# 条件
# 什么是条件？什么可以当做条件？为什么要有条件？
#  第一大类：显式的布尔值,True,False
# 1.条件可以是比较
age = 18
print(age > 16)  # 条件判断后会得到一个布尔值

# 2.条件可以是：True、False
is_beautiful = True
print(is_beautiful)

# 第二大类：隐式布尔值，所有的值都可以当成条件去用
# 其中0、None、空（空字符串、空列表、空字典）=》代表的布尔值为False，其余都为True
# '   '非空，字符串里的空格也是字符

# 逻辑运算符
# not：把紧跟其后的条件结果取反
# not与紧跟其后的条件是一个整体
print(not 16 > 18)

# and：与，用来连接两个条件，条件1 and 条件2，见假得假，全真得真
print(True and 10 and 10 > 3 and 3 != 4)
print(True and 0 and 10 > 3 and 3 != 4)

# or ：或，连接两个条件，见真得真，全假得假
print(1 or 3 < 2 or None)

# 优先级：not>and>or

# 成员运算符：in，not in
# in
print('凉宫春日' in '凉宫春日是老婆')  # 判断一个字符串是不是另一个字符串的子字符串
print('凉宫春日' in ['凉宫春日', '长门有希', '朝比奈实玖瑠'])  # 判断一个元素是不是存在于一个列表
print('凉宫春日' in {'老婆': '凉宫春日', '偶像': '长门有希', '女神': '朝比奈实玖瑠'})  # 字典
print('老婆' in {'老婆': '凉宫春日', '偶像': '长门有希', '女神': '朝比奈实玖瑠'})  # 判断一个key是不是存在于一个字典中

# not in，用法同in，但不推荐使用
print('凉宫春日' not in '凉宫春日是老婆')  # 判断一个字符串是不是另一个字符串的子字符串

# 身份运算符：is
# is 判断id是否相等

# 流程控制之if判断
# 语法1：
'''if 条件 :
      代码块
'''
name = '凉宫春日'
height = 158

if name == '凉宫春日' and height < 160 :
    print('老婆')
print('go home')

# 语法2：
'''if 条件 :
      代码块
   else :
      代码块
'''
if name == '凉宫春日' and height < 160 :
    print('老婆')
else :
    print('这不是我老婆！')

# 语法3：
'''if 条件1 :
      代码块
   elif 条件2 :
      代码块
   elif 条件3 :
      代码块
'''
heigt_of_wife = input('please input your height')
height_of_wife = int(heigt_of_wife)

if height_of_wife == 158:
    print('这是老婆的身高')
elif height_of_wife > 158:
    print('Taller than my wife')
elif height_of_wife < 158 :
    print('Shorter than my wife')

# 语法4：
'''if 条件1 :
      代码块
   elif 条件2 :
      代码块
   elif 条件3 :
      代码块
   else :
      代码块
'''
# if 可以嵌套 if

# 补充（了解）
# 短路运算：偷懒原则，偷懒到哪个位置，就把当前位置的值返回

# 深浅copy
l1 = ['凉宫春日', '长门有希', '朝比奈实玖瑠']
l2 = l1  # 这不叫copy
# 二者分隔不开，修改时同时改变，因为指向同一个地址
l1[0] = '灶门祢豆子'
print(l2)

# 需求：
# 1.copy原列表产生新列表
# 2.想使两个列表完全独立开
# 如何copy
# 浅copy # 在改操作上实现第一层（非容器元素）独立
l1 = ['凉宫春日', '长门有希', '朝比奈实玖瑠', ['阿虚', '古泉一树']]
l2 = l1.copy()
print(l2)
print(id(l1))
print(id(l2))  # 列表id不一样
print(id(l1[0]))
print(id(l2[0]))  # 元素id一样

l1[0] = '灶门祢豆子'
print(l1)
print(l2)  #independent

l1[3][0] = '我妻善逸'
print(id(l1[3][0]))
print(id(l2[3][0]))  # dependent
print(l1)
print(l2)

# 深copy，改操作实现完全独立
import copy

l2 = copy.deepcopy(l1)
print(id(l1[0]), id(l1[1]), id(l1[2]), id(l1[3]))
print(id(l2[0]), id(l2[1]), id(l2[2]), id(l2[3]))