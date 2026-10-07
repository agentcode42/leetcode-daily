# LeetCode 301 — Remove Invalid Parentheses

[LeetCode Problem](https://leetcode.com/problems/remove-invalid-parentheses/)

## Problem

Given a string `s` containing parentheses and letters, remove the **minimum number of invalid parentheses** so that the remaining string is valid.

Return all **unique valid strings** that can be created using exactly that minimum number of removals.

---

## Intuition

There are two things we need to figure out:

1. **How many parentheses must be removed?**
2. **Which parentheses should we remove?**

First, we scan the string to calculate the minimum number of removals needed.

We use `bal` to track the current number of unmatched opening parentheses.

* `(` → increase `bal`
* `)` → decrease `bal`
* If `bal` becomes negative, we have an extra `)`.

  * We must remove it.
  * Increase `min_remove`.
  * Restore `bal`.

After the scan, any remaining `bal` represents unmatched `(`, so those also need to be removed.

```python
min_remove = min_remove + bal
```

Now we know exactly how many parentheses must be removed.

---

## DFS

Once we know `min_remove`, we use DFS to try the possible choices.

At every character, there are two possibilities:

### Keep the character

We add it to `curr`.

For parentheses, we update the balance:

```python
if s[i] == "(":
    new_bal += 1
elif s[i] == ")":
    new_bal -= 1
```

Then we continue to the next character.

### Remove the character

We only have this choice when the character is a parenthesis:

```python
if s[i] in "()":
    dfs(i+1, rem+1, bal)
```

Letters are never removed.

---

## Pruning

We stop exploring a branch when it can no longer produce a valid answer.

### Negative balance

```python
if bal < 0:
    return
```

A negative balance means we have more closing parentheses than opening parentheses.

That string can never become valid by adding characters later, so we stop.

### Too many removals

```python
if rem > min_remove:
    return
```

We only want solutions using the minimum number of removals.

### End of the string

When we reach the end:

```python
if i == n:
    if rem == min_remove and bal == 0:
        res.add("".join(curr))
```

A solution is valid only when:

* We removed exactly `min_remove` characters.
* `bal == 0`, meaning there are no unmatched `(` left.

---

## Why Use a Set?

Different DFS paths can sometimes produce the same final string.

For example, removing different duplicate parentheses can lead to the same result.

So we store answers in:

```python
res = set()
```

This automatically removes duplicates.

At the end:

```python
return list(res)
```

---

## Code

```python
class Solution:

    def removeInvalidParentheses(self, s: str) -> list[str]:

        min_remove = 0

        bal = 0

        for c in s:

            if c == "(":
                bal += 1

            elif c == ")":
                bal -= 1

                if bal < 0:
                    min_remove += 1
                    bal += 1

        min_remove = min_remove + bal

        n = len(s)

        if min_remove == n:
            return [""]

        curr = []

        res = set()

        bal = 0

        def dfs(i, rem, bal):

            if i == n:
                if rem == min_remove and bal == 0:
                    res.add("".join(curr))
                return

            if bal < 0:
                return

            if rem > min_remove:
                return

            # Keep the current character
            curr.append(s[i])

            new_bal = bal

            if s[i] == "(":
                new_bal += 1

            elif s[i] == ")":
                new_bal -= 1

            dfs(i + 1, rem, new_bal)

            curr.pop()

            # Remove the current character
            if s[i] in "()":
                dfs(i + 1, rem + 1, bal)

            return

        dfs(0, 0, 0)

        return list(res)
```

---

## Complexity

Let `n` be the length of the string.

In the worst case, DFS can explore exponentially many possibilities because each parenthesis can potentially be kept or removed.

**Time:** `O(2^n * n)` in the worst case, because we may generate many candidate strings and joining `curr` takes `O(n)`.

**Space:** `O(2^n * n)` in the worst case for storing the unique results.

The actual search is reduced significantly by the balance and removal-count pruning.

---

## Key Takeaway

The important part of this solution is that we **don't blindly try every possible number of removals**.

First, we calculate the exact minimum number of removals required.

Then DFS makes two choices for every parenthesis:

**Keep it or remove it.**

The branch is valid only if:

```text
rem == minimum removals
AND
balance == 0
```

That combination lets us generate **all valid answers while guaranteeing the minimum number of removals**.
