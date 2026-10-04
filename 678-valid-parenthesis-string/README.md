# LeetCode 678. Valid Parenthesis String

[LeetCode Problem](https://leetcode.com/problems/valid-parenthesis-string/)

## Problem

Given a string `s` containing three types of characters:

* `(` represents an opening parenthesis.
* `)` represents a closing parenthesis.
* `*` can be treated as `(`, `)`, or an empty string.

Return `True` if the string can represent a valid parenthesis string.

A valid parenthesis string must have:

* Every `(` matched with a `)`.
* Parentheses closed in the correct order.

### Example

```text
Input: s = "(*))"

Output: True
```

The `*` can be treated as `(`:

```text
( * ) )
↓
( ( ) )
```

which is valid.

---

## Approach

The difficult part is deciding what each `*` should represent.

Instead of trying every possibility, we keep track of a **range of possible numbers of open parentheses**.

We use two variables:

```python
min_open = 0
max_open = 0
```

### `min_open`

The smallest possible number of currently open parentheses.

For `*`, we assume it acts as `)` to get the smallest possible value.

### `max_open`

The largest possible number of currently open parentheses.

For `*`, we assume it acts as `(` to get the largest possible value.

So at any point:

```text
min_open <= possible open parentheses <= max_open
```

---

## How Each Character Changes the Range

### When we see `(`

It must increase the number of open parentheses.

```python
min_open += 1
max_open += 1
```

### When we see `)`

It closes an opening parenthesis.

```python
min_open -= 1
max_open -= 1
```

### When we see `*`

It can be either `(`, `)` or empty.

For the minimum:

```python
min_open -= 1
```

For the maximum:

```python
max_open += 1
```

So:

```python
min_open -= 1
max_open += 1
```

---

## Why Do We Set `min_open` Back to `0`?

Suppose `min_open` becomes negative.

That simply means our minimum assumption treated some `*` as `)` when it could instead be empty.

A negative number of open parentheses is impossible, so the smallest valid value is `0`.

```python
if min_open < 0:
    min_open = 0
```

But `max_open` is different.

If `max_open` becomes negative, then **even the most optimistic interpretation cannot keep the string valid**.

Therefore:

```python
if max_open < 0:
    return False
```

---

## Example

Let's trace:

```text
s = "(*))"
```

Start:

```text
min_open = 0
max_open = 0
```

### 1. `(`

```text
min_open = 1
max_open = 1
```

Possible open parentheses:

```text
[1, 1]
```

### 2. `*`

The minimum assumes `* = )`:

```text
min_open = 0
```

The maximum assumes `* = (`:

```text
max_open = 2
```

So:

```text
[0, 2]
```

There could be 0, 1, or 2 open parentheses.

### 3. `)`

```text
min_open = -1
max_open = 1
```

Since `min_open < 0`, reset it:

```text
min_open = 0
```

Now:

```text
[0, 1]
```

### 4. `)`

```text
min_open = -1
max_open = 0
```

Again:

```text
min_open = 0
```

Final range:

```text
[0, 0]
```

Since `min_open == 0`, the string can be valid.

Therefore:

```text
True
```

---

## Why `max_open < 0` Means False

Consider:

```text
s = "())"
```

After processing the first two characters:

```text
(
)
```

we have:

```text
max_open = 0
```

The next `)` makes:

```text
max_open = -1
```

There is no `*` that can save us because there are no alternative interpretations left.

So:

```python
if max_open < 0:
    return False
```

---

## Code

```python
class Solution:
    def checkValidString(self, s: str) -> bool:

        min_open, max_open = 0, 0

        for c in s:

            if c == "(":
                min_open += 1
                max_open += 1

            elif c == ")":
                min_open -= 1
                max_open -= 1

            else:
                min_open -= 1
                max_open += 1

            if min_open < 0:
                min_open = 0

            if max_open < 0:
                return False

        return min_open == 0
```

## Complexity

### Time Complexity

```text
O(n)
```

We process every character once.

### Space Complexity

```text
O(1)
```

Only two variables are used.

---

## Key Idea

We do not need to decide exactly what every `*` represents.

Instead, we keep a range:

```text
min_open → smallest possible number of open parentheses
max_open → largest possible number of open parentheses
```

At the end, if:

```text
min_open == 0
```

then there is at least one way to interpret the `*` characters so that the parentheses are valid.
