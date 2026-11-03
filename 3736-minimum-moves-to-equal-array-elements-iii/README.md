# 3736. Minimum Moves to Equal Array Elements III

LeetCode · Easy · Python

Problem: [Minimum Moves to Equal Array Elements III](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/?utm_source=chatgpt.com)

## Problem Summary

Given an integer array `nums`, return the minimum number of moves required to make all array elements equal.

In one move, you can increase any element by `1`.

The goal is to make every element equal using the minimum number of moves.

## Intuition

Since we can only increase elements, the optimal target must be the maximum element in the array.

- We cannot decrease elements to match a smaller value.
- Therefore, every element must eventually reach the current maximum.
- The moves required for each element are simply `max(nums) - num`.

We calculate the difference for every element and add them together.

## Approach

1. Find the maximum element in the array using `max(nums)`.
2. Iterate through the array.
3. Calculate how many moves each element needs using `maxm - n`.
4. Sum all the differences and return the result.

## Python Solution

```
class Solution:    def minMoves(self, nums: List[int]) -> int:        maxm = max(nums)        return sum(maxm - n for n in nums)
```

## Example Walkthrough

Example 1:

```
nums = [1, 2, 3]
```

Maximum element = `3`

| Element | Moves required |
| ------- | -------------- |
| 1       | 3 - 1 = 2      |
| 2       | 3 - 2 = 1      |
| 3       | 3 - 3 = 0      |

Total moves = `2 + 1 + 0 = 3`

Output:

```
3
```

Example 2:

```
nums = [4, 4, 5]
```

Maximum element = `5`

Moves required = `1 + 1 + 0 = 2`

Output:

```
2
```

## Complexity Analysis

- Time Complexity: `O(n)` — Finding the maximum and calculating the sum both take linear time.
- Space Complexity: `O(1)` — Only a constant amount of extra space is used (excluding the input).

Key Takeaway: When you can only increase array elements, making every element equal to the maximum is optimal. The answer is simply the sum of differences between the maximum element and every other element.