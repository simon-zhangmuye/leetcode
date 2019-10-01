# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/1 6:32'


# 给定两个字符串 s 和 t，判断它们是否是同构的。
#
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
#
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
#
# 示例 1:
#
# 输入: s = "egg", t = "add"
# 输出: true
# 示例 2:
#
# 输入: s = "foo", t = "bar"
# 输出: false
# 示例 3:
#
# 输入: s = "paper", t = "title"
# 输出: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash = {}
        for i, c in enumerate(s):
            if hash.get(c):
                if t[i] != hash[c]:
                    return False
            else:
                if t[i] in hash.values():
                    return False
                hash[c] = t[i]
        return True
