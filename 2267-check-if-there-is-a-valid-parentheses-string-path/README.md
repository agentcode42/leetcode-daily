# LeetCode 2267: Check if There Is a Valid Parentheses String Path

## Problem

You are given a grid containing `(` and `)`.

Starting from the top-left cell, you can move only **down** or **right** until you reach the bottom-right cell.

The characters along the path form a parentheses string.

The goal is to determine whether **at least one path produces a valid parentheses string**.

A valid parentheses string must:

* Never have more `)` than `(` at any point.
* Have the same number of `(` and `)` at the end.

## Intuition

There can be a huge number of possible paths through the grid, so checking every complete path would be too slow.

Instead, we can use **DFS with memoization**.

While traversing the grid, we keep track of one extra piece of information:

`bal` = current number of unmatched opening parentheses.

For every cell:

* If it contains `(`, increase `bal`.
* If it contains `)`, decrease `bal`.

This gives us a DFS state:

`(row, col, bal)`

If we reach the same cell with the same balance again, the remaining result will be exactly the same. So we can cache that result using `@lru_cache`.

## Approach

### 1. Check the path length

Every path from `(0, 0)` to `(m - 1, n - 1)` contains:

`m + n - 1`

characters.

A valid parentheses string must have an even length.

So if:

`(m + n - 1) % 2 != 0`

we can immediately return `False`.

### 2. Check the first and last characters

A valid parentheses string cannot:

* Start with `)`
* End with `(`

So these cases can also be rejected immediately.

### 3. Track the parentheses balance

During DFS:

```text
'(' → bal + 1
')' → bal - 1
```

If `bal` becomes negative, we have already used more closing brackets than opening brackets.

That path can never become valid, so we stop exploring it.

### 4. Prune impossible paths

Suppose we currently have:

`bal = 5`

but there are only `3` cells remaining.

Even if all three remaining characters are `)`, we can only reduce the balance to `2`.

Therefore, the path can never finish with balance `0`.

So if:

`bal > remaining_cells`

we immediately stop exploring that path.

### 5. Memoization

The result only depends on:

* Current row
* Current column
* Current balance

Therefore, we cache:

`dfs(row, col, bal)`

This prevents us from repeatedly solving the same state.

### 6. Base Case

When we reach the bottom-right cell, the path is valid only if:

```text
bal == 0
```

Otherwise, there are still unmatched opening parentheses.

## Complexity

There are `m × n` possible cells and the balance can range up to `m + n`.

### Time Complexity

**O(m × n × (m + n))**

Each `(row, col, bal)` state is calculated at most once.

### Space Complexity

**O(m × n × (m + n))**

This is used by the memoization cache and the recursive DFS stack.

## Python Code

```python
from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        row, col = len(grid), len(grid[0])
        
        # Quick structural filters
        if (row + col - 1) % 2 != 0:
            return False
        
        if grid[0][0] == ")" or grid[row - 1][col - 1] == "(":
            return False
        
        @lru_cache(None)
        def dfs(i, j, bal):
            bal += 1 if grid[i][j] == '(' else -1
            
            # Too many closing brackets
            if bal < 0:
                return False
            
            # Not enough cells left to close all open brackets
            remain = (row - 1 - i) + (col - 1 - j)
            if bal > remain:
                return False
            
            # Reached destination
            if i == row - 1 and j == col - 1:
                return bal == 0
            
            right, down = False, False
            
            if i < row - 1:
                right = dfs(i + 1, j, bal)
            
            if j < col - 1:
                down = dfs(i, j + 1, bal)
            
            return right or down
        
        return dfs(0, 0, 0)
```
