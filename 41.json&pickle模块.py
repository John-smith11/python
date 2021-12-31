# 作用：序列化
# 什么是序列化？
# 我们把对象(变量)从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

# 为什么要序列化？
# 1：持久保存状态
#
# 2：跨平台数据交互
# 序列化之后，不仅可以把序列化后的内容写入磁盘，还可以通过网络传输到别的机器上，
# 如果收发的双方约定好实用一种序列化的格式，那么便打破了平台/语言差异化带来的限制，实现了跨平台数据交互。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

import json
dic = {'a':1}
x = None

res1 = json.dumps(dic)
res2 = str(dic)
print(res1,type(res1))  # {"a": 1} <class 'str'>
print(res2,type(res2))  # {'a': 1} <class 'str'>

print(json.dumps(x),type(json.dumps(x)))  # null <class 'str'>

# 序列化，把内存数据存储成中间文件json.dumps(),json.dump()
import json
user={'name':'凉宫春日','age':18,'is wife':True}
# with open('user.json','w',encoding='utf-8') as f:
#     f.write(json.dumps(user))
json.dump(user,open('user.json','w',encoding='utf-8'))

# 反序列化，读出中间文件中的数据json.loads(),json.load()
import json

# with open('user.json','r',encoding='utf-8') as f:
#     user = json.loads(f.read())
#     print(user)
user = json.load(open('user.json','r',encoding='utf-8'))
print(user)  # {'name': '凉宫春日', 'age': 18, 'is wife': True}

# pickle
# json适用于大部分python的数据类型（dict,list,str,int/float,True/False,None），仍有少部分不适用
# pickle适用所有python数据类型，但Pickle的问题和所有其他编程语言特有的序列化问题一样，
# 就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
# json序列化的结果是字符串，pickle序列化结果是bytes

# pickle序列化
import pickle

s={'凉宫春日',}
# print(pickle.dumps(s))  # b'\x80\x04\x95\x14\x00\x00\x00\x00\x00\x00\x00\x8f\x94(\x8c\x0c\xe5\x87\x89\xe5\xae\xab\xe6\x98\xa5\xe6\x97\xa5\x94\x90.'

# with open('s.pkl','wb') as f:
#     f.write(pickle.dumps(s))

pickle.dump(s,open('s.pkl','wb'))

# pickle反序列化
import pickle

# with open('s.pkl','rb') as f:
    # s=pickle.loads(f.read())
    # print(s,type(s))

s = pickle.load(open('s.pkl','rb'))
print(s,type(s))  # {'凉宫春日'} <class 'set'>

# 其他
# shelve
# shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，可读可写;key必须为字符串，而值可以是python所支持的数据类型
import shelve
# 存
f=shelve.open('db.shl')
f['frd1'] = {'name':'凉宫春日','age':18}
f['frd2'] = {'name':'长门有希','age':19}
# 取
print(f['frd1']['name'])
f.close()

# xml
# xml是实现不同语言或程序之间进行数据交换的协议，跟json差不多，但json使用起来更简单，
# 不过，古时候，在json还没诞生的黑暗年代，大家只能选择用xml呀，至今很多传统公司如金融行业的很多系统的接口还主要是xml。

# configparser(见博客)

