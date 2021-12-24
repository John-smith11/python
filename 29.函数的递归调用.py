# 函数的递归调用：是函数嵌套调用的一种形式
# 具体是是指：
#          在调用一个函数的过程中有直接或者间接的调用到本身

# 直接调用本身
# def f1:
#     print('是我是我还是我')
#     f1()
#
# f1()

# 间接调用本身
# def f1:
#     print('===>f1')
#     f2()
#
# def f2:
#     print('===>f2')
#     f1()
#
# f1()

# 递归调用的本质是循环
# 递归调用不应该无限地调用下去，必须在满足某种条件下结束递归调用

# 用递归调用实现while循环
# while True:
#     print('凉宫春日')
#     print('长门有希')
#
# def f1(x):
#     if x:
#         print('凉宫春日')
#         print('长门有希')
#         f1(x)
#
# f1(True)

# n=0
# while n<10:
#     print(n)
#     n += 1
#
# def f1(n):
#     if n >= 10:
#         return
#     print(n)
#     n += 1
#     f1(n)
#
# f1(0)

# 递归的两个阶段
# 回溯：一层一层调用下去
# 递推：满足某种结束条件，结束递归调用，然后一层一层返回

# 列：年龄推算
# age(5)=age(4)+10
# age(4)=age(3)+10
# age(4)=age(2)+10
# age(2)=age(1)+10
# age(1)=18

def age(n):
    if n == 1:
        return 18
    return age(n-1) + 10

res = age(5)
print(res)  # 58

# 递归的应用：打印l中的所有数字
l = [1,2,[3,[4,[5,[6,7,[8,[9,10,[11,]]]]]]]]

def f1(list1):
    for x in list1:
        if type(x) is list:
            # 如果是列表，应该再循环、再判断，即重新运行原来的代码
            f1(x)
        else:
            print(x)

f1(l)
