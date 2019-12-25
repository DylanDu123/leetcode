#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        stack = [{'val': root, 'deep': 1}]
        result = 0
        while len(stack):
            value = stack.pop()
            node = value['val']
            deep = value['deep']
            result = max(result, deep)
            if node.left:
                stack.append({'val':node.left,'deep':deep+1})

            if node.right:
                stack.append({'val':node.right,'deep':deep+1})
        return result
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         return self.caculate(root,0)
#         pass
#     def caculate(self,root:TreeNode,deep: int):
#         if root == None:
#             return deep
#         return max(self.caculate(root.left,deep+1),self.caculate(root.right,deep+1))

# @lc code=end
