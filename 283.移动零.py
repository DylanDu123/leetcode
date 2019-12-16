#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2 :
            return
        point = 0
        for fast_point in range(0,len(nums)):
            if nums[fast_point] != 0:
                nums[point],nums[fast_point] = nums[fast_point],nums[point]
                point += 1
                pass
            pass


    
# @lc code=end

