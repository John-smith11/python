# 1.作用
# 2.定义
wife = '凉宫春日'  # wife = str(‘凉宫春日’)
print(type(wife))

# 3.类型转换
# str可以把任意其他类型都转成字符串
res = str({'凉宫春日': '老婆', '朝比奈实玖瑠': '女神', '长门有希': '偶像'})
print(res, type(res))

# 4.使用：内置方法
# 4.1优先掌握
# 4.1.1 按索引取值（正向取+反向取）：只能取
wife = '老婆： 凉宫春日'
# 正向取
print(wife[0])
print(wife[3])

# 反向取
print(wife[-1])

# 只能取
# wife[3] = '是'  # 会报错

# 4.1.2 切片:索引的拓展应用，从一个大的字符串中copy一个子字符串（顾头不顾腚，步长）
wife = '老婆： 凉宫春日'
print(wife[3:])
print(wife[3:9])

# 步长
res = wife[0:9:2]  # 步长为2，方向0-->9
print(res)

res = wife[:]  # 完整copy

# 反向步长
res = wife[8:0:-1]  # 步长为1,方向8-->0
print(res)

res = wife[::-1]  # 倒着写
print(res)

# 4.1.3 长度len
wife = '老婆： 凉宫春日'
print(len(wife))

# 4.1.4 成员运算in和not in
# 判断一个短字符串是否存在于一个长字符串中
name_of_wife = '凉宫春日'
print(name_of_wife in wife)
print(name_of_wife not in wife)  #少用

# 4.1.5 移除字符串左右两侧的空白strip
# 默认形式，移除空格
wife = '  老婆： 凉宫春日  '
res = wife.strip()  # 默认去掉的是空格,返回新值，不改变原值
print(wife)
print(res)

# 其他
wife = '**老婆： 凉宫春日**'
res = wife.strip('*')
print(wife)
print(res)

wife = '*/<>()*老婆： 凉宫春日*\*{}[]'
res = wife.strip('*/\{}[]()<>')
print(wife)
print(res)

# 了解：只去除两边不去除中间
wife = '**老婆**： 凉宫春日**'
res = wife.strip('*')
print(wife)
print(res)
# 应用
# heigt_of_wife = input('please input your height').strip()
# '''
#  注意，input返回一个字符串，strip()是字符串的方法而不是input的方法'''
# height_of_wife = input(heigt_of_wife).strip()
#
# if height_of_wife == 158:
#     print('这是老婆的身高')
# elif height_of_wife > 158:
#     print('Taller than my wife')
# elif height_of_wife < 158 :
#     print('Shorter than my wife')

# 4.1.6 切分split:把一个字符串按照某种分隔符进行切分，得到一个列表
info = '凉宫春日 老婆 158'
res = info.split()  # 默认按空分割
print(info)  # 原字符串不变
print(res)

info = '凉宫春日*老婆*158'
res = info.split('*')  # 可以指定其他分隔符
print(info)  # 原字符串不变
print(res)

info = '凉宫春日*老婆*158'
res = info.split('*', 1)  # 可以指定分隔次数
print(info)  # 原字符串不变
print(res)

# 4.1.7 循环
info = '凉宫春日*老婆*158'
for i in info:
    print(i)

# 4.2 需要掌握
# strip, lstrip, rstrip

# lower, upper
NAME = 'SUZUMIYA HARUHI'
print(NAME.lower())

name = NAME.lower()
print(name.upper())

# startswitch, endswitch  #判断字符串开头和结尾
print('suzumiya haruhi is my wife'.startswith('suzumiya'))
print('suzumiya haruhi is my wife'.endswith('wife'))

# format的三种用法
# split, rsplit
info = '凉宫春日*老婆*158'
res = info.split('*')
res1 = info.rsplit('*')
print(res)   # ['凉宫春日', '老婆', '158']
print(res1)   # ['凉宫春日', '老婆', '158']

