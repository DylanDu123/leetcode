#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start


class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        l = size - 1
        for row in range(0, int(size/2)):
            for column in range(0, int((size + 1)/2)):
                temp = matrix[row][column]
                matrix[row][column] = matrix[l-column][row]
                matrix[l-column][row] = matrix[l-row][l-column]
                matrix[l-row][l-column] = matrix[column][l-row]
                matrix[column][l-row] = temp
            pass


# if __name__ == "__main__":
#     l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     Solution().rotate(l)
#     print(l)
# @lc code=end
