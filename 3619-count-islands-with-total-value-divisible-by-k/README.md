# 3619. Count Islands With Total Value Divisible by K

## Problem Summary

You are given an `m x n` integer grid and an integer `k`.

An island consists of connected cells containing positive integers (`grid[i][j] > 0`). Cells are connected horizontally or vertically, not diagonally.

The **total value of an island** is the sum of all values in its connected cells.

Return the number of islands whose total value is divisible by `k`.

## Intuition

We can use **Depth-First Search (DFS)** to explore each island and calculate its total value.

Whenever we find a cell containing a positive value, we have discovered a new island. We start DFS from that cell and visit every connected positive cell, adding their values together.

To avoid visiting the same cells multiple times, we mark each visited cell as `0`.

After DFS finishes, we have the total value of the entire island. If that sum is divisible by `k`, we increment our answer.

We repeat this process until every cell has been checked.

## Approach

1. Get the number of rows `m` and columns `n`.
2. Define the four possible movement directions: right, left, down, and up.
3. Implement a recursive DFS function:
   - Start with the value of the current cell.
   - Mark the current cell as `0` to indicate that it has been visited.
   - Explore all four neighboring cells.
   - If a neighbor is inside the grid and contains a positive value, recursively explore it and add its returned sum.
   - Return the total value of the island.
4. Iterate through every cell in the grid.
5. Whenever a positive cell is found, run DFS to calculate the island's total value.
6. If the island's total value is divisible by `k`, increment `total`.
7. Return `total`.

## Python Solution

```python
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            res = grid[i][j]
            grid[i][j] = 0

            for dx, dy in direction:
                x, y = i + dx, j + dy

                if 0 <= x < m and 0 <= y < n and grid[x][y] > 0:
                    res += dfs(x, y)

            return res

        total = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    if dfs(i, j) % k == 0:
                        total += 1

        return total
```

## Examples

### Example 1

**Input:**
```python
grid = [
    [0, 2, 1, 0, 0],
    [0, 3, 0, 0, 0],
    [0, 0, 0, 4, 5],
    [0, 0, 0, 1, 1]
]
k = 5
```

**Explanation:**

There are two islands:

- Island 1 contains `2, 1, 3`, with a total value of `6`. Since `6 % 5 != 0`, it does not count.
- Island 2 contains `4, 5, 1, 1`, with a total value of `11`. Since `11 % 5 != 0`, it does not count.

**Output:**
```python
0
```

### Example 2

**Input:**
```python
grid = [
    [0, 2, 1, 0, 0],
    [0, 3, 0, 0, 0],
    [0, 0, 0, 4, 5],
    [0, 0, 0, 1, 5]
]
k = 5
```

**Explanation:**

There are two islands:

- Island 1 contains `2, 1, 3`, with a total value of `6`. It is not divisible by `5`.
- Island 2 contains `4, 5, 1, 5`, with a total value of `15`. Since `15 % 5 == 0`, this island counts.

**Output:**
```python
1
```

## Complexity Analysis

Let `m` be the number of rows and `n` be the number of columns.

- **Time Complexity:** `O(m × n)` — Every cell is visited at most once, and each cell checks four neighbors.
- **Space Complexity:** `O(m × n)` in the worst case due to the recursive DFS call stack when the entire grid belongs to one island.

## Key Takeaway

DFS helps us explore an entire connected island in one traversal. By returning the sum of its cell values, we can determine whether the island's total is divisible by `k`.

**Pattern:** Graph Traversal · DFS · Connected Components
