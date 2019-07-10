#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-09 15:33
# @Author  : bingo
# @Site    : 
# @File    : 1.py
# @Software: PyCharm

"""
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
"""

import string
import random


def base_strs():
    return (string.digits + string.ascii_letters)


def key_gen(raw, length=20):
    activation_code = [random.choice(raw) for i in range(length)]
    return "".join(activation_code)


def get_all_codes(num):
    activation_codes = []
    for i in range(num):
        activation_codes.append(key_gen(base_strs(), 20))
    return activation_codes


def save_in_file(activation_codes, file='codes.txt'):
    with open(file, 'w') as f:
        for item in activation_codes:
            print(item, end='\n', file=f)


if __name__ == "__main__":
    codes = get_all_codes(200)
    save_in_file(codes)
