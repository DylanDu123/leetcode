#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        if len(nums) < 2:
            return []
        table = {}
        for index in range(0,len(nums)):
            num = nums[index]
            if num in table.keys():
                return [table[num], index]
            else:
                remain = target - num
                table[remain] = index

        return []
# if __name__ == "__main__":
#     print(Solution().twoSum([2,7,11,15],9))
    # pass
# @lc code=end
