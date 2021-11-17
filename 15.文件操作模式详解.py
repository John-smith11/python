# 已t模式为基础进行内存操作
# 1.r（默认的操作模式）：只读模式，当文件不存在时报错，当文件存在时文件指针跳到开始位置
with open('我与凉宫春日之二三事.txt', mode='rt', encoding='utf-8') as f:
    print('第一次读'.center(50, '*'))
    res=f.read()  # 把文件所有内容从硬盘读入内存
    print(res)

    print('第二次读'.center(50, '*'))
    res1=f.read()  # 指针在文件最后
    print(res1)  # 空

# 案例：
# input_username = input('input name').strip()
# input_password = input('input password').strip()
#
# with open('user.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')  # 凉宫春日：111\n
#         l=line.strip('\n').split(':')  # ['凉宫春日', '111']
#         print(l)
#         username, password = l
#         if input_username == username and input_password == password:
#             print('login successfully')
#             break
#     else:
#         print('your count or password is wrong!')

# 2.w:只写模式，当文件不存在时会创建空文件，当文件存在时会清空文件，指针在文件开头
with open('The story about suzumiya haruhi and me', mode='wt', encoding='utf-8') as f:
    # f.read() 报错，不可读
    f.write('This is a touching love story')
# 强调1：
# 在以w模式打开文件没有关闭的情况下，连续写入，新的内容总是跟在旧的之后
with open('The story about suzumiya haruhi and me', mode='wt', encoding='utf-8') as f:
    f.write('This is a touching love story. ')
    f.write('The chronology is not verifiable.\n')
    f.write('Tradition has it that ...')

# 强调2：
# 如果重新以w模式打开文件，则会清空文件内容
# with open('The story about suzumiya haruhi and me', mode='wt', encoding='utf-8') as f:
#     f.write('This is a touching love story. ')
# with open('The story about suzumiya haruhi and me', mode='wt', encoding='utf-8') as f:
#     f.write('The chronology is not verifiable.\n')
# with open('The story about suzumiya haruhi and me', mode='wt', encoding='utf-8') as f:
#     f.write('Tradition has it that ...')

# 3.a:只追加写，在文件不存在时会创建空文件，当文件存在时，文件指针在直接跳到文件末尾
with open('The story about suzumiya haruhi and me', mode='at', encoding='utf-8') as f:
    # f.read() 报错，不可读
    f.write('This is a touching love story')

#强调 w 模式与 a 模式的异同：
# 1 相同点：在打开的文件不关闭的情况下，连续的写入，新写的内容总会跟在前写的内容之后
# 2 不同点：以 a 模式重新打开文件，不会清空原文件内容，会将文件指针直接移动到文件末尾，新写的内容永远写在最后

# 案列
# name = input('input your name')
# pwd = input('set your password')
#
# with open('user.txt', mode='at',encoding='utf-8') as f:
#     f.write('{}:{}\n'.format(name, pwd))

# 案例：w模式用来创建新的文件
# 文本文件的copy工具

# src_file = input('源文件路径:').strip()
# dst_file = input('目标文件路径').strip()
# with open(r'{}'.format(src_file), mode='rt', encoding='utf-8') as f1,\
#     open(r'{}'.format(dst_file),mode='wt',encoding='utf-8') as f2:
#     res = f1.read()
#     f2.write(res)

# 4.x（了解）:只写模式，不可读，不存在则创建，存在则报错

# 了解：+不能单独使用，必须配合r,w,a
