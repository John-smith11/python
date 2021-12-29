# 形参:类型提示信息；函数声明->返回值类型提示信息

def register(name:str,age:int=18,hobbies:list=['reading','hiking']) ->int :
    print(name)
    print(age)
    print(hobbies)
    return 11

register('凉宫春日',)
register('凉宫春日',19,['swimming','cooking'])

# 查看提示信息
#{'name': <class 'str'>, 'age': <class 'int'>, 'hobbies': <class 'list'>, 'return': <class 'int'>}
print(register.__annotations__)  