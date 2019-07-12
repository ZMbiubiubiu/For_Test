#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-07-12 13:14
# @Author  : bingo
# @Site    : 
# @File    : 501.py
# @Software: PyCharm
"""
二叉搜索树中的众数
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 中序遍历+选举算法
    def findMode(self, root: TreeNode) -> 'List[int]':
        if root is None:
            return []
        orders = []  # 中序存储每个节点的值
        self.in_order(orders, root)
        return self.find_most(orders)

    def in_order(self, orders: 'List[int]', root: TreeNode):
        """
        中序遍历，将结果保存在一个列表中
        """
        if root is None:
            return
        self.in_order(orders, root.left)
        orders.append(root.val)
        self.in_order(orders, root.right)

    def find_most(self, orders):
        """
        根据中序遍历的结果，找到众数。
        需要注意的是，可能会有多个众数
        """
        pre_val = orders[0]
        pre_counts = 0
        most_counts = -1
        for num in orders:
            if num == pre_val:
                pre_counts += 1
            else:
                if pre_counts > most_counts:
                    most_counts = pre_counts
                    orders = [pre_val]
                elif pre_counts == most_counts:
                    orders.append(pre_val)
                else:
                    pass
                pre_counts = 1
                pre_val = num
        # 判断最后相同的数字的个数是否对之前生成的结果产生影响
        if pre_counts == most_counts:
            orders.append(pre_val)
        elif pre_counts > most_counts:
            orders = [pre_val]
        return orders


if __name__ == "__main__":
    l = [1, 22, 22, 33, 33]
    Solution().find_most(l)
