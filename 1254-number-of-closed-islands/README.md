# 1254. Number of Closed Islands — DFS Solution

## 1. Problem Summary

We are given an `m x n` grid where:

- `0` represents land.
- `1` represents water.

An **island** is a group of connected land cells. Two land cells are connected if they share a side (up, down, left, or right).

A **closed island** is an island completely surrounded by water. If an island touches the boundary of the grid, it is not closed.

**Goal:** Count the number of closed islands.

## 2. Intuition

The key observation is that **any island connected to the boundary cannot be a closed island**.

Instead of trying to determine whether every island is closed individually, we can eliminate all land connected to the boundary first.

We use DFS (Depth-First Search) to explore each connected land area and change its cells from `0` to `1` so that we do not visit them again.

Our strategy has two phases:

1. **Remove boundary-connected islands:** Start DFS from every land cell on the boundary. This eliminates all land connected to the edges of the grid.
2. **Count the remaining islands:** Traverse the grid again. Whenever we find an unvisited land cell (`0`), we have found a closed island. Run DFS to eliminate the entire island and increase the result by one.

After the first phase, every remaining island is guaranteed to be closed.

## 3. Python Solution

```python
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                grid[i][j] = 1

                dfs(i, j + 1)
                dfs(i, j - 1)
                dfs(i + 1, j)
                dfs(i - 1, j)

        # Phase 1: Eliminate all land connected to the boundary
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and grid[i][j] == 0:
                    dfs(i, j)

        # Phase 2: Count the remaining closed islands
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j)
                    res += 1

        return res
```

## 4. How DFS Works

The `dfs(i, j)` function explores one connected land area.

First, it checks three conditions:

- `0 <= i < m`: The row index is valid.
- `0 <= j < n`: The column index is valid.
- `grid[i][j] == 0`: The cell is land that has not been visited yet.

If all conditions are true, we mark the cell as water by setting `grid[i][j] = 1`.

Then DFS explores all four directions:

- Right: `dfs(i, j + 1)`
- Left: `dfs(i, j - 1)`
- Down: `dfs(i + 1, j)`
- Up: `dfs(i - 1, j)`

**Why mark the cell before exploring its neighbors?**

This prevents revisiting the same cell and stops the DFS from looping indefinitely between connected land cells.

## 5. Dry Run with an Example

Consider this grid:

```text
1 1 1 1 1
1 0 0 1 1
1 0 1 0 1
1 1 1 1 1
```

### Phase 1: Remove boundary-connected land

We inspect the first and last rows and columns.

Every boundary cell in this example is already water (`1`). Therefore, no DFS calls are needed in this phase.

The grid remains unchanged:

```text
1 1 1 1 1
1 0 0 1 1
1 0 1 0 1
1 1 1 1 1
```

### Phase 2: Count the remaining islands

We scan the grid from top to bottom, left to right.

**First island:** We encounter the land cell at `(1, 1)`.

DFS visits the connected land cells `(1, 1)`, `(1, 2)`, and `(2, 1)`. These cells form one connected island.

We mark all three cells as visited and increment `res` to `1`.

```text
1 1 1 1 1
1 1 1 1 1
1 1 1 0 1
1 1 1 1 1
```

**Second island:** We later encounter the land cell at `(2, 3)`.

DFS marks this cell as visited. It is separate from the first island, so we increment `res` to `2`.

Final grid:

```text
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
```

**Final answer: `2` closed islands.**

## 6. Complexity Analysis

Let `m` be the number of rows and `n` be the number of columns.

- **Time Complexity: `O(m × n)`**

  Each cell is visited and changed at most once. The boundary scan and the counting scan each take `O(m × n)` time.

- **Space Complexity: `O(m × n)` in the worst case**

  DFS uses the call stack to explore connected cells. In the worst case, a large connected island can cause up to `O(m × n)` recursive calls.

  The algorithm uses the input grid itself to mark visited cells, so it does not need a separate visited matrix.

## 7. Key Takeaway

The trick is to **eliminate all boundary-connected land before counting islands**.

Instead of checking whether each island touches the boundary, we remove every island that does. Whatever land remains must form closed islands.

This is a useful DFS pattern for grid problems where boundary-connected regions must be excluded.