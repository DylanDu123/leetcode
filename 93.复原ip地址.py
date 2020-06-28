#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start


class Solution:
    def restoreIpAddresses(self, s: str) -> [str]:
        if len(s) < 4 or len(s) > 12:
            return []

        def valid(c: str) -> bool:
            l = c.split(".")
            for i in l:
                if not(i) or int(i) > 255 or (i[0] == '0' and len(i) != 1):
                    return False
            return True

        result = []

        def backtrack(item, last_point, deep) -> [str]:
            if deep == 3:
                if valid(item):
                    result.append(item)
                return
            backtrack(
                item[:last_point + 1] +
                '.' + item[last_point + 1:],
                last_point + 2, deep + 1)
            backtrack(
                item[:last_point + 2] + '.' + item[last_point + 2:],
                last_point + 3, deep + 1)
            backtrack(
                item[:last_point + 3] + '.' + item[last_point + 3:],
                last_point + 4, deep + 1)

        backtrack(s, 0, 0)
        return result


# Solution().restoreIpAddresses("25525511135")
# 11111111
# @lc code=end
