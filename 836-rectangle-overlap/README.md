
# 836. Rectangle Overlap

[LeetCode Problem](https://leetcode.com/problems/rectangle-overlap/)

## Problem

Given two axis-aligned rectangles represented as:

```text
[x1, y1, x2, y2]
```

where `(x1, y1)` is the bottom-left corner and `(x2, y2)` is the top-right corner, return `true` if the rectangles overlap with **positive area**.

Rectangles that only touch at an edge or corner do **not** count as overlapping.

---

## Approach

Instead of checking individual corners, treat each rectangle as two intervals:

* An interval on the X-axis
* An interval on the Y-axis

For two rectangles to have a positive-area intersection:

1. Their X intervals must overlap.
2. Their Y intervals must overlap.

Both conditions must be true.

### X-axis overlap

Let:

```text
R1: r1x1 -------- r1x2
R2:      r2x1 -------- r2x2
```

For the intervals to overlap with positive length:

```python
r1x1 < r2x2
r2x1 < r1x2
```

### Y-axis overlap

Similarly:

```python
r1y1 < r2y2
r2y1 < r1y2
```

Therefore, the rectangles overlap when all four conditions are true.

### Why strict comparison?

We use `<` rather than `<=` because touching at an edge does not create positive area.

For example:

```text
R1: [0, 0, 2, 2]
R2: [2, 0, 4, 2]
```

The rectangles touch at `x = 2`, but there is no area shared between them.

---

## Solution

```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        r1x1, r1y1, r1x2, r1y2 = rec1
        r2x1, r2y1, r2x2, r2y2 = rec2

        return (r1x1 < r2x2 and r2x1 < r1x2 and
                r1y1 < r2y2 and r2y1 < r1y2)
```

```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0]<rec2[2] and rec2[0]<rec1[2]:
            if rec1[1]<rec2[3] and rec2[1]<rec1[3]:
                return True
        return False
```

## Examples

### Partial overlap

```text
rec1 = [0, 0, 3, 3]
rec2 = [2, 1, 5, 4]
```

The X ranges overlap and the Y ranges overlap, so the rectangles have positive intersection area.

### One rectangle inside the other

```text
rec1 = [0, 0, 10, 10]
rec2 = [2, 2, 5, 5]
```

Both X and Y intervals overlap, so the result is `true`.

The formula also works when `rec1` is completely inside `rec2`.

### Touching only

```text
rec1 = [0, 0, 2, 2]
rec2 = [2, 0, 4, 2]
```

The rectangles share an edge but no area, so the result is `false`.

---

## Complexity

**Time:** `O(1)`

Only a fixed number of comparisons are performed.

**Space:** `O(1)`

Only a few coordinate variables are used.
