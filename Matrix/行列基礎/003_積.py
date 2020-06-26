# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:32:52 2020

@author: PC
"""
import numpy as np


arr1 = np.arange(6).reshape((2, 3))

print(arr1)
# [[0 1 2]
#  [3 4 5]]

arr2 = np.arange(0, 12, 2).reshape((3, 2))

print(arr2)
# [[ 0  2]
#  [ 4  6]]
#  [ 8  10]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

# 行列の積
mat_mul_matrix = mat1 * mat2
print(mat_mul_matrix)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a@b)  # 行列積
print(np.matmul(a, b))  # 行列積