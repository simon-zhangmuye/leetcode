# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/18 19:48'


# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
# #
# # 示例 1:
# #
# # 输入: 27
# # 输出: true
# # 示例 2:
# #
# # 输入: 0
# # 输出: false
# # 示例 3:
# #
# # 输入: 9
# # 输出: true
# # 示例 4:
# #
# # 输入: 45
# # 输出: false


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        dd=False

        sumk=1

        while sumk <= n:

            if sumk==n:
                dd=True
                break

            sumk=sumk*3

        return dd
