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
        rows = len(matrix)
        if rows == 0:
            return False
        columns = len(matrix[0])
        if columns == 0:
            return False

        column = 0
        row = rows - 1
        while column < columns and row >= 0:
            number = matrix[row][column]
            if number == target:
                return True
            elif number > target:
                row -= 1
            else:
                column += 1
            pass
        return False

# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if len(matrix) <= 0 or len(matrix[0]) <= 0:
#             return False
#         column_count = len(matrix[0])

#         column_point = 0
#         row_point = len(matrix) - 1
#         while column_point < column_count and row_point >= 0:
#             num = matrix[row_point][column_point]
#             if num > target:
#                 row_point -= 1
#             elif num < target:
#                 column_point += 1
#                 pass
#             else:
#                 return True
#         return False


# if __name__ == "__main__":
#     result = Solution().searchMatrix([
#         [x for x in range(1, 4*4+2, 4)],
#         [x for x in range(2, 4*4+3, 4)],
#         [x for x in range(3, 4*4+4, 4)],
#         [x for x in range(10, 4*4+11, 4)],
#         [x for x in range(18, 4*4+19, 4)]
#     ], 12)
#     print(result)

# @lc code=end
