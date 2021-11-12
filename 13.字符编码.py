# 结论
'''
1.内存固定使用Unicode，我们可以改变的是存入硬盘采用格式
             内存            硬盘
        英文  -->Unicode--> ASCII
    英文，汉字 -->Unicode--> GBK
    英文，日文 -->Unicode--> shift-jis

2.文本文件存取乱码问题
    存乱了：解决方法是，编码格式应该设置成支持文件内字符的格式
    取乱了：解决方法是，文件是以什么编码格式存入硬盘的，就应该以什么编码格式读入内存

3.python解释器默认读文件的编码
    python2默认：ASCII
    python3默认：utf-8

4.保证运行python程序前两个阶段不乱码的核心法则：
    指定文件头
    # coding:文件当初存入硬盘所采用的编码格式
    如：#coding:GBK

5.python3的str类型默认直接存成Unicode格式，无论如何都不会乱码
  保证python2的str类型不乱码,在字符串前加u,如：x = u'凉宫春日'

6.了解：
    python2解释器有两种字符串类型：str, Unicode
    # str类型
    x = '凉宫春日'  # 字符串会按照文件头指定的编码格式存入变量值的内存空间
    # Unicode类型
    x = u'凉宫春日'  # 强制存成Unicode

    python3中编码与解码：
    x = '凉宫春日'
    res = x.encode('gbk')  #编码 Unicode-->gbk
    print(res)
    x = res.decode('gbk')  #解码
    print(x)

'''