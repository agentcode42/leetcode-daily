class Solution:
    def minOperations(self, s: str) -> int:
        mins = min(s)
        maxs = max(s)
        n = len(s)
        sort  = True
        for i in range(1,n):
            if s[i]<s[i-1]:
                sort=False
                break
        if sort:return 0
        if n==2:return -1
        if s[0]==mins or s[-1]==maxs:
            return 1
        mid = s[1:-1]
        if mins in mid or maxs in mid:
            return 2
        return 3