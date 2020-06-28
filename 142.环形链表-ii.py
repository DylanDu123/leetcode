#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def fetchPoint(self, head: ListNode):
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return fast
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        node = self.fetchPoint(head)
        if not node:
            return None
        curr = head
        while curr != node:
            curr = curr.next
            node = node.next
            pass
        return curr
# @lc code=end
