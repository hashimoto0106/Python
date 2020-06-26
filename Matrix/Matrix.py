# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:25:35 2019

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 並進行列(x軸方向に並進)
def L(l):
    Li = np.matrix((
        ( 1., 0., l),
        ( 0., 1., 0.),
        ( 0., 0., 1.)
    ));
    return Li


def rotate_x_deg(deg):
    r = np.radians(deg)
    c = np.cos(r)
    s = np.sin(r)
    # 回転行列Rx
    Rx = np.matrix([
        [1,0,0],
        [0,c,-s],
        [0,s,c]])
    
    return Rx
 

def rotate_y_deg(deg):
    r = np.radians(deg)
    c = np.cos(r)
    s = np.sin(r)
    # 回転行列Ry
    Ry = np.matrix([
        [c,0,s],
        [0,1,0],
        [-s,0,c]])
    
    return Ry
 

def rotate_z_deg(deg):
    r = np.radians(deg)
    c = np.cos(r)
    s = np.sin(r)
    # 回転行列Rx
    Rz = np.matrix([
        [c,-s,0],
        [s,c,0],
        [0,0,1]])
    
    return Rz


def rotate_x_rad(rad):
    r = rad
    C = np.cos(r)
    S = np.sin(r)
    # 回転行列Rx
    R_x = np.matrix((
        (1, 0, 0),
        (0, C, -S),
        (0, S, C)
    ))

    return R_x


def rotate_y_rad(rad):
    r = rad
    c = np.cos(r)
    s = np.sin(r)
    # 回転行列Ry
    Ry = np.matrix([
        [c,0,s],
        [0,1,0],
        [-s,0,c]])
    
    return Ry


def rotate_z_rad(rad):
    r = rad
    c = np.cos(r)
    s = np.sin(r)
    # 回転行列Rx
    Rz = np.matrix([
        [c,-s,0],
        [s,c,0],
        [0,0,1]])
    
    return Rz


# 3D座標設定関数
def coordinate_3d(axes, range_x, range_y, range_z, grid = True):
    axes.set_xlabel("x", fontsize = 16)
    axes.set_ylabel("y", fontsize = 16)
    axes.set_zlabel("z", fontsize = 16)
    axes.set_xlim(range_x[0], range_x[1])
    axes.set_ylim(range_y[0], range_y[1])
    axes.set_zlim(range_z[0], range_z[1])
    if grid == True:
        axes.grid()


# 3Dベクトル描画関数
def visual_vector_3d(axes, loc, vector, color = "red"):
    axes.quiver(loc[0], loc[1], loc[2],
              vector[0], vector[1], vector[2],
              color = color, length = 1,
              arrow_length_ratio = 0.2)



# 設定関数
def init(axes, title, range_x, range_y):
    axes.set_title(title)
    axes.set_xlabel("x", fontsize = 16)
    axes.set_ylabel("y", fontsize = 16)
    axes.set_xlim(-range_x, range_x)
    axes.set_ylim(-range_y, range_y)
    axes.grid()


# Point描画関数
def plot_point(axes, x, y, marker='.', color = "red"):
    # Point描画
    axes.plot(x, y, marker=marker, markersize=10, color=color)
    axes.legend()

    # 座標位置表示
    txt = "(" + str(x) + ", " + str(y) + ")"
    axes.text(x+0.5, y+0.5, txt, color = color, size = 9)
