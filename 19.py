# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/9/14 16:05'

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

"""
    1. dp问题, 公式为: dp[i] = dp[i - 1] + dp[i - 2].
    2. dp[0], dp[1]都为1
"""
def climbStairs(n):
    # 类似斐波拉契
    a, b = 1, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

def climbStairs1(n):
    r = [0 for _ in range(n + 1)]
    r[0], r[1] = 1, 1
    for i in range(2, n + 1):
        r[i] = r[i - 1] + r[i - 2]
    return r[n]

print(climbStairs(10))
print(climbStairs1(10))

