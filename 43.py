# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/9/24 3:17'

#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false


class Solution:
   def isPalindrome(self, s: str) -> bool:
       str = '#'
       for c in s:
           if c.isalnum():
               str += c + '#'
       mid = len(str)>>1
       l = mid-1
       r = mid+1
       while l>=0 and r < len(str):
           if str[l].upper() == str[r].upper():
               l -= 1
               r += 1
           else:
               return False
       return True
