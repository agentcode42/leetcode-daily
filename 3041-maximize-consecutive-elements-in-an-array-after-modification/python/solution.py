
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        mx = max(nums)
        freq = [0] * (mx + 2)

        for x in nums:
            freq[x] += 1

        dp = [0] * (mx + 2)
        res = 0

        for x in range(1, mx + 1):
            for _ in range(freq[x]):
                dp[x + 1] = dp[x] + 1
                dp[x] = dp[x - 1] + 1
                res = max(res, dp[x], dp[x + 1])

        return res
