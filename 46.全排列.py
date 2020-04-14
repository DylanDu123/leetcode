#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start

# 两个函数的原理区别  nums[:] 会生成一个新的数组 不需要担心被更改


# class Solution:
#     def permute(self, nums: []) -> [[]]:

#         result = []

#         def backtrack(first, aNums):
#             if first == len(aNums):
#                 result.append(aNums)
#             for i in range(first, len(aNums)):
#                 tNums = aNums.copy()
#                 tNums[first], tNums[i] = tNums[i], tNums[first]
#                 backtrack(first+1, tNums)

#         backtrack(0, nums)
#         return result


class Solution:
    def permute(self, nums: []) -> [[]]:
        result = []

        def backtrack(first):
            if first == len(nums):
                result.append(nums[:])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return result
# @lc code=end
