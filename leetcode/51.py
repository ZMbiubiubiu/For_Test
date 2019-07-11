#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-11 17:55
# @Author  : bingo
# @Site    : 
# @File    : 51.py
# @Software: PyCharm
"""
51. N皇后
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

国际象棋中的皇后比中国象棋里的大车还厉害，皇后能横向，纵向和斜向移动，在这三条线上的其他棋子都可以被吃掉。
所谓n皇后问题就是：将n位皇后放在一张8x8的棋盘上，使得每位皇后都无法吃掉别的皇后，（即任意两个皇后都不
在同一条横线，竖线和斜线上），问一共有多少种摆法
"""


class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, pie, na):"""
            :param queens: queens 存储各个皇后所在的列。皇后的列应该彼此不同
            :param pie: 皇后所在位置的`撇`的位置也不能存在皇后
            :param na: 皇后所在位置的`捺`的位置也不能存在皇后
            :return: 返回所有可能的结果
            """
            row = len(queens)
            if row == n:
                result.append(queens)
                return None
            for col in range(n):
                if col not in queens and col + row not in pie and row - col not in na:
                    DFS(queens + [col], pie + [col + row], na + [row - col])

        result = []
        DFS([], [], [])
        # return [['.'*col+'Q'+'.'*(n-col-1) for col in queens] for queens in result]
        return self.generate_checkboard(result, n)

    def generate_checkboard(self, result, n):
        checkboards = []
        for i in range(len(result)):  # 构建每一个符合皇后问题的棋谱
            queens = result[i]
            checkboard = ['.' * col + 'Q' + '.' * (n - col - 1) for col in queens]
            checkboards.append(checkboard)
        return checkboards
