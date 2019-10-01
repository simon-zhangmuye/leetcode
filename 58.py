# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/2 4:16'


# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        for i in range(2, n):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                #print(i)
                res += 1
        return res
