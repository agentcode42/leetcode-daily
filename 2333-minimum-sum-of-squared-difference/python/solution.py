class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [abs(nums1[i]-nums2[i]) for i in range(n)]
        max_diff = max(diff)
        dp = [0]*(max_diff+1)
        for x in diff:
            dp[x]+=1
        
        k = k1+k2
        for i in range(max_diff,0,-1):
            take = min(k,dp[i])
            dp[i]-=take
            dp[i-1]+=take
            k-=take
            if k==0:
                break
        return sum(i*i*dp[i] for i in range(1,max_diff+1))
