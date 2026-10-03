class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res  = 0
        open_b=close_b=0

        for c in s:
            if c=="(":
                open_b += 1
            elif c==")":
                close_b += 1
            if open_b ==close_b:
                res = max(res,close_b*2)
            if close_b>open_b:
                open_b=close_b=0
        
        open_b=close_b=0

        for c in reversed(s):
            if c=="(":
                open_b += 1
            elif c==")":
                close_b += 1
            if open_b ==close_b:
                res = max(res,close_b*2)
            if close_b<open_b:
                open_b=close_b=0
        return res