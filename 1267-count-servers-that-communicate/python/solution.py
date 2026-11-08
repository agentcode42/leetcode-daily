class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        r_count = [0]*rows
        c_count = [0]*cols
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    r_count[r]+=1
                    c_count[c]+=1
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    if max(r_count[r],c_count[c])>1:
                        res+=1
        return res