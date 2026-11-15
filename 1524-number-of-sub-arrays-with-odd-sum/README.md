# LeetCode 1524 — Number of Sub-arrays With Odd Sum

# 1524. Number of Sub-arrays With Odd Sum

[LeetCode Problem](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/)

## Problem Summary

Given an integer array `arr`, count the number of non-empty subarrays whose sum is odd.

Return the answer modulo \(10^9 + 7\).

## Intuition

A brute-force approach checks every possible subarray and calculates its sum, resulting in O(n²) time complexity.

We can optimize this using **prefix sums and parity**.

The key observation is:

- Even prefix sum - Even prefix sum = Even.
- Odd prefix sum - Odd prefix sum = Even.
- Even prefix sum - Odd prefix sum = Odd.
- Odd prefix sum - Even prefix sum = Odd.

Therefore, a subarray has an odd sum whenever its two surrounding prefix sums have different parity.

Instead of checking every subarray, we can simply count the number of even and odd prefix sums.

The empty prefix (sum = 0) must also be included, so we initialize `even = 1`.

## Approach

1. Create a prefix parity array where each element stores the parity of the corresponding prefix sum.
2. Initialize `even = 1` to account for the empty prefix and `odd = 0`.
3. Iterate through the array and calculate the current prefix parity using `(prefix[i] + arr[i]) % 2`.
4. If the current prefix is odd, increment `odd`. Otherwise, increment `even`.
5. Every even prefix can pair with every odd prefix to form an odd-sum subarray.
6. Return `(even * odd) % MOD`.

## Code

```python
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        

        prefix = [0] * (n + 1)
        odd = 0
        even = 1

        for i in range(n):
            prefix[i+1] = (prefix[i] + arr[i]) % 2

            if prefix[i+1] % 2:
                odd += 1
            else:
                even += 1
        MOD = 10**9 + 7
        return (even * odd) % MOD
```

## Complexity Analysis

- **Time Complexity:** O(n) — We traverse the array exactly once.
- **Space Complexity:** O(n) — We use a prefix array of size n + 1.

## Key Takeaway

A subarray sum can be represented as the difference between two prefix sums.

For parity problems, we don't need the actual prefix sums. We only need to know whether they are odd or even.

**Different prefix parities produce an odd-sum subarray.**

This transforms a brute-force O(n²) solution into an O(n) solution using prefix parity counting.