# 元组就是一个“不可变的列表”
# 作用：按索引/位置存放多个值，只用于读不用于改
# 定义：在()内用逗号分隔开多个任意类型的值，一个值称之为一个元素
t = ('老婆', '凉宫春日', 158)
print(t, type(t))  # ('老婆', '凉宫春日', 158) <class 'tuple'>

t = (158)  # 单独一对括号代表包含的意思
print(t, type(t))  # 158 <class 'int'>

t = (158,)  # 如果元组中只有一个元素，必须加逗号
print(t, type(t))  # (158,) <class 'tuple'>

# 体会：元组不让改的是成员的内存地址
t = ('老婆', '凉宫春日', 158)  # t-->(0-->值'老婆'的内存地址,1-->值'凉宫春日'的内存地址,2-->值158的内存地址）
# t[0] = 'wife'  # 报错

t = ('老婆', ['凉宫春日', 158])  # t-->(0-->值'老婆'的内存地址,1-->值['凉宫春日', 158]的内存地址）
print(id(t[0]), id(t[1]))  # 2513178927440 2513177609856
# t[0] = 'wife'  # 报错
# t[1] = ['suzumiya haruhi', 158]  # 报错
t[1][0] = 'suzumiya haruhi'  # 可以改
print(t, id(t[0]), id(t[1]))  # ('老婆', ['suzumiya haruhi', 158]) 2513178927440 2513177609856

t = ('老婆', ('凉宫春日', 158))
# t[1][0] = 'suzumiya haruhi'  #报错

# 类型转换：但凡能被for循环遍历的类型都可以当做参数传给tuple()转成元组
print(tuple('suzumiya haruhi'))
print(tuple(['老婆', '凉宫春日', 158]))
print(tuple({'凉宫春日': '老婆', '朝比奈实玖瑠': '女神', '长门有希': '偶像'}))  # ('凉宫春日', '朝比奈实玖瑠', '长门有希')

# 4.内置方法
# 4.1优先掌握
# 4.1.1 按索引取值（正向取+反向取）：只能取
t = ('凉宫春日', '朝比奈实玖瑠', '长门有希')
# 正向取
print(t[0])

# 反向取
print(t[-1])

# 只能取
# t[0] = 'suzumiya haruhi'  # 会报错

# 4.1.2 切片（顾头不顾腚，步长）
t = ('老婆', '凉宫春日', 158, '阿虚', '情敌', '阿', '虚')
print(t[3:])

# 步长
res = t[::2]  # 步长为2，方向0-->
print(res)


# 反向步长
res = t[len(t):0:-1]  # 步长为1,方向len(l)-->0
print(res)

res = t[::-1]  # 倒着写
print(res)

# 4.1.3 长度：len()
t = ('老婆', '凉宫春日', 158, '阿虚', '情敌', '阿', '虚')
print(len(t))

# 4.1.4 成员运算in和not in
name_of_wife = '凉宫春日'
print(name_of_wife in t)
print(name_of_wife not in t)  #少用

# 4.1.5.循环
for element in ('老婆', '凉宫春日', 158):
    print(element)

# 4.1.6.index(),count()  #用法同列表
