# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:19:08 2020

@author: PC
"""

import numpy as np


arr1 = np.arange(6).reshape((2, 3))

print(arr1)
# [[0 1 2]
#  [3 4 5]]

arr2 = np.arange(0, 12, 2).reshape((2, 3))

print(arr2)
# [[ 0  2  4]
#  [ 6  8 10]]

arr_sum = arr1 + arr2

print(arr_sum)
# [[ 0  3  6]
#  [ 9 12 15]]


mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

mat_sum = mat1 + mat2

print(mat_sum)
# [[ 0  3  6]
#  [ 9 12 15]]
