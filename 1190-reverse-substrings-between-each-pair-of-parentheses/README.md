# LeetCode 1190 — Reverse Substrings Between Each Pair of Parentheses

[LeetCode Problem](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)

## Problem

You are given a string `s` containing lowercase English letters and parentheses.

For every matching pair of parentheses:

* Reverse the string inside the parentheses.
* Nested parentheses should be processed from the **innermost pair outward**.
* The final answer should contain **no parentheses**.

### Example

```text
Input:
s = "(abcd)"

Output:
"dcba"
```

Another example:

```text
Input:
s = "(u(love)i)"

First reverse:
(love) → evol

Then:
(u evol i) → u love? 
```

More precisely, the operations happen from the innermost parentheses outward.

---

## Intuition

The key observation is that when we encounter a closing parenthesis `)`, everything after the most recent opening parenthesis `(` belongs to the substring that needs to be reversed.

A **stack** is perfect for this.

While scanning the string:

* Normal characters are pushed onto the stack.
* `(` is also pushed onto the stack as a marker.
* When we encounter `)`, we pop characters until we reach `(`.
* The popped characters are collected in `curr`.
* Because a stack pops elements in reverse order, `curr` is already the reversed substring.
* We remove the matching `(`.
* Finally, we put the reversed substring back onto the stack.

This automatically handles nested parentheses because the **innermost pair is always completed first**.

---

## Approach

1. Create an empty stack.
2. Traverse every character in `s`.
3. If the character is not `)`:

   * Push it onto the stack.
4. If the character is `)`:

   * Create a temporary list `curr`.
   * Pop characters from the stack until `(` is found.
   * Add every popped character to `curr`.
   * Remove the `(`.
   * Extend the stack with `curr`.
5. At the end, join everything remaining in the stack.

---

## Why Does This Reverse the String?

Suppose the stack contains:

```text
( a b c d
```

When we encounter `)`:

```python
curr = []

while stack and stack[-1] != '(':
    curr.append(stack.pop())
```

The characters are popped in this order:

```text
d
c
b
a
```

So:

```text
curr = ['d', 'c', 'b', 'a']
```

The substring has effectively been reversed without explicitly calling `reverse()`.

Then we remove the opening parenthesis:

```python
stack.pop()
```

And put the reversed characters back:

```python
stack.extend(curr)
```

The stack now contains:

```text
d c b a
```

---

## Handling Nested Parentheses

Consider:

```text
(u(love)i)
```

When we reach the first `)`:

```text
(u(love)i)
    ^^^^
```

The innermost substring `love` is reversed first:

```text
evol
```

The stack then contains the partially processed string.

When the final `)` is reached, the outer substring is processed using the same logic.

So we don't need separate logic for nested parentheses — **the stack naturally processes them from the inside out.**

---

## Code

```python
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ')':
                curr = []

                while stack and stack[-1] != '(':
                    curr.append(stack.pop())

                stack.pop()
                stack.extend(curr)

            else:
                stack.append(c)

        return "".join(stack)
```

---

## Complexity

Let `n` be the length of the input string.

### Time Complexity

**O(n)**

Each character is pushed onto and popped from the stack at most once.

Even with nested parentheses, we don't repeatedly process the same character.

### Space Complexity

**O(n)**

The stack can contain up to `n` characters, and the temporary `curr` list can also contain characters from the current substring.

---

## Key Takeaway

The important idea is to use the closing parenthesis `)` as a signal to process the most recent opening parenthesis.

Because a stack is **Last In, First Out (LIFO)**, popping everything until `(` automatically reverses the substring.

**Stack + parentheses = process nested substrings from the inside out.**
