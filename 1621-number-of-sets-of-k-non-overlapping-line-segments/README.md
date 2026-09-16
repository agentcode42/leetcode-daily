# 1621. Number of Sets of K Non-Overlapping Line Segments

[LeetCode Problem](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/)

## Intuition

We have `n` points on a line:

```text
0  1  2  3  4  ...  n-1
```

We need to choose exactly `k` non-overlapping line segments.

A segment is represented by its two endpoints. For example:

```text
0-----2
```

means a segment from point `0` to point `2`.

For `k` segments, the endpoints can be written as:

```text
a1 < b1 <= a2 < b2 <= a3 < b3 ...
```

The important part is that two consecutive segments are allowed to share an endpoint.

For example:

```text
0-----2
      2-----4
```

is valid because the first segment ends where the second segment starts.

### Removing the Shared-Endpoint Problem

To turn this into a normal combination problem, we shift the endpoints of each segment.

For segment `1`, add `0`.

For segment `2`, add `1`.

For segment `3`, add `2`.

And so on.

So:

```text
Segment 1: +0
Segment 2: +1
Segment 3: +2
...
Segment k: +(k-1)
```

This converts

```text
a1 < b1 <= a2 < b2 <= ...
```

into a strictly increasing sequence of `2k` values.

After shifting, the largest possible value becomes:

```text
(n - 1) + (k - 1) = n + k - 2
```

So there are:

```text
n + k - 1
```

possible positions for the transformed endpoints.

We therefore only need to choose `2k` positions from `n + k - 1` positions.

That is simply:

```text
C(n + k - 1, 2k)
```

where

```text
C(n, k) = n! / (k! * (n-k)!)
```

---

## Example 1

### Input

```text
n = 3
k = 2
```

The formula gives:

```text
C(3 + 2 - 1, 4)
= C(4, 4)
= 1
```

The only possibility is:

```text
0-----1-----2
```

which represents the two segments:

```text
0-----1
      1-----2
```

So the answer is:

```text
1
```

---

## Example 2

### Input

```text
n = 4
k = 2
```

We get:

```text
C(4 + 2 - 1, 4)
= C(5, 4)
= 5
```

So there are `5` valid ways to choose two non-overlapping segments.

This also shows why simply counting the minimum number of points is not enough. Segments can either share endpoints or be separated by unused points.

---

## Calculating the Combination

We need:

```text
C(n + k - 1, 2k)
```

Using the factorial formula:

```text
C(total, choose)
= total! / (choose! * (total - choose)!)
```

where:

```text
total = n + k - 1
choose = 2k
```

Because the answer is required modulo `10^9 + 7`, we cannot perform normal division.

Instead, we use a modular inverse:

```text
a / b ≡ a * b^(-1) (mod MOD)
```

Since `MOD = 10^9 + 7` is prime, Fermat's Little Theorem gives:

```text
b^(-1) ≡ b^(MOD-2) (mod MOD)
```

In Python:

```python
pow(b, MOD - 2, MOD)
```

computes the modular inverse of `b`.

---

## Solution

```python
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        total = n + k - 1
        choose = 2 * k

        def factorial(x):
            res = 1

            for i in range(2, x + 1):
                res = (res * i) % MOD

            return res

        a = factorial(total)
        b = factorial(choose)
        c = factorial(total - choose)

        return (
            a
            * pow(b, MOD - 2, MOD)
            * pow(c, MOD - 2, MOD)
        ) % MOD
```

## Complexity Analysis

Let:

```text
total = n + k - 1
```

We calculate three factorials, each taking at most `O(total)` time.

The modular inverse using `pow(..., MOD - 2, MOD)` takes `O(log MOD)` time.

Therefore:

**Time Complexity:** `O(n + k + log MOD)`

Since `MOD` is fixed, this is effectively:

**Time Complexity:** `O(n + k)`

**Space Complexity:** `O(1)`

Only a few variables are used, and the factorial calculation does not require an additional array.

---

## Key Takeaway

The main trick is recognizing that the shared endpoints make the endpoint sequence non-strict.

By shifting the endpoints of each segment:

```text
segment 1 → +0
segment 2 → +1
segment 3 → +2
...
```

we convert the problem into choosing `2k` strictly increasing positions from `n + k - 1` positions.

Therefore:

```text
Answer = C(n + k - 1, 2k)
```
