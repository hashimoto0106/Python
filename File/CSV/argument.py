# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 22:28:07 2018

@author: hashimoto
"""

import pandas as pd


csv_input = pd.read_csv(filepath_or_buffer="exchange.csv",
                        encoding="ms932",
                        header=1,
                        names=['date', 'USD', 'rate'],
                        skipinitialspace=True,
                        index_col=0,
                        parse_dates=True,
                        sep=",")

print(csv_input)

# インプットの項目数（行数 * カラム数）を返却します。
print(csv_input.size)

#行数を確認
print(len(csv_input))

#カラム数を確認
print(len(csv_input.columns))

#次元の確認
print(csv_input.shape)

#カラム情報
print(csv_input.columns)
