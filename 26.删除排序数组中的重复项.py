#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        point = 0
        fast_point = 1
        while fast_point < len(nums):

            if nums[point] != nums[fast_point]:
                point += 1
                nums[point] = nums[fast_point]
            fast_point += 1

        return point+1

# @lc code=end
