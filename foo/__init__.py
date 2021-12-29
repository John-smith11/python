# 绝对导入，以包的文件夹作为起始来进行导入，更通用
# from foo.m1 import f1
# from foo.m2 import f2
# from foo.m3 import f3
# from foo.bbb.m4 import f4

# 相对导入:仅限于包内使用，不能跨出包（包内模块之间的导入，推荐使用相对导入）
# . 代表当前文件夹
# .. 代表上一层文件夹
# ...再上一层文件夹，以此类推
from .m1 import f1
from .m2 import f2
from .m3 import f3
from .bbb.m4 import f4