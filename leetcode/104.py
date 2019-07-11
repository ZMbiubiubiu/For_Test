#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-11 08:39
# @Author  : bingo
# @Site    : 
# @File    : 104.py
# @Software: PyCharm

"""
二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 递归解法
        if root is None: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

    def maxDepth2(self, root: TreeNode) -> int:
        # 层次遍历法
        if root is None: return 0
        queue = collections.deque()
        queue.append(root)
        total_levels = 0
        while queue:
            current_level_size = len(queue)
            total_levels += 1
            for _ in range(current_level_size):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return total_levels
