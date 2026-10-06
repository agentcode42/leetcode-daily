# LeetCode 921 — Minimum Add to Make Parentheses Valid

[LeetCode 921 — Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

## Problem

Given a string `s` containing only `(` and `)`, return the **minimum number of parentheses** we need to add to make the string valid.

A valid parentheses string must have:

* Every `(` matched with a `)`
* Every `)` matched with a previous `(`

### Example

```text
s = "())"

Add one `(`:

"()()" 
```

Answer:

```text
1
```

---

## Intuition

We can scan the string from left to right while keeping track of how many unmatched `(` we currently have.

We use two variables:

```python
count = 0
res = 0
```

* `count` = number of unmatched `(` currently available
* `res` = number of `(` we need to add because we found an unmatched `)`

### When we see `(`

It can potentially match a future `)`:

```python
count += 1
```

### When we see `)`

We first try to match it with an existing `(`:

```python
count -= 1
```

But if:

```python
count < 0
```

there was no `(` available.

So this `)` is unmatched, and we must add a `(` before it:

```python
res += 1
count += 1
```

The `count += 1` restores the balance because the newly added `(` can match the current `)`.

---

## What About Unmatched `(`?

After processing the entire string, `count` tells us how many `(` are still unmatched.

Each one needs a `)`.

So the final answer is:

```python
res + count
```

---

## Example Walkthrough

Consider:

```text
s = "())("
```

Start:

```text
count = 0
res = 0
```

### 1. `(`

```text
count = 1
res = 0
```

### 2. `)`

Match it with the previous `(`:

```text
count = 0
res = 0
```

### 3. `)`

There is no `(` available.

```text
count = -1
```

So we add a `(`:

```text
res = 1
count = 0
```

### 4. `(`

```text
count = 1
```

End of string:

```text
res = 1
count = 1
```

The remaining `(` needs one `)`.

Therefore:

```text
answer = res + count
       = 1 + 1
       = 2
```

---

## Approach

1. Keep `count` for unmatched opening parentheses.
2. Keep `res` for parentheses that must be added.
3. For `(`, increase `count`.
4. For `)`, decrease `count`.
5. If `count` becomes negative:

   * We found an unmatched `)`.
   * Add one `(`.
   * Increase `res`.
   * Restore `count`.
6. At the end, every remaining unmatched `(` needs one `)`.
7. Return `res + count`.

---

## Python

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        count = 0
        res = 0

        for c in s:
            if c == "(":
                count += 1

            else:
                count -= 1

                if count < 0:
                    res += 1
                    count += 1

        return res + count
```

---

## C

```cpp
    int minAddToMakeValid(string s) {

        int count = 0;
        int res = 0;

        int n = s.length();

        for (int i = 0; i < n; i++) {

            if (s[i] == '(')
                count++;

            else {
                count--;

                if (count < 0) {
                    res++;
                    count++;
                }
            }
        }

        return res + count;
    }
```

---

## Complexity

Let `n` be the length of the string.

* **Time:** `O(n)` — we scan the string once.
* **Space:** `O(1)` — only two counters are used.

---

## Key Takeaway

We don't need to actually add parentheses to the string.

We only need to count **how many additions are necessary**.

The greedy idea is:

> If a `)` appears without an available `(`, we must add a `(`.

And after the scan:

> Every remaining unmatched `(` requires one `)`.

So:

```text
Answer = unmatched ')' fixes + unmatched '(' fixes
       = res + count
```
