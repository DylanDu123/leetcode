#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start


class ListNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.valus = {}
        self.capacity = capacity
        self.count = 0
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        pass

    def remove(self, node):
        self.count -= 1
        tail = node.next
        tail.prev = node.prev
        node.prev.next = tail
        self.valus.pop(node.key)
        pass

    def add(self, node):
        self.count += 1
        first = self.head.next

        first.prev = node
        node.next = first

        self.head.next = node
        node.prev = self.head

        self.valus[node.key] = node
        if self.count > self.capacity:
            self.remove(self.tail.prev)
            pass
        pass

    def moveTop(self, node):
        self.remove(node)
        self.add(node)
        pass

    def get(self, key: int) -> int:
        if key in self.valus.keys():
            value = self.valus[key]
            self.moveTop(value)
            return value.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.valus.keys():
            node = self.valus[key]
            node.val = value
            self.moveTop(node)
        else:
            self.add(ListNode(value, key))
            pass
# @lc code=end
