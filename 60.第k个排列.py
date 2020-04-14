#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start

# 假设 n = 6 k = 321 生成 nums = [1,2,3,4,5,6]
# 经分析 首位为 1 的数量有 5！个 首位为 2 的数量有 5！个，可得首位数字为 nums[k/5!]
# 将 nums 剔除 k/5! 位置
# 继续确定下位，从剩余的 nums 中找到  k % 5！ 排列的数
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        nums = [x for x in range(1, n + 1)]
        result = ''
        k -= 1
        while len(nums) > 0:
            factorial = math.factorial(len(nums) - 1)
            index = k // factorial
            num = nums[index]
            result = '{}{}'.format(result, num)
            nums.remove(num)
            k = k % factorial
            pass

        return result


# @lc code=end
