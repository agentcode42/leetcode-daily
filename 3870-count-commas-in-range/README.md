# LeetCode 3870 — Count Commas in Range

# 3870. Count Commas in Range

[LeetCode Problem](https://leetcode.com/problems/count-commas-in-range/)

## Problem

You are given an integer `n`.

Return the total number of commas used when writing all integers from `1` to `n` inclusive using standard number formatting.

A comma is inserted after every three digits from the right.

For example:

* `1` → `1` → 0 commas
* `999` → `999` → 0 commas
* `1000` → `1,000` → 1 comma
* `9999` → `9,999` → 1 comma

### Constraint

* `1 <= n <= 10^5`

## Approach

The important observation is that, under the given constraint, the largest number is `99999`.

Therefore, every number from `1` to `999` contains **no commas**, while every number from `1000` onward contains **exactly one comma**.

So instead of checking every number individually, we can directly count how many integers are in the range `[1000, n]`.

The number of such integers is:

```text
n - 1000 + 1 = n - 999
```

Therefore:

* If `n < 1000`, the answer is `0`.
* Otherwise, the answer is `n - 999`.

## Algorithm

1. If `n < 1000`, return `0`.
2. Otherwise, return `n - 999`.

## Complexity

* **Time:** `O(1)`
* **Space:** `O(1)`

## Python

```python
class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        if 999 < n < 1000000:
            return n - 999
```

## Example

For:

```text
n = 1005
```

The numbers containing commas are:

```text
1000, 1001, 1002, ..., 1005
```

There are:

```text
1005 - 999 = 6
```

commas in total.

## Key Takeaway

Since every number from `1000` to `n` has exactly one comma, the problem reduces to simply counting the numbers in that range.
