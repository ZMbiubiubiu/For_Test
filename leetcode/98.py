"""
验证二叉搜索树

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def goAlongWithLeftBranch(self, node, stack):
        while node:
            stack.append(node)
            node = node.left

    def isAsc(self, in_order):
        for index in range(1, len(in_order)):
            if in_order[index - 1] >= in_order[index]:
                return False
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        #  method 1.中序遍历法
        # 如果为二叉搜索树，那么中序遍历应该为递增
        if root is None:
            return True
        node = root
        in_order = []
        stack = []
        while 1:
            self.goAlongWithLeftBranch(node, stack)
            if not stack:
                break
            node = stack.pop()
            in_order.append(node.val)
            node = node.right
        return self.isAsc(in_order)

    ###############################################
    #method 2.中序遍历.此时我们只需要比较中序遍历的前一个与当前节点

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        node = root
        pre = None
        stack = []
        while 1:
            self.goAlongWithLeftBranch(node, stack)
            if not stack:
                break
            node = stack.pop()
            if pre is not None and pre.val >= node.val:
                return False
            pre = node
            node = node.right
        return True