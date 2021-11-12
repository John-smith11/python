# 1.作用
# 1.1 关系运算
friends1 = ['凉宫春日', '朝比奈实玖瑠', '长门有希', '阿虚']
friends2 = ['碳治郎', '善逸', '伊之助', '阿虚']
# 找共同好友
# 一般方法
com_friends = []
for friend in friends1:
    if friend in friends2:
        com_friends.append(friend)
print(com_friends)  # ['阿虚']

# 1.2 去重(了解），利用集合内的元素不能重复的特点

# 2.定义：在{}内用逗号分隔开多个元素，多个元素满足一下三个条件
#           1.集合内的元素必须为不可变元素
#           1.集合内的元素无序
#           1.集合内的元素不能重复
s = {'凉宫春日', '朝比奈实玖瑠', '长门有希'}  # s=set({'凉宫春日', '朝比奈实玖瑠', '长门有希'} )

# s ={'凉宫春日', ['朝比奈实玖瑠', '长门有希']}   # 有可变元素报错

print({'凉宫春日', '朝比奈实玖瑠', '长门有希'})  # {'朝比奈实玖瑠', '凉宫春日', '长门有希'} 无序

s = {'凉宫春日', '凉宫春日', '朝比奈实玖瑠', '长门有希'}
print(s)  # {'朝比奈实玖瑠', '凉宫春日', '长门有希'}

# 了解
s = {}  # 默认是创建空字典
print(type(s))  # <class 'dict'>
# 定义空集合
s = set()
print(s, type(s))  # set() <class 'set'>

# 3.类型转换
set({'凉宫春日', '朝比奈实玖瑠', '长门有希'})
print(set('凉宫春日 凉宫春日 '))  # {'日', '春', '宫', '凉', ' '}

print(set(['凉宫春日', '朝比奈实玖瑠', '长门有希']))  # {'凉宫春日', '长门有希', '朝比奈实玖瑠'}

# print(set(['凉宫春日', ['朝比奈实玖瑠', '长门有希']]))  # 报错

print(set({"k1": '凉宫春日', 'k2': '朝比奈实玖瑠', 'k3': '长门有希'}))  # {'k2', 'k1', 'k3'}

# 4.内置方法
friends1 = {'凉宫春日', '朝比奈实玖瑠', '长门有希', '阿虚'}
friends2 = {'碳治郎', '善逸', '伊之助', '阿虚'}


# 4.1 取交集：共同好友
res = friends1 & friends2
print(res)  # {'阿虚'}

res = friends1.intersection(friends2)  # 求交集的内置方法
print(res)  # {'阿虚'}

# 4.2 取并集：所有好友
print(friends2 | friends1)  # {'碳治郎', '凉宫春日', '善逸', '长门有希', '阿虚', '伊之助', '朝比奈实玖瑠'}
print(friends2.union(friends1))  # 内置方法 {'碳治郎', '凉宫春日', '善逸', '长门有希', '阿虚', '伊之助', '朝比奈实玖瑠'}

# 4.3 做差：取friends1独有的好友
print(friends1 - friends2)  # {'朝比奈实玖瑠', '长门有希', '凉宫春日'}
print(friends2 - friends1)  # 取friends2独有的好友

print(friends1.difference(friends2))  # 内置方法
print(friends2.difference(friends1))

# 4.4 对称差集：去掉共同好友
print((friends1 - friends2) | (friends2 - friends1))  # {'朝比奈实玖瑠', '伊之助', '凉宫春日', '善逸', '长门有希', '碳治郎'}
print(friends2 ^ friends1)  # 功能同上

print(friends2.symmetric_difference(friends1))  # 内置方法


# 4.5 集合与其子集：包含关系
friends3 = {'凉宫春日', '朝比奈实玖瑠', '长门有希'}
friends4 = {'凉宫春日', '朝比奈实玖瑠', '长门有希'}
friends5 = {'碳治郎', '善逸', '伊之助'}
# print(friends1 > friends3)  # True，friends3是friends1的真子集，
# # 内置方法friends1.issupset(friend3)或者friends3.issubset(friends1)
#
# print(friends1 >= friends1)  # True，friends1是friends1的子集
# print(friends1 > friends2)  # False，friends2不是friends1的真子集
# print(friends1 < friends2)  # False，friends1不是friends2的真子集
# print(friends3 == friends4)  # 判断两个集合是否相同
print(friends5.isdisjoint(friends4) )  #两集合交集为空则返回True

# 其他
s = {'凉宫春日', '朝比奈实玖瑠', '长门有希', '阿虚'}
s1 = { '朝比奈实玖瑠', '长门有希'}
s.remove('阿虚')  # 删除指定元素，若元素不存在则报错
s.discard('阿虚')  # 删除指定元素，若元素不存在什么都不做
s.add('阿虚')  # 添加元素
s.pop()  # 随机删除一个元素

# s_diff = s.difference(s1)
# s = s_diff
# print(s)
s = s.difference_update(s1)  # 一行代码实现上面的功能
print(s)