# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:51:35 2019

@author: PC
"""

import change

# 値渡し
num = 10
change.double(num)
print(num)

# 参照渡し
num = [42, 256, 16]
change.change(num)
print(num)
