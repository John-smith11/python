# 1.while 语法与基本使用
'''
while 条件：
    代码块
'''

count = 0

while count <5 :  #条件成立进入循环
    print(count)
    count += 1
print('发射')

# 2.死循环与效率问题
# 纯计算无IO的死循环会导致致命的效率问题

# 3.循环的应用
# 两个问题
# 1.重复调用
# 2.输对了不要再重复

NAME = '凉宫春日'
HEIGHT = '158'
tag = True
while tag:
    name_of_wife = input('please inpt your name')
    height_of_wife = input('please inpt your height')

    if name_of_wife == NAME or height_of_wife == HEIGHT:
        print('宝')
        tag = False
    else:
        print('you are not my wife, please input your name and height again')

# 4、退出循环的两种方式
# 方式一：将条件改成假，等到下次循环判断条件时才会生效
# 方式二：break，只要运行到break就会终止本层循环
while True:
    name_of_wife = input('please inpt your name')
    height_of_wife = input('please inpt your height')

    if name_of_wife == NAME or height_of_wife == HEIGHT:
        print('宝')
        break  # 立刻终止本层循环
    else:
        print('you are not my wife, please input your name and height again')

# 5.while循环的嵌套
# 体会如下两种方式退出循环的不同
'''
while True:
    while True:
        while True:
            break
        break
    break
'''

'''
tag = True
while tag:
    while tag:
        while tag:
            tag = False

'''

# 6.while + continue：结束本次循环，直接进入下一次
# 在continue之后添加同级代码毫无意义，因为该代码永远无法运行

count = 0

while count <5 :
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

# 7.while + else
count = 0

while count <5 :
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1
else:
    print('else包含的代码块会在while循环结束后，'
          '并且while循环是在没有被break打断的情况下正常结束的，才会运行')
# 应用案例
NAME = '凉宫春日'
HEIGHT = '158'
count = 0
while count < 3:
    name_of_wife = input('please inpt your name')
    height_of_wife = input('please inpt your height')

    if name_of_wife == NAME or height_of_wife == HEIGHT:
        print('宝')
        break
    else:
        print('you are not my wife, please input your name and height again')
        count += 1
else:
    print('你已输错三次，告辞')