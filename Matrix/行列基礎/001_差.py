# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:22:42 2020

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

arr_sub = arr1 - arr2

print(arr_sub)
# [[ 0 -1 -2]
#  [-3 -4 -5]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

mat_sub = mat1 - mat2

print(mat_sub)
# [[ 0 -1 -2]
#  [-3 -4 -5]]
