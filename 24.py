# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/9/16 22:52'


# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。

class TreeNode(object):
    """ Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
