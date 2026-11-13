# 3420. Count Non-Decreasing Subarrays After K Operations

[LeetCode Problem](https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/)

## Problem Summary

Given an integer array `nums` and an integer `k`, count the number of subarrays that can be made non-decreasing using at most `k` increment operations.

Each operation increments any one element by 1.

The goal is to find all subarrays whose minimum required number of increments does not exceed `k`.

## Intuition

To make a subarray non-decreasing, every element must be at least as large as the maximum element encountered before it.

For example:

```python
nums = [5, 1, 4, 2, 3]
```

The required values become:

```text
Original:  [5, 1, 4, 2, 3]
Modified:  [5, 5, 5, 5, 5]
```

The number of operations required is:

```text
0 + 4 + 1 + 3 + 2 = 10
```

We can calculate the cost using:

**Cost = Sum of running maximums - Sum of original elements**

Recalculating the running maximums for every window would be too slow, so we optimize this using a monotonic stack, a precomputed chain array, a monotonic deque, and sliding window.

## Approach

### 1. Next Greater Element

Use a monotonic stack to find the next strictly greater element for every index.

`nxt[i]` stores the next index to the right where `nums[j] > nums[i]`.

If no greater element exists, its value remains `n`.

### 2. Build the Chain Array

Calculate the sum of running maximums starting from each index.

```python
chain[i] = nums[i] * (nxt[i] - i) + chain[nxt[i]]
```

This works because all elements between `i` and the next greater element have `nums[i]` as their running maximum.

### 3. Sliding Window with a Monotonic Deque

Maintain a decreasing deque of indices.

- The front contains the index of the maximum element in the current window.
- The deque helps maintain the maximum efficiently.
- `window_sum` maintains the sum of the original window.

Let `c = dq[0]`.

The sum of running maximums is:

```python
chain[left] - chain[c] + nums[c] * (right - c + 1)
```

Therefore:

```python
cost = running_max_sum - window_sum
```

If the cost exceeds `k`, move the left boundary forward until the window becomes valid.

For every valid window ending at `right`, all subarrays starting between `left` and `right` are also valid.

Add:

```python
res += right - left + 1
```

## Python Solution

```python
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nxt = [n] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                nxt[stack.pop()] = i
            stack.append(i)

        chain = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            chain[i] = nums[i] * (nxt[i] - i) + chain[nxt[i]]

        dq = deque()
        left = 0
        window_sum = 0
        res = 0

        for right in range(n):
            window_sum += nums[right]

            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()
            dq.append(right)

            while True:
                c = dq[0]
                cost = chain[left] - chain[c] + nums[c] * (right - c + 1)
                cost -= window_sum

                if cost <= k:
                    break

                if dq[0] == left:
                    dq.popleft()

                window_sum -= nums[left]
                left += 1

            res += right - left + 1

        return res
```

## Complexity Analysis

Let `n` be the length of `nums`.

| Operation | Time Complexity |
|---|---|
| Next Greater Element | O(n) |
| Chain Array | O(n) |
| Sliding Window + Deque | O(n) |

**Total Time Complexity:** O(n)

**Space Complexity:** O(n)

Each index is pushed and popped at most once from the stack and deque, allowing the entire solution to run in linear time.