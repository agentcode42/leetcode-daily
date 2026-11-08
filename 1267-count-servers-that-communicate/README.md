# 1267. Count Servers that Communicate

**LeetCode Problem:** [1267. Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate/)

## Problem Summary

We are given an `m x n` binary grid where `1` represents a server and `0` represents an empty cell.

A server can communicate with another server if they are located in the same row or the same column.

Return the total number of servers that can communicate with at least one other server.

## Intuition

Instead of checking every server against every other server, we can count how many servers exist in each row and column.

For any server at position `(r, c)`:

- If its row contains more than one server, it can communicate.
- If its column contains more than one server, it can communicate.
- Otherwise, it cannot communicate.

We only need to count servers that satisfy at least one of these conditions.

## Approach: Row and Column Counting

1. Create two arrays:
   - `r_count`: Stores the number of servers in each row.
   - `c_count`: Stores the number of servers in each column.

2. Traverse the grid once. Whenever we encounter a server (`1`), increment its corresponding row and column counts.

3. Traverse the grid again. For every server, check whether its row or column contains more than one server.

4. If either count is greater than one, increment the result.

5. Return the total count.

## Complexity Analysis

Let `m` be the number of rows and `n` be the number of columns.

- **Time Complexity:** `O(m × n)` — We traverse the entire grid twice.
- **Space Complexity:** `O(m + n)` — We use two additional arrays to store row and column counts.

## Python Solution

```python
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        r_count = [0] * rows
        c_count = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    r_count[r] += 1
                    c_count[c] += 1

        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if max(r_count[r], c_count[c]) > 1:
                        res += 1

        return res
```

## Key Takeaway

By precomputing row and column frequencies, we avoid repeatedly searching for communicating servers.

**Two passes + frequency counting = O(m × n) time complexity.**