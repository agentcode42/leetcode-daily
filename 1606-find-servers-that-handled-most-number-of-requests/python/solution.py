class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        n = len(arrival)
        if n<=k:
            return list(range(n))
        available = SortedList(range(k))
        busy = []
        count = [0]*k
        max_count = 0

        for i,(start,curr_load) in enumerate(zip(arrival,load)):
            while busy and busy[0][0]<=start:
                _ , curr_idx = heappop(busy)
                available.add(curr_idx)
            
            if available:
                s = i%k
                pos = available.bisect_left(s)
                if pos == len(available):
                    pos = 0
                idx = available.pop(pos)

                heappush(busy,(start+curr_load,idx))
                count[idx]+=1
                max_count = max(max_count,count[idx])
        
        res = []
        for i,c in enumerate(count):
            if c== max_count:res.append(i)
        return res























