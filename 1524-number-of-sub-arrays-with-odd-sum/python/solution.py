class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        MOD = 10**9+7
        prefix = [0]*(n+1)
        odd = 0
        even = 1
        for i in range(n):
            prefix[i+1] =  (prefix[i] + arr[i])%2
            if prefix[i+1]%2:odd+=1
            else:even+=1
        MOD = 10**9+7
        return (even*odd)%MOD