# 2333. Minimum Sum of Squared Difference

[LeetCode Problem Link](https://leetcode.com/problems/minimum-sum-of-squared-difference/)

## Problem Summary

You are given two integer arrays, `nums1` and `nums2`, along with two integers, `k1` and `k2`.

You can perform at most `k1 + k2` operations. In each operation, you can increase or decrease any element in either array by `1`.

Your goal is to minimize the sum of squared differences between corresponding elements:

`sum((nums1[i] - nums2[i])²)`

Return the minimum possible sum.

## Intuition

The key idea is simple: **reduce the largest differences first.**

Suppose the differences between corresponding elements are:

`[5, 3, 2]`

Reducing the difference of `5` to `4` decreases its squared contribution from `25` to `16`, saving `9`.

But reducing the difference of `2` to `1` only saves `3`.

Therefore, reducing larger differences gives us a greater improvement in the total sum.

Instead of sorting the differences and repeatedly finding the largest one, we can use a frequency array to count how many times each difference occurs.

## Approach

1. Calculate the absolute difference between each pair of corresponding elements.
2. Find the maximum difference and create a frequency array, `dp`, where `dp[i]` stores how many elements have a difference of `i`.
3. Combine `k1` and `k2` into a single operation budget, `k`.
4. Iterate through the differences from largest to smallest.
5. At each difference `i`, reduce as many occurrences as possible by one, moving them into the next smaller difference, `i - 1`.
6. Stop when all operations are used or all differences become zero.
7. Calculate the final sum of squared differences using the frequency array.

## Python Solution

```python
class Solution:
    def minSumSquareDiff(
        self,
        nums1: list[int],
        nums2: list[int],
        k1: int,
        k2: int
    ) -> int:
        n = len(nums1)

        diff = [
            abs(nums1[i] - nums2[i])
            for i in range(n)
        ]

        max_diff = max(diff)

        dp = [0] * (max_diff + 1)

        for x in diff:
            dp[x] += 1

        k = k1 + k2

        for i in range(max_diff, 0, -1):
            take = min(k, dp[i])

            dp[i] -= take
            dp[i - 1] += take
            k -= take

            if k == 0:
                break

        return sum(
            i * i * dp[i]
            for i in range(1, max_diff + 1)
        )
```

## Complexity Analysis

- **Time Complexity:** `O(n + D)`, where `n` is the array length and `D` is the maximum absolute difference. We build the frequency array in `O(n)`, process the differences in `O(D)`, and calculate the final sum in `O(D)`.

- **Space Complexity:** `O(n + D)`, where `O(n)` is used to store the differences and `O(D)` is used for the frequency array.

## Key Takeaway

When minimizing a sum of squared differences, reducing the largest differences first gives the greatest immediate improvement. A frequency array lets us process these differences efficiently without sorting them.