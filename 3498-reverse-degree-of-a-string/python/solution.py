class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i,ch in enumerate(s):
            alpha_index = 26-(ord(ch)-ord('a'))
            res+=alpha_index*(i+1)
        return res