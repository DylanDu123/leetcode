#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        digits = [0]*(len(num1) + len(num2))
        for i1, n1 in enumerate(reversed(num1)):
            for i2, n2 in enumerate(reversed(num2)):
                num = int(n1) * int(n2)
                digits[i1 + i2 + 1] += (digits[i1 + i2] + num) // 10
                digits[i1 + i2] = (digits[i1 + i2] + num) % 10

        return ''.join([str(s) for s in list(reversed(digits))]).lstrip('0')


# @lc code=end
