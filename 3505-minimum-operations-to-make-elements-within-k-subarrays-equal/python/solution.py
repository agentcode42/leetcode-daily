
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        left  = SortedList(nums[:x])
        right  = SortedList()

        while len(left)>(x+1)//2:
            right.add(left.pop())
        
        left_sum = sum(left)
        right_sum = sum(right)

        def add(num):
            nonlocal left_sum ,right_sum

            if num<=left[-1]:
                left.add(num)
                left_sum+=num
            else:
                right.add(num)
                right_sum+=num

        def remove(num):
            nonlocal left_sum ,right_sum

            if num in left:
                left.remove(num)
                left_sum-=num
            else:
                right.remove(num)
                right_sum-=num
        def balance():
            nonlocal left_sum ,right_sum

            while len(left)>(x+1)//2:
                val = left.pop()
                left_sum-=val
                right.add(val)
                right_sum+=val
            
            while len(left)<(x+1)//2:
                val = right.pop(0)
                right_sum-=val
                left.add(val)
                left_sum+=val
                
        costs = []

        for i in range(n-x+1):
            mid = left[-1]

            moves = (mid*len(left) - left_sum) + (right_sum - mid*len(right))
            costs.append(moves)

            if i<n-x:
                add(nums[i+x])
                remove(nums[i])
                balance()
        
        dp = [[float('inf')]*(k+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=0
        for i in range(1,n+1):
            for j in range(1,k+1):
                dp[i][j]=dp[i-1][j]
                if i>=x:
                    take = dp[i-x][j-1] + costs[i-x]
                    dp[i][j]=min(dp[i][j],take)
        return dp[n][k]



















