"""
二叉树的最近公共祖先

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# method 1.
# 如果节点有指向父亲节点的指针，那么就很好做了。
# 找出两个节点的祖先路径，然后找到两个路径的公共节点，那么两个路径的最后一个公共节点便是最低公共祖先


# method 2.递归
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None and right is None:
            return None
        elif left is None:   # 左子树中，q和p都没有
            return right
        elif right is None:  # 右子树种，q和p都没有
            return left
        else:                # 左子树，右子树其中各占一个节点，那么最低公共祖先一定在根节点上
            return root
