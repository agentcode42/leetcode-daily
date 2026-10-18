class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9+7
        def dfs(arr):
            n = len(arr)
            if n<3:
                return 1
            left = [a for a in arr if a<arr[0]]
            right = [a for a in arr if a>arr[0]]

            return dfs(left)*dfs(right)*comb(n-1,len(left))%MOD
        return (dfs(nums)-1)%MOD