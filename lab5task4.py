import time
import datetime
class Time(object):
        def __init__(self, y=2019, m=2, d=2, h=10, m=0, s=0):
        self.date = datetime.datetime(y, m, d, h, m, s)
        def mktime(self):
        return time.mktime(self.date.timetuple())
t1 = Time(2019, 2, 6, 7)
t2 = Time(2019, 2, 6, 14)
        def is_after(time1, time2):
        return time1.mktime() > time2.mktime()
print (is_after(t1, t2))
