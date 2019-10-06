# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/6 9:23'


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
        if not head or not head.next:return True
        # 取中位数的上边界，比如[1, 2, 2, 3] 取到是第二个2
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 奇数时候，中点位置下一个，（这样翻转才一样）
        if fast:
            slow = slow.next
        # 翻转操作
        prev = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # 对比
        p1 = head
        p2 = prev
        while p1 and p2:
            if p1.val != p2.val:
                return False
