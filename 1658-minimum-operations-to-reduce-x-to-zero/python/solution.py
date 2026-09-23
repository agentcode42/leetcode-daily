class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total-x
        n = len(nums)
        if target<0:
            return -1
        if target==0:
            return n
        left=0
        res = -1
        curr = 0
        for right in range(n):
            curr+=nums[right]
            while target<curr:
                curr-=nums[left]
                left+=1
            if target==curr:
                res = max(res,right-left+1)
        return n-res if res!=-1 else -1
    
'''
MEMORY LIMIT EXIT SOLUTION
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        curr_x = [x]
        @cache
        def dfs(left,right):
            if left>right or right<left:
                if curr_x[0]==0:
                    return (True,0)
                else:
                    return (False,-1)
            if curr_x[0]==0:
                return (True,0)
            l,r = (False,-1),(False,-1)
            if nums[left]<=curr_x[0]:
                curr_x[0]-=nums[left]
                l=dfs(left+1,right)
                curr_x[0]+=nums[left]
            if nums[right]<=curr_x[0]:
                curr_x[0]-=nums[right]
                r=dfs(left,right-1)
                curr_x[0]+=nums[right]
            
            if l[0] and r[0]:
                return (True,min(l[1],r[1])+1)
            elif l[0]:
                return (l[0],l[1]+1)
            elif r[0]:
                return (r[0],r[1]+1)
            else:
                return (False,-1)
            
        return dfs(0,len(nums)-1)[1]
'''