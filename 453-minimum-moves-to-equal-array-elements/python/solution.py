# These solution works 
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        res = 0
        min_val = min(nums)
        for n in nums:
            res+= (n-min_val)
        return res

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_val = min(nums)
        return sum((n-min_val) for n in nums)

# this one TLEs in leetcode solution 
# but this is brute force solution i came up with 
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)
        while len(set(nums))>1:
            idx_max_val = nums.index(max(nums))
            for i in range(n):
                if i!=idx_max_val:
                    nums[i]+=1
            count+=1
        return count
