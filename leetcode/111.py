#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-11 09:52
# @Author  : bingo
# @Site    : 
# @File    : 111.py
# @Software: PyCharm
"""
二叉树的最小深度
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 宽度优先搜索
        # 在任何一层，只要找到叶子节点
        # 则层数便是二叉树的最小深度
        if root is None: return 0
        queue = collections.deque()
        queue.append(root)
        min_level = 0
        flag = True
        while queue and flag:
            current_level_size = len(queue)
            min_level += 1
            for _ in range(current_level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.left is None and node.right is None:
                    flag = False
                    break
        return min_level
