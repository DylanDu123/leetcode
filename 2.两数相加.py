#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumber(self,l1: ListNode, l2: ListNode,sale: int) -> ListNode:
        if l1 == None and l2 == None:
            if sale > 0:
                return ListNode(sale)
            return None

        value = (0 if l1==None else l1.val) + (0 if l2==None else l2.val)
        l = ListNode((value + sale)%10)
        sale = int(((value+sale)/10))
        l.next = self.addTwoNumber(None if l1==None else l1.next,None if l2==None else l2.next,sale)
        return l
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # result = self.addTwoNumber(l1,l2,0)
        result = ListNode(0)
        ne = result
        sale = 0
        while l1 or l2:
            l1_v = l1.val if l1 else 0
            l2_v = l2.val if l2 else 0
            value = l1_v + l2_v
            ne.next = ListNode((value + sale)%10)
            sale = int(((value+sale)/10))
            ne = ne.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            pass
        if sale > 0:
            ne.next = ListNode(sale)
            pass
        return result.next
    

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(8)
    l1.next.next = ListNode(3)   

    l2 = ListNode(0)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print(Solution().addTwoNumbers(l1,l2))   

