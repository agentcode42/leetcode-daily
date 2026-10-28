class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[[-1]*1024 for _ in range(n)]for _ in range(m)]
        def dfs(i,j,curr_xor):
            curr_xor = curr_xor^grid[i][j]
            if i==m-1 and j==n-1:
                return curr_xor
            if dp[i][j][curr_xor] !=-1:
                return dp[i][j][curr_xor]
            
            right=down = float('inf')
            if j<n-1:
                right = dfs(i,j+1,curr_xor)
            if i<m-1:
                down = dfs(i+1,j,curr_xor)
            
            dp[i][j][curr_xor]= min(right,down)
            return dp[i][j][curr_xor]
        return dfs(0,0,0)
