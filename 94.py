# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/19 0:41'



# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
#
# 示例：
#
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3


class NumArray:

    def __init__(self, nums):
        self.dp = nums[:]
        # self.dp[i]存储0~i的子序列和
        for i in range(1, len(self.dp)):
            self.dp[i] += self.dp[i - 1]

    def sumRange(self, i, j):
        return self.dp[j] - self.dp[i - 1] if i > 0 else self.dp[j]
