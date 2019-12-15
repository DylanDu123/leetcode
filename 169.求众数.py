#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#

# @lc code=start


class Solution:
    def majorityElement(self, nums: [int]) -> int:
        group = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                group = num
                count = 1
                continue
            if num == group:
                count += 1
            else:
                count -= 1
        
        return group


# @lc code=end
