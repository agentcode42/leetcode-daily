# 2124. Check if All A's Appears Before All B's

**LeetCode Problem:** [2124. Check if All A's Appears Before All B's](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/)

## Problem Summary

We are given a string `s` containing only the characters `'a'` and `'b'`.

We need to determine whether all occurrences of `'a'` appear before any occurrence of `'b'`.

In other words, the string must follow this pattern:

- Zero or more `'a'` characters.
- Followed by zero or more `'b'` characters.

Once we encounter a `'b'`, we must never encounter another `'a'`.

Return `True` if the string follows this rule; otherwise, return `False`.

### Examples

**Example 1:**

```text
Input: s = "aaabbb"
Output: true
```

All `'a'` characters appear before all `'b'` characters.

**Example 2:**

```text
Input: s = "abab"
Output: false
```

After encountering the first `'b'`, we encounter another `'a'`. This violates the required order.

**Example 3:**

```text
Input: s = "bbb"
Output: true
```

There are no `'a'` characters, so the condition is satisfied.

**Example 4:**

```text
Input: s = "aaa"
Output: true
```

There are no `'b'` characters, so the condition is also satisfied.

---

## Intuition

The key observation is that **the first occurrence of `'b'` marks the point after which no `'a'` is allowed.**

We do not need to count the characters, sort the string, or compare every pair of positions.

We only need to remember whether we have already encountered a `'b'`.

Consider:

```text
s = "aaabbba"
```

While traversing the string:

1. We encounter `'a'` characters. Everything is valid so far.
2. We encounter the first `'b'`. From this point onward, we cannot accept another `'a'`.
3. We eventually encounter `'a'` again.
4. This immediately violates the condition, so we return `False`.

This leads to a simple one-pass solution using two boolean flags.

## Approach: Single Pass with Two Flags

We maintain two boolean variables:

- `flag_a`: Indicates whether we have encountered an `'a'`.
- `flag_b`: Indicates whether we have encountered a `'b'`.

Both initially start as `False`.

### Step-by-Step Logic

We traverse the string one character at a time.

**Case 1: Current character is `'a'`**

```python
if c == "a":
    flag_a = True
    if flag_b:
        return False
```

We mark that an `'a'` has been encountered.

Then we check `flag_b`.

If `flag_b` is already `True`, it means we previously encountered a `'b'`.

Since an `'a'` cannot appear after a `'b'`, the string is invalid, and we immediately return `False`.

**Case 2: Current character is `'b'`**

```python
else:
    flag_b = True
```

We mark that we have encountered a `'b'`.

There is no need to return `False` here because `'b'` characters are allowed to appear consecutively or after `'a'` characters.

The only forbidden situation is encountering an `'a'` after this point.

**After the loop**

```python
return True
```

If we finish traversing the entire string without finding an invalid `'a'`, the string satisfies the condition.

Therefore, we return `True`.

---

## Walkthrough

Let's trace the algorithm using:

```text
s = "aaabbba"
```

Initial state:

```text
flag_a = False
flag_b = False
```

| Index | Character | flag_a | flag_b | Action |
|---|---|---|---|---|
| 0 | a | True | False | Valid |
| 1 | a | True | False | Valid |
| 2 | a | True | False | Valid |
| 3 | b | True | True | Valid |
| 4 | b | True | True | Valid |
| 5 | b | True | True | Valid |
| 6 | a | True | True | Return False |

At index `6`, we encounter `'a'` while `flag_b` is already `True`.

This means a `'b'` appeared before an `'a'`.

We immediately return `False` without processing the remaining string.

### Another Example: "aabbb"

| Index | Character | flag_a | flag_b | Action |
|---|---|---|---|---|
| 0 | a | True | False | Valid |
| 1 | a | True | False | Valid |
| 2 | b | True | True | Valid |
| 3 | b | True | True | Valid |
| 4 | b | True | True | Valid |

The traversal completes without finding an invalid character.

We return `True`.

---

## Python Solution

```python
class Solution:
    def checkString(self, s: str) -> bool:
        flag_a = False
        flag_b = False

        for c in s:
            if c == "a":
                flag_a = True

                if flag_b:
                    return False
            else:
                flag_b = True

        return True
```

## C Solution

```c
bool checkString(char* s) {
    bool flag_a = false;
    bool flag_b = false;

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == 'a') {
            flag_a = true;

            if (flag_b)
                return false;
        }
        else {
            flag_b = true;
        }
    }

    return true;
}
```

### Python vs C Implementation

Both implementations follow exactly the same logic.

The only differences are in how we traverse the string:

- **Python:** Uses a `for` loop to iterate directly over each character.
- **C:** Uses an index-based loop and continues until the null terminator `'\0'` is reached.

The boolean flags and validation logic remain identical.

---

## Complexity Analysis

Let `n` be the length of the input string.

**Time Complexity: O(n)**

We traverse the string at most once.

Each character requires only a constant amount of work:

- Check whether it is `'a'` or `'b'`.
- Update a boolean flag.
- Check whether the current character violates the condition.

In the worst case, we examine all `n` characters.

We may also terminate early if an invalid character is encountered.

**Space Complexity: O(1)**

We use only two boolean variables:

- `flag_a`
- `flag_b`

No additional data structures are required, and the amount of extra memory remains constant regardless of the input size.

---

## Important Observation

Although we maintain two flags, technically, we only need `flag_b` to solve this problem.

Why?

Because the only condition that can make the string invalid is:

**Encountering an `'a'` after encountering a `'b'`.**

We do not actually need to know whether an `'a'` has appeared before.

A simplified implementation could be:

```python
class Solution:
    def checkString(self, s: str) -> bool:
        flag_b = False

        for c in s:
            if c == "b":
                flag_b = True
            elif flag_b:
                return False

        return True
```

The original two-flag implementation is still perfectly valid. It explicitly tracks both character states and makes the validation logic easy to follow.

## Final Takeaway

This problem demonstrates a useful pattern for string traversal:

**Track an important event in the past and use that information to validate future characters.**

Here, the first occurrence of `'b'` changes what is allowed for the rest of the string.

Instead of repeatedly checking the entire string or counting character positions, we maintain a small amount of state and detect an invalid transition immediately.

- One traversal.
- Constant extra space.
- Early termination when the ordering rule is violated.

A simple example of how a small state variable can eliminate unnecessary work.