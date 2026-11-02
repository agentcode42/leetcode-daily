# 462. Minimum Moves to Equal Array Elements II

## Problem Summary

Given an integer array `nums`, we need to make all elements equal.

In one move, we can increase or decrease any element by 1.

Our task is to find the **minimum number of moves** required to make every element equal.

## Intuition

The key observation is that the **median minimizes the sum of absolute differences** between all elements and a chosen target.

Why the median?

- If we choose a target smaller than the median, more elements will need to move upward.
- If we choose a target larger than the median, more elements will need to move downward.
- Choosing the median balances the number of elements on both sides and minimizes the total movement.

For example:

`[1, 2, 3, 4, 5]`

The median is `3`.

Moves required:

- `1 → 3` = 2 moves
- `2 → 3` = 1 move
- `3 → 3` = 0 moves
- `4 → 3` = 1 move
- `5 → 3` = 2 moves

Total = `2 + 1 + 0 + 1 + 2 = 6`

Therefore, the minimum number of moves is **6**.

## Approach

1. Get the length of the array.
2. Sort the array in ascending order.
3. Find the middle element, which is the median.
4. Calculate the absolute difference between the median and every element.
5. Return the sum of all these differences.

We use `abs()` because we only care about the number of moves, regardless of whether an element needs to increase or decrease.

## Python Code

```python
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        mid = nums[n//2]
        return sum(abs(mid-a) for a in nums)
```

## Complexity Analysis

- **Time Complexity:** `O(n log n)` — Sorting the array takes `O(n log n)`, and calculating the total moves takes `O(n)`.
- **Space Complexity:** `O(1)` auxiliary space for the sorting and calculation, assuming in-place sorting.

## Example

**Input:**
```python
nums = [1, 2, 3, 4, 5]
```

**Sorted Array:**
```python
[1, 2, 3, 4, 5]
```

**Median:**
```python
3
```

**Total Moves:**
```python
abs(3-1) + abs(3-2) + abs(3-3) + abs(3-4) + abs(3-5)

= 2 + 1 + 0 + 1 + 2

= 6
```

**Output:**
```python
6
```

## Key Takeaway

When minimizing the sum of absolute differences between array elements and a common target, the **median is the optimal target**.

Sorting gives us an easy way to find the median and calculate the minimum moves.