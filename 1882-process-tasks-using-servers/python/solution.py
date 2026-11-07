class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)

        avaliable = [(w,i) for i,w in enumerate(servers)]
        heapq.heapify(avaliable)
        busy = []
        res = []
        time = 0

        for i , duration in enumerate(tasks):
            time = max(time,i)

            while busy and busy[0][0]<=time:
                end,w,idx = heapq.heappop(busy)
                heapq.heappush(avaliable,(w,idx))
            
            if not avaliable :
                time = busy[0][0]
                while busy and busy[0][0]<=time:
                    end,w,idx = heapq.heappop(busy)
                    heapq.heappush(avaliable,(w,idx))
            w,idx = heapq.heappop(avaliable)
            res.append(idx)
            heapq.heappush(busy,(time+duration,w,idx))
        return res