#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start


class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        result = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        nums1_point = 0
        nums2_point = 0
        while nums1_point < len(nums1) and nums2_point < len(nums2):
            num1 = nums1[nums1_point]
            num2 = nums2[nums2_point]
            if num1 == num2:
                result.append(num1)
                nums1_point += 1
                nums2_point += 1
            elif num1 < num2:
                nums1_point += 1
            else:
                nums2_point += 1
        return result

# @lc code=end
