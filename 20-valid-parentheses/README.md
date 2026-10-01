# LeetCode 20. Valid Parentheses

[LeetCode Problem](https://leetcode.com/problems/valid-parentheses/)

## Problem

Given a string `s` containing only the characters:

* `(`
* `)`
* `{`
* `}`
* `[`
* `]`

Determine if the brackets are **valid**.

A valid string must satisfy:

1. Every opening bracket has a matching closing bracket.
2. Brackets must close in the correct order.
3. Every closing bracket must have a corresponding opening bracket.

### Examples

```text
Input: s = "()"
Output: true
```

```text
Input: s = "()[]{}"
Output: true
```

```text
Input: s = "(]"
Output: false
```

```text
Input: s = "([)]"
Output: false
```

---

## Intuition

The important thing here is **order**.

For example:

```text
([{}])
```

When we see an opening bracket, we need to remember it until its closing bracket appears.

This makes a **stack** a natural choice.

A stack follows **Last In, First Out (LIFO)**.

For example:

```text
( [ {
```

The `{` was opened last, so it must be closed first:

```text
( [ { } ] )
```

We can use a dictionary to store which closing bracket belongs to each opening bracket:

```python
table = {
    "(": ")",
    "{": "}",
    "[": "]"
}
```

---

## Approach

We go through the string one character at a time.

### 1. Opening bracket

If the character is an opening bracket:

```python
if c in table:
    stack.append(c)
```

Push it onto the stack.

For example:

```text
s = "({["

stack = ['(', '{', '[']
```

### 2. Closing bracket

If the character is a closing bracket, we need to check two things:

* Is the stack empty?
* Does this closing bracket match the most recently opened bracket?

```python
if not stack or table[stack.pop()] != c:
    return False
```

`stack.pop()` gives us the most recently opened bracket.

For example:

```text
stack = ['(', '{', '[']
```

If we encounter:

```text
]
```

we pop:

```text
[
```

Then check:

```text
table["["] == "]"
```

If it matches, we continue.

### 3. Check the stack at the end

After processing the entire string:

```python
return not stack
```

If the stack is empty, every opening bracket was matched.

If something remains in the stack, there are unmatched opening brackets.

---

## Code

```python
class Solution:
    def isValid(self, s: str) -> bool:

        table = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for c in s:

            if c in table:
                stack.append(c)

            else:
                if not stack or table[stack.pop()] != c:
                    return False

        return not stack
```

---

## Dry Run

Let's take:

```text
s = "({[]})"
```

| Character | Action      | Stack       |
| --------- | ----------- | ----------- |
| `(`       | Push        | `(`         |
| `{`       | Push        | `(` `{`     |
| `[`       | Push        | `(` `{` `[` |
| `]`       | Matches `[` | `(` `{`     |
| `}`       | Matches `{` | `(`         |
| `)`       | Matches `(` | Empty       |

At the end:

```text
stack = []
```

So the answer is:

```text
true
```

---

## Why `return not stack`?

Instead of writing:

```python
if len(stack) == 0:
    return True
else:
    return False
```

we can simply write:

```python
return not stack
```

An empty list is considered `False` in Python.

Therefore:

```text
stack = []       → not stack = True
stack = ['(']    → not stack = False
```

So `return not stack` directly tells us whether all brackets were matched.

---

## Complexity

### Time Complexity

**O(n)**

We visit every character in the string once.

### Space Complexity

**O(n)**

In the worst case, all characters can be opening brackets and stored in the stack.

---

## Key Takeaway

When dealing with **nested brackets**, a stack is a natural fit because the **last bracket opened must be the first one closed**.

The main idea is:

```text
Opening bracket → PUSH
Closing bracket → POP and CHECK
End → Stack must be empty
```
