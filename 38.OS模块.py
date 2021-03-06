# os模块是与操作系统交互的一个接口

# os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径

# os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd

# os.curdir  返回当前目录: ('.')

# os.pardir  获取当前目录的父目录字符串名：('..')

# os.makedirs('dirname1/dirname2')    可生成多层递归目录

# os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推

# os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname

# os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname

# os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印

# os.remove()  删除一个文件

# os.rename("oldname","newname")  重命名文件/目录

# os.stat('path/filename')  获取文件/目录信息

# os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"

# os.linesep    输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"

# os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:

# os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'

# os.system("bash command")  运行shell命令，直接显示

# os.environ  获取系统环境变量

# os.path.abspath(path)  返回path规范化的绝对路径

# os.path.split(path)  将path分割成目录和文件名二元组返回

# os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素

# os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素

# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False

# os.path.isabs(path)  如果path是绝对路径，返回True

# os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False

# os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False

# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略

# os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间

# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间

# os.path.getsize(path) 返回path的大小

# 特别的
import os
# 获取某个文件夹下所有的子文件和子文件夹名字
# 当前文件夹下：
res = os.listdir('.')
print(res)

# 获取文件大小,单位：字节
print(os.path.getsize('.'))  # 8192

# os.remove()
# os.rename()

# os.system(命令)  代替在shell中的操作
# 如查看某个文件夹下的文件名
# os.system(r'dir D:\\')

# sys.path 导模块时使用

# 往系统环境的字典中增加元素，key与value必须都是字符串
# os.environ['key':'value']
# print(os.environ)

# os.path.系列
print(__file__)  # E:/ML/document/python course/38.OS模块.py
print(os.path.abspath(__file__))  # E:\ML\document\python course\38.OS模块.py

# 把最后一级与前面的路径分开
res = os.path.split(r'C:\\d\\e\\f.txt')
print(res)  # ('C:\\\\d\\\\e', 'f.txt')

print(os.path.dirname(r'C:\\d\\e\\f.txt'))  # C:\\d\\e
print(os.path.basename(r'C:\\d\\e\\f.txt'))  # f.txt

# 判断是否为绝对路径
print(os.path.isabs(r'C:\\d\\e\\f.txt'))  # True

# 判断是否是一个处在的文件
print(os.path.isfile(r'C:\\d\\e\\f.txt'))  # False

# 路径拼接，从根目录开始
print(os.path.join('a','C:','d','e','f'))  # C:d\e\f

# 规范化路径
print(os.path.normpath('c://windows\\System32\\../Temp/'))  # c:\windows\Temp

# 获取上一级目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)
# 或
p = os.path.join(
    __file__,
    '..',
    '..'
)
BASE_DIR = os.path.normpath(p)

# python3.5之后可以用pathlib
from pathlib import Path

res = Path(__file__).parent.parent
print(res)

res.resolve()  # 效果同os.path.normpath()