info = '凉宫春日*老婆*158'
res = info.split('*', 1)
res1 = info.rsplit('*', 1)
print(res)   # ['凉宫春日', '老婆*158']
print(res1)   # ['凉宫春日*老婆', '158']

# join: 把列表拼接成字符串

list1 = ['凉宫春日', '老婆', '158']
res = list1[0] +'*'+list1[1]+'*'+list1[2]
print(res)
res1 = '*'.join(list1)  # 按照某个分隔符，把元素全为字符串的列表拼接成一个长字符串
print(res1)

# '*'.join(['凉宫春日', '老婆', 158])  # 列表中有非字符串元素会报错

# replace
name_of_my_wife = 'suzumiya haruhi suzumiya haruhi suzumiya haruhi suzumiya haruhi'
#                              要替换的             替换成
print(name_of_my_wife.replace('suzumiya haruhi', 'SUZUMIYA HARUHI'))  # 默认全替换
#                              要替换的             替换成           换几个
print(name_of_my_wife.replace('suzumiya haruhi', 'SUZUMIYA HARUHI', 2))

# isdigit: 判断字符串是否由纯数字组成
print('158'.isdigit())  # True
print('1.58'.isdigit())  # False

# 4.3 了解
# find, rfind, index, rindex, count
name_of_my_wife = 'suzumiya haruhi'
print(name_of_my_wife.find('u'))  # 返回要查找的字符串在长字符串中的起始索引
print(name_of_my_wife.find('haruhi'))  # 返回要查找的字符串在长字符串中的起始索引
print(name_of_my_wife.index('haruhi'))  # 能找到时find与index用法一致
# 区别：如果找不到
print(name_of_my_wife.find('凉宫春日'))  # 返回-1
# print(name_of_my_wife.index('凉宫春日'))  # 报错

name_of_my_wife = 'suzumiya haruhi suzumiya haruhi suzumiya haruhi suzumiya haruhi'
print(name_of_my_wife.count('haruhi'))  # 统计个数

# center, ljust, rjust, zfill:控制输出
print('凉宫春日'.center(50, '♥'))  # 字符串居中，不够的用'♥'补齐
print('凉宫春日'.ljust(50, '♥'))  # 字符串左对齐，不够的用'♥'补齐
print('凉宫春日'.rjust(50, '♥'))  # 字符串右对齐，不够的用'♥'补齐
print('凉宫春日'.zfill(50))  # 字符串右对齐，不够的用'0'补齐

# expandtabs:指定制表符宽度
msg = 'suzumiya\tharuhi'
print(msg)
print(msg.expandtabs(20))  # 设定制表符代表的空格数为20

# captalize, swapcase, title
'suzumiya haruhi'.capitalize()  # 首字母大写，Suzumiya haruhi
'suzumiya HARUHI'.swapcase()  # 大小写翻转，SUZUMIYA haruhi
'suzumiya haruhi'.title()  # 每个单词首字母大写，Suzumiya Haruhi

# is其他
'suzumiya haruhi'.islower()  # 判断是否全为小写，True
'SUZUMIYA HARUHI'.isupper()  # 判断是否全为大写,True
'suzumiya haruhi'.isalpha()  # 是否全字母
'    '.isspace()  # 是否全空格
'suzumiya haruhi'.isidentifier()  # 检查变量名是否合法
# 关于数字
# 格式'字符串'
num1 = b'4'  #bytes
num2 = u'4'  #unicode,python3中无需加u就是unicode
num3 = '四'  #中文数字
num4 = 'Ⅳ'  #罗马数字

# isdigit只能识别前两种
print(num1.isdigit())  # True
print(num2.isdigit())  # True
print(num3.isdigit())  # False
print(num4.isdigit())  # False

# isnumeric可以识别后三种
print(num2.isnumeric())  # True
print(num3.isnumeric())  # True
print(num4.isnumeric())  # True

# isdecimal只能识别：num2
print(num2.isdecimal())  # True
print(num3.isdecimal())  # False
print(num4.isdecimal())  # False
