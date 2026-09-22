# 3525. Find X Value of Array II

[LeetCode Problem](https://leetcode.com/problems/find-x-value-of-array-ii/)

## Problem

You are given an integer array `nums`, an integer `k`, and a list of queries.

Each query is `[index, value, start, x]` and requires us to:

1. Update `nums[index] = value`.
2. Consider the subarray `nums[start:]`.
3. Remove a suffix from this subarray, leaving a non-empty prefix.
4. Count how many possible remaining prefixes have a product whose remainder modulo `k` is `x`.

The updates persist, so every query works on the array produced by the previous query.

---

## Approach

A straightforward solution would scan from `start` to the end of the array for every query and calculate the prefix product.

That would take `O(n)` per query.

With `n, q <= 10^5`, this can become roughly `O(n * q)`, which is far too slow.

The important observation is that:

* `k <= 5`
* We only care about products **modulo `k`**.
* Every query performs a **point update** and a **range query**.

This makes a **Segment Tree** a good fit.

---

## What Does Each Segment Tree Node Store?

For every segment, we store:

### 1. Total Product

`tree_product[node]` stores the product of every element in the segment modulo `k`.

For example:

```text
prod = (a × b × c) % k
```

### 2. Prefix Remainder Counts

`tree_reminder[node][r]` stores how many prefixes of this segment have product:

```text
product % k == r
```

Since `k <= 5`, this array contains at most 5 values.

So each segment can summarize all of its possible prefix products very cheaply.

---

## Merging Two Segments

Suppose we have two adjacent segments:

```text
Left | Right
```

We need to build the information for their combined segment.

### Total Product

The total product is simply:

```text
(left_product × right_product) % k
```

### Prefixes

There are two types of prefixes.

#### Prefix ends inside the Left segment

These prefixes don't use anything from the Right segment.

So their remainder counts remain unchanged:

```text
res = left_rem
```

#### Prefix extends into the Right segment

Such a prefix contains:

```text
entire Left segment + a prefix of Right
```

If:

```text
left_product = P
right prefix remainder = R
```

then the combined remainder is:

```text
(P × R) % k
```

Therefore, for every possible remainder `R` in the Right segment:

```python
curr_rem = (left_prod * R) % k
res[curr_rem] += right_rem[R]
```

That's the key idea behind the segment tree.

---

## Example

Suppose:

```text
Left  = [2, 3]
Right = [4, 5]
```

and `k = 5`.

The prefixes of the combined segment are:

```text
[2]
[2, 3]
[2, 3, 4]
[2, 3, 4, 5]
```

The first two prefixes are already represented by the Left node.

For prefixes extending into the Right node, we take the total product of the Left:

```text
2 × 3 = 6 ≡ 1 (mod 5)
```

and multiply it by each prefix remainder from the Right.

This lets us merge two nodes in only `O(k)` time.

---

## Why Segment Tree?

Each query has two operations:

```text
Point Update:
nums[index] = value

Range Query:
nums[start ... n-1]
```

A Segment Tree supports both efficiently.

Because every node stores only `k` remainder counts and `k <= 5`, merging nodes is very cheap.

---

## Complexity

Let `n = len(nums)` and `q = len(queries)`.

### Build

Each node takes `O(k)` work to construct:

```text
O(k × n)
```

### Update

A point update touches `O(log n)` nodes, and every merge costs `O(k)`:

```text
O(k log n)
```

### Query

The range query visits `O(log n)` nodes, with `O(k)` work per merge:

```text
O(k log n)
```

### Overall

```text
O(k × (n + q log n))
```

Since `k <= 5`, this is efficient enough for `n, q <= 10^5`.

### Space

The segment tree contains `O(n)` nodes, each storing `O(k)` remainder counts:

```text
O(k × n)
```

---

## Python 3

```python
from typing import List


class SegTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k

        self.tree_product = [1] * (4 * self.n)
        self.tree_reminder = [[0] * self.k for _ in range(4 * self.n)]

        if self.n > 0:
            self.build(0, 0, self.n - 1, nums)

    def merge(self, left: tuple, right: tuple):
        left_prod, left_rem = left
        right_prod, right_rem = right

        res = list(left_rem)

        for i in range(self.k):
            curr_rem = (left_prod * i) % self.k
            res[curr_rem] += right_rem[i]

        return (
            (left_prod * right_prod) % self.k,
            res
        )

    def build(self, node: int, l: int, r: int, nums: List[int]):
        if l == r:
            val = nums[l] % self.k

            self.tree_product[node] = val
            self.tree_reminder[node][val] = 1

            return (
                self.tree_product[node],
                self.tree_reminder[node]
            )

        mid = (l + r) // 2

        left = self.build(
            2 * node + 1,
            l,
            mid,
            nums
        )

        right = self.build(
            2 * node + 2,
            mid + 1,
            r,
            nums
        )

        prod, rem = self.merge(left, right)

        self.tree_product[node] = prod
        self.tree_reminder[node] = rem

        return prod, rem

    def update(
        self,
        node: int,
        l: int,
        r: int,
        idx: int,
        val: int
    ):
        if l == r:
            val %= self.k

            self.tree_product[node] = val
            self.tree_reminder[node] = [0] * self.k
            self.tree_reminder[node][val] = 1

            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(
                2 * node + 1,
                l,
                mid,
                idx,
                val
            )
        else:
            self.update(
                2 * node + 2,
                mid + 1,
                r,
                idx,
                val
            )

        prod, rem = self.merge(
            (
                self.tree_product[2 * node + 1],
                self.tree_reminder[2 * node + 1]
            ),
            (
                self.tree_product[2 * node + 2],
                self.tree_reminder[2 * node + 2]
            )
        )

        self.tree_product[node] = prod
        self.tree_reminder[node] = rem

    def query(
        self,
        node: int,
        l: int,
        r: int,
        start: int,
        end: int
    ):
        if start <= l and r <= end:
            return (
                self.tree_product[node],
                self.tree_reminder[node]
            )

        if r < start or l > end:
            return (1, [0] * self.k)

        mid = (l + r) // 2

        left = self.query(
            2 * node + 1,
            l,
            mid,
            start,
            end
        )

        right = self.query(
            2 * node + 2,
            mid + 1,
            r,
            start,
            end
        )

        return self.merge(left, right)


class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)
        seg = SegTree(nums, k)
        res = []

        for idx, val, start, x in queries:
            seg.update(
                0,
                0,
                n - 1,
                idx,
                val
            )

            _, rem = seg.query(
                0,
                0,
                n - 1,
                start,
                n - 1
            )

            res.append(rem[x])

        return res
```

## Key Takeaway

The trick is not to store every possible subarray product.

Instead, each Segment Tree node stores just enough information to answer future queries:

```text
Total product modulo k
+
Count of prefix products for every remainder
```

Because `k` is at most `5`, this small amount of information is enough to efficiently handle both updates and range queries.
