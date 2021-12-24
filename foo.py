print('==>foo')

__all__=['x','get']

x=1
def get():
    print(x)
def change():
    global x
    x=0
class Foo:
    def func(self):
       print('from the func')

print(__name__)
# 当foo.py被运行时，__name__的值为'__main__'
# 当foo.py被当做模块导入时，__name__的值为‘foo’

# 如下代码实现测试模块的功能
if __name__ == '__main__':
    get()
    change()
else:
    ...