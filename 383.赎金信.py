#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return False if collections.Counter(ransomNote) - collections.Counter(magazine) else True

# @lc code=end
