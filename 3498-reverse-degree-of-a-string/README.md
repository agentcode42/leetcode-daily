# 3498. Reverse Degree of a String

[LeetCode Problem](https://leetcode.com/problems/reverse-degree-of-a-string/)

## Problem

Given a string `s`, calculate its **reverse degree**.

For each character:

* `a` has reverse alphabet value `26`
* `b` has reverse alphabet value `25`
* `c` has reverse alphabet value `24`
* ...
* `z` has reverse alphabet value `1`

For every character at position `i`, using **1-based indexing**, multiply its reverse alphabet value by its position.

Finally, return the sum of all these values.

### Example

For:

```text
s = "abc"
```

Reverse alphabet values are:

```text
a → 26
b → 25
c → 24
```

Multiply by their positions:

```text
26 × 1 = 26
25 × 2 = 50
24 × 3 = 72
```

So the answer is:

```text
26 + 50 + 72 = 148
```

## Approach

We can calculate everything in a single loop.

### 1. Find the reverse alphabet value

Normally:

```python
ord('a') = 97
ord('b') = 98
...
ord('z') = 122
```

So:

```python
ord(ch) - ord('a')
```

gives a value from `0` to `25`.

To reverse the alphabet, we use:

```python
26 - (ord(ch) - ord('a'))
```

This gives:

```text
a → 26
b → 25
c → 24
...
z → 1
```

### 2. Multiply by the position

Python's `enumerate()` gives us a zero-based index, so the actual position is:

```python
i + 1
```

Therefore, for every character:

```python
res += alpha_index * (i + 1)
```

## Code

```python
class Solution:
    def reverseDegree(self, s: str) -> int:

        res = 0

        for i, ch in enumerate(s):

            alpha_index = 26 - (ord(ch) - ord('a'))

            res += alpha_index * (i + 1)

        return res
```

## Complexity Analysis

Let `n` be the length of the string.

**Time Complexity:** `O(n)`

We visit every character exactly once.

**Space Complexity:** `O(1)`

We only use a few variables regardless of the size of the string.

## Key Idea

The main trick is converting the normal alphabet index into its reverse index:

```text
Reverse Index = 26 - Normal Index
```

Then simply multiply it by the character's 1-based position and add it to the result.
