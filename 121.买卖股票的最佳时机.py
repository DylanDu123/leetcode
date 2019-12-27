#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
import sys
# @lc code=start


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if len(prices) < 2:
            return 0
        minprice = sys.maxsize
        profit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > profit:
                profit = price - minprice
                pass
            pass
        return profit


# @lc code=end
