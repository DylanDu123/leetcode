#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start


class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        index = len(digits) - 1
        while index >= 0:
            digits[index] += 1
            digits[index] = digits[index] % 10
            if digits[index] != 0:
                return digits
            index -= 1
        digits = [0] * (len(digits) + 1)
        digits[0] = 1
        return digits
# if __name__ == "__main__":
#     print([0] * 2)
#     print(Solution().plusOne([9]))
# @lc code=end
