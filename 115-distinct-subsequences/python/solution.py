class Solution:
    def numDistinct(self, s: str, t: str) -> int:
            n = len(s)
            m = len(t)
            dp = {}
            def dfs(i,j):
                if j==m:
                    return 1
                if i==n:
                    return 0
                if (i,j) in dp:
                    return dp[(i,j)]
                if s[i]==t[j]:
                    take = dfs(i+1,j+1)
                    skip = dfs(i+1,j)
                    dp[(i,j)]= take+skip
                else:
                    dp[(i,j)]= dfs(i+1,j)
                return dp[(i,j)]
            return dfs(0,0)


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
            n = len(s)
            m = len(t)
            dp = {}
            def dfs(i,j):
                if j==m:
                    return 1
                if i==n:
                    return 0
                if (n-i)<(m-j):
                    return 0
                if (i,j) in dp:
                    return dp[(i,j)]
                if s[i]==t[j]:
                    take = dfs(i+1,j+1)
                    skip = dfs(i+1,j)
                    dp[(i,j)]= take+skip
                else:
                    dp[(i,j)]= dfs(i+1,j)
                return dp[(i,j)]
            return dfs(0,0)