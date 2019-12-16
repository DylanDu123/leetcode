#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        # 逐个遍历 记录当前行 当前列是否出现过这个数字
        # 分配9个背包 判断3✖️3宫内是否只出现了一次
        if len(board) != 9:
            return False
        row_table = {}
        colmun_table = {}
        pack_table = {}

        for index in range(0,9):
            row_table[index] = []
            colmun_table[index] = []
            pack_table[index] = []
            pass

        for row_index in range(0,len(board)):
            row = board[row_index]
            if len(row) != 9:
                return False;
            for column_index in range(0,len(row)):
                num = board[row_index][column_index]
                pack_index = int(row_index/3)*3 + int(column_index/3)
                if num == '.':
                    continue

                if num in row_table.get(row_index,[]):
                    return False
                elif num in colmun_table.get(column_index,[]):
                    return False
                elif num in pack_table.get(pack_index,[]):
                    return False
                row_table.get(row_index,[]).append(num) 
                colmun_table.get(column_index,[]).append(num)
                pack_table.get(pack_index,[]).append(num)
                pass
            pass
        return True

# if __name__ == "__main__":
#     Solution().isValidSudoku([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
# )
#     pass
        
# @lc code=end

