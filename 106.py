'''
-*- coding: utf-8 -*-
@Author  : Simon Zhang
@Time    : 2019/11/5 13:37
@Software: PyCharm
@File    : 106.py
'''

#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
# 示例 1:
#
# 输入: 2.00000, 10
# 输出: 1024.00000
# 示例 2:
#
# 输入: 2.10000, 3
# 输出: 9.26100
# 示例 3:
#
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
# 说明:
#
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。


class Solution:
    def myPow(self, x: float, n: int) -> float:
        judge = True
        if n<0:
            n = -n
            judge = False
        if n==0:
            return 1
        final = 1     # 记录当前的乘积值
        tmp = x       # 记录当前的因子
        count = 1     # 记录当前的因子是底数的多少倍
        while n>0:
            if n>=count:
                final *= tmp
                tmp = tmp*x
                n -= count
                count +=1
            else:
                tmp /= x
                count -= 1
        return final if judge else 1/final
