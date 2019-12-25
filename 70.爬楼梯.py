#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        result = {}
        result[1] = 1
        result[2] = 2
        for index in range(3,n+1):
            result[index] = result[index-1]+result[index-2]
            pass
        return result[n]


# 栈开销太多容易卡死
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         return self.climbStairs(n-1) + self.climbStairs(n-2)

# if __name__ == "__main__":
#     print(Solution().climbStairs(10))
# @lc code=end
