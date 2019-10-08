# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/8 23:44'


# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        l = 0
        r = len(tmp)-1
        while l<r:
            if tmp[l] != tmp[r]:
                return False
            l += 1
            r -= 1
        return True
