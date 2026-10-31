class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9+7
        m,n = len(grid),len(grid[0])
        @cache
        def dfs(i,j,d):
            if i==m-1 and j==n-1:
                return 1
            if not 0<=i<m or not 0<=j<n:
                return 0
            
            if grid[i][j]==1:
                if d==0:
                    return dfs(i+1,j,1)%MOD
                else:
                    return dfs(i,j+1,0)%MOD
            return (dfs(i+1,j,1)+dfs(i,j+1,0))%MOD
        return dfs(0,0,0)
            