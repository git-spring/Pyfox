# datetime
import datetime
'''
datetime模块中包含如下类:
    date	    日期对象
    time	    时间对象
    datetime	日期时间对象
    timedelta	时间间隔,即两个时间点之间的长度
    tzinfo	    时区信息对象
    datetime_CAPI	日期时间对象C语言接口
'''


## datetime.date 类
# date 类的 __init__ 方法
datetime.date(2020,11,29)   # 2020-11-29
# 获取当前日期
today = datetime.date.today()  # 2020-11-30
year = today.year
month = today.month
day = today.day

# 查看星期
week = today.weekday()  # 星期一,返回0;星期二,返回1,以此类推
today.isoweekday()      # 星期一,返回1;星期二,返回2,以此类推

# 格式化时间,格式为'yyyy-MM-dd'  不能指定格式
today.isoformat()


## datetime.time 类
now = datetime.time(12,30,56)



## datetime.datetime 类

# 获取现在的日期时间
dt = datetime.datetime.today()
datetime.datetime.now()

# 属性和方法
dt.year
dt.month
dt.day
dt.hour
dt.minute
dt.second

dt.date()
dt.time()


## datetime.timedelta 类   时间加减类

dt = datetime.datetime.now()
dt1 = dt + datetime.timedelta(days=-1)   # 昨天
dt2 = dt - datetime.timedelta(days=1)    # 昨天
dt3 = dt + datetime.timedelta(days=1)    # 明天

daydiff = dt3 - dt1                      # 日期差
