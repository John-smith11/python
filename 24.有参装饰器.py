# 无参装饰器的局限性
# 由于语法糖@的限制，outter函数只能有一个参数，并且该参数只能用来接收被装饰对象的内存地址
# def outter(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         res = func(*args,**kwargs)
#         stop = time.time()
#         print(stop-start)
#         return res
#     return wrapper
#
# @outter  # index = outer(index)
# def index(x,y):
#     time.sleep(3)
#     print('index %s %s' % (x,y))
#     return '凉宫春日'

# 实现一个用来为被装饰对象添加认证功能的装饰器
# def auth(func):
#     def wrapper(*args,**kwargs):
#         name = input('your name>>>:').strip()
#         pwd = input('your password>>>:').strip()
#         if name == '凉宫春日' and pwd == '123456':
#             print('login successfully')
#             res = func(*args,**kwargs)
#             return res
#     return wrapper
#
# @auth
# def index(x,y):
#     print('index-->>%s:%s' %(x,y))
#
# index(1,2)

# 如果我们想提供多种不同的认证方式以供选择，单从wrapper函数的实现角度改写如下
def auth(driver):
    def deco(func):
        def wrapper(*args, **kwargs):
            if driver == 'file':
                # 编写基于文件的认证, 认证通过则执行
                res = func(*args, **kwargs)
                return res
            elif driver == 'mysql':
                # 编写基于mysql认证, 认证通过则执行
                res = func(*args, **kwargs)
                return res

        return wrapper
    return deco

# 调用
@auth(driver='file')  # @deco # index=deco(index)  # index=wrapper
def index():
    pass

@auth(driver='mysql')
def home():
    pass

# 总结有参装饰器模板
def 有参装饰器(x,y,z):
    def outter(func):
        def wrapper(*args,**kwargs):
            # 1.调用原函数
            # 2.为其增加新功能
            res = func(*args,**kwargs)
            return res
        return wrapper
    return outter

@有参装饰器(1,2,y=3)
def 被装饰对象():
    pass