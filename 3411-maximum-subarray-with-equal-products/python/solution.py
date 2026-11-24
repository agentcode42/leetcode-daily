class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        res =0
        for i in range(n):
            p= l = g = nums[i]
            for j in range(i+1,n):
                p = nums[j]*p
                l = lcm(l,nums[j])
                g = gcd(g,nums[j])
                if p>g*l:
                    break
                if p==g*l:
                    res = max(res,j-i+1)
        return res