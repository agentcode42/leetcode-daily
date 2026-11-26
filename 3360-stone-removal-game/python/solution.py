class Solution:
    def canAliceWin(self, n: int) -> bool:
        curr = 10
        a = True
        while curr>0:
            if curr<=n:
                n-=curr
                curr-=1
                a = not a
            else: return not a
        return not a