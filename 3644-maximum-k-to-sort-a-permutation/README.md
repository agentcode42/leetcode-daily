# 3644. Maximum K to Sort a Permutation

[LeetCode Problem](https://leetcode.com/problems/maximum-k-to-sort-a-permutation/)

## Problem Summary

You are given a permutation `nums` containing every integer from `0` to `n - 1` exactly once. You may swap two values only when their bitwise AND is exactly `k`:

`nums[i] & nums[j] == k`

Return the **maximum value of `k`** that allows the permutation to be sorted. If the array is already sorted, return `0`.

## Intuition

In the sorted permutation, every value `x` belongs at index `x`. Therefore, whenever `nums[i] != i`, that value is misplaced and must move.

A value can participate in an allowed swap only if it contains every set bit of `k`. So every misplaced value must share all the set bits of `k`.

The bitwise AND of all misplaced values keeps exactly the bits that are present in **every** misplaced value. This gives us the largest possible `k`.

If the permutation is already sorted, there are no misplaced values, so the answer is `0`.

## Approach

1. Initialize `res` to `-1` in Python or `INT_MAX` in C. These starting values let the first bitwise AND keep the bits of the first misplaced value.
2. Visit every index `i` in the array.
3. If `nums[i] == i`, the value is already in its correct position, so skip it.
4. Otherwise, update `res` with `res & nums[i]`.
5. If no value was misplaced, return `0`; otherwise, return `res`.

### Why does this work?

Suppose the AND of all misplaced values is `k`. Every misplaced value contains all the set bits of `k`, so for any misplaced value `x`, `x & k == k`. Since `nums` is a permutation of `0` through `n - 1`, the value `k` is also available as an element. It can be used as a temporary helper to perform valid swaps and put the misplaced values in their correct positions.

A larger `k` would require a set bit that is missing from at least one misplaced value. That value could not take part in any swap with that `k`, so the array could not be sorted. Therefore, the AND of all misplaced values is the maximum valid answer.

## Examples

### Example 1

**Input:**

```text
nums = [0, 3, 2, 1]
```

**Output:**

```text
1
```

**Explanation:**

- `0` is at index `0`, and `2` is at index `2`; both are already correctly placed.
- The misplaced values are `3` and `1`.
- Their bitwise AND is `3 & 1 = 1` (`011 & 001 = 001` in binary).
- We can swap `3` and `1` because `3 & 1 == 1`, producing `[0, 1, 2, 3]`.
- Therefore, the maximum `k` is `1`.

### Example 2

**Input:**

```text
nums = [0, 1, 3, 2]
```

**Output:**

```text
2
```

**Explanation:**

- `0` and `1` are already correctly placed.
- The misplaced values are `3` and `2`.
- Their bitwise AND is `3 & 2 = 2` (`011 & 010 = 010` in binary).
- Swapping `3` and `2` is allowed because `3 & 2 == 2`, producing `[0, 1, 2, 3]`.
- Therefore, the maximum `k` is `2`.

### Example 3

**Input:**

```text
nums = [3, 2, 1, 0]
```

**Output:**

```text
0
```

**Explanation:**

Every value is misplaced. The bitwise AND of all values is `3 & 2 & 1 & 0 = 0`. Thus, the maximum possible `k` is `0`.

## Python Solution

```python
from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1

        for i in range(n):
            if nums[i] == i:
                continue
            res &= nums[i]

        return 0 if res == -1 else res
```

## C Solution

```c
#include <limits.h>

int sortPermutation(int* nums, int numsSize) {
    int res = INT_MAX;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == i) {
            continue;
        }
        res = res & nums[i];
    }

    return res == INT_MAX ? 0 : res;
}
```

## Complexity Analysis

- **Time Complexity:** `O(n)` — we inspect each array element once.
- **Space Complexity:** `O(1)` — only a constant amount of extra space is used.

## Key Takeaway

Ignore values already at their correct indices. The answer is the **bitwise AND of every misplaced value**, or `0` if the permutation is already sorted.