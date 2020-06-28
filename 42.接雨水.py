#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start


class Solution:
    def trap(self, height: [int]) -> int:
        left, leftmax, right, rightmax = 0, 0, len(height) - 1, 0
        result = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    result += leftmax - height[left]
                left += 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    result += rightmax - height[right]
                right -= 1

            pass
        return result


# Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
# @lc code=end
