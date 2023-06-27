"""
======================
Author: 潘师傅
Time: 2023-06-26 11:08
Project: yinlian
Company: 无限主义
======================
"""

import unittest

from Common.my_logger import logger

class BlindBox(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        logger.info('************ 翻牌模块用例 开始执行 ************')



    def test_001(self):
        pass