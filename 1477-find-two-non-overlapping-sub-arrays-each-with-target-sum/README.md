# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

## Problem

Given an array `arr` and an integer `target`, find two **non-overlapping subarrays** where each subarray has a sum equal to `target`.

Return the minimum possible sum of their lengths.

If no such two subarrays exist, return `-1`.

---

## Approach

The brute-force idea is to find every subarray whose sum equals `target`, then compare every pair of valid subarrays to find two that do not overlap.

However, there can be many valid subarrays, making the pairwise comparison expensive.

The key observation is:

> When combining two non-overlapping subarrays, for any position we only need the **shortest valid subarray on the left** and the **shortest valid subarray on the right**.

Because all values in `arr` are positive, we can use a **sliding window** to find target-sum subarrays in linear time.

We build two arrays:

* `prefix[i]` = shortest target-sum subarray that ends at or before index `i`
* `suffix[i]` = shortest target-sum subarray that starts at or after index `i`

Then, for every split between `i` and `i + 1`:

```text
[  left part  ][  right part  ]
       i            i + 1
```

we can combine:

```python
prefix[i] + suffix[i + 1]
```

and take the minimum.

---

## Building `prefix`

We scan from left to right using a sliding window.

```python
curr = 0
left = 0

for right in range(n):
    curr += arr[right]

    while curr > target and left < right:
        curr -= arr[left]
        left += 1

    if curr == target:
        length = right - left + 1
        best = min(best, length)

    prefix[right] = best
```

`best` stores the shortest valid subarray found so far.

Therefore, even if there is no target-sum subarray ending exactly at `right`, `prefix[right]` still remembers the best one found earlier.

---

## Building `suffix`

The same idea is applied from right to left.

The sliding window now moves in the opposite direction.

```python
curr = 0
right = n - 1

for left in range(n - 1, -1, -1):
    curr += arr[left]

    while curr > target and left < right:
        curr -= arr[right]
        right -= 1

    if curr == target:
        length = right - left + 1
        best = min(best, length)

    suffix[left] = best
```

Here:

```text
suffix[i]
```

stores the shortest valid subarray starting at or after `i`.

---

## Combining the Two Arrays

Now consider every possible split:

```text
arr:

[ 0 ........ i ][ i + 1 ........ n-1 ]
       prefix          suffix
```

The two chosen subarrays cannot overlap because the first one is completely within the left side and the second one is completely within the right side.

Therefore:

```python
for i in range(n - 1):
    res = min(res, prefix[i] + suffix[i + 1])
```

If no valid combination was found, return `-1`.

---

## Example

```text
arr = [3, 2, 2, 4, 3]
target = 5
```

The target-sum subarrays include:

```text
[3, 2]       length = 2
[2, 3]       length = 2
```

These two subarrays are non-overlapping:

```text
[3, 2] [2, 4, 3]
 ^^^^

              [2, 3]
```

Their total length is:

```text
2 + 2 = 4
```

So the answer is:

```text
4
```

---

## Why Sliding Window Works

All elements of `arr` are positive.

Therefore:

* Increasing `right` can only increase the window sum.
* Increasing `left` can only decrease the window sum.

This allows us to maintain a valid sliding window in linear time.

For each element, the `left` and `right` pointers only move forward within their respective passes, so the total work of each sliding-window pass is `O(n)`.

---

## Complexity Analysis

Let `n` be the length of `arr`.

### Time Complexity

* Build `prefix`: `O(n)`
* Build `suffix`: `O(n)`
* Check every split: `O(n)`

Therefore:

**Time: `O(n)`**

### Space Complexity

We store two arrays of length `n`:

* `prefix`
* `suffix`

Therefore:

**Space: `O(n)`**

---

## Code

```python
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        best = 2 * n
        prefix = [best] * n

        curr = 0
        left = 0

        for right in range(n):
            curr += arr[right]

            while curr > target and left < right:
                curr -= arr[left]
                left += 1

            if curr == target:
                length = right - left + 1
                best = min(best, length)

            prefix[right] = best

        best = 2 * n
        suffix = [best] * n

        curr = 0
        right = n - 1

        for left in range(n - 1, -1, -1):
            curr += arr[left]

            while curr > target and left < right:
                curr -= arr[right]
                right -= 1

            if curr == target:
                length = right - left + 1
                best = min(best, length)

            suffix[left] = best

        res = 2 * n

        for i in range(n - 1):
            res = min(res, prefix[i] + suffix[i + 1])

        return res if res != 2 * n else -1
```
