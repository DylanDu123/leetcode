#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = result = ListNode(0)
        sale = 0
        while l1 or l2:
            l1_v = l1.val if l1 else 0
            l2_v = l2.val if l2 else 0
            value = l1_v + l2_v
            dummy.next = ListNode((value + sale) % 10)
            dummy = dummy.next
            sale = (value+sale)//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            pass
        if sale > 0:
            dummy.next = ListNode(sale)
            pass
        return result.next
