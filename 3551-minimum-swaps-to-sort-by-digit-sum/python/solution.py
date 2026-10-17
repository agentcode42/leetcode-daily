class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sums(x):
            s = 0
            while x>0:
                s += x%10
                x = x//10
            return s

        sorted_nums = sorted(nums,key = lambda x:(digit_sums(x),x))

        index = {}
        for i,num in enumerate(nums):
            index[num]=i 
        
        res = 0
        for i,curr in enumerate(sorted_nums):
            idx = index[curr]
            if idx==i:
                continue
            displaced = nums[i]
            nums[i],nums[idx]=nums[idx],nums[i]
            index[curr]=i
            index[displaced]=idx
            res+=1
        return res