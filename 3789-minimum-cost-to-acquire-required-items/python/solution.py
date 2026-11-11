class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total = cost1*need1 + cost2*need2
        cost3 = costBoth
        total1 = 0
        if need1<need2:
            total1 = cost3*need1 + cost2*(need2-need1)
        else:
            total1 = cost3*need2 + cost1*(need1-need2)
        
        total2 = cost3 * max(need1,need2)
        return min(total,total1,total2)

        