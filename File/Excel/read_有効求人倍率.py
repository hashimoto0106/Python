# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 22:28:07 2018

@author: hashimoto
"""

import pandas as pd


xls_input = pd.read_excel('第3表.xls',
                        skiprows=3,  # 先頭3行無視
                        skip_footer=2,  # 末尾2無視
                        parse_cols='W,Y:AJ',
                        index_col=0)  # 西暦列をインデックス指定

print(xls_input)

# インプットの項目数（行数 * カラム数）を返却します。
print(xls_input.size)

#行数を確認
print(len(xls_input))

#カラム数を確認
print(len(xls_input.columns))

#次元の確認
print(xls_input.shape)

#カラム情報
print(xls_input.columns)
