#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start

# f(1) = 1
# f(2) = max(1,2)
# f(3) = max(f(2),f(1)+3)
# f(n) = max(f(n-1),f(n-2)+n)

class Solution:
    def rob(self, nums: [int]) -> int:

        curr_max = 0
        pre_max = 0
        for num in nums:
            temp = pre_max
            pre_max = max(pre_max,curr_max+num)
            curr_max = temp
            pass
        return pre_max

        

# @lc code=end
