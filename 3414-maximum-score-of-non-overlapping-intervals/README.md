# 3414. Maximum Score of Non-overlapping Intervals

## Problem

You are given a list of intervals where:

```text
intervals[i] = [lefti, righti, weighti]
```

You can choose **at most 4 non-overlapping intervals**.

The score is the sum of the weights of the chosen intervals.

Two intervals are considered overlapping if they share any point, so for:

```text
[1, 3]
[3, 5]
```

they are overlapping.

Return the indices of the selected intervals that produce the maximum score.

If multiple selections have the same maximum score, return the **lexicographically smallest** list of indices.

---

## Approach

I first sort the intervals by their starting position and keep the original index with every interval.

Each interval becomes:

```text
[start, end, weight, original_index]
```

After sorting, I can use binary search to find the first interval that starts **after** the current interval ends.

Because intervals sharing a boundary are considered overlapping, the next interval must satisfy:

```text
next_start > current_end
```

So:

```python
next_i = bisect_right(starts, end)
```

gives the first possible non-overlapping interval.

### DFS + Memoization

Define:

```python
dfs(i, k)
```

as the best result we can obtain starting from sorted interval `i` when we can still select at most `k` intervals.

At every interval there are two choices.

### 1. Skip the current interval

```python
skip = dfs(i + 1, k)
```

We simply move to the next interval.

### 2. Take the current interval

If we take the current interval, we add its weight and continue from the first compatible interval:

```python
score, arr = dfs(next_i, k - 1)
take = (score + val, sorted([index] + arr))
```

The answer is whichever choice gives the larger score.

If both choices have the same score, Python can compare the lists directly:

```python
min(take, skip)
```

Since Python compares lists lexicographically, this automatically gives the required smallest index list.

---

## Why Memoization?

Without memoization, the DFS would repeatedly solve the same states.

For example:

```text
dfs(i, k)
```

can be reached through many different combinations of skipped intervals.

Using:

```python
@cache
```

stores the result for every `(i, k)` state so it only needs to be calculated once.

Since `k` can only be from `0` to `4`, the number of states is small relative to the number of intervals.

---

## Complexity

Let `n` be the number of intervals.

### Sorting

Sorting the intervals takes:

```text
O(n log n)
```

### Binary Search

For each DFS state, finding the next compatible interval takes:

```text
O(log n)
```

There are at most:

```text
O(4n) = O(n)
```

different `(i, k)` states.

Therefore, the overall complexity is approximately:

```text
Time:  O(n log n)
Space: O(n)
```

The DFS recursion and memoization require `O(n)` space, while storing the sorted intervals and starting positions also requires `O(n)` space.

---

## Python

```python
from bisect import bisect_right
from functools import cache

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        inv = []
        n = len(intervals)

        for i in range(n):
            start, end, val = intervals[i]
            inv.append([start, end, val, i])

        inv.sort()

        starts = [x[0] for x in inv]

        @cache
        def dfs(i, k):
            if i >= n or k == 0:
                return (0, [])

            start, end, val, index = inv[i]

            next_i = bisect_right(starts, end)

            # Skip current interval
            skip = dfs(i + 1, k)

            # Take current interval
            score, arr = dfs(next_i, k - 1)
            take = (score + val, sorted([index] + arr))

            if take[0] > skip[0]:
                return take
            elif take[0] < skip[0]:
                return skip

            # Same score -> lexicographically smaller indices
            return min(take, skip)

        return dfs(0, 4)[1]
```

## Key Idea

The important part of the solution is reducing the problem to two decisions:

```text
             dfs(i, k)
              /     \
           skip     take
            |         |
        dfs(i+1,k)   value
                       +
                 dfs(next_i,k-1)
```

Binary search finds where the next non-overlapping interval begins, while memoized DFS determines the best combination of up to 4 intervals.
