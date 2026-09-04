class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix = [0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=max(prefix[i-1],nums[i])
        
        suffix = [0]*n
        suffix[-1]=nums[-1]
        for i in reversed(range(n-1)):
            suffix[i]=min(suffix[i+1],nums[i])
        
        for i in range(n):
            if prefix[i]-suffix[i]<=k:
                return i
        return -1