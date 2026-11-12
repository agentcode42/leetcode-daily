# LeetCode 3105 — Longest Strictly Increasing or Strictly Decreasing Subarray

# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

**LeetCode:** [3105. Longest Strictly Increasing or Strictly Decreasing Subarray](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/)

## Problem Summary

Given an integer array `nums`, find the length of the longest subarray that is either:

- **Strictly Increasing:** Every element is greater than the previous element.
- **Strictly Decreasing:** Every element is smaller than the previous element.

A subarray must contain contiguous elements.

Return the maximum length among both types of subarrays.

## Intuition

We can solve this problem in a single traversal by maintaining two counters:

- `inc`: Length of the current strictly increasing subarray.
- `dec`: Length of the current strictly decreasing subarray.

For every adjacent pair, we compare the current element with the previous one.

- If the current element is greater, extend the increasing subarray and reset the decreasing counter.
- If the current element is smaller, extend the decreasing subarray and reset the increasing counter.
- If both elements are equal, reset both counters because neither subarray can continue.

Keep updating the maximum length using both counters.

## Approach

1. Initialize `inc`, `dec`, and `max_val` to `1`, since every single element forms a valid subarray.
2. Traverse the array starting from index `1`.
3. Compare `nums[i]` with `nums[i-1]`:
   - If `nums[i] > nums[i-1]`, increment `inc` and reset `dec` to `1`.
   - If `nums[i] < nums[i-1]`, increment `dec` and reset `inc` to `1`.
   - Otherwise, reset both counters to `1`.
4. Update the maximum length after every comparison.
5. Return the maximum length.

## Python Solution

```python
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dec, inc = 1, 1
        max_val = 1

        for i in range(1, n):
            if nums[i] < nums[i-1]:
                dec += 1
                inc = 1
            elif nums[i] > nums[i-1]:
                inc += 1
                dec = 1
            else:
                inc = 1
                dec = 1

            max_val = max(max_val, inc, dec)

        return max_val
```

## C Solution

```c
int longestMonotonicSubarray(int* nums, int numsSize) {
    int inc_count = 1;
    int dec_count = 1;
    int max_count = 1;

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > nums[i-1]) {
            inc_count++;
            dec_count = 1;
        }
        else if (nums[i] < nums[i-1]) {
            inc_count = 1;
            dec_count++;
        }
        else {
            inc_count = 1;
            dec_count = 1;
        }

        int max = dec_count;
        if (inc_count > max) max = inc_count;
        if (max_count < max) max_count = max;
    }

    return max_count;
}
```

## Complexity Analysis

Let `n` be the length of the input array.

- **Time Complexity:** `O(n)` — We traverse the array exactly once, performing constant-time operations at each index.
- **Space Complexity:** `O(1)` — Only a few variables are used, regardless of the input size.

## Key Takeaway

Both increasing and decreasing subarrays can be tracked simultaneously using two counters. Resetting the opposite counter whenever the direction changes ensures that we always maintain the lengths of the current valid monotonic subarrays.

A simple **one-pass greedy approach** is enough to solve this problem efficiently.