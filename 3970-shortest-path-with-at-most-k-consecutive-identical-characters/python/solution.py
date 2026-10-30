class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
        
        dist = [[float('inf')]*(k+1) for _ in range(n)]
        dist[0][1]=0
        heap = [(0,0,1)] #total cost, curr node , consecutive count
        while heap:
            cost,node,count = heappop(heap)
            if cost>dist[node][count]:
                continue
            for nei,weight in adj[node]:
                if labels[node]==labels[nei]:
                    new_count = count+1
                else:
                    new_count = 1
                if new_count>k:
                    continue
                new_cost = cost + weight 

                if new_cost <dist[nei][new_count]:
                    dist[nei][new_count] = new_cost
                    heappush(heap,(new_cost,nei,new_count))
        
        res = min(dist[n-1])
        return -1 if res==float('inf') else res













