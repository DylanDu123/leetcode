#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        a = 0
        b = 0
        for num in nums:
            a = (a^num) & ~b
            b = (b^num) & ~a
            pass
        return a
# 0 ^ x = x,
# x ^ x = 0；
# x & ~x = 0,
# x & ~0 =x;

# 第一次出现 将数值记录到a中
# 第二次出现 将a值清除，将数值记录到b中
# 第三次出现 将b值清除

# if __name__ == "__main__":

    # print(Solution().singleNumber([3,3,3,2]))
    # pass
# @lc code=end

