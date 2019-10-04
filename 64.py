# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/5 7:28'


# 翻转一棵二叉树。
#
# 示例：
#
# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root != None:
            node = root
            node.left, node.right = self.invertTree(node.right), self.invertTree(node.left)
        else:
            return None

        return node
