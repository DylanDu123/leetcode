#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start

import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = collections.Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx

        return -1


# if __name__ == "__main__":
#     Solution().firstUniqChar('dddccdbba')
#     pass
# @lc code=end
