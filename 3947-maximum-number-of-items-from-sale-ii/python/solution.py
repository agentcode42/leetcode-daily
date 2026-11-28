class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0]*(n+1)
        for factor,price in items:
            freq[factor]+=1
        
        gain = [0]*(n+1)
        for f in range(1,n+1):
            for j in range(f,n+1,f):
                gain[f]+=freq[j]
            gain[f]-=1
        items.sort(key=lambda x:x[1])

        res = 0
        min_price = items[0][1]
        for factor,price in items:
            if price>=min_price*2:
                break
            count = min(gain[factor],budget//price)
            res+= count*2
            budget-=count*price
            
        res+= budget//min_price
        return res






















