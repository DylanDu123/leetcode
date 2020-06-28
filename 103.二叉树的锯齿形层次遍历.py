#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        if root == None:
            return []
        result, stack, left = [], collections.deque([root]), False
        while len(stack):
            items = []
            for _ in range(0, len(stack)):
                node = stack.popleft()
                items.append(node.val)
                stack.append(node.left) if node.left else None
                stack.append(node.right) if node.right else None
            result.append(items[::-1] if left else items)
            left = False if left else True
        return result


# @lc code=end
