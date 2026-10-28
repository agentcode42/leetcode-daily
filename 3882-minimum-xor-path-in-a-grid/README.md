# 3882. Minimum XOR Path in a Grid

[LeetCode Problem Link](https://leetcode.com/problems/minimum-xor-path-in-a-grid/)

## Problem Summary

Given an `m × n` grid of non-negative integers, find the minimum possible XOR value among all paths from the top-left cell `(0, 0)` to the bottom-right cell `(m - 1, n - 1)`.

From each cell, we can move only **right** or **down**.

The XOR value of a path is calculated by XOR-ing the values of every cell visited, including the starting and destination cells.

## Intuition

A simple DFS can explore every possible path, calculate its XOR value, and return the minimum. However, the number of possible paths grows rapidly with the grid dimensions.

To avoid recalculating the same subproblems, we can use **DFS with memoization**.

The key observation is that the result depends on three things:

- `i`: the current row.
- `j`: the current column.
- `curr_xor`: the XOR value accumulated along the path so far.

We cannot memoize using only the cell coordinates because different paths can reach the same cell with different accumulated XOR values.

Since each grid value is at most `1023`, every accumulated XOR value also lies between `0` and `1023`. Therefore, we can use a three-dimensional DP array to store the results for these states.

## Approach: DFS + 3D Memoization

1. Create a three-dimensional DP array of dimensions `m × n × 1024`, initialized with `-1`. Each entry stores the minimum final XOR achievable from a particular state.
2. At every cell, XOR its value with `curr_xor` to include the current cell in the path.
3. If the current cell is the destination, return the accumulated XOR value.
4. If the result for the current state is already cached, return it.
5. Otherwise, recursively explore the right and down directions when those moves are valid.
6. Take the minimum of the two results, store it in the DP array, and return it.
7. Start the search at `(0, 0)` with an initial XOR value of `0`.

## Python Solution

```python
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[[-1] * 1024 for _ in range(n)]
              for _ in range(m)]

        def dfs(i, j, curr_xor):
            curr_xor ^= grid[i][j]

            if i == m - 1 and j == n - 1:
                return curr_xor

            if dp[i][j][curr_xor] != -1:
                return dp[i][j][curr_xor]

            right = down = float('inf')

            if j < n - 1:
                right = dfs(i, j + 1, curr_xor)

            if i < m - 1:
                down = dfs(i + 1, j, curr_xor)

            dp[i][j][curr_xor] = min(right, down)

            return dp[i][j][curr_xor]

        return dfs(0, 0, 0)
```

## Example 1

**Input:**

```python
grid = [
    [1, 2],
    [3, 4]
]
```

There are two possible paths.

**Path 1: Right → Down**

```text
1 → 2 → 4
```

XOR calculation:

```text
1 ^ 2 ^ 4 = 7
```

**Path 2: Down → Right**

```text
1 → 3 → 4
```

XOR calculation:

```text
1 ^ 3 ^ 4 = 6
```

**Output:**

```text
6
```

The minimum XOR value is `6`.

## Complexity Analysis

Let `K = 1024` be the number of possible XOR values.

**Time Complexity:** `O(m × n × K)`

There are at most `m × n × K` memoization states, and each state performs constant work apart from its recursive calls, which are cached.

**Space Complexity:** `O(m × n × K)`

The three-dimensional DP array stores up to `m × n × 1024` entries. The recursive call stack additionally uses `O(m + n)` space because each path moves only right or down.

## Key Takeaway

Memoization is most effective when the state captures all the information that affects the result. Here, the accumulated XOR value is essential: reaching the same cell with different XOR values represents different subproblems.

By combining DFS with a bounded XOR state space, we avoid repeatedly exploring identical states.
