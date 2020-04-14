#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start


class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = list(filter(lambda e:  e.isalnum(), [v for v in s.lower()]))
        return r == r[::-1]


# @lc code=end
