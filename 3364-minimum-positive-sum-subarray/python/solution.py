
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        res = float('inf')
        for i in range(n-l+1):
            total = sum(nums[i:i+l])
            if total>0:
                res = min(total,res)
            for j in range(i+l,min(i+r,n)):
                total+=nums[j]
                if total>0:
                    res = min(total,res)
        return -1 if res==float('inf') else res
            