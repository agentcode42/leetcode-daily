class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        res = set()
        def dfs(s):
            r = s.find('}')
            if r==-1:
                res.add(s)
                return 
            l = 0
            for i in range(r-1,-1,-1):
                if s[i]=='{':
                    l = i
                    break
            mid = s[l+1:r].split(',')
            left= s[:l]
            right =s[r+1:]
            for ch in mid:
                dfs(left+ch+right)
        dfs(expression)
        return sorted(res)