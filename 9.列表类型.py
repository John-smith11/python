#1、作用：按位置存多个值，索引对应值
# 2.定义
l1 = [520, '凉宫春日', '长门有希', ['朝比奈实玖瑠', '古泉一树']]  # l1 =list([520, '凉宫春日', '长门有希', ['朝比奈实玖瑠', '古泉一树']])
print(type(l1))

# 3.类型转换但凡能被for循环遍历的类型都可以当做参数传给list()转成列表
res = list('凉宫春日')
print(res)
# 原理如下
res = []
for element in '凉宫春日':
    res.append(element)

res = list( {'凉宫春日': '老婆', '朝比奈实玖瑠': '女神', '长门有希': '偶像'})  # [k1, k2, k3]
print(res)

# 4.内置方法
# 4.1优先掌握
# 4.1.1 按索引取值（正向取+反向取）：可以取也可以改
l= ['老婆', '凉宫春日', 158]
# 正向取
print(l[0])

# 反向取
print(l[-1])

# 可以取也可以改:索引存在则修改对应的值，索引不存在则报错
l[0] = 'wife'
print(l)

# 4.1.2 切片（顾头不顾腚，步长）
l = ['老婆', '凉宫春日', 158, '阿虚', '情敌', '阿', '虚']
print(l[3:])

l1 = l[:]  # 切片等同于copy行为，而且相当于浅copy

# 步长
res = l[::2]  # 步长为2，方向0-->
print(res)


# 反向步长
res = l[len(l):0:-1]  # 步长为1,方向len(l)-->0
print(res)

res = l[::-1]  # 倒着写
print(res)

# 4.1.3 长度：len()
l = ['老婆', '凉宫春日', 158, '阿虚', '情敌', '阿', '虚']
print(len(l))

# 4.1.4 成员运算in和not in
name_of_wife = '凉宫春日'
print(name_of_wife in l)
print(name_of_wife not in l)  #少用

# 4.1.5.往列表里添加值
# 4.1.5.1 追加
l= ['老婆', '凉宫春日', 158]
l.append('suzumiya haruhi')
print(l)

# 4.1.5.2 插入值
l= ['老婆', '凉宫春日', 158]
l.insert(1, 'suzumiya haruhi')
print(l)

#4.1. 5.3 extend（）接受可迭代对象
l= ['老婆', '凉宫春日', 158]
l1 = ['阿虚', '情敌']
l.extend(l1)  # l= ['老婆', '凉宫春日', 158, '阿虚', '情敌']
print(l)
l.extend('阿虚')
print(l)

# 4.1.6.删除
# 方式一：通用方法，没有返回值
l= ['老婆', '凉宫春日', 158]
del l[2]
print(l)
# 方式二：list.pop(),根据索引删除，有返回值,返回删除的值
l= ['老婆', '凉宫春日', 158]
l.pop()  # 不指定索引，默认删最后一个
res = l.pop(0)
print(res)

# 方式三：list.remove(),根据元素删，没有返回值
l= ['老婆', '凉宫春日', 158]
res = l.remove(158)
print(res)  # None

# 4.1.7.循环
for element in ['老婆', '凉宫春日', 158]:
    print(element)

# 需要掌握的操作
l= ['老婆', '凉宫春日', 158, 158]
# l.count()  # 统计元素个数
print(l.count(158))

# l.index()  # 查元素的第一个索引，找不到就报错
print(l.index('凉宫春日'))

# l.clear()  # 清楚整个列表
# l.clear()
# print(l)

# l.reverse()  # 将列表翻转
l.reverse()
print(l)

# l.sort()  # 排序,列表内元素必须是同种类型，否则报错
l = [11, -3, 2.5, 43, 99]
l.sort()  # 默认从小到大排,升序
print(l)  # [-3, 2.5, 11, 43, 99]
l.sort(reverse=True)  # 设置为降序
print(l)  # [99, 43, 11, 2.5, -3]

# 了解：字符串可以比大小，按照对应位置的字符依次PK，每个字符按ASCI码先后顺序区分
# 了解：列表之间也可以比大小，按照对应位置的元素依次PK，对应位置元素必须为同种类型否则报错，每个元素按ASCI码先后顺序区分

# 补充：用操作列表实现队列和堆栈
# 队列：FIFO，先进先出
l=[]
# 入队操作
l.append('first')
l.append('second')
l.append('third')
print(l)
# 出队操作
print(l.pop(0))
print(l.pop(0))
print(l.pop(0))

# 堆栈：LIFO，后进先出
l=[]
# 入栈操作
l.append('first')
l.append('second')
l.append('third')
print(l)
# 出栈操作
print(l.pop())
print(l.pop())
print(l.pop())