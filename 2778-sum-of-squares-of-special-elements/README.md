# 2778. Sum of Squares of Special Elements

[LeetCode Problem Link](https://leetcode.com/problems/sum-of-squares-of-special-elements/)

## Problem Summary

You are given a 0-indexed integer array `nums` of length `n`.

An element `nums[i]` is considered **special** if `n` is divisible by `i + 1`.

Return the sum of the squares of all special elements.

## Intuition

The key observation is that an element is special when its **1-based position divides the length of the array evenly**.

Since Python uses 0-based indexing, the position of `nums[i]` is `i + 1`.

For every element, we check whether `n % (i + 1) == 0`. If the condition is true, we add the square of that element to our result.

There is no need for extra data structures or complicated algorithms. We can solve the problem in a single pass through the array.

## Approach

1. Get the length of the array and store it in `n`.
2. Initialize `res = 0` to store the sum of squares.
3. Iterate through every index `i` in the array.
4. Check whether `n % (i + 1) == 0`.
5. If the condition is true, add `nums[i] * nums[i]` to `res`.
6. Return `res`.

## Python Solution

```python
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            if n % (i + 1) == 0:
                res += nums[i] ** 2

        return res
```

## C Solution

```c
int sumOfSquares(int* nums, int numsSize) {
    int n = numsSize;
    long long res = 0;

    for (int i = 0; i < n; i++) {
        if (n % (i + 1) == 0) {
            res += nums[i] * nums[i];
        }
    }

    return (int)res;
}
```

## Complexity Analysis

- **Time Complexity:** `O(n)` — We iterate through the array exactly once, performing a constant-time divisibility check for each element.
- **Space Complexity:** `O(1)` — We use only a constant number of extra variables.

## Key Takeaway

An element is special if its 1-based index divides the array length. A simple modulo operation lets us identify these elements efficiently in a single pass.