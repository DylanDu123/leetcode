#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
import sys
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True
        stack = []
        inorder = -sys.maxsize - 1
        while len(stack) or root != None:
            while root != None:
                stack.append(root)
                root = root.left
                pass
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True

# if __name__ == "__main__":
#     t=TreeNode(2)
#     l=TreeNode(1)
#     r=TreeNode(3)
#     t.left = l
#     t.right = r
#     Solution().isValidBST(t)
#     pass
# @lc code=end
