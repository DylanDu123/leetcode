#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start


class Solution:
    def permuteUnique(self, nums: []) -> [[]]:
        result = []

        def backtrack(first):
            if first == len(nums):
                result.append(nums[:])
                return

            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
                pass
        backtrack(0)

        return list(set([tuple(t) for t in result]))


# if __name__ == "__main__":
#     result = Solution().permuteUnique([1, 1,  2])
#     print(result)
#     pass
# @lc code=end
