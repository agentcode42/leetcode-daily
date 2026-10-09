class Solution:
    def minInsertions(self, s: str) -> int:
        left=right = 0
        for c in s:
            if c=="(":
                if right%2==1:
                    left+=1
                    right-=1
                right+=2
            else:
                right-=1
                if (right<0):
                    left+=1
                    right=1
        return left+right