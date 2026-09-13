class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        one1 = []
        one2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    one1.append((i,j))
                if img2[i][j]:
                    one2.append((i,j))
        if not one1 or not one2:
            return 0
        diff = []
        for x1,y1 in one1:
            for x2,y2 in one2:
                dx = x1-x2
                dy = y1-y2
                diff.append((dx,dy))
        
        count = Counter(diff)
        value = max(list(count.values()))
        return value