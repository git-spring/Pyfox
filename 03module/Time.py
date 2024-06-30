# time

import time


# 获取当前时间戳
time.time()
# 线程睡眠指定秒
time.sleep(1)
# 接收秒级时间戳,返回一个时间元组(本地时间)   gmtime   伦敦时间
struct = time.localtime()   # time.struct_time(tm_year=2020, tm_mon=11, tm_mday=30, tm_hour=9, tm_min=37, tm_sec=18, tm_wday=0, tm_yday=335, tm_isdst=0)
# 接收秒级时间戳,返回一个可读的时间形式
time.asctime(struct)    # Mon Nov 30 09:37:18 2020
# 作用与 asctime 类似,可以接收时间戳,没有参数的话,默认是当前时间
time.ctime()        # Mon Nov 30 09:43:34 2020
# 格式化时间
time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())   # 2020-11-30 09:46:40
# 根据 指定格式 把一个时间字符串 解析为 时间元组
time.strptime('2020-11-30','%Y-%m-%d')
