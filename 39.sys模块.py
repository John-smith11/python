# sys.argv           命令行参数List，第一个元素是程序本身路径
# sys.exit(n)        退出程序，正常退出时exit(0)
# sys.version        获取Python解释程序的版本信息
# sys.maxint         最大的Int值
# sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform       返回操作系统平台名称

# 特别的,sys.argv
import sys
# 命令行输入：python run.py 1 2 3
# 用于给py文件传参，sys.argv获取解释器后参数值
# print(sys.argv)  # ['run.py', '1', '2', '3']

# 案例：copy文件
import sys
src_file = sys.argv[1]
dst_file = sys.argv[2]

with open(r'%s' %src_file,mode=rb) as read_f,\
    open(r'%s' %dst_file,mode='wb') as write_f :
    for line in read_f:
        write_f.write(line)