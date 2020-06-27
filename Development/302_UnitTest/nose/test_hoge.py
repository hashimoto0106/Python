# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 23:04:58 2018

@author: PC
"""

from unittest import TestCase
from nose.tools import ok_, eq_
# from hoge import sum, is_even


def sum(a, b):
    return a + b


def is_even(n):
    return (n % 2 == 0)


class HogeTestCase(TestCase):
    def setUp(self):
        print('before test')

    def tearDown(self):
        print('after test')

    def test_sum(self):
        eq_(sum(1, 2), 3)
        eq_(sum(5, 11), 16)
        eq_(sum(0, 0), 0)

    def test_is_even(self):
        ok_(is_even(2))
        ok_(not is_even(3))


if __name__ == "__main__":
    TestCase.main()
