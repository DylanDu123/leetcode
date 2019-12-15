#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if len(prices) < 2:
            return 0
        result = 0
        for index in range(1, len(prices)):
            if prices[index] > prices[index - 1]:
                result += prices[index] - prices[index-1]
                pass
            pass
        return result


# @lc code=end
