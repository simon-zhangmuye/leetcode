# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/2 4:17'


# 删除链表中等于给定值 val 的所有节点。
#
# 示例:
#
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        last = prev.next
        while last :
            if last.val == val:
                prev.next = last.next
                last = prev.next
            else:
                prev = prev.next
                last = prev.next
        return dummy.next
