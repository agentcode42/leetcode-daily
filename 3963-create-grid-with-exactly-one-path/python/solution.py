class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = ["."*n]

        for i in range(1,m):
            res.append("#"*(n-1)+".")
        return res
        
        