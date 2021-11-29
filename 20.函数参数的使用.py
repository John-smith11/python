# 一、形参与实参介绍
# 形参：在定义函数阶段所定义的参数称为形式参数，简称形参，相当于变量名
def func(x,y):
    ...

# 实参：在调用函数阶段传入的值称为实际参数，简称实参，相当于变量值
fun(1,2)

# 形参与实参的关系：
#   在调用阶段，实参（变量值）会绑定给形参（变量名），此绑定关系只能在函数体内使用
#   实参与形参的绑定关系在函数调用时生效，函数调用结束后解除绑定

# 实参是传入的值，值可以是以下形式：
# 形式一：
# func(1,2)

# 形式二：
# a = 1
# b = 2
#
# func(a,b)

# 形式三：
# func(func1(1,2),func(2,3))
