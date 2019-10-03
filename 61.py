# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/3 12:28'


# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None

        while head:
            tmp = head.next  # 备份原来head节点的next地址
            head.next = new_head
            new_head = head
            head = tmp

        return new_head
