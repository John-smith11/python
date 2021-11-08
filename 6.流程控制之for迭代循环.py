'''
1.什么是for循环
    循环就是重复做某件事，for循环是python提供的第二种循环机制

2.为何会有for循环
    理论上for循环能做的事，while也可以
    之所以会有for循环，是因为for在循环取值（遍历取值）上比while更方便

3.如何用for循环
语法：
for 变量名 in 可迭代对象：  # 可迭代对象可以是：列表、字典、字符串、元组、集合等
    代码块

'''
# 一、for循环基本使用之遍历取值
# 案例1：列表循环取值
# 简单版
l1 = ['凉宫春日', '长门有希', '朝比奈实玖瑠']

for name in l1:  # 按位置顺序依次取出列表中的值赋给变量name，每次完成取值赋值后都进入循环体进行一次循环，直到取完列表的值
    print(name)

# 复杂版
i = 0
while i < 3:
    print(l1[i])
    i +=1

# 案例2：字典循环取值
# 简单版
dic1 = {'凉宫春日': '老婆', '朝比奈实玖瑠': '女神', '长门有希': '偶像'}

for name in dic1:  # 取key赋值
    print(name, dic1[name])

# 复杂版：while也可以，但太麻烦

# 案例3：字符串循环取值
# 简单版
truth = '凉宫春日， 你是我老婆[狗头]'

for character in truth:  # 逐个字符取值赋值
    print(character)

# 二、总结for循环与while循环的异同
# 1.相同之处：都是循环， for可以干的事，while也可以
# 2.不同之处：
#       while循环被称为条件循环，循环次数取决于条件何时变为假
#       for循环被称为迭代循环，循环次数取决于in后对象包含的元素的个数
for var in [1, 2, 3]:  # 可以只取不用，但var必须要写
    print("老婆是凉宫春日")
    print('凉宫春日是老婆')

# 三、for循环控制循环次数：range()
'''
有局限性
for var in [1, 2, 3]:  # 可以只取不用，但var必须要写
    print("老婆是凉宫春日")
    print('凉宫春日是老婆')
'''
# range功能介绍
# range(10)
# [0, 1, 2, 3, 4, 5 ,6, 7, 8, 9]
#     头 腚 步长
range(1,10, 1)   # 顾头不顾腚

print('凉宫春日')
for i in range(10):
    print('我爱你♥')

# 用range生成索引取对应列表中的值
l1 = ['凉宫春日', '长门有希', '朝比奈实玖瑠']
for i in range(len(l1)):
    print(i, l1[i])

# 3.break和else在for中的用法与在while中一样

# 4.range()在python3中得到的是一只“会下蛋的老母鸡”

# 四、for+continue与在while中用法一致
for i in range(6):
    if i == 4:
        continue
    print(i)

# for循环嵌套:外层循环每循环一次，内层循环需要完整的循环完毕
for i in range(3):
    print("外层循环-->", i)
    for j in range(5):
        print('内层循环——>', j)

# 补充：终止for循环只有break一种方式

# print（）补充：体会一下区别
print('凉宫春日', '长门有希', '朝比奈实玖瑠')

print('凉宫春日')
print('长门有希')

print('凉宫春日', end='')
print('长门有希')

print('凉宫春日', end='*')
print('长门有希')

