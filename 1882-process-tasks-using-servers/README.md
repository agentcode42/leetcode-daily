# 1882. Process Tasks Using Servers

[LeetCode Problem Link](https://leetcode.com/problems/process-tasks-using-servers/)

## Problem Summary

We are given:
- `servers`: An array where each element represents the weight of a server.
- `tasks`: An array where each element represents the time required to complete a task.

Tasks arrive sequentially. Task `i` arrives at time `i`.

We must assign each task to an available server following these rules:

1. Choose the available server with the smallest weight.
2. If multiple servers have the same weight, choose the one with the smallest index.
3. If no server is available, wait until one or more servers finish their current tasks.
4. Each server can process only one task at a time.

Return an array containing the index of the server assigned to each task.

## Intuition

The main challenge is managing two different priorities:

- Finding the best available server based on weight and index.
- Finding the next server that will become available based on its task completion time.

We can handle these two requirements efficiently using **two min-heaps**.

Instead of maintaining one complicated structure, we separate available and busy servers.

## Approach: Two Min-Heaps

### 1. Available Servers

We maintain a min-heap containing:

`(weight, index)`

Python compares tuples lexicographically, so the heap automatically prioritizes:
- Smaller server weight.
- Smaller server index when weights are equal.

This allows us to retrieve the best available server in `O(log n)` time.

### 2. Busy Servers

We maintain another min-heap containing:

`(end_time, weight, index)`

The heap prioritizes the earliest completion time.

When a server finishes its task, we remove it from the busy heap and move it back into the available heap.

### 3. Process Each Task

For every task:

1. Update the current time using `max(time, i)`, since tasks arrive at time `i`, but previous tasks might have forced us to wait.
2. Move all servers whose completion time is less than or equal to the current time into the available heap.
3. If no server is available, advance the current time to the earliest completion time.
4. Move all servers finishing at that time into the available heap.
5. Extract the best available server.
6. Record its index in the result.
7. Calculate its completion time as `time + duration` and insert it into the busy heap.

## Python Solution

```python
import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)

        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        res = []
        time = 0

        for i, duration in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                end, w, idx = heapq.heappop(busy)
                heapq.heappush(available, (w, idx))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end, w, idx = heapq.heappop(busy)
                    heapq.heappush(available, (w, idx))

            w, idx = heapq.heappop(available)
            res.append(idx)

            heapq.heappush(busy, (time + duration, w, idx))

        return res
```

## Complexity Analysis

Let:
- `n` = number of servers.
- `m` = number of tasks.

**Time Complexity:**

- Building the available heap: `O(n)`
- Each server is moved between heaps at most once per assigned task.
- Each heap insertion and removal takes `O(log n)`.

Overall:

`O(n + m log n)`

**Space Complexity:**

- Available and busy heaps together store at most `n` servers: `O(n)`.
- Result array stores `m` server indices: `O(m)`.

Overall: `O(n + m)`.

## Key Takeaway

The important observation is that we have two independent priorities in this scheduling problem.

- Available servers are prioritized by `(weight, index)`.
- Busy servers are prioritized by `(end_time, weight, index)`.

Using two min-heaps allows us to manage both priorities efficiently without repeatedly sorting the servers.