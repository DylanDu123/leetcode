#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack, result = [root], []
        while len(stack):
            node = stack.pop()
            result.append(node.val)

            if node.left:
                stack.append(node.left)
                pass
            if node.right:
                stack.append(node.right)
                pass

        return result[::-1]

# @lc code=end
