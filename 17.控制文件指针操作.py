# 指针移动都是以字节为单位
# 只有一种特殊情况：
#   t模式下的read（n）,n代表的是字符个数
# with open('我与凉宫春日之二三事.txt', mode='rt', encoding='utf-8') as f:
#     res=f.read(6)
#     print(res)

# f.seek(n,模式)：n指的是移动的字节数
# 模式：0，1,2
# 模式0：基准为文件开头
# f.seek(9, 0)  # 9
# f.seek(2, 0)  # 2

# 模式1：基准为当前指针所在位置
# f.seek(9, 1)  # pisition+9
# f.seek(2, 1)  # pisition+9+2

# 模式2：基准为文件末尾，要反向移动
# f.seek(-9, 2)  # 倒数9
# f.seek(-2, 2)  # 倒数2

# 强调：在t模式下只有0模式可以使用，1模式和2模式只能在b模式使用

# f.tell()  # 获取文件指针当前的位置

# 案例：
# a.txt用utf-8编码，内容如下（abc各占1个字节，中文“你好”各占3个字节）
# abc你好

# 0模式的使用
# with open('a.txt',mode='rt',encoding='utf-8') as f:
#     f.seek(3,0)     # 参照文件开头移动了3个字节
#     print(f.tell()) # 查看当前文件指针距离文件开头的位置，输出结果为3
#     print(f.read()) # 从第3个字节的位置读到文件末尾，输出结果为：你好
#     # 注意：由于在t模式下，会将读取的内容自动解码，所以必须保证读取的内容是一个完整中文数据，否则解码失败

# with open('a.txt',mode='rb') as f:
#     f.seek(6,0)
#     print(f.read().decode('utf-8')) #输出结果为: 好

# 1模式的使用
# with open('a.txt',mode='rb') as f:
#     f.seek(3,1) # 从当前位置往后移动3个字节，而此时的当前位置就是文件开头
#     print(f.tell()) # 输出结果为：3
#     f.seek(4,1)     # 从当前位置往后移动4个字节，而此时的当前位置为3
#     print(f.tell()) # 输出结果为：7


# 2模式的使用
# with open('a.txt',mode='rb') as f:
#     f.seek(0,2)     # 参照文件末尾移动0个字节， 即直接跳到文件末尾
#     print(f.tell()) # 输出结果为：9
#     f.seek(-3,2)     # 参照文件末尾往前移动了3个字节
#     print(f.read().decode('utf-8')) # 输出结果为：好

# 小练习：实现动态查看最新一条日志的效果
# import time
# with open('access.log',mode='rb') as f:
#     f.seek(0,2)
#     while True:
#         line=f.readline()
#         if len(line) == 0:
#             # 没有内容
#             time.sleep(0.5)
#         else:
#             print(line.decode('utf-8'),end='')