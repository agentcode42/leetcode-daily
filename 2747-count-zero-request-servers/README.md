# 2747. Count Zero Request Servers

[LeetCode Problem](https://leetcode.com/problems/count-zero-request-servers/)

## Problem Summary

We are given `n` servers, a list of request logs, a time interval `x`, and a list of query times.

Each log contains:
- `server_id`: The server that received the request.
- `time`: The time at which the request was received.

For every query time `q`, we need to count how many servers received **zero requests** during the interval `[q - x, q]`.

The result must be returned in the original order of the queries.

## Intuition

A straightforward brute-force approach would be to iterate through every query and check all logs to determine which servers received requests within its time window.

However, this would take `O(m * q)` time, where:
- `m` = number of logs.
- `q` = number of queries.

We can optimize this using **sorting and a sliding window**.

The key observation is that if we process queries in increasing order, their time windows also move forward.

Instead of checking every log for every query, we can maintain a window of relevant logs using two pointers.

## Approach: Sorting + Sliding Window

1. **Sort the logs** by their timestamps so that we can process requests chronologically.

2. **Sort the queries** by their timestamps. We also store their original indices because the final answers must follow the original query order.

3. Maintain two pointers:
   - `l`: Points to the first log currently inside or potentially inside the window.
   - `r`: Points to the next log that needs to be added.

4. Use a frequency dictionary `count` to track the number of requests made by each server inside the current window.

5. For every query `q`:

   **Expand the window:**
   - Add logs while their timestamps are less than or equal to `q`.
   - Increase the corresponding server's frequency in the dictionary.

   **Shrink the window:**
   - Remove logs whose timestamps are strictly smaller than `q - x`.
   - Decrease their server frequencies.
   - Remove a server from the dictionary when its frequency reaches zero.

6. The number of active servers is `len(count)` because the dictionary contains only servers with at least one request in the current window.

7. Calculate the number of inactive servers:

   `n - len(count)`

8. Store the answer using the original query index.

## Python Solution

```python
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
```

## Complexity Analysis

Let:
- `m` = number of logs.
- `q` = number of queries.

**Time Complexity:**

- Sorting logs: `O(m log m)`
- Sorting queries: `O(q log q)`
- Sliding window: `O(m)` because each log is added and removed at most once.
- Calculating answers: `O(q)`

Overall:

`O(m log m + q log q)`

**Space Complexity:**

- Sorted query pairs and result array: `O(q)`
- Frequency dictionary: `O(n)` in the worst case.

Overall auxiliary space: `O(n + q)`, excluding the sorting implementation's internal space.

## Key Takeaway

The main optimization comes from processing queries in sorted order.

Instead of rebuilding the active server set for every query, we reuse the previous window and only add or remove logs as the window moves.

This turns an `O(m * q)` brute-force approach into an efficient sorting + sliding-window solution.