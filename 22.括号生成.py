#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n):
        return self.generate(n, n, [], '')

    def generate(self, left, right, result, string):

        if left == 0 and right == 0:
            result.append(string)

        if left > 0:
            self.generate(left - 1, right, result, string + '(')

        if left < right:
            self.generate(left, right - 1, result, string + ')')

        return result


# if __name__ == "__main__":
#     result = Solution().generateParenthesis(3)
#     print(result)


# @lc code=end
