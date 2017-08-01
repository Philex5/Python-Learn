"""
    Python之所以自称“batteries included”，就是因为内置了许多非常有用的模块，无需额外安装和配置，即可直接使用。
"""
import re
from datetime import datetime, timezone, timedelta
"""
    datatime是Python处理日期和时间的标准库
"""

# 获取当前按日期和时间
now = datetime.now()
print(now)

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# datetime 转换为timestamp
# timestamp :当前时间相当于epoch time(1970.1.1 00:00:00 UTC+00:00时区)d的秒数
dt = datetime(2015, 4, 19, 12, 20)
print(dt.timestamp())

# timestamp 转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))
# UTC标准时区
print(datetime.utcfromtimestamp(t))

# str 转换为 datetime
# 使用datetime.strptime()
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime加减
print(now - timedelta(days=5, hours=10))


# 本地时间转换为UTC时间个datetime到底是哪个时区，除非强行给datetime设置一个时区：
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8)   # 强制设置为UTC+8:00

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = dt.astimezone(timezone(timedelta(hours=8)))  # 转换为北京时区
print(bj_dt)


"""
datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
"""
# Exercises


def to_timestamp(dt_str, tz_str):
    # 获取datetime
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 提取时区信息
    r = re.match(r'^(\w{3})\+(\d):(\d*)$', tz_str)
    print(r)
    tz = int(r.group(2))
    print(tz)
    # 转换到标准时区
    tz = timezone(timedelta(hours=tz))
    dt_tz8 = dt.replace(tzinfo=tz)
    dt_utc = dt_tz8.astimezone(timezone.utc)
    t = datetime.timestamp(dt_utc)

    return float(t)


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC+9:00')
assert t2 == 1433056230.0, t2
print('Pass')





