import time
import calendar
def time_test():
    localtime = time.localtime(time.time())  # 返回的是时间元组
    print("本地时间为 :", localtime)

    localtime = time.asctime(time.localtime(time.time()))  # 接受时间元组并返回一个可读的形式
    print("本地时间为 :", localtime)

    # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # 格式化成Sat Mar 28 22:24:24 2016形式  # 根据fmt的格式把一个时间字符串解析为时间元组。
    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

    # 将格式字符串转换为时间戳
    a = "Sat Mar 28 22:24:24 2016"
    print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

    cal = calendar.month(2020, 8)
    print("以下输出2020年8月份的日历:")
    print(cal)

def procedure():
    time.sleep(2.5)

def clock_test() :
    # time.clock
    t0 = time.clock()
    procedure()
    print(time.clock() - t0)

    # time.time
    t0 = time.time()
    procedure()
    print(time.time() - t0)
# 格式化
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身


# 日历

# 序号	函数及描述
# 1	calendar.calendar(year,w=2,l=1,c=6)
# 返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。
# 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
# 2	calendar.firstweekday( )
# 返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
# 3	calendar.isleap(year)是闰年返回 True，否则为 false。
#
#
# 4	calendar.leapdays(y1,y2)
# 返回在Y1，Y2两年之间的闰年总数。
# 5	calendar.month(year,month,w=2,l=1)
# 返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。
# 每行的长度为7* w+6。l是每星期的行数。
# 6	calendar.monthcalendar(year,month)
# 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
# 7	calendar.monthrange(year,month)
# 返回两个整数。第一个是该月的星期几，第二个是该月有几天。星期几是从0（星期一）到 6（星期日）。
#
#
# 8	calendar.prcal(year, w=0, l=0, c=6, m=3)
# 相当于 print (calendar.calendar(year, w=0, l=0, c=6, m=3))。
# 9	calendar.prmonth(theyear, themonth, w=0, l=0)
# 相当于 print(calendar.month(theyear, themonth, w=0, l=0))。
# 10	calendar.setfirstweekday(weekday)
# 设置每周的起始日期码。0（星期一）到6（星期日）。
# 11	calendar.timegm(tupletime)
# 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）。
# 12	calendar.weekday(year,month,day)
# 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。