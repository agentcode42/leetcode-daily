class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])

        direction = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(i,j):
            res = grid[i][j]
            grid[i][j]=0
            for dx,dy in direction:
                x,y = i+dx,j+dy
                if 0<=x<m and 0<=y<n and grid[x][y]>0:
                    res+=dfs(x,y)
            return res
        
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    if dfs(i,j)%k==0:
                        total+=1
        return total