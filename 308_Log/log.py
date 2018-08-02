# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 22:23:00 2018

@author: hashimoto
"""

import logging
import os

# コンソールクリア
os.system('cls')

# ログの出力名を設定
logger = logging.getLogger('Logging')

# ログレベルの設定
logger.setLevel(10)

# ログのファイル出力先を設定
fh = logging.FileHandler('loging.log')
logger.addHandler(fh)

# ログのコンソール出力の設定
sh = logging.StreamHandler()
logger.addHandler(sh)

# ログの出力形式の設定
formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(filename)s,%(funcName)s,%(module)s,%(name)s,%(process)d,%(thread)d,%(lineno)d,%(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

logger.debug('10_hashimoto')
logger.info('20_hashimoto')
logger.warning('30_hashimoto')
logger.error('40_hashimoto')
logger.critical('50_hashimoto')
