# 1385. Find the Distance Value Between Two Arrays

[LeetCode Problem](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/)

## Problem Summary

Given two integer arrays `arr1` and `arr2`, and an integer `d`, find the number of elements in `arr1` whose absolute difference with **every element in `arr2` is greater than `d`**.

In other words, count elements `a` in `arr1` for which:

`abs(a - b) > d` for every `b` in `arr2`.

## Intuition

For every element in `arr1`, we compare it with every element in `arr2`.

If we find even one element where the absolute difference is less than or equal to `d`, that element from `arr1` does not qualify.

Otherwise, we increase our result count.

We can stop checking an element as soon as we find a match because we already know it cannot be counted.

## Approach

1. Initialize a result counter `res` to zero.
2. Iterate through every element `a` in `arr1`.
3. Assume the element is valid by setting `flag = True`.
4. Iterate through every element `b` in `arr2`.
5. If `abs(a - b) <= d`, mark the element as invalid and break out of the inner loop.
6. If the flag remains `True` after checking all elements in `arr2`, increment the result.
7. Return the final count.

## Code

```python
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res = 0

        for a in arr1:
            flag = True

            for b in arr2:
                if abs(a - b) <= d:
                    flag = False
                    break

            if flag:
                res += 1

        return res
```

## Example

**Input:**
```python
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
```

**Output:**
```python
2
```

**Explanation:**

- `4`: No element in `arr2` has a difference of 2 or less. Count it.
- `5`: No element in `arr2` has a difference of 2 or less. Count it.
- `8`: The element `8` exists in `arr2`, so it does not qualify.

The final answer is `2`.

## Complexity Analysis

- **Time Complexity:** `O(n * m)` — We potentially compare every element of `arr1` with every element of `arr2`.
- **Space Complexity:** `O(1)` — We only use a counter and a boolean flag.