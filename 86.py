# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/14 0:30'


# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 示例 1:
#
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 示例 2:
#
# 输入: dividend = 7, divisor = -3
# 输出: -2


def divide(self, dividend: int, divisor: int) -> int:
    sign = (dividend > 0) ^ (divisor > 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0
    #把除数不断左移，直到它大于被除数
    while dividend >= divisor:
        count += 1
        divisor <<= 1
    result = 0
    while count > 0:
        count -= 1
        divisor >>= 1
        if divisor <= dividend:
            result += 1 << count #这里的移位运算是把二进制（第count+1位上的1）转换为十进制
            dividend -= divisor
    if sign: result = -result
    return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1
