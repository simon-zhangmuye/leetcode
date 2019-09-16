# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/9/16 22:51'


# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or root.left is root.right: return True
        l, r, i, o = root.left, root.right, TreeNode(0), TreeNode(0)
        if (l and l.val) != (r and r.val): return False
        i.left, i.right, o.left, o.right = l.left, r.right, l.right, r.left
        return self.isSymmetric(i) and self.isSymmetric(o)
