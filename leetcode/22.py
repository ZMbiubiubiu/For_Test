#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-11 17:23
# @Author  : bingo
# @Site    : 
# @File    : 22.py
# @Software: PyCharm
"""
22. 括号生成
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

解答方法：
DFS + 剪枝
剪枝的条件为：left > n or right > n or left < right
"""


class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        self.list = []
        self._gen(0, 0, n, '')
        return self.list

    def _gen(self, left, right, n, result):
        # left,right 表示使用了多少个左、右括号
        if left > n or right > n or left < right: return
        if left == n and right == n:
            self.list.append(result)
            return
        self._gen(left + 1, right, n, result + "(")
        self._gen(left, right + 1, n, result + ")")
