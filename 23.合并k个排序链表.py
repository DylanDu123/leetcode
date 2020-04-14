#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):

        amount = len(lists)
        if amount == 0:
            return lists
        if amount == 1:
            return lists[0]
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval*2):
                lists[i] = self.merge2ListsZ(lists[i], lists[i + interval])
            interval *= 2
            pass
        return lists[0]

    def merge2ListsZ(self, l1, l2) -> ListNode:
        dummy = head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next

# @lc code=end
