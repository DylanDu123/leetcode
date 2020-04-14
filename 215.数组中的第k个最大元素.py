#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
import heapq
# @lc code=start


class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
# @lc code=end
