# 时间模块优先掌握的操作
# 一：time
import time

# 时间分为三种格式
# 1.时间戳：从1979到现在经过的秒数
#   作用：用于时间间隔计算
print(time.time())

# 2.按照某种格式显示的时间：2021-12-28 17:16:28 PM
#   作用：用于展示时间
print(time.strftime('%Y-%m-%d %H:%M:%S %p'))  # 2021-12-28 17:16:28 PM
print(time.strftime('%Y-%m-%d %X'))  #2021-12-28 17:16:28

# 结构化时间
#   作用：用于单独获取时间的某一部分
res=time.localtime()
# time.struct_time(tm_year=2021, tm_mon=12, tm_mday=28, tm_hour=17, tm_min=18, tm_sec=43, tm_wday=1, tm_yday=362, tm_isdst=0)
print(res)
print(res.tm_year)  # 2021
print(res.tm_yday)  # 362

# 二：datetime
import datetime
print(datetime.datetime.now())  # 2021-12-29 11:04:13.172087
print(datetime.datetime.now() + datetime.timedelta(days=3))  # 2022-01-01 11:04:13.172087
print(datetime.datetime.now() + datetime.timedelta(weeks=3))  # 2022-01-19 11:04:13.172087

# 需要掌握的操作
# 1.时间格式的转换
# struct_time->时间戳
import time
s_time=time.localtime()
print(time.mktime(s_time))  # 1640748015.0

# 时间戳->struct_time
tp_time = time.time()
# time.struct_time(tm_year=2021, tm_mon=12, tm_mday=29, tm_hour=11, tm_min=20, tm_sec=15, tm_wday=2, tm_yday=363, tm_isdst=0)
print(time.localtime(tp_time))  # 本地时间，
# time.struct_time(tm_year=2021, tm_mon=12, tm_mday=29, tm_hour=3, tm_min=20, tm_sec=15, tm_wday=2, tm_yday=363, tm_isdst=0)
print(time.gmtime(tp_time))  # 世界标准时间，

# struct_time->格式化的字符串形式的时间
s_time = time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S',s_time))  # 2021-12-29 11:26:26

# 格式化的字符串形式的时间->struct_time
# time.struct_time(tm_year=2021, tm_mon=12, tm_mday=29, tm_hour=11, tm_min=11, tm_sec=11, tm_wday=2, tm_yday=363, tm_isdst=-1)
print(time.strptime('2021-12-29 11:11:11','%Y-%m-%d %H:%M:%S'))

# format string与timestamp格式不能直接相互转换，需要先装换成struct_time格式

# 休眠
time.sleep(3)