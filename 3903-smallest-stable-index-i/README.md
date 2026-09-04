# LeetCode 3903 — Smallest Stable Index I

## Problem

You are given an integer array `nums` of length `n` and an integer `k`.

For each index `i`, define its **instability score** as:

```text
max(nums[0..i]) - min(nums[i..n-1])
````

An index is **stable** if its instability score is less than or equal to `k`.

Return the **smallest stable index**. If no stable index exists, return `-1`.

## Approach

For every index `i`, we need two values:

* The maximum value from `nums[0]` to `nums[i]`
* The minimum value from `nums[i]` to `nums[n-1]`

We precompute these using two arrays:

### Prefix Maximum

`prefix[i]` stores:

```text
max(nums[0..i])
```

### Suffix Minimum

`suffix[i]` stores:

```text
min(nums[i..n-1])
```

Then the instability score at index `i` is:

```text
prefix[i] - suffix[i]
```

Since we need the **smallest stable index**, we scan from left to right and immediately return the first index whose score is at most `k`.

If no index satisfies the condition, return `-1`.

## Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

## Code

```python
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = max(nums[i], prefix[i - 1])

        suffix = [0] * n
        suffix[-1] = nums[-1]

        for i in reversed(range(n - 1)):
            suffix[i] = min(suffix[i + 1], nums[i])

        for i in range(n):
            if prefix[i] - suffix[i] <= k:
                return i

        return -1
```

```


