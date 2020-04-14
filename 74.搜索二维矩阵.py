#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start

# 二分法


class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right)//2
            row = mid // n
            column = mid % n
            if matrix[row][column] > target:
                right = mid - 1
            elif matrix[row][column] < target:
                left = mid + 1
            else:
                return True
        return False

# @lc code=end
