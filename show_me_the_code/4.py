#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-10 16:02
# @Author  : bingo
# @Site    : 
# @File    : 4.py
# @Software: PyCharm

"""
任一个英文的纯文本文件，统计其中的单词出现的个数
"""

from collections import defaultdict
import re

d = defaultdict(int)
# 匹配单词的正则表达式
PATTERN = re.compile('[a-zA-Z]+')


def get_word_from_file(file: str) -> 'generator':
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            results = PATTERN.finditer(line)
            for word in results:
                yield word.group().lower()


for word in get_word_from_file('4_articles.txt'):
    d[word] += 1

print(d)

