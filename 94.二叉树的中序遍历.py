#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
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
    def inorderTraversal(self, root: TreeNode) -> [int]:
        result, curr, stack = [], root, []
        while len(stack) or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            result.append(node.val)
            curr = node.right

        return result

    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        if len(nums):
            mid = int(len(nums)/2)
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root
        return None

# @lc code=end
