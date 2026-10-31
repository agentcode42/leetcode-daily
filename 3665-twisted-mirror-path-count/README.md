# 3665. Twisted Mirror Path Count

[LeetCode Problem](https://leetcode.com/problems/twisted-mirror-path-count/)

## Problem Summary

We are given an `m x n` grid containing two types of cells:

- `0` – We can move either right or down.
- `1` – A twisted mirror that forces us to change our movement direction.

We start at the top-left cell `(0, 0)` and need to reach the bottom-right cell `(m-1, n-1)`.

The task is to count the number of valid paths, returning the result modulo `10^9 + 7`.

## Intuition

We can solve this problem using **DFS + Memoization**.

At every cell, we need to know not only our current position but also our previous movement direction.

Why?

Because when we enter a twisted mirror cell (`1`), our next movement depends on the direction we used to enter it.

We use three parameters:

- `i` – Current row.
- `j` – Current column.
- `d` – Previous movement direction.
  - `0` – Right.
  - `1` – Down.

If we reach a normal cell (`0`), we can move either right or down.

If we reach a mirror cell (`1`), we must switch directions:
- If we arrived moving right (`d == 0`), we must move down.
- If we arrived moving down (`d == 1`), we must move right.

We use `@cache` to remember previously calculated states so that we don't repeat the same DFS calculations.

## Approach: DFS + Memoization

1. Define a recursive DFS function with the current position `(i, j)` and previous direction `d`.
2. If we reach the destination, return `1` because we found a valid path.
3. If we move outside the grid, return `0`.
4. If the current cell is a mirror (`1`):
   - If the previous direction was right, move down.
   - Otherwise, move right.
5. If the current cell is normal (`0`), explore both possible directions:
   - Move down.
   - Move right.
6. Add the results and take modulo `10^9 + 7`.
7. Use memoization to avoid recalculating states.

## Python Solution

```python
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9+7
        m,n = len(grid),len(grid[0])

        @cache
        def dfs(i,j,d):
            if i==m-1 and j==n-1:
                return 1

            if not 0<=i<m or not 0<=j<n:
                return 0

            if grid[i][j]==1:
                if d==0:
                    return dfs(i+1,j,1)%MOD
                else:
                    return dfs(i,j+1,0)%MOD

            return (dfs(i+1,j,1)+dfs(i,j+1,0))%MOD

        return dfs(0,0,0)
```

## Complexity Analysis

Let `m` be the number of rows and `n` be the number of columns.

- **Time Complexity:** `O(m × n)` – Each cell can have at most two different direction states, so each state is calculated only once.
- **Space Complexity:** `O(m × n)` – The cache stores at most two states per cell, along with the recursion stack.

## Key Takeaway

The important part of this problem is that **position alone is not enough to determine the next move**.

We also need to track the direction from which we entered the current cell.

By adding direction to our DFS state, we can correctly handle the twisted mirrors using DFS and memoization.