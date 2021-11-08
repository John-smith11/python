
#垃圾回收机制（了解）
# 引用计数为0时回收内存

# 1.引用计数
x = 10
y = x
print(x)  # 直接引用，从栈区出发可以直接找到堆区的数据
print(y)
l = ['凉宫春日', x]
d = {'朝比奈实玖瑠' : y }
print(l[1])  # 间接引用，从栈区出发到堆区先找的数据的地址，再通过地址找到数据
print(d['朝比奈实玖瑠'])
print(id(x))
print(id(l[1]))

# 注意区别
x = 10
l = ['凉宫春日', x]  # l-->['凉宫春日'的内存地址,10的内存地址]
x=123
print(l[1])
print(x)

# 2.标记清除
del y
# 循环引用=>导致内存泄露
l1=['凉宫春日']
l2=['长门有希']

l1.append(l2)  # l1-->['凉宫春日'的内存地址，列表l2的内存地址]
l2.append(l1)  # l2-->['长门有希'的内存地址，列表l1的内存地址]
del l1
del l2
# 此时引用计数并不为0，不能被GE回收，标记清除机制发挥作用，清除堆区中与栈区没有引用关系的循环块

#3.分代回收（垃圾扫描规则）




# 与用户交互
#接收用户的输入
# 在python3：input会将用户输入的所有内容都存成字符串类型
user_name = input('请输入您的姓名')
print(user_name,type(user_name))

age = input('请输入您的年龄')
age = int(age)  # int只能将纯数字的字符串转成整型

# 在python2中：
# raw_input():用法与python3的input一模一样
# input():要求用户必须输入一个没抢到数据类型，输入的是什么类型，就存成什么类型

#字符串格式化输出
#1. %s
info_0 = 'my name is %s, my height is %s' %('凉宫春日', '158')  # 按位置传值
info_1 = '我的名字是 %(name)s, 我的身高是 %(height)s' %{'name':'凉宫春日','height': '158'}  # 按Key传值,以字典的形式
info_2 = 'my name is %s' %'凉宫春日'
print(info_0)
print(info_1)
print(info_2)

# %s可以接收任意类型，%d只能接收int
print('my height is %d' % 158)

# 输出%字符
print('成功率 %s%%'% 97)

#2. str.format方法:兼容性好
info_0 = 'my name is{}, my height is {}'.format ('凉宫春日', '158')  # 按位置传值
print(info_0)
info_0 = 'my name is{0}{0}{0}, my height is {1}{0}'.format ('凉宫春日', '158')
print(info_0)

info_1 = '我的名字是 {name}, 我的身高是 {height}' .format(name ='凉宫春日',height='158') # 按Key传值,以函数的形式
print(info_1)

#四舍五入精确到小数点后几位
print('{pi:.3f}'.format(pi=3.1415926))

#3 f:python3.5以后才推出，最快
name= input('your name')
height = input('your height')
info = f'她的名字是{name}, 她的身高是{height}'
print(info)
#输出‘{}’
info = f'她的名字是{{{name}}}, 她的身高是{height}'
print(info)

#f的其他用法：{}内的字符串可以被当做表达式运行
res =f'{10+3}'
print(res)

f'{print("凉宫春日")}'

#基本运算符
#1.数学运算符
#特别的
print(10/3)  # 除
print(10//3)  # 整除
print(10%3)  # mod
print(10**3)  # power

#2.比较运算符：>,<,>=,<=,==,!=

#3.赋值运算符
#3.1 =：变量的赋值
#3.2 增量赋值：
age = 18
age += 1  # age = age + 3
age *= 1  # age = age * 3
age /= 1  # age = age / 3
age **= 1  # age = age ** 3

#3.3 链式赋值
x = 10
y = x
z = y
print(id(x), id(y), id(z))
z = y = x = 10 # 链式赋值

#3.4 交叉赋值

m = 10
n = 20
temp = m
m = n
n= temp
print(m, n)

m,n = n,m #交叉赋值
print(m,n)

#3.5 解压赋值
salaries = [1000, 2000, 3000, 4000, 5000]
# 把五个月的工资取出来分别赋给不同的变量名
mon0 = salaries[0]
mon1 = salaries[1]
mon2 = salaries[2]
mon3 = salaries[3]
mon4 = salaries[4]
print(mon0)
print(mon1)
print(mon2)
print(mon3)
print(mon4)

mon0,mon1,mon2,mon3,mon4 = salaries #解压赋值，一一对应，不多不少
mon0,mon1,mon2,*_ = salaries #解压赋值，只取前三个，’_'作为容器接收废弃数据
mon0,mon1,mon2,*mon = salaries #解压赋值，只取前三个，’mon'作为容器接收剩余数据，mon是一个list
*_,mon2,mon3,mon4 = salaries #解压赋值，只取后三个，’_'作为容器接收废弃数据
mon0,*_,mon3,mon4 = salaries #解压赋值，只取后头尾，’_'作为容器接收废弃数据

#解压字典默认解压出来的是字典的key
x, y, z =dic = {'a':1, 'b':2,'c':3}
print(x,y,z)


