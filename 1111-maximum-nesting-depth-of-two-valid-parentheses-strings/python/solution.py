class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        depth = 0
        for c in seq:
            if c=="(":
                depth+=1
                res.append(depth%2)
            elif c==")":
                res.append(depth%2)
                depth-=1
        return res