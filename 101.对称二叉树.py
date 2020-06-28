#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if root == None:
#             return True
#         return self.compare(root.left, root.right)

#     def compare(self, left: TreeNode, right: TreeNode) -> bool:
#         if left == None and right == None:
#             return True
#         if left == None or right == None:
#             return False
#         if left.val != right.val:
#             return False
#         return self.compare(left.left, right.right) and self.compare(left.right, right.left)

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if root == None:
#             return True
#         left_stack = [root]
#         right_stack = [root]
#         while len(left_stack):
#             left = left_stack.pop()
#             right = right_stack.pop()
#             if left == None and right == None:
#                 continue
#             if left == None or right == None:
#                 return False
#             if left.val != right.val:
#                 return False
#             left_stack.append(left.left)
#             right_stack.append(right.right)
#             left_stack.append(left.right)
#             right_stack.append(right.left)
#             pass

#         return True

# @lc code=end
