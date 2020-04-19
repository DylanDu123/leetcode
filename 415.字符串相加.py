#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2, carry = len(num1) - 1, len(num2) - 1, 0
        result = ''
        while l1 >= 0 or l2 >= 0:
            n1 = num1[l1] if l1 >= 0 else 0
            n2 = num2[l2] if l2 >= 0 else 0
            result = str((int(n1) + int(n2) + carry) % 10) + result
            carry = (int(n1) + int(n2) + carry) // 10
            l1 -= 1
            l2 -= 1
            pass
        result = ('1'+result if carry == 1 else result)
        return result


# if __name__ == "__main__":
#     Solution().addStrings("99", "9")
#     pass
# @lc code=end
