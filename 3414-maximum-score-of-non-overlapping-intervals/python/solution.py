class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        inv = []
        n = len(intervals)
        for i in range(n):
            start,end,val = intervals[i]
            inv.append([start,end,val,i])
        inv.sort()
        starts = [x[0] for x in inv]
        @cache
        def dfs(i,k):
            if i>=n or k==0:
                return (0,[])

            start,end,val,index = inv[i]
            next_i = bisect_right(starts,end)
            skip = dfs(i+1, k)
            score,arr = dfs(next_i,k-1)
            take = (score+val,sorted([index] + arr))
            if take[0]>skip[0]:
                return take
            elif take[0]<skip[0]:
                return skip
            return min(take,skip)
        return dfs(0,4)[1]