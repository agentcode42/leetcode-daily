class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        small = nsmallest(3, nums)
        large = nlargest(3, nums)

        diff1 = large[0] - small[2]
        diff2 = large[1] - small[1]
        diff3 = large[2] - small[0]

        return min(diff1, diff2, diff3)


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()

        diff1 = nums[-3] - nums[0]
        diff2 = nums[-2] - nums[1]
        diff3 = nums[-1] - nums[2]

        return min(diff1, diff2, diff3)
