# LeetCode 32 — Longest Valid Parentheses

[LeetCode Problem](https://leetcode.com/problems/longest-valid-parentheses/)

## Problem

Given a string containing only `(` and `)`, find the length of the **longest valid parentheses substring**.

### Example

```text
Input:  s = ")()())"
Output: 4
```

The longest valid substring is:

```text
()()
```

Its length is `4`.

---

## Intuition

A valid parentheses substring must have:

* The same number of `(` and `)`
* No point where `)` appears without a matching `(` before it

We can keep track of:

```text
open_b  = number of '('
close_b = number of ')'
```

Whenever:

```text
open_b == close_b
```

we have a balanced valid substring, so its length is:

```text
close_b * 2
```

### But why do we need two passes?

Consider:

```text
((())
```

From left to right:

```text
open_b  = 3
close_b = 2
```

The counts never become equal after the final `(`, so the valid part may be missed.

The problem here is an **extra `(`**.

To handle this, we scan the string a second time from **right to left**.

The reverse scan handles the opposite situation: an extra `(`.

So:

1. **Left → Right:** reset when there are too many `)`
2. **Right → Left:** reset when there are too many `(`

---

## Approach

### Pass 1 — Left to Right

For every character:

* If it is `(`, increment `open_b`
* If it is `)`, increment `close_b`

If:

```text
open_b == close_b
```

then the current balanced substring has length:

```text
close_b * 2
```

Update `res`.

If:

```text
close_b > open_b
```

we have more closing brackets than opening brackets.

That means the current substring can no longer become valid, so we reset:

```python
open_b = close_b = 0
```

---

### Pass 2 — Right to Left

Now we repeat the same idea in reverse.

If:

```text
open_b == close_b
```

we again have a balanced substring.

But this time, if:

```text
close_b < open_b
```

there are too many opening brackets.

We reset the counters.

This catches valid substrings that the first pass could not detect.

---

## Code

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        open_b = close_b = 0

        # Left to right
        for c in s:
            if c == "(":
                open_b += 1
            elif c == ")":
                close_b += 1

            if open_b == close_b:
                res = max(res, close_b * 2)

            if close_b > open_b:
                open_b = close_b = 0

        # Right to left
        open_b = close_b = 0

        for c in reversed(s):
            if c == "(":
                open_b += 1
            elif c == ")":
                close_b += 1

            if open_b == close_b:
                res = max(res, close_b * 2)

            if close_b < open_b:
                open_b = close_b = 0

        return res
```

---

## Walkthrough

Consider:

```text
s = ")()())"
```

### Left → Right

We start with:

```text
open_b = 0
close_b = 0
res = 0
```

The first character is `)`:

```text
open_b = 0
close_b = 1
```

Now:

```text
close_b > open_b
```

so we reset.

Then we process:

```text
()
```

The counts become:

```text
open_b = 1
close_b = 1
```

Balanced:

```text
res = max(0, 2)
```

Continue with:

```text
()
```

Again:

```text
open_b = 2
close_b = 2
```

So:

```text
res = 4
```

The answer is:

```text
4
```

---

## Why the Second Pass Matters

Consider:

```text
s = "(()"
```

### Left → Right

At the end:

```text
open_b = 2
close_b = 1
```

The counts never become equal after the final `(`.

But:

```text
()
```

is still a valid substring of length `2`.

The right-to-left scan finds it:

```text
()
```

because from the reverse direction we can detect the balance correctly.

So the two passes complement each other.

---

## Complexity

Let `n` be the length of the string.

### Time

We scan the string twice:

```text
O(n) + O(n) = O(n)
```

**Time Complexity: `O(n)`**

### Space

We only use a few variables:

```text
res
open_b
close_b
```

**Space Complexity: `O(1)`**

---

## Key Takeaway

The important idea is that **one directional scan is not enough**.

* Left → Right catches cases with too many `)`
* Right → Left catches cases with too many `(`

Whenever the counts are equal:

```python
open_b == close_b
```

we have a balanced section whose length is:

```python
close_b * 2
```

By combining both scans, we can find the longest valid parentheses substring in **O(n) time and O(1) space**.
