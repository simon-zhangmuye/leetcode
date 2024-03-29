# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/9/9 1:54'


# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4



def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        if l1.val > l2.val: l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1 or l2
