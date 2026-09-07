class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9+7
        last_total = [0]*26
        curr = 1
        for c in s:
            idx = ord(c)-ord('a')
            old = curr
            curr = (2*old-last_total[idx])%MOD
            last_total[idx]=old
        return (curr-1)%MOD
    

# dfs solution but only useful in understanding this problem 
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        seq = set()
        MOD = 10**9+7

        def dfs(i,curr):
            if i==n:
                if curr:
                    seq.add(curr)
                return 
            dfs(i+1,curr+s[i])
            dfs(i+1,curr)
        dfs(0,'')
        return len(seq)%MOD