# 3871. Count Commas in Range II

**LeetCode:** [3871. Count Commas in Range II](https://leetcode.com/problems/count-commas-in-range-ii/)

## Problem

You are given an integer `n`.

Return the total number of commas used when writing all integers from `1` to `n` inclusive using standard number formatting.

A comma is inserted after every three digits from the right.

Examples:

* `1` → `999` → no commas
* `1,000` → 1 comma
* `1,000,000` → 2 commas
* `1,000,000,000` → 3 commas

### Constraint

```text
1 <= n <= 10^15
```

---

## Approach

Instead of formatting every number individually, count how many numbers contribute a comma at each position.

A comma appears:

* After 3 digits for numbers `>= 10^3`
* After 6 digits for numbers `>= 10^6`
* After 9 digits for numbers `>= 10^9`
* After 12 digits for numbers `>= 10^12`
* After 15 digits for numbers `>= 10^15`

For a particular comma position `10^k`, every number from `10^k` through `n` contributes one comma.

Therefore, if:

```text
n >= 10^k
```

the number of commas contributed by that position is:

```text
n - 10^k + 1
```

We simply add this for every multiple of three digits.

---

## Solution

```python
class Solution:
    def countCommas(self, n: int) -> int:
        res = 0

        for i in range(3, 16, 3):
            if n >= 10**i:
                res += n - ((10**i) - 1)

        return res
```

### How the formula works

For example, suppose:

```text
n = 2500
```

Numbers from `1000` to `2500` contain one comma.

Count:

```text
2500 - 1000 + 1 = 1501
```

The code calculates the same thing as:

```python
n - (10**3 - 1)
```

which is:

```text
2500 - 999 = 1501
```

For larger `n`, the same calculation is performed for `10^6`, `10^9`, `10^12`, and `10^15`.

---

## Alternative Direct Solution

Because the constraint only goes up to `10^15`, the possible comma positions are fixed. We can also write the solution explicitly:

```python
class Solution:
    def countCommas(self, n: int) -> int:
        res = 0

        if n >= 10**3:
            res += n - (10**3 - 1)

        if n >= 10**6:
            res += n - (10**6 - 1)

        if n >= 10**9:
            res += n - (10**9 - 1)

        if n >= 10**12:
            res += n - (10**12 - 1)

        if n >= 10**15:
            res += n - (10**15 - 1)

        return res
```

The loop-based version is preferable because it avoids repeating the same logic and makes the pattern more obvious.

---

## Complexity

There are only 5 possible comma positions because `n <= 10^15`.


- **Time:** O(1) — exactly 5 iterations
- **Space:** O(1)
---

## Key Insight

The important observation is:

> **Don't count commas number by number. Count how many numbers contribute a comma at each digit position.**

For every comma position `10^3, 10^6, 10^9, ...`, all numbers from that threshold through `n` contribute exactly one comma.

This turns what could look like a formatting problem into a simple counting problem.
