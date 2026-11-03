class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxm = max(nums)
        return sum(maxm-n for n in nums)