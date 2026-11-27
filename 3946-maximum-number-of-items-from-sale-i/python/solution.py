class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        dp = [0]*(budget+1)
        min_price = float('inf')
        for i in range(n):
            factor , price = items[i]
            min_price = min(min_price,price)
            count = 0
            for j in range(n):
                if items[j][0]%factor==0:
                    count+=1
            
            for b in range(budget,price-1,-1):
                dp[b] = max(dp[b],dp[b-price]+count)
        
        return max(dp[b] + (budget-b)//min_price for b in range(budget+1))


























