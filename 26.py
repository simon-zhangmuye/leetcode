# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/9/17 0:46'


# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n==0:
            return None
        target = n//2
        root = TreeNode(nums[target])
        root.left = self.sortedArrayToBST(nums[0:target])
        root.right = self.sortedArrayToBST(nums[target+1:n])
        return root
