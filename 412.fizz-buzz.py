#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start


class Solution:
    def fizzBuzz(self, n: int) -> [str]:
        result = []
        for i in range(1, n+1):
            s = ''
            if i % 3 == 0:
                s = "Fizz"
            if i % 5 == 0:
                s = s+"Buzz"
            s = str(i) if len(s) == 0 else s
            result.append(s)
        return result

# @lc code=end
