'''
控制文件读写内容的操作：t和b
    强调：t和b不能单独使用，必须跟r/w/a连用
    t文本（默认的模式）
        1.读写都是以str（Unicode）为单位的
        2.对象是文本文件
        3.必须指定encoding:'utf-8'

    b二进制/bytes
        1.读写都是以bytes为单位的
        2.可以针对所有类型文件
        3.一定不能指定字符编码，即不能指定encoding参数

总结：1、在操作纯文本文件方面t模式帮我们省去了编码与解码的环节，b模式则需要手动编码与解码，所以此时t模式更为方便
     2、针对非文本文件（如图片、视频、音频等）只能使用b模式
'''
# 错误演示：t模式只能读文本文件
# with open('凉宫春日的忧郁.mp4', mode='r') as f:
#     f.read()  # 报错，硬盘中的二进制读入内存-->t模式会将读入内存的二进制进行decode解码，对于非文本文件会报错

# b模式可以读所有文件
# 读视频
with open('凉宫春日的忧郁.mp4', mode='rb') as f:
    res = f.read()  # 硬盘中的二进制读入内存-->b模式会将二进制直接读入内存，不做任何转换
    print(res,type(res))  # bytes类型,python打印显示为16进制数字

# 读文本
with open('我与凉宫春日之二三事.txt', mode='rb') as f:
    res =f.read()  # utf-8的二进制
    print(res)  # bytes类型,python打印显示为16进制数字,英文字符打印显示为英文字符本身

    print(res.decode('utf-8'))

# 案例
# 文件拷贝工具
# src_file = input('源文件路径:').strip()
# dst_file = input('目标文件路径').strip()
# with open(r'{}'.format(src_file), mode='rb') as f1,\
#     open(r'{}'.format(dst_file),mode='wb') as f2:
#     res = f1.read()  # 一次性读入可能导致内存占用过大的问题
#     f2.write(res)

# 循环读取文件的方式
# 方式一：自己指定每次读取的数据量
with open('我与凉宫春日之二三事.txt', mode='rb') as f:
    while True:
        res = f.read(256)  #每次读256个字节
        if len(res) == 0:
            break
        print(res)

# 方式二：以行为单位读，当一行内容过长同样会导致占用内存过大的问题
with open('我与凉宫春日之二三事.txt', mode='rb') as f:
    for line in f:  # 按行取值，遇到\n结束该行
        print(line,len(line))
        
# f.readline()  # 读取一行内容,光标移动到第二行首部
# f.readlines()  # 读取每一行内容,存放于列表中
# f.writelines(['333\n','444\n'])  # 文件模式
# f.writelines([bytes('333\n',encoding='utf-8'),'444\n'.encode('utf-8')]) #b模式

# 了解
# f.readable()  # 文件是否可读
# f.writable()  # 文件是否可读
# f.closed  # 文件是否关闭
# f.encoding  # 如果文件打开模式为b,则没有该属性
# f.flush()  # 立刻将文件内容从内存刷到硬盘
# f.name
with open('我与凉宫春日之二三事.txt', mode='wb') as f:
    # f.readable()  # False
    # f.writable()  # True
    # f.closed  # False
    # f.flush()  # 立刻将文件内容从内存刷到硬盘
