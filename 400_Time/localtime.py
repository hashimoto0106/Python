import time

class MyTime(object):
    def __init__(self, hour, minutes, sec):
        self.hour = hour
        self.minute = minutes
        self.sec = sec
        
    @staticmethod
    def now():
        t = time.localtime()
        return MyTime(t.tm_hour, t.tm_min, t.tm_sec)
    
a = MyTime(15, 20, 58)
b = MyTime.now()

print(a.minute)
print(b.minute)
