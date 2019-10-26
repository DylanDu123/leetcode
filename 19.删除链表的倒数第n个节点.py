#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        head_pointer = dummy
        pointer = dummy

        while n > 0:
            head_pointer = head_pointer.next
            n -= 1
            pass

        while head_pointer.next:
            head_pointer = head_pointer.next
            pointer = pointer.next
            pass
        
        pointer.next = pointer.next.next

        return dummy.next
        
# @lc code=end

