#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start

# class Solution: # 冒泡排序 会超时
#     def sortArray(self, nums: [int]) -> [int]:
#         if len(nums) <= 1:
#             return nums

#         for i in range(1, len(nums)):
#             for j in range(0, len(nums) - i):
#                 if nums[j] > nums[j+1]:
#                     nums[j], nums[j + 1] = nums[j + 1], nums[j]
#         return nums


# class Solution:  # 插入排序 会超时
#     def sortArray(self, nums: [int]) -> [int]:
#         if len(nums) <= 1:
#             return nums
#         for i in range(1, len(nums)):
#             while nums[i] < nums[i - 1] and i > 0:
#                 nums[i], nums[i - 1] = nums[i - 1], nums[i]
#                 i -= 1
#             pass
#         return nums

class Solution:  # 归并排序 时间只能超过 28.38 %
    def sortArray(self, nums: [int]) -> [int]:
        if len(nums) <= 1:
            return nums
        mid = int(len(nums) / 2)
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
            pass
        result += left[i:]
        result += right[j:]
        return result


# @lc code=end
