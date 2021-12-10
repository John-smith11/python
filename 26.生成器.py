# 生成器
# 如何得到自定义的迭代器：
# 在函数内一旦存在yield关键字，调用函数并不会执行函数体代码
# 会返回一个生成器对象，生成器即自定义的迭代器
def func():
    print('第一段代码')
    yield '凉宫春日'
    print('第二段代码')
    yield '长门有希'
    print('第三段代码')
    yield '朝比奈实玖瑠'
    print('第四段代码')

g = func()
print(g)  # <generator object func at 0x000002728ED1D890>
# 生成器就是迭代器
# g.__iter__()
# g.__next__()

# 会触发函数体代码的运行,然后遇到yield停下来,将yield后的值当做本次调用的结果返回
# res1=g.__next__()  # 第一段代码
# print(res1)  # 凉宫春日
#
# res2=g.__next__()  # 第一段代码
# print(res2)  # 凉宫春日
#
# res3=g.__next__()  # 第一段代码
# print(res3)  # 凉宫春日
#
# res4=g.__next__()  # 第四段代码，异常：StopIteration

# 函数与方法
# len('凉宫春日')
# '凉宫春日'.__len__()
#
# iter(g)
# g.__iter__()
#
# next(g)
# g.__next__()

# 应用案例
def my_range(start,stop,step):
    while start < stop:
        yield start
        start += step

g = my_range(1,5,2)
print(next(g))  # 1
print(next(g))  # 3
# print(next(g))  # StopIteration

for n in my_range(1,7,2):
    print(n)  #1  3  5

# yield表达式
# x=yied 返回值
# 一：
def boy(boy_name):
    print('%s脱单啦'%boy_name)
    while True:
        # girl_name拿到的是g send给yield的值
        girl_name = yield
        print('%s的女朋友是%s'%(boy_name,girl_name))

g=boy('PS')
# next(g)  # PS脱单啦
g.send(None)  # PS脱单啦，等同于next(g)
g.send('凉宫春日')  # PS的女朋友是凉宫春日，把'凉宫春日'给yield然后传给girl_name，再运行接下来的代码直到再次遇到yield
g.send(['凉宫春日','Suzumiya Haruhi'])  # PS的女朋友是['凉宫春日', 'Suzumiya Haruhi']
g.send('一歧日和')  # PS的女朋友是一歧日和，把'一歧日和'给yield然后传给girl_name，再运行接下来的代码直到再次遇到yield
g.send('灶门祢豆子')  # PS的女朋友是灶门祢豆子，把'灶门祢豆子'给yield然后传给girl_name，再运行接下来的代码直到再次遇到yield
g.close()  # 关闭
# g.send('一个女的')  # StopIteration

# 二：
def boy(boy_name):
    girl_friend_list=[]
    print('%s脱单啦'%boy_name)
    while True:
        # girl_name拿到的是g send给yield的值
        girl_name = yield girl_friend_list
        print('%s的女朋友是%s'%(boy_name,girl_name))
        girl_friend_list.append(girl_name)

g=boy('PS')
res=g.send(None)  # PS脱单啦
print(res)  #[]

res=g.send(['凉宫春日','Suzumiya Haruhi'])  # PS的女朋友是['凉宫春日', 'Suzumiya Haruhi']
print(res)  #[['凉宫春日', 'Suzumiya Haruhi']]

g.send('一歧日和')  # PS的女朋友是一歧日和，把'一歧日和'给yield然后传给girl_name，再运行接下来的代码直到再次遇到yield
print(res)  #[['凉宫春日', 'Suzumiya Haruhi'], '一歧日和']
