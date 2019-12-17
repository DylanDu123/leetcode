#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l2_index = n - 1
        l1_index = m - 1
        while l2_index >= 0 and l1_index >= 0:
            l1_num = nums1[l1_index]
            l2_num = nums2[l2_index]
            if l1_num > l2_num:
                nums1[l2_index + l1_index + 1] = l1_num
                l1_index -= 1
            else:
                nums1[l2_index + l1_index + 1] = l2_num
                l2_index -= 1
            pass
        if l2_index >= 0:
            nums1[0:l2_index+1] = nums2[0:l2_index+1]
            pass
# if __name__ == "__main__":
#     Solution().merge([0],0,[1],1)
# @lc code=end

