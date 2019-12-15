#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return False
        column_count = len(matrix[0])

        column_point = 0
        row_point = len(matrix) - 1
        while column_point < column_count and row_point >= 0:
            num = matrix[row_point][column_point]
            if num > target:
                row_point -= 1
            elif num < target:
                column_point += 1
                pass
            else:
                return True
        return False


if __name__ == "__main__":
    Solution().searchMatrix([[1, 1 ]], 2)

# @lc code=end
