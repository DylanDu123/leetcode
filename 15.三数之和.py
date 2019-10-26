#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        if len(nums) < 3 or nums == None:
            return []
        nums.sort()
        baseline = 0
        result = []
        while baseline <= len(nums) - 3 and nums[baseline] <= 0:
            left_index = baseline + 1
            right_index = len(nums) - 1
            while left_index < right_index:
                base_num = nums[baseline]
                left_num = nums[left_index]
                right_num = nums[right_index]
                num = base_num + left_num + right_num
                if num > 0:
                    right_index -= 1
                elif num < 0:
                    left_index += 1
                else:
                    while left_index < right_index and left_num == nums[left_index+1] :
                        left_index += 1
                    while left_index < right_index and right_num == nums[right_index-1]:
                        right_index -= 1
                    left_index += 1
                    right_index -= 1
                    result.append([base_num,left_num,right_num])
            while baseline <= len(nums) - 3 and nums[baseline] == nums[baseline +1]:
                baseline += 1
            baseline += 1
        return result

        
if __name__ == "__main__":
    print (Solution().threeSum([-1, 0, 1, 2, -1, -4]))
