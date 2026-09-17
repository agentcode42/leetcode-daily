class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = 2*n #or (INF)
        prefix = [best]*n
        curr= 0
        left = 0
        for right in range(n):
            curr += arr[right]

            while curr>target and left<right:
                curr -=arr[left]
                left+=1
            
            if curr==target:
                length = right-left+1
                best = min(best,length)
            prefix[right]=best
        
        best = 2*n #or (INF)
        suffix = [best]*n
        curr= 0
        right = n-1
        for left in range(n-1,-1,-1):
            curr += arr[left]

            while curr>target and left<right:
                curr -=arr[right]
                right-=1
            
            if curr==target:
                length = right-left+1
                best = min(best,length)
            suffix[left]=best
        
        res = 2*n
        for i in range(n-1):
            res = min(res,prefix[i]+suffix[i+1])
        return res if res!=2*n else -1
