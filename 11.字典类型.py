# 字典：key对应值，其中key通常为字符串，key对值有描述性功能

# 1.作用：用来存多个值，每个值都有唯一的key与其对应

# 2.定义：在{}内用逗号分隔开多个key：value,按key取值
# value可以是任意类型，key必须是不可变类型且不能重复
d = {'k1': 111,('k2', 'k3'): 222}  # d = dict( {'k1': 111,('k2', 'k3'): 222})
print(type(d))  # <class 'dict'>
print(d['k1'])
print(d[('k2', 'k3')])

# 造字典的另一种方法
d = dict(老婆 = '凉宫春日', 身高 = 158)  # 此处key是参数名，不需要加引号
print(d)  # {'老婆': '凉宫春日', '身高': 158}

# 3.数据类型转换
info = [
    ['name', 'suzumiya haruhi'],
    ['height', 158],
    ['gender', 'female']
]
d = {}
for item in info:
    print(item)
    d[item[0]] = item[1]
print(d)  # {'name': 'suzumiya haruhi', 'height': 158, 'gender': 'female'}

# 解压操作
for k,v in info:  # 第一次，k,v = ['name', 'suzumiya haruhi']
    d[k] = v
print(d)  # {'name': 'suzumiya haruhi', 'height': 158, 'gender': 'female'}

# 一行代码搞定上述for循环操作
res = dict(info)
print(res)  # {'name': 'suzumiya haruhi', 'height': 158, 'gender': 'female'}

# 快速初始化字典：例如造初始value为None的字典
keys = ['name', 'height', 'gender']
d = {}.fromkeys(keys, None)
print(d)  # {'name': None, 'height': None, 'gender': None}

# 4.内置方法
# 4.1优先掌握
# 4.1.1 按key存取值：可存可取
d = {'老婆': '凉宫春日', '身高': 158}
# 可以取也可以改:key存在则修改对应的value，key不存在则创建新键值对
d['老婆'] = 'suzumiya haruhi'
d['性别'] = 'female'
print(d)

# 4.1.3 长度：len()
d = {'老婆': '凉宫春日', '身高': 158}
len(d)

# 4.1.4 成员运算in和not in:判断对象为key
d = {'老婆': '凉宫春日', '身高': 158}
print('老婆' in d)  # True
print('凉宫春日' in d)  # False

# 4.1.5.删除
# 方式一：通用方法，没有返回值
d = {'老婆': '凉宫春日', '身高': 158}
del d['老婆']
print(d)

# 方式二：pop删除:根据key删除，有返回值，返回删除key对应的那个value值
d = {'老婆': '凉宫春日', '身高': 158}
res = d.pop('老婆')
print(d)  # {'身高': 158}
print(res)  # 凉宫春日

# 方式三：popitem删除:随机删除，有返回值，返回删除的key：value
d = {'老婆': '凉宫春日', '身高': 158}
res = d.popitem()
print(res)  # ('身高', 158)

# 4.1.6 键keys(),值values(),键值对items()==>在python3中得到的是“老母鸡”
d = {'老婆': '凉宫春日', '身高': 158}
print(d.keys())  # dict_keys(['老婆', '身高'])
print(d.values())  # dict_values(['凉宫春日', 158])
print(d.items())  # dict_items([('老婆', '凉宫春日'), ('身高', 158)])

# 4.1.7 for循环
d = {'老婆': '凉宫春日', '身高': 158}
for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for item in d.items():
    print(item)

print(d.keys())
print(d.values())
print(d.items())

# 需要掌握的其他内置方法:clear,update,get,setdefault
d = {'老婆': '凉宫春日', '身高': 158}
d.clear()  # 清空
print(d)  # {}

d = {'老婆': '凉宫春日', '身高': 158}  #更新前
d1 = {'老婆': '凉宫春日', '身高':1.58, '性别': 'female'}
d.update(d1)  # 更新,将d1中的新元素更新到d中，对于key相同的，按d1的新值更新老字典d的旧值
print(d)  # 更新后，{'老婆': '凉宫春日', '身高': 1.58, '性别': 'female'}

d = {'老婆': '凉宫春日', '身高': 158}
print(d['老婆'])
print(d.get('老婆'))  # key存在与一般方法取值一致
# print(d['wife'])  # key不存在，则报错
print(d.get('wife'))  # key不存在，不报错，返回None，容错性好

# .setdefault():对于key，实现有则不改，无则添加。返回执行setdefault后字典中key对应的值
d = {'老婆': '凉宫春日', '身高': 158}
res = d.setdefault('老婆', 'suzumiya haruhi')  # 不变
print(d)  # {'老婆': '凉宫春日', '身高': 158}
print(res)  # 凉宫春日
d.setdefault('身高', 1.58)  # 不变
print(d)  # {'老婆': '凉宫春日', '身高': 158}
res = d.setdefault('性别', 'female')  # 改了
print(d)  # {'老婆': '凉宫春日', '身高': 158, '性别': 'female'}
print(res)  # female




