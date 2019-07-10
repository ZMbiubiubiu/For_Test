#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-10 15:23
# @Author  : bingo
# @Site    : 
# @File    : 3.py
# @Software: PyCharm

"""
**第 0003 题：**将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。
"""

import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    db=3,
)


# 取出文件中的数据
def get_datas(file: str) -> 'generator':
    """

    :param file: 存储数据的文件
    :return: 一个迭代器，每个元素是文件中的一行
    """
    with open(file, 'r') as f:
        for line in f:
            yield line.strip()


# 存入redis数据库
def save_in_redis(r: 'redis-cli', datas: 'generator'):
    for i, item in enumerate(datas):
        r.set(name=i, value=item)


if __name__ == "__main__":
    save_in_redis(r, get_datas('codes.txt'))
