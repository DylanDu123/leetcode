#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        if root == None:
            return []
        result = []
        stack = [root]
        while len(stack):
            temp = []
            temp2 = []
            for latest in stack:
                temp.append(latest.val)
                if latest.left:
                    temp2.append(latest.left)
                if latest.right:
                    temp2.append(latest.right)
                pass
            result.append(temp)
            stack = temp2
        return result

        
# @lc code=end

