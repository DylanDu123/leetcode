#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
import math 
class Solution:
    def maxArea(self, height: [int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:

            left_num = height[left]
            right_num = height[right]
            area = max(area,((right - left) * min(left_num,right_num)))
            if left_num < right_num:
                left += 1
            else:
                right -= 1

            
        return area


# if __name__ == "__main__":
    # print (Solution().maxArea([10,14,10,4,10,2,6,1,6,12]))
