#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
# 
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if strs == None or len(strs) == 0:
            return ''

        for index in range(0,len(strs[0])+1):
            f = strs[0][0:index]
            for s in strs:
                if s.startswith(f) == False:
                    return strs[0][0:index-1]
        return strs[0] 

   

# class Solution:
#     def longestCommonPrefix(self, strs: [str]) -> str:
#         if strs == None or len(strs) == 0:
#             return ''
#         flag = strs[0]
#         left = 0
#         right = len(flag)
#         while left < right:
#             mid = int((right+left + 1)/2)
#             if self.cmpstr(strs,mid):
#                 left = mid
#             else:
#                 right = mid - 1
#         return flag[0:min(left,right)]
    
#     def cmpstr(self,strs: [str],len) -> bool:
#         flag = strs[0][0:len]
#         for s in strs:
#             if s.startswith(flag) == False:
#                 return False
#         return True

# if __name__ == "__main__":
    # Solution().longestCommonPrefix(['aa','a','aaa'])


        
# @lc code=end

