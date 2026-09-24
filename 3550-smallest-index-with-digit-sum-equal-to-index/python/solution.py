class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            total = 0
            while n>0:
                total += n%10
                n = n//10
            if total==i:
                return i
        return -1