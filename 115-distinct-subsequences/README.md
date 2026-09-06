# 115. Distinct Subsequences

**LeetCode:** [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)

## Problem

Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equal `t`.

A subsequence is created by deleting zero or more characters from `s` without changing the relative order of the remaining characters.

Two subsequences are considered distinct when they use different indices from `s`, even if they produce the same string.

### Example

```text
s = "aaa"
t = "aa"
```

There are 3 distinct subsequences:

```text
s[0], s[1]
s[0], s[2]
s[1], s[2]
```

All three produce `"aa"`, but they use different indices.

---

# Approach 1: DFS + Memoization

The natural way to think about this problem is as a DFS over the possible choices we can make while constructing `t` from `s`.

At every position, if the current characters match, we have two choices:

1. **Take** `s[i]` and use it to match `t[j]`.
2. **Skip** `s[i]` and try to match `t[j]` using a later character.

If the characters do not match, we cannot use `s[i]`, so we simply skip it.

## DFS State

```text
dfs(i, j)
```

represents:

> The number of ways to construct `t[j:]` using characters from `s[i:]`.

Therefore, when:

```text
s[i] == t[j]
```

we calculate:

```text
take = dfs(i + 1, j + 1)
skip = dfs(i + 1, j)
```

and add the two possibilities:

```text
take + skip
```

If the characters do not match:

```text
dfs(i + 1, j)
```

is the only possibility.

## Base Cases

### `j == len(t)`

We have successfully matched the entire target string.

```text
return 1
```

This represents one valid subsequence.

### `i == len(s)`

We have reached the end of `s` without matching all of `t`.

```text
return 0
```

## Why Memoization?

The DFS can reach the same `(i, j)` state through different paths.

For example:

```text
dfs(5, 2)
```

always represents the same subproblem:

> How many ways can we construct `t[2:]` using `s[5:]`?

Therefore, once we calculate a state, we store its result in a dictionary.

### Code

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        dp = {}

        def dfs(i, j):
            if j == m:
                return 1

            if i == n:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == t[j]:
                take = dfs(i + 1, j + 1)
                skip = dfs(i + 1, j)
                dp[(i, j)] = take + skip
            else:
                dp[(i, j)] = dfs(i + 1, j)

            return dp[(i, j)]

        return dfs(0, 0)
```

## Complexity

There are at most `n × m` unique `(i, j)` states.

Each state performs constant work apart from recursive calls that are memoized.

```text
Time:  O(n × m)
Space: O(n × m)
```

The space includes the memoization dictionary and the recursion stack.

---

# Approach 2: DFS + Memoization + Pruning

We can improve the DFS by identifying states that are immediately impossible.

At any state `(i, j)`:

```text
Remaining characters in s = n - i
Remaining characters in t = m - j
```

If:

```text
n - i < m - j
```

then there are not enough characters remaining in `s` to construct the remaining part of `t`.

Therefore, the answer for this state must be:

```text
0
```

### Example

Suppose:

```text
s[i:] = "bag"
t[j:] = "bagg"
```

There are:

```text
3 characters remaining in s
4 characters remaining in t
```

Even if every remaining character matched perfectly, we could not construct `t`.

So we can immediately stop exploring this branch.

## Code

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        dp = {}

        def dfs(i, j):
            if j == m:
                return 1

            if i == n:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            # Pruning:
            # Not enough characters remain in s to construct t[j:].
            if (n - i) < (m - j):
                return 0

            if s[i] == t[j]:
                take = dfs(i + 1, j + 1)
                skip = dfs(i + 1, j)
                dp[(i, j)] = take + skip
            else:
                dp[(i, j)] = dfs(i + 1, j)

            return dp[(i, j)]

        return dfs(0, 0)
```

## Why the Pruning Is Correct

A subsequence cannot contain more characters than the string it comes from.

At state `(i, j)`:

```text
s[i:] has n - i characters
t[j:] has m - j characters
```

If:

```text
n - i < m - j
```

then it is mathematically impossible to match all remaining characters of `t`.

Returning `0` is therefore safe.

---

# DFS Decision Tree

The core idea can be visualized as:

```text
                    dfs(i, j)
                       |
              s[i] == t[j] ?
                 /          \
              YES            NO
             /                 \
         TAKE + SKIP            SKIP
          /       \               |
 dfs(i+1,j+1)   dfs(i+1,j)   dfs(i+1,j)
```

Memoization prevents recalculating the same `(i, j)` state.

Pruning prevents exploring states where there are not enough characters remaining in `s`.

---

# Key Takeaways

### 1. Distinct means different index selections

The resulting strings do not have to look different.

```text
s = "aaa"
t = "aa"
```

Selecting indices `(0,1)`, `(0,2)`, and `(1,2)` produces three distinct subsequences.

### 2. DFS naturally represents the choices

When:

```text
s[i] == t[j]
```

we can either:

```text
take s[i]
```

or:

```text
skip s[i]
```

### 3. Memoization removes repeated work

The state:

```text
(i, j)
```

completely describes the remaining subproblem.

### 4. Pruning removes impossible states

If:

```text
n - i < m - j
```

there are not enough characters left in `s` to construct the remainder of `t`.

### Final Complexity

```text
Time:  O(n × m)
Space: O(n × m)
```

The solution remains fundamentally a **DFS**, with memoization used to avoid solving the same state repeatedly and pruning used to stop impossible branches early.
