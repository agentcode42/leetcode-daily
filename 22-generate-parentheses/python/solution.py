class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        curr = []
        def dfs(i,bal):
            if i==2*n:
                if bal==0:
                    res.append("".join(curr))
                return
            if bal<0:
                return 
            if bal<n:
                curr.append("(")
                dfs(i+1,bal+1)
                curr.pop()
            if bal>0:
                curr.append(")")
                dfs(i+1,bal-1)
                curr.pop()
        dfs(0,0)
        return res