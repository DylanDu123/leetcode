#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start


class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        return False if (len(set(nums)) == len(nums)) else True
# @lc code=end
