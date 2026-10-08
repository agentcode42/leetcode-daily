class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0
        for c in s:
            if c==")":
                depth-=1
            if depth>0:
                res.append(c)
            if c=="(":
                depth+=1
        return "".join(res)