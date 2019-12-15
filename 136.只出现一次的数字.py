#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        result = 0
        for num in nums:
            result = result^num
            pass
        return result

# if __name__ == "__main__":
    # print(1^0)
        
# @lc code=end

