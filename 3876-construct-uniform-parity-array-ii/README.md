# LeetCode 3876 — Construct Uniform Parity Array II

# Construct Uniform Parity Array I — LeetCode 3875

## Problem

You are given an array `nums1` containing `n` distinct integers.

For every index `i`, you can choose either:

* `nums2[i] = nums1[i]`
* `nums2[i] = nums1[i] - nums1[j]`, where `j != i` and the result is at least `1`

The goal is to determine whether we can construct `nums2` such that **all elements are either odd or all elements are even**.

---

## Key Observation

The important question is:

> When can subtracting another element change the parity of a number?

Parity behaves like this:

```text
even - even = even
odd  - odd  = even

even - odd  = odd
odd  - even = odd
```

Therefore, subtracting an **odd number flips the parity**.

So if we want to turn an even number into an odd number, we need to subtract an odd number.

---

## Why Does the Smallest Odd Number Matter?

Suppose the array contains odd numbers.

Take the smallest odd number:

```text
minOdd
```

This number cannot be changed from odd to even.

To change its parity, we would need to subtract another odd number that is smaller than it:

```text
minOdd - smallerOdd >= 1
```

But no smaller odd number exists.

Therefore, the smallest odd number is forced to remain odd.

That means if the array contains both odd and even numbers, the final array **must be all odd**.

---

## What About the Even Numbers?

Every even number must become odd.

The easiest candidate to subtract is `minOdd`:

```text
even - minOdd = odd
```

But the result must also be at least `1`.

Therefore:

```text
even - minOdd >= 1
```

which means:

```text
minOdd < even
```

This must be true for **every even number**.

So we only need to compare the smallest even number:

```text
minOdd < minEven
```

If this is true, `minOdd` is smaller than every even number, so every even number can be converted into a positive odd number.

---

## Final Condition

There are three cases.

### 1. No odd numbers

The original array is already entirely even.

```text
→ true
```

### 2. No even numbers

The original array is already entirely odd.

```text
→ true
```

### 3. Both odd and even numbers exist

We need:

```text
minOdd < minEven
```

Therefore:

```python
return minOdd < minEven
```

---

## Solution 1 — `% 2`

```python
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd = float('inf')
        minEven = float('inf')

        for n in nums1:
            if n % 2:
                minOdd = min(minOdd, n)
            else:
                minEven = min(minEven, n)

        if minOdd == float('inf') or minEven == float('inf'):
            return True

        return minOdd < minEven
```

---

## Solution 2 — Bitwise Parity Check

We can also check whether a number is odd using:

```python
n & 1
```

For an integer:

```text
even → binary ends in 0
odd  → binary ends in 1
```

The bitwise AND with `1` extracts the last bit:

```text
6  = 110
6 & 1 = 0

7  = 111
7 & 1 = 1
```

So:

```python
if n & 1:
```

means:

> `n` is odd.

The solution becomes:

```python
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd = float('inf')
        minEven = float('inf')

        for n in nums1:
            if n & 1:
                minOdd = min(minOdd, n)
            else:
                minEven = min(minEven, n)

        if minOdd == float('inf') or minEven == float('inf'):
            return True

        return minOdd < minEven
```

### `% 2` vs `& 1`

Both correctly determine parity for integers.

```python
n % 2
```

is usually easier to read and understand.

```python
n & 1
```

is the classic bitwise way of checking the least significant bit.

The main advantage here is that it directly expresses the bit-level fact that the least significant bit determines parity.

---

## Complexity

We scan the array once.

* **Time:** `O(n)`
* **Space:** `O(1)`

---

## Main Takeaway

The entire problem reduces to one observation:

> If an odd number exists, the smallest odd number cannot change parity.

Therefore, it must remain odd.

Every even number must be larger than it so that we can subtract it and obtain a positive odd number.

Hence:

```text
minOdd < minEven
```

with the special cases where the array contains only odd numbers or only even numbers returning `true`.
