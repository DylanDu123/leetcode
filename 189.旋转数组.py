#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start


class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        point = (k % len(nums))
        dummy = list(reversed(nums))
        nums[0:point] = reversed(dummy[0:point])
        nums[point:len(nums)] = reversed(dummy[point:len(nums)])

# if __name__ == "__main__":
#     array = [1,2,3,4,5,6,7]
#     Solution().rotate(array,3)
#     print(array)
# @lc code=end
