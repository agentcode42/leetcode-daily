# 2567. Minimum Score by Changing Two Elements

[LeetCode Problem Link](https://leetcode.com/problems/minimum-score-by-changing-two-elements/)

## Problem Summary

We are given an integer array `nums`.

We can change **at most two elements** to any values we want. Our goal is to minimize the difference between the maximum and minimum elements after making these changes.

In other words, we want to minimize:

`max(nums) - min(nums)`

The key observation is that we don't need to consider every possible replacement value. Instead, we can sort the array and focus on the three smallest and three largest elements.

## Intuition

The score depends only on the minimum and maximum elements.

Since we can change two elements, we can eliminate the influence of up to two extreme values.

After sorting the array, the smallest elements are at the beginning, and the largest elements are at the end.

To minimize the final difference, we have three possible strategies:

1. Change the two largest elements.
2. Change the largest and smallest elements.
3. Change the two smallest elements.

These are the only three possibilities because we can remove at most two elements from the extremes.

Let's understand each case.

## Approach 1: Sorting

First, sort the array in ascending order.

After sorting, we have:

`nums[0] <= nums[1] <= ... <= nums[n-1]`

Now consider the three possible cases.

### Case 1: Change the two largest elements

If we change the two largest elements, the remaining minimum is `nums[0]`, and the remaining maximum is `nums[n-3]`.

Therefore:

`diff1 = nums[n-3] - nums[0]`

### Case 2: Change the smallest and largest elements

If we change the smallest and largest elements, the remaining minimum is `nums[1]`, and the remaining maximum is `nums[n-2]`.

Therefore:

`diff2 = nums[n-2] - nums[1]`

### Case 3: Change the two smallest elements

If we change the two smallest elements, the remaining minimum is `nums[2]`, and the remaining maximum is `nums[n-1]`.

Therefore:

`diff3 = nums[n-1] - nums[2]`

Finally, return the minimum among these three differences.

### Python Code

```python
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()

        diff1 = nums[-3] - nums[0]
        diff2 = nums[-2] - nums[1]
        diff3 = nums[-1] - nums[2]

        return min(diff1, diff2, diff3)
```

## Walkthrough

Consider:

`nums = [1, 4, 7, 8, 10, 15]`

After sorting:

`[1, 4, 7, 8, 10, 15]`

We calculate all three possibilities:

| Case | Remaining minimum | Remaining maximum | Difference |
|---|---:|---:|---:|
| Change two largest | 1 | 8 | 7 |
| Change smallest and largest | 4 | 10 | 6 |
| Change two smallest | 7 | 15 | 8 |

The three possible scores are:

- `diff1 = 8 - 1 = 7`
- `diff2 = 10 - 4 = 6`
- `diff3 = 15 - 7 = 8`

The minimum is `6`.

**Answer: 6**

## Approach 2: Using nsmallest and nlargest

Sorting the entire array is not strictly necessary.

We only need the three smallest and three largest elements to calculate our three possible differences.

Python provides two useful functions from the `heapq` module:

- `nsmallest(3, nums)` returns the three smallest elements in ascending order.
- `nlargest(3, nums)` returns the three largest elements in descending order.

We can use these two lists to calculate the same three possibilities.

Let:

- `small` = three smallest elements in ascending order.
- `large` = three largest elements in descending order.

The differences become:

**Case 1: Change the two largest elements**

`diff1 = large[2] - small[0]`

**Case 2: Change the smallest and largest elements**

`diff2 = large[1] - small[1]`

**Case 3: Change the two smallest elements**

`diff3 = large[0] - small[2]`

Return the minimum of these three differences.

### Python Code

```python
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        small = nsmallest(3, nums)
        large = nlargest(3, nums)

        diff1 = large[0] - small[2]
        diff2 = large[1] - small[1]
        diff3 = large[2] - small[0]

        return min(diff1, diff2, diff3)
```

**Note:** This approach requires importing `nsmallest` and `nlargest` from `heapq`.

```python
from heapq import nsmallest, nlargest
```

## Complexity Analysis

### Approach 1: Sorting

- **Time Complexity:** O(n log n) — Sorting the entire array.
- **Space Complexity:** O(n) in the worst case for Python's sorting implementation.

### Approach 2: nsmallest and nlargest

- **Time Complexity:** O(n log 3), effectively O(n), since we only need three smallest and three largest elements.
- **Space Complexity:** O(1) auxiliary space with respect to n, since both result lists contain only three elements. The functions may use additional internal storage depending on their implementation.

## Key Takeaway

The important observation is that changing two elements allows us to remove two extreme values from consideration.

There are only three ways to distribute those two changes across the smallest and largest ends of the sorted array:

1. Remove two largest elements.
2. Remove one smallest and one largest element.
3. Remove two smallest elements.

Once we recognize these three possibilities, the problem becomes a straightforward comparison of three differences.

**We don't need to try different replacement values. We only need to determine which two extreme elements should be ignored.**