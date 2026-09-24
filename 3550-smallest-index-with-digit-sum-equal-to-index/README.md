# 3550. Smallest Index With Digit Sum Equal to Index

[LeetCode Problem](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/)

## Problem

Given an integer array `nums`, find the **smallest index** `i` such that the **sum of the digits of `nums[i]` is equal to `i`**.

If no such index exists, return `-1`.

### Example

```text
nums = [1, 3, 2, 6]

Index:       0   1   2   3
Value:       1   3   2   6
Digit Sum:   1   3   2   6
```

At index `2`, the value is `2`, whose digit sum is `2`.

So the answer is:

```text
2
```

---

## Intuition

We simply check every index from left to right.

For each number:

1. Calculate the sum of its digits.
2. Compare that sum with the current index.
3. If they are equal, return the index immediately.

Because we scan from index `0` onwards, the **first match is automatically the smallest index**.

---

## Approach

For every index `i`:

* Take `nums[i]`.
* Extract its digits one by one using:

  * `n % 10` → gets the last digit.
  * `n // 10` → removes the last digit.
* Add all the digits together.
* If the digit sum equals `i`, return `i`.

If we finish checking the entire array without finding a match, return `-1`.

---

## How Digit Extraction Works

Suppose:

```text
n = 123
```

We can extract its digits from right to left:

```text
123 % 10 = 3
123 // 10 = 12

12 % 10 = 2
12 // 10 = 1

1 % 10 = 1
1 // 10 = 0
```

So:

```text
Digit Sum = 3 + 2 + 1 = 6
```

This lets us calculate the digit sum without converting the number into a string.

---

## Code

```python
class Solution:

    def smallestIndex(self, nums: List[int]) -> int:

        for i, n in enumerate(nums):

            total = 0

            while n > 0:
                total += n % 10
                n = n // 10

            if total == i:
                return i

        return -1
```

---

## Complexity

Let:

* `n` = number of elements in `nums`
* `d` = maximum number of digits in any number

For every element, we may examine all of its digits.

### Time Complexity

```text
O(n × d)
```

Since `d` is the number of digits in an integer, this is effectively very small for typical constraints.

### Space Complexity

```text
O(1)
```

We only use a few variables and do not allocate additional data structures.

---

## Key Takeaway

The important observation is that **we don't need to search for the smallest index separately**.

By scanning the array from left to right:

```text
0 → 1 → 2 → 3 → ...
```

the first index whose digit sum matches the index is automatically the smallest valid index.

For the digit sum itself, `% 10` extracts the last digit and `// 10` removes it.
