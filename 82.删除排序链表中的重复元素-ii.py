#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def nodeFactory(length: int) -> ListNode:
    head = ListNode(1)
    pointer = head
    for index in range(2,length+2):
        node = ListNode(index)
        pointer.next = node
        pointer = node
        pass
    pass
    pointer.next = None
    return head

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy
        fast_pointer = head
        while fast_pointer:

            while fast_pointer.next and fast_pointer.val == fast_pointer.next.val:
                fast_pointer = fast_pointer.next
                pass

            if pointer.next == fast_pointer:
                pointer = fast_pointer
            else:
                pointer.next = fast_pointer.next
            pass
            fast_pointer = fast_pointer.next
        
        return dummy.next


# @lc code=end

