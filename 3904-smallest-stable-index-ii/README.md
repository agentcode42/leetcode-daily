# LeetCode 3904 — Smallest Stable Index II


**Difficulty:** Medium
**Problem:** [3904. Smallest Stable Index II](https://leetcode.com/problems/smallest-stable-index-ii/)

## Problem

Given an integer array `nums` and an integer `k`, find the **smallest stable index** `i`.

An index `i` is stable if:

```text
max(nums[0..i]) - min(nums[i..n-1]) <= k
```

Return the smallest such index. If no stable index exists, return `-1`.

## Approach

We need two pieces of information for every index:

* The maximum value from the beginning of the array up to `i`.
* The minimum value from `i` to the end of the array.

### 1. Build the suffix minimum array

Create `suffix[i]` such that:

```text
suffix[i] = min(nums[i..n-1])
```

We calculate it from right to left.

### 2. Track the prefix maximum

While scanning from left to right, maintain:

```text
prefix = max(nums[0..i])
```

For each index `i`, the stability condition becomes:

```text
prefix - suffix[i] <= k
```

The first index satisfying this condition is the answer.

## Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

## Python

```python
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suffix = [float('inf')] * n
        suffix[-1] = nums[-1]

        for i in reversed(range(n - 1)):
            suffix[i] = min(suffix[i + 1], nums[i])

        prefix = 0

        for i in range(n):
            prefix = max(prefix, nums[i])

            if prefix - suffix[i] <= k:
                return i

        return -1
```

## Key Idea

The condition for an index to be stable depends only on:

```text
maximum on the left - minimum on the right
```

So instead of repeatedly calculating these values for every index, we precompute the suffix minimum and maintain the prefix maximum while scanning.

This reduces the solution from a potentially `O(n²)` approach to **O(n)**.
