#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> [str]:

        table = {"2": ["a","b","c"],
                 "3": ["d","e","f"],
                 "4": ["g","h","i"],
                 "5": ["j","k","l"],
                 "6": ["m","n","o"],
                 "7": ["p","q","r","s"],
                 "8": ["t","u","v"],
                 "9": ["w","x","y","z"]}
        result = []
        for digit in digits:
            values = table[digit]
            temp = result.copy()
            result.clear()
            if len(temp):
                for val in values:
                    for t in temp:
                        result.append(t+val)
            else:
                result = values.copy()
        return result
if __name__ == "__main__":
    print(Solution().letterCombinations('22'))
# @lc code=end
