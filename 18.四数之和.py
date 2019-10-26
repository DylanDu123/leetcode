#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        if len(nums) < 4 or nums == None:
            return []
        nums.sort()
        base_left_index = 0
        while base_left_index <= len(nums) - 4:
            base_right_index = base_left_index + 1
            while base_right_index <= len(nums) - 3:
                pass
            
            while base_left_index < len(nums) - 4 and nums[base_left_index] == nums[base_left_index +1]:
                base_left_index += 1
                pass
            base_left_index += 1
            pass


        pass
