class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        max_res = 0
        for c in s:
            if c =="(":
                res+=1
                max_res = max(max_res,res)
            elif c==")":
                res-=1
        return max_res