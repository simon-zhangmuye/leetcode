# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/12 15:26'


# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        end = head
        start = head
        for i in range(n):
            end = end.next
        if not end:
            return head.next

        while end.next:
            start = start.next
            end = end.next
        if start.next.next:
            start.next = start.next.next
        else:
            start.next = None

        return head
