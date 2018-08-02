# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 22:23:00 2018

@author: hashimoto
"""

import logging

# ログの出力名を設定（1）
logger = logging.getLogger('LoggingTest')

# ログレベルの設定（2）
logger.setLevel(10)

# ログのファイル出力先を設定（3）
fh = logging.FileHandler('test.log')
logger.addHandler(fh)

# ログのコンソール出力の設定（4）
sh = logging.StreamHandler()
logger.addHandler(sh)

logger.log(20, 'info')
logger.log(30, 'warning')
logger.log(100, 'test')

logger.info('info')
logger.warning('warning')

# ログの出力名を設定
logger = logging.getLogger('LoggingTest')

# ログレベルの設定
logger.setLevel(10)

# ログのファイル出力先を設定
fh = logging.FileHandler('test.log')
logger.addHandler(fh)

# ログのコンソール出力の設定
sh = logging.StreamHandler()
logger.addHandler(sh)

# ログの出力形式の設定
#formatter = logging.Formatter('%(asctime)s'+'.'+'%(msecs)d'+',%(levelname)s,%(filename)s,%(funcName)s,%(module)s,%(name)s,%(process)d,%(thread)d,%(lineno)d,%(message)s')
formatter = logging.Formatter('%(relativeCreated),%(levelname)s,%(filename)s,%(funcName)s,%(module)s,%(name)s,%(process)d,%(thread)d,%(lineno)d,%(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)

logger.log(20, 'info')
logger.log(30, 'warning')
logger.log(100, 'test')


logger.debug('10_hashimoto')
logger.info('20_hashimoto')
logger.warning('30_hashimoto')
logger.error('40_hashimoto')
logger.critical('50_hashimoto')
