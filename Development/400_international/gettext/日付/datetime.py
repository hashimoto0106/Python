# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:16:52 2020

@author: PC
"""

from datetime import datetime, timezone, timedelta


current_time = datetime.now(timezone.utc)

# 任意の時刻を作成する場合はこう
update_time = datetime(2018, 8, 19, 12, 0, 0, tzinfo=timezone.utc)
print(update_time.astimezone())

print(current_time.astimezone())

timezone_newyork = timezone(timedelta(hours=-5))
print(current_time.astimezone(timezone_newyork))

current_time = datetime.now(timezone.utc)
tokyo = timezone(timedelta(hours=9))
newyork = timezone(timedelta(hours=-5))
print(current_time.astimezone(tokyo) == current_time.astimezone(newyork))
