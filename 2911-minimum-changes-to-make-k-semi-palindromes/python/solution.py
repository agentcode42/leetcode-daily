class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')
        cost = [[INF]*(n+1) for _ in range(n)]
        for i in range(n):
            for j in range(i+2,n+1):
                m = j-i
                for d in range(1,m):
                    if m%d:continue
                    changes = 0
                    group_len = m//d

                    for r in range(d):
                        for t in range(group_len//2):
                            left  = i+r+t*d
                            right = i + r + (group_len - 1 -t)*d
                            if s[left]!=s[right]:
                                changes+=1
                    cost[i][j] = min(cost[i][j],changes)
        dp = [[INF]*(k+1) for _ in range(n+1)]
        dp[0][0]=0
        for i in range(1,n+1):
            for p in range(1,k+1):
                for j in range(2*(p-1),i-1):
                    if dp[j][p-1]==INF:continue
                    dp[i][p] = min(
                        dp[i][p],
                        dp[j][p-1]+cost[j][i]
                    )
        return dp[n][k]

























