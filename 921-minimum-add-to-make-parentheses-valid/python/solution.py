class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        res = 0
        for c in s:
            if c=="(":
                count+=1
            else:
                count-=1
                if count<0:
                    res+=1
                    count+=1
        return res+count