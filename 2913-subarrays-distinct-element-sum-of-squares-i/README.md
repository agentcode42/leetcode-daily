# 2913. Subarrays Distinct Element Sum of Squares I

**LeetCode Problem:** [2913. Subarrays Distinct Element Sum of Squares I](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/)

## Problem Summary

Given an integer array `nums`, consider every possible contiguous subarray.

For each subarray, count the number of distinct elements, square that count, and add it to the final result.

Return the sum of these squared counts.

## Intuition

We need to examine every possible subarray and count its distinct elements.

Instead of generating each subarray from scratch, we can fix a starting index and extend the subarray one element at a time.

A set automatically stores only distinct elements. As we extend the subarray, we add each new element to the set and use `len(s)` to get the number of distinct elements.

We then add the square of this count to our result.

## Approach

1. Initialize `res = 0` to store the final sum.
2. Iterate through every possible starting index `i`.
3. Create an empty set `s` for each starting index.
4. Iterate through every ending index `j`, starting from `i`.
5. Add `nums[j]` to the set.
6. Calculate the number of distinct elements using `len(s)` and add its square to `res`.
7. Return `res` after processing all subarrays.

## Python Solution

```python
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            s = set()

            for j in range(i, n):
                s.add(nums[j])
                res += len(s) ** 2

        return res
```

## Complexity Analysis

- **Time Complexity:** \(O(n^2)\) average time, where `n` is the length of `nums`. There are \(O(n^2)\) subarrays, and set insertion takes \(O(1)\) average time.
- **Space Complexity:** \(O(n)\), because the set can store up to `n` distinct elements.

## Key Takeaway

By fixing a starting index and expanding each subarray, we can count distinct elements efficiently using a set without rebuilding every subarray from scratch.