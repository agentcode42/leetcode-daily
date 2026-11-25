class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        MOD = 10**9+7
        BASE = 10007
        n = len(nums)
        h = [0]*(n+1)
        prefix = [0]*(n+1)
        prefix[0]=1
        for i in range(n):
            h[i+1] = (h[i]*BASE + nums[i])%MOD
            prefix[i+1] = prefix[i]*BASE %MOD

        def check(l):
            count = defaultdict(int)
            for i in range(n-l+1):
                j = i+l
                key = (h[j]-h[i]*prefix[l]%MOD + MOD )%MOD
                count[key]+=1
            for c in count.values():
                if c==1:
                    return True
            return False

        low , high = 1,n
        while low<high:
            mid = (low+high)//2
            if check(mid):
                high = mid
            else:
                low = mid+1
        return low

























