# 一、int类型
# 1.作用
# 2.定义：
age = 10  # age = int(10)
# 名字（参数），表示某种function（功能、函数）有的有返回值，有的没有
x = int(10)

res = print('凉宫春日'); print(res)

name = input('凉宫春日')

#3.类型转换
 # 3.1 可以把纯数字的字符串转换成int
res = int('1111'); print(res, type(res))
# 3.2（了解）
# 3.2.1 10进制-->其他进制
# 10进制-->2进制
print(bin(11))  # 0b1011

# 10进制-->8进制
print(oct(11))  # 0o13

# 10进制-->16进制
print(hex(111))  # 0x6f

# 3.2.2其他进制-->10进制
# 2进制-->10进制
print(int('0b1011', 2))  # 11

# 8进制-->10进制
print(int('0o13', 8))  # 11

# 16进制-->10进制
print(int('0x6f', 16))  # 11

# 4.使用

# 二、float类型
# 1.作用
# 2.定义
height = 1.58  # height = float(1.58)
# 3.类型转换
res = float('1.58')
print(res, type(res))

# 4.使用
# int与float没有需要掌握的内置方法
# 它们的使用就是数学运算+比较运算

# 补充：复数运算与位运算见知乎