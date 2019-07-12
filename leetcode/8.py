#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-12 13:09
# @Author  : bingo
# @Site    : 
# @File    : 8.py
# @Software: PyCharm
"""
字符串转换成正数
"""
import re


class Solution:
    def myAtoi(self, strs: str) -> int:
        MAX_INT = 2147483647  # 2**31-1
        MIN_INT = -2147483648  # -2**31
        PATTERN = '^[\+\-]?\d+'
        num = int(*re.findall(PATTERN, strs.strip()))   # *star 解开列表
        return max(min(num, MAX_INT), MIN_INT)  #最精彩的逻辑
