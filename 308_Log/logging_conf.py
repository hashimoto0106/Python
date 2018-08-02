# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 00:12:13 2018

@author: hashimoto
"""

import logging.config

# ログ設定ファイルからログ設定を読み込み
logging.config.fileConfig('logging.conf')
logger = logging.getLogger()

logger.debug('10_hashimoto')
logger.info('20_hashimoto')
logger.warning('30_hashimoto')
logger.error('40_hashimoto')
logger.critical('50_hashimoto')
