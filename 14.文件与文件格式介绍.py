# 1.什么是文件
# 文件是操作系统提供给用户/应用程序操作硬盘的一种虚拟的概念/接口
# 2.如何用文件：open()
#     2.1 控制文件读写内容的操作：t和b
#     强调：t和b不能单独使用，必须跟r/w/a连用
#     t文本（默认的模式）
#         1.读写都是以str（Unicode）为单位的
#         2.对象是文本文件
#         3.必须指定encoding:'utf-8'
#
#     b二进制/bytes
#
#     2.2 控制文件读写的操作模式
#         r只读模式
#         w只写模式
#         a只追加写模式
#         +：r+,w+,a+

# 3.文件操作的基本流程
# 3.1 打开文件
# Windows下分隔符问题
# open('d:\a\nb\我与凉宫春日之二三事.txt')  # '\'在字符串中存在转义符的问题，如'\n'表示换行
# 解决方案一：推荐
# open(r'd:\a\b\我与凉宫春日之二三事.txt')  # 'r'表示rawstring
# 解决方案二：
# open('d:/a/nb/我与凉宫春日之二三事.txt')  # 同Linux

# 相对路径
f = open('我与凉宫春日之二三事.txt', mode='rt')  # 与当前py文件同在一个文件夹,mode默认即为'rt'
print(f)  # <_io.TextIOWrapper name='我与凉宫春日之二三事.txt' mode='r' encoding='cp936'>
# 干了两件事：创建对象，申请一片内存空间；向操作系统发出系统调用，读取硬盘中的对应文件

# 2.文件操作：读/写文件
# 应用程序对文件的读写都是向操作系统发出系统调用，由操作系统控制把硬盘数据读入内存或把内存数据写入硬盘
res = f.read()
print(res)
# 3，关闭文件
f.close()  # 回收操作系统中的占用
print(f)  # 应用程序内存中变量f仍然存在
f.read()  # 但不能在进行读写操作
# del f  # 回收应用程序中内存占用，由Python垃圾回收机制自动实现

# 没有指定encoding参数操作系统会使用自己默认的编码
# Linux，Mac系统默认utf-8
# Windows默认gbk
f = open('我与凉宫春日之二三事.txt', mode='rt',encoding='utf-8')
res = f.read()
print(res)
f.close()

# with上下文管理：可以省掉f.close()操作
# 文件对象又称文件句柄
with open('我与凉宫春日之二三事.txt', mode='rt',encoding='utf-8') as f1:  # 功能同f1=open('a.txt', mode='rt')
    res = f1.read()
    print(res)
    f.write('凉宫春日')
# 打开多个
# with open('a.txt', mode='rt',encoding='utf-8') as f1, \
#     open('a.txt', mode='rt', encoding='utf-8') as f1:
#     res1 = f1.read()
#     res2 = f2.read()
#     print(res1)
#     print(res2)
