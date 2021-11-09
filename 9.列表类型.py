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

# 4.1.2 （顾头不顾腚，步长）
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