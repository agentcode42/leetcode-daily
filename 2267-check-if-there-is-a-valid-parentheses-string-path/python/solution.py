class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        row,col = len(grid),len(grid[0])
        bal = 0
        if (row+col-1)%2!=0 :
            return False
        if grid[0][0]==")" or grid[row-1][col-1]=="(":
            return False
        @lru_cache(None)
        def dfs(i,j,bal):
            bal += 1 if grid[i][j]=='(' else -1
            if bal<0:
                return False
            remain = (row-1-i) + (col-1 -j)
            if bal>remain:
                return False
            if i==row-1 and j==col-1:
                return bal==0
            right,down = False,False
            if i<row-1:
                right = dfs(i+1,j,bal)
            if j<col-1:
                down = dfs(i,j+1,bal)
            return right or down
        return dfs(0,0,0)