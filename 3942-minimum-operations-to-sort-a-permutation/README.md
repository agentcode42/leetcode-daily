# 3942. Minimum Operations to Sort a Permutation

**LeetCode:** [3942. Minimum Operations to Sort a Permutation](https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/)  
**Difficulty:** Medium

## Problem

You are given a permutation of the integers from `0` to `n - 1`. You may only:

1. Reverse the entire array.
2. Rotate the array left by one position (move the first element to the end).

Return the minimum number of operations needed to sort the array in increasing order, or `-1` if it cannot be sorted using these operations.

## Intuition

These operations cannot rearrange elements arbitrarily. Rotating an array only changes where its circular order starts, and reversing it changes the direction of that order. Therefore, a sortable permutation must be either:

- In increasing order when we walk **right from `0`**, wrapping around to the beginning when needed.
- In increasing order when we walk **left from `0`**, wrapping around to the end when needed.

We test both possibilities separately. If neither works, sorting is impossible.

## Step-by-Step Approach

### 1. Find the position of `0`

```python
zero = nums.index(0)
```

The sorted target always begins with `0`. Its current index tells us how many left rotations would bring it to the front. We call this index `zero` and use it to start both circular checks.

### 2. Check the circular order in either direction

```python
def check(step):
    for i in range(1, n):
        prev = (zero + (i - 1) * step) % n
        curr = (zero + i * step) % n

        if nums[prev] > nums[curr]:
            return False
    return True
```

- `step = 1` visits indices to the **right** of `zero`.
- `step = -1` visits indices to the **left** of `zero`.
- `% n` wraps an index around the array boundaries.
- `prev` and `curr` are two neighboring indices in the chosen traversal. If their values decrease, that traversal is not increasing, so `check` returns `False`.
- We make `n - 1` comparisons because we only need to check the full sequence starting from `0`; there is no need to compare the last value back to `0`.

### 3. Reject arrays that match neither direction

```python
inc = check(1)
dec = check(-1)

if not inc and not dec:
    return -1
```

Both directions are independent possibilities. The array is impossible to sort only when **both** checks fail.

### 4. Calculate the minimum cost for the valid direction

The four expressions come from counting the exact operations in two possible methods for each valid pattern.

#### If `inc` is `True`: increasing when walking right from `0`

```python
return min(zero, n - zero + 2)
```

**Method A — rotate only: `zero` operations**

A left rotation moves each element one position toward the front. Since `0` is at index `zero`, rotating left `zero` times brings `0` to the beginning, and the increasing circular order becomes `[0, 1, ..., n - 1]`.

Cost: `zero`.

**Method B — reverse, rotate, reverse again: `n - zero + 2` operations**

1. Reverse the array: `1` operation.
2. Rotate left `n - zero` times: `n - zero` operations.
3. Reverse again: `1` operation.

Total: `1 + (n - zero) + 1 = n - zero + 2`.

We take the smaller of these two costs.

#### Otherwise: increasing when walking left from `0`

```python
return min(zero + 2, n - zero)
```

**Method A — rotate, then reverse: `zero + 2` operations**

1. Rotate left `zero` times to bring `0` to the beginning.
2. Rotate left once more to move `0` to the end: `zero + 1` rotations in total.
3. Reverse the array once to put `0` at the beginning and produce increasing order.

Total: `(zero + 1) + 1 = zero + 2`.

**Method B — reverse, then rotate: `n - zero` operations**

1. Reverse the array: `1` operation.
2. Rotate left `n - zero - 1` times to bring `0` to the beginning.

Total: `1 + (n - zero - 1) = n - zero`.

We take the smaller of these two costs.

## Python Solution

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)

        def check(step):
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n

                if nums[prev] > nums[curr]:
                    return False
            return True

        inc = check(1)
        dec = check(-1)

        if not inc and not dec:
            return -1

        if inc:
            return min(zero, n - zero + 2)
        else:
            return min(zero + 2, n - zero)
```

## Example Walkthrough

For `nums = [0, 2, 1]`:

- `n = 3` and `zero = 0`.
- Walking right from `0` gives `0, 2, 1`, which is not increasing, so `check(1)` is `False`.
- Walking left from `0` gives `0, 1, 2`, so `check(-1)` is `True`.
- The two costs for this direction are `zero + 2 = 2` and `n - zero = 3`.
- The answer is `min(2, 3) = 2`.

One way to achieve it is to rotate left once, producing `[2, 1, 0]`, then reverse to get `[0, 1, 2]`.

## Complexity Analysis

- **Time:** `O(n)` — finding `0` and checking both directions take linear time.
- **Extra space:** `O(1)` — the solution uses only a fixed number of variables and does not create another array.
