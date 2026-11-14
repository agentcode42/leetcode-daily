# 3364. Minimum Positive Sum Subarray

[LeetCode Problem](https://leetcode.com/problems/minimum-positive-sum-subarray/)

## Problem Summary

Given an integer array `nums` and two integers `l` and `r`, find the minimum positive sum of a subarray whose length is between `l` and `r` (inclusive).

If no subarray has a positive sum, return `-1`.

## Intuition

We need to examine every possible subarray with a length between `l` and `r`.

Instead of calculating the sum of every subarray independently, we can start with a subarray of length `l` and gradually extend it by adding one element at a time.

This allows us to check all valid subarray lengths while reusing the previously calculated sum.

## Approach: Brute Force with Incremental Sum

1. Iterate through every possible starting index `i`.
2. Calculate the sum of the first `l` elements using slicing.
3. If the sum is positive, update the minimum result.
4. Extend the subarray one element at a time until its length reaches `r` or the array ends.
5. After adding each element, check whether the current sum is positive and update the result.
6. If no positive sum was found, return `-1`.

## Python Code

```python
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        res = float('inf')

        for i in range(n-l+1):
            total = sum(nums[i:i+l])

            if total > 0:
                res = min(total, res)

            for j in range(i+l, min(i+r, n)):
                total += nums[j]

                if total > 0:
                    res = min(total, res)

        return -1 if res == float('inf') else res
```

## Complexity Analysis

Let `n` be the length of `nums`.

- **Time Complexity:** `O(n * r)` — For every starting position, we calculate the initial subarray sum and extend it up to length `r`.
- **Space Complexity:** `O(l)` — The slicing operation creates a temporary list of up to `l` elements.

## Key Takeaway

By extending the current subarray and maintaining its running sum, we avoid recalculating the sum for every possible subarray length.

This is a straightforward brute-force solution with incremental sum calculation.