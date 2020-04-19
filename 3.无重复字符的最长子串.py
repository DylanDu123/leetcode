#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maps = {}
        result, left, length = 0, 0, 0
        for right, key in enumerate(s):
            if key in maps.keys() and maps[key] >= left:
                left = maps[key] + 1
                length = right - maps[key]
                pass
            else:
                length += 1
                result = max(result, length)
                pass
            maps[key] = right
        return result

# if __name__ == "__main__":
# print(Solution().lengthOfLongestSubstring('abcabcab'))
