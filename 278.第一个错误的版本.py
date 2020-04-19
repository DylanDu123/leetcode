#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n) -> bool:
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = left + ((right - left) // 2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

# @lc code=end
