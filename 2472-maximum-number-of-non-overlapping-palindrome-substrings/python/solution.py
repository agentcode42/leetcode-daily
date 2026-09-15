class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        next_end = [n]*n
        for center in range(n):
            #odd length
            left=right=center
            while left>=0 and right <n and s[left]==s[right]:
                if right-left+1>=k:
                    next_end[left]=min(next_end[left],right)
                left-=1
                right+=1

            #even length
            left = center
            right = center+1
            while left>=0 and right <n and s[left]==s[right]:
                if right-left+1>=k:
                    next_end[left]=min(next_end[left],right)
                left-=1
                right+=1
        @cache
        def dfs(i):
            if i>=n:
                return 0                
            res = dfs(i+1) #skip this 
            if next_end[i]<n:
                res = max(res,1 + dfs(next_end[i]+1))
            return res
        return dfs(0)