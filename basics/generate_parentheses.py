from typing import List

# The idea is to add ')' only after valid '('
# We use two integer variables left & right to see how many '(' & ')' are in the current string
# If left < n then we can add '(' to the current string
# If right < left then we can add ')' to the current string

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(left, right, str):
            if len(str) == n * 2:
                ret.append(str)
                return
            if left < n:
                dfs(left + 1, right, str + '(')
            if right < left:
                dfs(left, right + 1, str + ')')
        
        ret = []
        dfs(0, 0, "")
        return ret


if __name__ == "__main__":

    strs = Solution().generateParenthesis(11)
    for s in strs:
        print(s)
            

  