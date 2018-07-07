import time


def t_time():
    sttime = time.time()
    time.sleep(1)
    # for i in xrange(50000):
    #   pass
    entime = time.time()
    return (entime - sttime)


def c_time():
    sttime = time.clock()
    time.sleep(1)
    # for i in xrange(50000):
    #   pass
    entime = time.clock()
    return (entime - sttime)


print("\ntime.time")
print(str(t_time()))

print("\ntime.clock")
print(str(c_time()))
