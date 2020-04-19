#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start


class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 0:
            return '/'
        stack = []
        paths = path.split("/")
        for r in paths:
            if r == "..":
                if len(stack):
                    stack.pop()
            elif r == "" or r == ".":
                continue
            else:
                stack.append(r)
        return "/" + "/".join(stack)


# re = Solution().simplifyPath("/a/../../b/../c//.//")
# print(re)
# @lc code=end
