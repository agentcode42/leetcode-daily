# 3970. Shortest Path With at Most K Consecutive Identical Characters

[LeetCode Problem](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/)

## Problem Summary

Given a directed, weighted graph with `n` nodes, a string `labels` representing the character assigned to each node, and an integer `k`, find the minimum cost to travel from node `0` to node `n-1`.

The path cannot contain more than `k` consecutive nodes with the same character.

Return the minimum path cost. If no valid path exists, return `-1`.

## Intuition

We can use **Dijkstra's Algorithm** because we need to find the shortest path in a weighted graph.

However, tracking only the current node is not enough.

We also need to track how many consecutive times we have visited nodes with the same character.

Therefore, instead of maintaining a single distance for each node, we maintain distances for each combination of:

`(node, consecutive_count)`

This allows us to reach the same node through different paths while keeping track of different consecutive character counts.

## Approach: Dijkstra's Algorithm

1. **Build the Graph:** Create an adjacency list to store each node's neighbors and edge weights.

2. **Initialize Distance Array:** Create a 2D distance array where `dist[node][count]` represents the minimum cost to reach a node with a particular consecutive character count.

3. **Initialize the Heap:** Start from node `0` with cost `0` and consecutive count `1`.

4. **Process the Heap:** Extract the state with the minimum cost using Dijkstra's algorithm.

5. **Calculate Consecutive Count:**
   - If the current node and next node have the same character, increment the count.
   - Otherwise, reset the count to `1`.

6. **Validate the Move:** Skip the neighbor if the new consecutive count exceeds `k`.

7. **Update Distance:** Calculate the new cost. If it is smaller than the previously recorded distance for that state, update the distance and push the new state into the heap.

8. **Return the Result:** Take the minimum distance among all states at the destination. If every state is unreachable, return `-1`.

## Python Solution

```python
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
```

## Complexity Analysis

Let `V` be the number of nodes, `E` the number of edges, and `K` the maximum consecutive count.

- **Time Complexity:** `O(V + E + EK log(VK))`
- **Space Complexity:** `O(VK + E)`

## Key Takeaway

The main challenge is recognizing that reaching the same node does not necessarily mean reaching the same state.

A path reaching a node with a consecutive count of `1` may have more flexibility than a path reaching that same node with a count of `k`.

By expanding our Dijkstra state to `(node, consecutive_count)`, we can correctly find the shortest valid path.