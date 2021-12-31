# 用作文件处理
import shutil

# shutil.copyfileobj(fsrc, fdst[, length])
# 将文件内容拷贝到另一个文件中
shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))

# shutil.copyfile(src, dst)
# 拷贝文件
shutil.copyfile('f1.log', 'f2.log') #目标文件无需存在

# shutil.copymode(src, dst)
# 仅拷贝权限。内容、组、用户均不变
shutil.copymode('f1.log', 'f2.log') #目标文件必须存在

# shutil.copy(src, dst)
# 拷贝文件和权限
shutil.copy('f1.log', 'f2.log')

# shutil.copy2(src, dst)
# 拷贝文件和状态信息
shutil.copy2('f1.log', 'f2.log')

# shutil.ignore_patterns(*patterns)
# shutil.copytree(src, dst, symlinks=False, ignore=None)
# 递归的去拷贝文件夹
shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*')) #目标目录不能存在，注意对folder2目录父级目录要有可写权限，ignore的意思是排除

shutil.copytree('f1', 'f2', symlinks=True, ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
'''
通常的拷贝都把软连接拷贝成硬链接，即对待软连接来说，创建新的文件
'''

# shutil.rmtree(path[, ignore_errors[, onerror]])
# 递归的去删除文件
shutil.rmtree('folder1')

# shutil.move(src, dst)
# 递归的去移动文件，它类似mv命令，其实就是重命名。
shutil.move('folder1', 'folder3')
'''
shutil.make_archive(base_name, format,...)

创建压缩包并返回文件路径，例如：zip、tar

创建压缩包并返回文件路径，例如：zip、tar

    base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
    如 data_bak                       =>保存至当前路径
    如：/tmp/data_bak =>保存至/tmp/
    format： 压缩包种类，“zip”, “tar”, “bztar”，“gztar”
    root_dir： 要压缩的文件夹路径（默认当前目录）
    owner： 用户，默认当前用户
    group： 组，默认当前组
    logger： 用于记录日志，通常是logging.Logger对象

'''
#将 /data 下的文件打包放置当前程序目录
ret = shutil.make_archive("data_bak", 'gztar', root_dir='/data')
#将 /data下的文件打包放置 /tmp/目录
ret = shutil.make_archive("/tmp/data_bak", 'gztar', root_dir='/data')

# shutil 对压缩包的处理是调用 ZipFile 和 TarFile 两个模块来进行的，详细：
import zipfile

# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('a.log')
z.write('data.data')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall(path='.')
z.close()

