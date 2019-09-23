# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/9/24 3:12'



# 给定一个链表，判断链表中是否有环。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
#  
#
# 示例 1：
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
# 示例 2：
#
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
# 示例 3：
#
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。

def hasCycle(self, head):
    if not head:
        return False
    while head.next and head.val != None:
        head.val = None  # 遍历的过程中将值置空
        head = head.next
    if not head.next:  # 如果碰到空发现已经结束，则无环
        return False
    return True  # 否则有环
