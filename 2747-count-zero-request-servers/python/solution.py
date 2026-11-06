class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda x:x[1])
        queue = [(i,q) for i,q in enumerate(queries)]
        queue.sort(key = lambda x:x[1])
        res = [0]*len(queue)

        l,r = 0,0
        count = defaultdict(int)
        for i,q in queue:
            while r<len(logs) and logs[r][1]<=q:
                count[logs[r][0]]+=1
                r+=1
            
            while l<r and logs[l][1]<q-x:
                count[logs[l][0]]-=1
                if count[logs[l][0]]==0:
                    del count[logs[l][0]]
                l+=1
            res[i]= n- len(count)
        return res
            
