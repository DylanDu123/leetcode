#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
import sys
class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        if len(nums) < 3 or nums == None:
            return []
        nums.sort()
        baseline = 0
        last_target = sys.maxsize
        result = None
        while baseline <= len(nums) - 3 :
            left_index = baseline + 1
            right_index = len(nums) - 1
            while left_index < right_index:
                base_num = nums[baseline]
                right_num = nums[right_index]
                left_num = nums[left_index]
                num = base_num + left_num + right_num 

                flag = max(target,num) - min(target,num)
                if flag >= last_target:
                    if num >= target:
                        right_index -= 1
                    else:
                        left_index += 1
                    pass
                elif flag == 0:
                    return num
                else:
                    last_target = flag
                    result = num
                    pass

            while baseline <= len(nums) - 3 and nums[baseline] == nums[baseline +1]:
                baseline += 1
            baseline += 1
        return result
        

if __name__ == "__main__":
    print (Solution().threeSumClosest([1,1,1,1],0))
    pass
    