#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.

import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if root.left == None and root.right == None:
            return 1

        result = sys.maxsize
        if root.left:
            result = min(result, self.minDepth(root.left) + 1)

        if root.right:
            result = min(result, self.minDepth(root.right) + 1)

        return result


# a = TreeNode(1)
# a.left = TreeNode(2)
# r = Solution().minDepth(a)
# print(r)
# @lc code=end
