#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        n1 = 0
        n2 = 0
        fact = 1
        while head:
            n1 = n1 * 10 + head.val
            n2 = n2 + head.val * fact
            fact = fact * 10
            head = head.next
            pass
        return n1 == n2

# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         n1 = 0
#         n2 = 0
#         fact = 1
#         while head:
#             n1 = n1 * 10 + head.val
#             n2 = n2 + head.val * fact
#             fact = fact * 10
#             head = head.next
#             pass
#         return n1 == n2
        
# @lc code=end

