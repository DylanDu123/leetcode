#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prep = None
#         curr = head
#         while curr != None:
#             temp = curr.next
#             curr.next = prep
#             prep = curr
#             curr = temp
#             pass
#         return prep
        
# @lc code=end

