# 1614. Maximum Nesting Depth of the Parentheses

[LeetCode Problem](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)

## Problem

Given a valid parentheses string `s`, return the **maximum nesting depth** of the parentheses.

The nesting depth is the maximum number of open parentheses `(` that are active at the same time.

### Example

```text
Input:  s = "(1+(2*3)+((8)/4))+1"

Output: 3
```

The deepest part is:

```text
((8))
```

At that point, there are 3 open parentheses.

---

## Intuition

We can keep track of how deeply nested we currently are.

Think of `res` as our current depth:

* When we see `(`, we enter another level → increase the depth.
* When we see `)`, we leave a level → decrease the depth.
* Every time we increase the depth, update the maximum depth seen so far.

For example:

```text
(1+(2*3)+((8)/4))+1
    ↑
```

As we scan the string:

```text
(        → depth = 1
(        → depth = 2
)        → depth = 1
(        → depth = 2
(        → depth = 3
)        → depth = 2
)        → depth = 1
)        → depth = 0
```

The maximum value reached is `3`.

---

## Approach

1. Initialize `res = 0` to store the current nesting depth.
2. Initialize `max_res = 0` to store the maximum depth.
3. Traverse every character in the string:

   * If the character is `(`:

     * Increment `res`.
     * Update `max_res`.
   * If the character is `)`:

     * Decrement `res`.
4. Return `max_res`.

---

## Code

```python
class Solution:

    def maxDepth(self, s: str) -> int:

        res = 0
        max_res = 0

        for c in s:

            if c == "(":
                res += 1
                max_res = max(max_res, res)

            elif c == ")":
                res -= 1

        return max_res
```

---

## Why This Works

At any point while scanning the string:

```text
res = number of currently open parentheses
```

Every `(` increases the nesting depth by one, while every `)` decreases it by one.

Therefore, the largest value reached by `res` is exactly the maximum nesting depth.

---

## Complexity

Let `n` be the length of the string.

* **Time:** `O(n)` — we scan the string once.
* **Space:** `O(1)` — only two integer variables are used.

---

## Key Takeaway

This problem is essentially a **counter problem**.

We don't need a stack because we only care about **how many parentheses are currently open**, not about matching or storing them.

```text
"(" → depth + 1
")" → depth - 1
```

The highest depth reached during the scan is the answer.
