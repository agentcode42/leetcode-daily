
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nxt = [n]*n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]]<nums[i]:
                nxt[stack.pop()]=i
            stack.append(i)
        
        chain = [0]*(n+1)
        for i in range(n-1,-1,-1):
            chain[i]=nums[i]*(nxt[i]-i) + chain[nxt[i]]
        dq = deque()
        left = 0
        window_sum = 0
        res = 0
        for right in range(n):
            window_sum +=nums[right]

            while dq and nums[dq[-1]]<=nums[right]:
                dq.pop()
            dq.append(right)

            while True:
                c = dq[0]
                cost = chain[left]-chain[c] + nums[c]*(right - c+1)
                cost -=window_sum 
                if cost<=k:
                    break
                if dq[0]==left:
                    dq.popleft()

                window_sum -=nums[left]
                left+=1
            res+= right -left +1
        return res


















































