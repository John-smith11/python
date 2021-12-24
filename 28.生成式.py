# 列表生成式
l =['一歧日和老婆','灶门祢豆子','凉宫春日老婆','朝比奈实玖瑠','长门有希','冯宝宝老婆']
new_l=[]
# for name in l:
#     if name.endswith('老婆'):
#         new_l.append(name)
#
# print(new_l)

new_l = [name for name in l if name.endswith('老婆')]
print(new_l)  # ['一歧日和老婆', '凉宫春日老婆', '冯宝宝老婆']

new_l = [name for name in l]  # new_l = [name for name in l if True]
print(new_l)  # ['一歧日和老婆', '灶门祢豆子', '凉宫春日老婆', '朝比奈实玖瑠', '长门有希', '冯宝宝老婆']

# 把所有名字去掉后缀“老婆”
new_l =[name.replace('老婆','') for name in l]
print(new_l)

# 语法
# l = [表达 for x in 可迭代对象 if 条件成立]
# [expression for item1 in iterable1 if condition1
# for item2 in iterable2 if condition2
# ...
# for itemN in iterableN if conditionN
# ]

#类似于
res=[]
# for item1 in iterable1:
#     if condition1:
#         for item2 in iterable2:
#             if condition2
#                 ...
#                 for itemN in iterableN:
#                     if conditionN:
#                         res.append(expression)

# 字典生成式
# dic1 ={k:v for k,v in 可迭代对象 if 条件}
keys = ['name','height','gender']
dic1={key:None for key in keys}
print(dic1)  # {'name': None, 'height': None, 'gender': None}

items = [('name','凉宫春日'),('height',158),('gender','female')]
res ={k:v for k,v in items if k != 'gender'}
print(res)

# 集合生成式
# set1 ={元素 for k in 可迭代对象 if 条件}
keys = ['name','height','gender']
set1={key for key in keys}
print(set1,type(set1))  # {'name', 'height', 'gender'} <class 'set'>

# 没有元组生成式
# 生成器生成式
g = (i for i in range(10) if i > 3)
# !!!!!!强调!!!!!!
# 此时g内部一个值也没有
print(g,type(g))  # <generator object <genexpr> at 0x000001F18A9D2740> <class 'generator'>

print(next(g))  # 4
print(next(g))  # 5
print(next(g))  # 6
print(next(g))  # 7
print(next(g))  # 8
print(next(g))  # 9
# print(next(g))  # StopIteration

# 案例：统计文件的字符个数
with open('The story about suzumiya haruhi and me',mode='rt',encoding='utf-8') as f:
    # 方式一：
    # res = 0
    # for line in f:
    #     res += len(line)
    # print(res)

    # 方式二：弊端是行数过多是需要比较大的存储空间来存l
    # l = [len(line) for line in f]
    # res = sum(l)
    # print(res)

    # 方式二：合理的方式是用生成器的方法
    g = (len(line) for line in f)
    res = sum(g)
    # 简写
    # res = sum((len(line) for line in f))
    # 或
    # res = sum(len(line) for line in f)
    print(res)

