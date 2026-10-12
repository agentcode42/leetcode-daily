class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        res = 0
        count = [0]*32
        for n in nums:
            for i in range(32):
                if n & (1<<i):
                    count[i]+=1
        
        for _ in range(k):
            binary =""
            for i in range(31,-1,-1):
                if count[i]>0:
                    binary+="1"
                    count[i]-=1
                else:
                    binary+="0"
            x = int(binary,2)
            res = (res+x*x)%MOD
        return res



class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        res = 0
        count = [0]*32
        for n in nums:
            for i in range(32):
                if n & (1<<i):
                    count[i]+=1
        
        for _ in range(k):
            x = 0
            for i in range(31,-1,-1):
                if count[i]>0:
                    x|=1<<i
                    count[i]-=1                    
            res = (res+x*x)%MOD
        return res