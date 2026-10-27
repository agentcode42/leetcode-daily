# 3963. Create Grid With Exactly One Path

**LeetCode Problem:** [Create Grid With Exactly One Path](https://leetcode.com/problems/create-grid-with-exactly-one-path/)

## Problem Summary

Given two integers `m` and `n`, construct an `m × n` grid containing `.` and `#` such that there is exactly one valid path from the top-left cell to the bottom-right cell.

- `.` represents an open cell.
- `#` represents a blocked cell.

The goal is to construct a grid that guarantees exactly one path between the two corners.

## Intuition

The simplest way to guarantee exactly one path is to create an L-shaped path.

1. Fill the entire first row with `.`.
2. Fill the last column of every remaining row with `.`.
3. Fill all other cells with `#`.

This creates a path that moves right along the first row and then down the last column. Since every other cell is blocked, no alternative path exists.

## Approach

1. Create the first row containing `n` dots.
2. Iterate through the remaining `m - 1` rows.
3. For each row, add `n - 1` hashes followed by a dot.
4. Return the constructed grid.

This approach constructs each row directly without modifying individual characters in Python strings.

## Example

**Input:**
```text
m = 3, n = 4
```

**Output:**
```text
....
###.
###.
```

**Explanation:**

The only valid path moves right across the first row and then down the last column to reach the bottom-right cell. All other cells are blocked, so no alternative path is possible.

## Python Solution

```python
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = ["." * n]

        for i in range(1, m):
            res.append("#" * (n - 1) + ".")

        return res
```

### Python Explanation

- `"." * n` creates the first row with all cells open.
- `"#" * (n - 1) + "."` creates each remaining row with blocked cells followed by one open cell.
- `append()` adds each constructed row to the result.
- Finally, `res` contains the complete grid.

## C Solution

```c
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced,
 * assume caller calls free().
 */
char** createGrid(int m, int n, int* returnSize) {
    char** res = malloc(m * sizeof(char*));

    res[0] = malloc((n + 1) * sizeof(char));
    memset(res[0], '.', n);
    res[0][n] = '\0';

    for (int i = 1; i < m; i++) {
        res[i] = malloc((n + 1) * sizeof(char));
        memset(res[i], '#', n - 1);
        res[i][n - 1] = '.';
        res[i][n] = '\0';
    }

    *returnSize = m;
    return res;
}
```

### C Explanation

- **Memory allocation:** `malloc()` allocates memory for the array of row pointers and each individual row.
- **First row:** `memset()` fills the first `n` characters with dots.
- **Remaining rows:** `memset()` fills the first `n - 1` characters with hashes, and the next character is set to a dot.
- **Null terminator:** Each row allocates `n + 1` characters. The final character is explicitly set to `'\0'` so the row is a valid C string.
- **Return size:** `*returnSize = m` tells LeetCode how many rows the returned array contains.

The caller must free each allocated row and then the outer array.

## Complexity Analysis

Let `m` be the number of rows and `n` be the number of columns.

- **Time Complexity:** `O(m × n)` — constructing all rows requires writing a total of `m × n` grid characters.
- **Space Complexity:** `O(m × n)` — the returned grid contains `m × n` characters, plus a small amount of additional memory for row pointers.

## Key Takeaway

A constructive problem does not always require graph traversal or a search algorithm. Sometimes, the best solution is to identify a simple structure that guarantees the required property.

Here, an L-shaped path gives us exactly one valid path, and constructing each row directly keeps the implementation simple in both Python and C.
