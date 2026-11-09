# 1606. Find Servers That Handled Most Number of Requests

[LeetCode Problem](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/)

## Problem Summary

We are given `k` servers and two arrays, `arrival` and `load`, representing the arrival time and processing time of each request.

Each request is assigned according to the following rules:

- Request `i` initially tries server `i % k`.
- If that server is busy, we search for the next available server in circular order.
- If all servers are busy, the request is dropped.

Our task is to return the IDs of the servers that successfully handled the maximum number of requests.

## Intuition

We need to track two things:

1. Which servers are currently available.
2. When busy servers will become available again.

A **Min Heap** can efficiently track busy servers based on their completion times.

For available servers, we need more than just the smallest index. We need to find the first available server whose index is greater than or equal to `i % k`, with circular wrapping if necessary.

A `SortedList` is useful here because it maintains available server indices in sorted order and supports efficient searching, insertion, and removal.

## Approach: Min Heap + SortedList

1. **Initialize Available Servers:**
   - Create a `SortedList` containing all server indices from `0` to `k-1`.
   - This maintains available servers in sorted order.

2. **Track Busy Servers:**
   - Use a Min Heap storing `(end_time, server_index)`.
   - The server with the earliest completion time is always at the top.

3. **Process Each Request:**
   - Before handling a request, release all servers whose completion time is less than or equal to the current arrival time.
   - Add those servers back to the available `SortedList`.

4. **Find the Next Available Server:**
   - Calculate the starting server using `i % k`.
   - Use `bisect_left()` to find the first available server with an index greater than or equal to the starting index.
   - If no such server exists, wrap around and select the smallest available index.
   - Remove the selected server from the `SortedList`.

5. **Assign the Request:**
   - Calculate its completion time as `arrival[i] + load[i]`.
   - Push `(completion_time, server_index)` into the busy heap.
   - Increment the request count for that server.

6. **Find the Busiest Servers:**
   - Track the maximum request count while processing requests.
   - Finally, return all server indices whose request count equals the maximum.

## Python Solution

```python
from heapq import heappush, heappop
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        n = len(arrival)
        if n <= k:
            return list(range(n))

        available = SortedList(range(k))
        busy = []
        count = [0] * k
        max_count = 0

        for i, (start, curr_load) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, curr_idx = heappop(busy)
                available.add(curr_idx)

            if available:
                s = i % k
                pos = available.bisect_left(s)

                if pos == len(available):
                    pos = 0

                idx = available.pop(pos)

                heappush(busy, (start + curr_load, idx))
                count[idx] += 1
                max_count = max(max_count, count[idx])

        res = []
        for i, c in enumerate(count):
            if c == max_count:
                res.append(i)

        return res
```

## Complexity Analysis

Let `n` be the number of requests and `k` be the number of servers.

- **Time Complexity:** `O((n + k) log k)`
  - Initializing the SortedList takes `O(k log k)`.
  - Each request performs at most one assignment and one heap insertion, taking `O(log k)`.
  - Each server can be released at most once per request, with each release requiring `O(log k)` for heap removal and SortedList insertion.
  - Finding and removing an available server takes `O(log k)`.

- **Space Complexity:** `O(k)`
  - Available servers: `O(k)`.
  - Busy servers: `O(k)`.
  - Request counts: `O(k)`.

## Key Takeaway

The important part of this problem is finding the next available server in circular order.

A Min Heap efficiently handles server completion times, while `SortedList` allows us to find the next available server without scanning all `k` servers for every request.