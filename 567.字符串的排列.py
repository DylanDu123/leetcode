#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1, c2 = [0] * 26, [0] * 26
        for i in range(0, len(s1)):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1
            pass
        for i in range(len(s1), len(s2)):
            if self.cmp(c1, c2):
                return True
            c2[ord(s2[i]) - ord('a')] += 1
            c2[ord(s2[i-len(s1)]) - ord('a')] -= 1

        return self.cmp(c1, c2)

    def cmp(self, a1: [], a2: []) -> bool:
        for i in range(0, 26):
            if a1[i] != a2[i]:
                return False
            pass
        return True


# re = Solution().checkInclusion('ab', 'eidboaoo')
# print(re)
# @lc code=end
