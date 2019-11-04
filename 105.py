'''
-*- coding: utf-8 -*-
@Author  : Simon Zhang
@Time    : 2019/11/4 17:45
@Software: PyCharm
@File    : 105.py
'''


# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 说明：
#
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":  # 处理特殊情况
            return "0"

        l1, l2 = len(num1), len(num2)
        if l1 < l2:
            num1, num2 = num2, num1  # 保障num1始终比num2长， 个人习惯
            l1, l2 = l2, l1

        num2 = num2[::-1]  # 注意要倒过来乘，方便进位
        res = "0"
        for i, digit in enumerate(num2):
            tmp = self.StringMultiplyDigit(num1, int(digit)) + "0" * i  # 计算num1和num2的当前位的乘积
            res = self.StringPlusString(res, tmp)  # 计算res和tmp的和

        return res
