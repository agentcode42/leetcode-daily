# 835. Image Overlap

[LeetCode Problem](https://leetcode.com/problems/image-overlap/)

## Problem

Given two binary `n x n` matrices, translate one image horizontally and/or vertically without rotation.

After each translation, count how many positions contain `1` in both images.

Return the maximum possible overlap.

## Approach

Instead of actually translating the images and checking the overlap for every possible position, we can look at the **relative displacement between every pair of `1`s**.

First, store the coordinates of all `1`s in both images.

For every `1` at `(x1, y1)` in `img1` and every `1` at `(x2, y2)` in `img2`, calculate:

```text
(dx, dy) = (x1 - x2, y1 - y2)
```

This displacement represents a translation that would make these two `1`s overlap.

If multiple pairs of `1`s produce the same `(dx, dy)`, then all those pairs can overlap under the same translation.

Therefore, we count how frequently each displacement occurs using a `Counter`.

The most frequent displacement gives the maximum possible overlap.

### Why does this work?

Suppose several pairs of `1`s have the same displacement:

```text
(x1 - x2, y1 - y2) = (dx, dy)
```

Translating one image by that same `(dx, dy)` aligns all of those pairs simultaneously.

So the number of times a displacement occurs is exactly the number of overlapping `1`s produced by that translation.

## Complexity

Let:

* `k1` = number of `1`s in `img1`
* `k2` = number of `1`s in `img2`

Finding all `1` coordinates takes:

```text
O(n²)
```

Comparing every `1` in `img1` with every `1` in `img2` takes:

```text
O(k1 × k2)
```

Therefore, the overall complexity is:

```text
Time:  O(n² + k1 × k2)
Space: O(k1 + k2 + k1 × k2)
```

In the worst case, both images contain `n²` ones, giving:

```text
Time:  O(n⁴)
Space: O(n⁴)
```

However, the coordinate-pair approach can be considerably smaller for sparse images because it depends on the number of `1`s rather than directly iterating over every possible translation.

## Code

```python
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        one1 = []
        one2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    one1.append((i, j))
                if img2[i][j] == 1:
                    one2.append((i, j))

        count = Counter()

        for x1, y1 in one1:
            for x2, y2 in one2:
                dx = x1 - x2
                dy = y1 - y2
                count[(dx, dy)] += 1

        return max(count.values(), default=0)
```

## Key Takeaway

Instead of simulating every possible translation, **count the relative displacement between every pair of `1`s**.

The displacement that occurs most frequently represents the translation that produces the largest overlap.
