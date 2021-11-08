
print('hello word')
name = 'peter'
print(id(name))
print(type(name))
print(name)

# 变量：刻画事物的状态，包括变量名，赋值动作，变量值
# 变量：先定义后使用
# 变量名》门牌号（记录变量地址）
# 变量值有不同的类型

# 变量名格式：字母、数字、下划线。推荐小写字母加下划线。要见名知意


# is 与==
name_1 = '凉宫春日'
name_2 = '凉宫春日'
name_3 = '长门有希'
name_4 = '长门有希'
# is比较两值的ID是否相等（pycharm与python解释器不同）
# print(id(name_1))
# print(id(name_2))
# print(id(name_3))
# print(id(name_4))
# print(name_1 is name_2)
# print(name_3 is name_4)
# ==比较值是否相等
# print(name_1 == name_2)

# 小整数池 [-5,256]
# python启动时会自动申请一些内存空间存放一些常用整数

# 常量：不变的量
# 注意：python语法中没有常量的定义，但是程序设计中会涉及常量概念
HIGHT_OF_SUZUMIYA_HARUHI = 158  # 用字母全大写代表常量，这是一种约定、规范

# 基本数据（变量值）类型：（见知乎）
# 整型
age = 18
print(type(age))
print(age > 18)
# 浮点型
price = 3.5
type(price)
# 字符串,用’ ‘，“ ”，'' '',"" "",''' ''',""" """括起来
name = '凉宫春日'
name = '''凉宫春日'''
# 字符串嵌套，注意：引号要配套使用，外层用单引号，内层用双引号,反之亦然。或者用转义符
'her name is "suzumiya haruhi"'
'her name is \'suzumiya haruhi\''

# 列表：索引对应值，索引从0开始
# 作用：记录多个值，按索引取值
# 定义：在[]内用逗号分隔开多个任意类型的值，一个值称之为一个元素
# index： 0    1         2         3
list = [520, '凉宫春日', '长门有希', ['朝比奈实玖瑠', '古泉一树']]
# print(list)
# print(list[1])
# print(list[3][0])

# 字典：key对应值，其中key通常为字符串，key对值有描述性功能
# 作用：用来存多个值，每个值都有唯一的key与其对应
# 定义：在{}内用逗号分隔开多个key：value,按key取值
# 列表元素有顺序字典无顺序
register = {'凉宫春日': '老婆', '朝比奈实玖瑠': '女神', '长门有希': '偶像'}
print(type(register))
print(register['凉宫春日'])

# 布尔型