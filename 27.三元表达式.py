# 针对以下需求
def func(x,y):
    if x>y:
        return x
    else:
        return y

res=func(1,2)
print(res)

# 三元表达式
# 语法格式：条件成立时要返回的值 if 条件 else 条件不成立时要返回的值
x=1
y=2
res=x if x>y else y
print(res)  # 2

res= '凉宫春日' if True else 'Suzumiya Haruhi'
print(res)  # 凉宫春日