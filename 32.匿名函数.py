# 1.def用于定义有名函数
# func = 函数的内存地址
def func(x,y):
    return x+y

print(func)  # <function func at 0x0000022D7FF861F0>

# 2.lambda用于定义匿名函数
# (lambda x,y : x+y) = 函数的内存地址
lambda x,y : x+y

print(lambda x,y : x+y)  # <function <lambda> at 0x000001E0D64CC0D0>

# 3.调用匿名函数
# 方式一：
res = (lambda x,y : x+y)(1,2)
print(res)  # 3

# 方式二：用一个函数名获取内存地址,不如直接定义有名函数，是脱裤子放屁行为
func1 = lambda x,y : x+y
print(func1)  # <function <lambda> at 0x000001E0D64CC0D0>
res = func1(1,2)
print(res)

# 4.匿名函数用于临时调用一次的场景：更多的是将匿名函数与其他函数配合使用

# 应用
favorable = {
    '冯宝宝':92,
    'Kamado Nezuko':90,
    'Suzumiya Haruhi':99,
    'Iki Hiyori':95
}
# 需求1：找出好感度最高的那个人-->max()
# res=max(favorable)
# print(res)  # 冯宝宝
#
# 迭代出的内容        比较的值
# '冯宝宝'             92
# 'Kamado Nezuko'     90
# 'Suzumiya Haruhi'   99
# 'Iki Hiyori'        95
#
def func(iter_key):
    iter_value = favorable[iter_key]
    return iter_value

res=max(favorable, key=func)  # 与key返回的值作为比较的依据取最大,返回可迭代对象中满足条件的元素
print(res)  # Suzumiya Haruhi

# 换成匿名函数实现
res=max(favorable, key=lambda iter_key : favorable[iter_key])
print(res)  # Suzumiya Haruhi

# 需求2：找出好感度最低的那个人-->min()
res=min(favorable, key=lambda iter_key : favorable[iter_key])
print(res)  # Kamado Nezuko

# 需求3：按好感度由低到高排序-->sorted()
# res=sorted(favorable)
# print(res)  # ['Iki Hiyori', 'Kamado Nezuko', 'Suzumiya Haruhi', '冯宝宝']
#
res=sorted(favorable, key=lambda iter_key : favorable[iter_key])
print(res)  # ['Kamado Nezuko', '冯宝宝', 'Iki Hiyori', 'Suzumiya Haruhi']

# 按好感度从高到低
res=sorted(favorable, key=lambda iter_key : favorable[iter_key],reverse= True)
print(res)  # ['Suzumiya Haruhi', 'Iki Hiyori', '冯宝宝', 'Kamado Nezuko']


# ==============>map的应用（了解）
l =['凉宫春日','一歧日和','冯宝宝','灶门祢豆子']
# new_l =(name +'老婆' for name  in l)
# print(new_l)  # <generator object <genexpr> at 0x000002014A926580>
# print(new_l.__next__())  # 凉宫春日老婆

new_l = map(lambda name:name+'老婆', l)  # map(函数（从可迭代对象产生的值）, 可迭代对象)返回一个生成器
print(new_l)  # <map object at 0x000002470FB2C310>
print(new_l.__next__())  # 凉宫春日老婆
print(new_l.__next__())  # 一歧日和老婆
print(new_l.__next__())  # 冯宝宝老婆
print(new_l.__next__())  # 灶门祢豆子老婆

# ==============>filter的应用（了解）
l =['凉宫春日老婆','一歧日和老婆','冯宝宝','灶门祢豆子']
# new_l =(name for name  in l if name.endswith('老婆'))
# print(new_l)  # <generator object <genexpr> at 0x0000024F266DABA0>
# print(new_l.__next__())  # 凉宫春日老婆

# filter(函数（从可迭代对象产生的值）, 可迭代对象),filter(True, 可迭代对象)保留，filter(False, 可迭代对象)丢弃
new_l = filter(lambda name:name.endswith('老婆'), l)
print(new_l)  # <filter object at 0x0000014D6AC17370>
print(new_l.__next__())  # 凉宫春日老婆
print(new_l.__next__())  # 一歧日和老婆
# print(new_l.__next__())  # StopIteration

# ==============>reduce的应用（了解）
from functools import reduce
res=reduce(lambda x,y:x+y,[1,2,3],10)
print(res)  # 16

res=reduce(lambda x,y:x+y,l,'老婆')
print(res)  # 老婆凉宫春日老婆一歧日和老婆冯宝宝灶门祢豆子
