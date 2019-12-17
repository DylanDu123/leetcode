#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        prep = dummy
        while l1 and l2:
            if l1.val < l2.val:
                prep.next = l1
                l1 = l1.next
            else:
                prep.next = l2
                l2 = l2.next
            prep = prep.next

        if l1:
            prep.next = l1
        if l2:
            prep.next = l2
        return dummy.next

        
# @lc code=end

