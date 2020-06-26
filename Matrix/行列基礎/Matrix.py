
# coding: utf-8

# In[5]:


# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 22:25:05 2018

@author: hashimoto
"""
# https://note.nkmk.me/python-numpy-matrix/

import numpy as np


# In[6]:


# 行列の和と差
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

arr_sub = arr1 - arr2

print(arr_sub)
# [[ 0 -1 -2]
#  [-3 -4 -5]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

mat_sum = mat1 + mat2

print(mat_sum)
# [[ 0  3  6]
#  [ 9 12 15]]

mat_sub = mat1 - mat2

print(mat_sub)
# [[ 0 -1 -2]
#  [-3 -4 -5]]


# In[7]:


# スカラー倍
arr_mul = arr1 * 2

print(arr_mul)
# [[ 0  2  4]
#  [ 6  8 10]]

mat_mul = mat1 * 2

print(mat_mul)
# [[ 0  2  4]
#  [ 6  8 10]]


# In[8]:


# 行列の積
mat_mul_matrix = mat1 * mat2

print(mat_mul_matrix)


# In[9]:


# 行列の積
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a@b)  # 行列積
print(np.matmul(a, b))  # 行列積
print(a.dot(b))  # 内積
print(np.dot(a, b))  #  内積


# In[10]:


# 行列とベクトルの積
import numpy

a = numpy.array([[1, 2], [3, 4]])
b = numpy.array([5, 6])

print(a@b)
print(a.dot(b))
print(numpy.dot(a, b))
print(numpy.matmul(a, b))


# In[11]:


# べき乗


# In[12]:


# 内積
arr = np.random.randn(6,3)
print(arr)
print(arr.T)
print(np.dot(arr.T,arr))


# In[13]:


# 逆行列


# In[14]:


# 転置
arr = np.array([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]])
print(arr)
print(arr.T)


# In[15]:


# 行列式


# In[15]:


# 固有値と固有ベクトル

