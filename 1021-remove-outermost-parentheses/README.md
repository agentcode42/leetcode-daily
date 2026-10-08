# 1021. Remove Outermost Parentheses

[LeetCode Problem](https://leetcode.com/problems/remove-outermost-parentheses/)

## Problem

A **valid parentheses string** is made up of one or more primitive valid parentheses strings.

A primitive parentheses string cannot be split into two smaller non-empty valid parentheses strings.

For every primitive string, we need to remove its **outermost pair of parentheses** and return the remaining string.

### Example

```text
Input:
"(()())(())"

Output:
"()()()"
```

The input can be divided into two primitive strings:

```text
(()())  (())
```

Remove the outermost parentheses from each:

```text
()()    ()
```

Result:

```text
()()()
```

---

## Intuition

We can solve this by tracking the **parentheses depth**.

The important part is knowing when a parenthesis is the outermost one.

For an opening parenthesis:

```text
(
```

we are currently at the outside of a primitive if `depth == 0`.

So we should **not add that `(`**.

For a closing parenthesis:

```text
)
```

if we decrease the depth first and it becomes `0`, then this `)` is the outermost closing parenthesis, so we should **not add it**.

This gives us a simple rule:

* For `(` → increase depth **after** checking whether to append.
* For `)` → decrease depth **before** checking whether to append.
* Append the character only when `depth > 0`.

---

## Approach

We maintain:

```python
depth = 0
```

Then process every character.

### If the character is `)`

First decrease the depth:

```python
depth -= 1
```

If `depth > 0`, this closing parenthesis is not the outermost one, so we add it.

### If the character is `(`

First check whether we are already inside the primitive.

If:

```python
depth > 0
```

we add the opening parenthesis.

Then increase the depth:

```python
depth += 1
```

This lets us remove exactly the first `(` and last `)` of every primitive.

---

## Code

```python
class Solution:

    def removeOuterParentheses(self, s: str) -> str:

        res = []

        depth = 0

        for c in s:

            if c == ")":
                depth -= 1

            if depth > 0:
                res.append(c)

            if c == "(":
                depth += 1

        return "".join(res)
```

---

## Dry Run

For:

```text
(()())
```

We track the depth:

| Character | Depth before/after | Add? |
| --------- | -----------------: | ---- |
| `(`       |              0 → 1 | ❌    |
| `(`       |              1 → 2 | ✅    |
| `)`       |              2 → 1 | ✅    |
| `(`       |              1 → 2 | ✅    |
| `)`       |              2 → 1 | ✅    |
| `)`       |              1 → 0 | ❌    |

The characters we keep are:

```text
()()
```

So the answer is:

```text
()()
```

---

## Why the Ordering Matters

The interesting part of the solution is the order of these operations.

For `)`:

```python
if c == ")":
    depth -= 1

if depth > 0:
    res.append(c)
```

We decrease `depth` **before** adding the character.

This means the outermost closing parenthesis changes:

```text
depth: 1 → 0
```

so it is not added.

For `(`, we add it before increasing the depth:

```python
if depth > 0:
    res.append(c)

if c == "(":
    depth += 1
```

The outermost opening parenthesis starts at:

```text
depth = 0
```

so it is not added.

---

## Complexity

Let `n` be the length of the string.

### Time Complexity

```text
O(n)
```

We process every character exactly once.

### Space Complexity

```text
O(n)
```

The result can contain up to `n` characters.

The `depth` variable itself uses `O(1)` extra space, but the output stored in `res` requires `O(n)` space.
