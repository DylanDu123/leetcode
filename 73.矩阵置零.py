#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        columns = []
        rows = []

        for column_index in range(0,len(matrix)):
            for row_index in range(0,len(matrix[column_index])):
                if matrix[column_index][row_index] == 0:
                    columns.append(column_index)
                    rows.append(row_index)

        for column_index in range(0,len(matrix)):
            for row_index in range(0,len(matrix[column_index])):
                if column_index in columns or row_index in rows:
                    matrix[column_index][row_index] = 0


        """
        Do not return anything, modify matrix in-place instead.
        """
        
# @lc code=end

