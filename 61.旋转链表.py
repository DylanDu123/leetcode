#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head

        #一次循环 统计长度同时将其 组成环形链表
        pointer = head
        length = 1
        while pointer.next is not None:
            length += 1
            pointer = pointer.next
            pass
        pointer.next = head

        length = length - (k % length)
        pointer = head
        while length > 1:
            length -= 1
            pointer = pointer.next
            pass
        head = pointer.next
        pointer.next = None
        return head

if __name__ == "__main__":
    generate_node = nodeFactory(4)
    generate_node = Solution().rotateRight(generate_node,2)
    while generate_node is not None:
        print (generate_node.val)
        generate_node = generate_node.next
        pass
    pass
# @lc code=end

