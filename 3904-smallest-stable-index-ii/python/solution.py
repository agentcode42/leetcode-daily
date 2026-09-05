class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix = [float('inf')]*n
        suffix[-1]=nums[-1]

        for i in reversed(range(n-1)):
            suffix[i]=min(suffix[i+1],nums[i])
        
        prefix = 0
        for i in range(n):
            prefix = max(prefix,nums[i])
            if prefix-suffix[i]<=k:
                return i
        return -1