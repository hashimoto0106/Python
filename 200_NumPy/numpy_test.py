# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():
    # x�̒l�𐶐�
    x = np.arange(-3.14, 3.14, 0.25)
    # �������v�Z
    sin = np.sin(x) # sin(x)�̌v�Z
    cos = np.cos(x) # cos(x)�̌v�Z
    tan = np.tan(x) # tan(x)�̌v�Z
    exp = np.exp(x) # �w���֐��̌v�Z
    log = np.log(x) # �ΐ��֐��̌v�Z
    # �O���t�\��
    plt.plot(x, sin,"-o",lw=2,alpha=0.7,label="sin(x)")
    plt.plot(x, cos,"-o",lw=2,alpha=0.7,label="cos(x)")
    plt.plot(x, tan,"-o",lw=2,alpha=0.7,label="tan(x)")
    plt.plot(x, exp,"-o",lw=2,alpha=0.7,label="exp(x)")
    plt.plot(x, log,"-o",lw=2,alpha=0.7,label="log(x)")
    fn = "Times New Roman"                      # �t�H���g
    plt.tick_params(labelsize=15)               # ���ڐ��̃t�H���g�T�C�Y
    plt.xlabel("$x$", fontsize=30, fontname=fn) # x���̃��x��
    plt.ylabel("$y$", fontsize=30, fontname=fn) # y���̃��x��
    plt.xlim([-4, 4])                           # x���͈̔�
    plt.ylim([-4, 4])                           # y���͈̔�
    plt.grid()                                  # �O���b�h�̕\��
    plt.legend(fontsize=13)                     # �}��̕\��
    plt.show()                                  # �O���t�̕`��

if __name__ == '__main__':
    main()