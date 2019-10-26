#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 递归解
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None:
#             return head
#         next = head.next
#         head.next = self.swapPairs(next.next)
#         next.next = head
#         return next

# 循环解
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy
        
        while pointer.next is not None and pointer.next.next is not None:
            left = pointer.next
            right = pointer.next.next
            pointer.next = right
            left.next = right.next
            right.next = left
            pointer = left
            pass
        return dummy.next


def nodeFactory(length: int) -> ListNode:
    head = ListNode(0)
    pointer = head
    for index in range(1,length+1):
        node = ListNode(index)
        pointer.next = node
        pointer = node
        pass
    pass
    return head

# if __name__ == "__main__":
#     generate_node = nodeFactory(20)
#     generate_node = Solution().swapPairs(generate_node)
#     while generate_node.next is not None:
#         print (generate_node.val)
#         generate_node = generate_node.next
#         pass
#     pass

# @lc code=end

