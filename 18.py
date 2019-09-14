# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/9/14 16:04'

#
实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。


class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        while l < h:
            m = (l + h) // 2
            if m**2 <= x < (m+1)**2:
                return m
            elif m**2 < x:
                l = m + 1
            else:
                h = m - 1
        return l
