#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
# 动态规划
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_sum = nums[0]
        for index in range(1, len(nums)):
            if nums[index - 1] > 0:
                nums[index] = nums[index] + nums[index - 1]
                pass
            max_sum = max(max_sum, nums[index])
        return max_sum

# 贪心算法
# 如果当前位置的数 大于和 则设置为起点
# 记录已知的最大的和
# class Solution:
#     def maxSubArray(self, nums: [int]) -> int:
#         if len(nums) == 0: return 0
#         if len(nums) == 1: return nums[0]
#         max_sum = cur_sum = nums[0]

#         for index in range(1,len(nums)):
#             cur_sum = max(nums[index],nums[index] + cur_sum)
#             max_sum = max(max_sum,cur_sum)
#         return max_sum
# if __name__ == "__main__":
    # Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

# @lc code=end
