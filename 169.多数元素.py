#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#

# @lc code=start
import collections


class Solution:
    def majorityElement(self, nums: []) -> int:
        nums.sort()
        return nums[len(nums)//2]

# class Solution:
#     def majorityElement(self, nums: []) -> int:
#         counts = collections.Counter(nums)
#         return max(counts.keys(), key=counts.get)


if __name__ == "__main__":
    Solution().majorityElement([1, 1, 1, 2, 2])

# @lc code=end
