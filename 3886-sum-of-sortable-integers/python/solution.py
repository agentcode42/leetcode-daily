class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n= len(nums)
        res = 0
        for k in range(1,n+1):
            if n%k:
                continue
            flag = True
            prev_max = 0
            for i in range(0,n,k):
                count = 0
                max_n = min_n = nums[i]
                for j in range(k):
                    a = nums[i+j]
                    b = nums[i + (j+1)%k]
                    if a>b:
                        count+=1
                    min_n = min(a,min_n)
                    max_n = max(a,max_n)
                if count>1 or prev_max>min_n:
                    flag = False
                    break
                prev_max = max_n
            if flag:
                res+=k
        return res
