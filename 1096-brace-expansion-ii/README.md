# LeetCode 1096 — Brace Expansion II
[LeetCode Problem](https://leetcode.com/problems/brace-expansion-ii/)

## Problem

Given a string expression containing:

* Lowercase letters
* Braces `{ }`
* Commas `,`

the expression represents a **set of possible words**.

There are two important operations:

1. **Union** — expressions separated by commas represent alternatives.
2. **Concatenation** — expressions placed next to each other are concatenated in every possible combination.

Return all possible words in **sorted order**, without duplicates.

### Examples

#### Example 1

```text
Input:
"{a,b}"

Output:
["a","b"]
```

The expression means either `a` or `b`.

---

#### Example 2

```text
Input:
"{{a,z},a{b,c},{ab,z}}"

Output:
["a","ab","ac","z"]
```

Different parts of the expression can produce the same word, so duplicates are removed.

---

#### Example 3

```text
Input:
"{a,b}{c,d}"

Output:
["ac","ad","bc","bd"]
```

The first brace gives:

```text
a, b
```

The second brace gives:

```text
c, d
```

We combine every possibility:

```text
a + c = ac
a + d = ad
b + c = bc
b + d = bd
```

---

## Intuition

Instead of trying to evaluate the entire expression at once, we can **expand one pair of braces at a time**.

For example:

```text
{a,b}c
```

We can replace `{a,b}` with each of its choices:

```text
ac
bc
```

Then we continue recursively.

The important observation is that we can always find the **first closing brace `}`**.

For that closing brace, we search backwards to find its matching `{`.

For example:

```text
a{b,c}d
```

We find:

```text
   {b,c}
   ↑   ↑
   l   r
```

The contents between them are:

```text
b,c
```

So we split them into:

```text
b
c
```

Then replace the whole brace expression with each option:

```text
abd
acd
```

We recursively continue this process until there are no braces left.

At that point, the expression is a complete word, so we add it to a `set`.

Using a set automatically removes duplicate words.

Finally, we sort the set and return the result.

---

## Approach

We use **DFS (Depth-First Search)** with recursive expansion.

### Step 1 — Find the first closing brace

```python
r = s.find('}')
```

If there is no `}`, the expression contains no more braces.

That means `s` is a complete word:

```python
if r == -1:
    res.add(s)
    return
```

---

### Step 2 — Find the matching opening brace

Starting from the closing brace, move backwards until we find `{`.

```python
l = 0

for i in range(r - 1, -1, -1):
    if s[i] == '{':
        l = i
        break
```

For:

```text
abc{d,e}fg
```

we identify:

```text
abc {d,e} fg
    ↑   ↑
    l   r
```

---

### Step 3 — Extract the choices

Everything between `{` and `}` contains the alternatives.

```python
mid = s[l + 1:r].split(',')
```

For:

```text
{d,e}
```

we get:

```python
["d", "e"]
```

---

### Step 4 — Separate the expression into three parts

```python
left = s[:l]
right = s[r + 1:]
```

For:

```text
abc{d,e}fg
```

we get:

```text
left  = "abc"
mid   = ["d", "e"]
right = "fg"
```

---

### Step 5 — Try every possibility

For every choice inside the braces, construct a new expression:

```python
for ch in mid:
    dfs(left + ch + right)
```

So:

```text
abc{d,e}fg
```

becomes:

```text
abcdfg
abcefg
```

Each new expression is processed recursively.

---

## Example Walkthrough

Consider:

```text
{a,b}{c,d}
```

### First expansion

We find:

```text
{a,b}{c,d}
```

and expand `{a,b}`:

```text
a{c,d}
b{c,d}
```

### Recursive expansion

For:

```text
a{c,d}
```

we get:

```text
ac
ad
```

For:

```text
b{c,d}
```

we get:

```text
bc
bd
```

Eventually:

```text
ac
ad
bc
bd
```

are added to the set.

Finally:

```python
sorted(res)
```

returns:

```text
["ac", "ad", "bc", "bd"]
```

---

## Code

```python
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        res = set()

        def dfs(s):
            r = s.find('}')

            if r == -1:
                res.add(s)
                return

            l = 0

            for i in range(r - 1, -1, -1):
                if s[i] == '{':
                    l = i
                    break

            mid = s[l + 1:r].split(',')

            left = s[:l]
            right = s[r + 1:]

            for ch in mid:
                dfs(left + ch + right)

        dfs(expression)

        return sorted(res)
```

## Why the `set` is Important

The same word can be generated through different paths.

For example:

```text
{{a,b},{b,c}}
```

produces:

```text
a
b
b
c
```

But the required result is:

```text
["a", "b", "c"]
```

Using:

```python
res = set()
```

automatically removes the duplicate `"b"`.

---

## Complexity

Let **N** be the length of the expression and **K** be the number of unique words produced.

The recursive expansion can generate many intermediate expressions, so the worst-case complexity is **exponential** in the number of choices.

A useful way to think about it is:

```text
Time:  O(number of generated expansions × length of each expansion)

Space: O(number of generated unique words)
```

The final sorting also costs:

```text
O(K log K)
```

comparisons, with the cost of comparing strings depending on their length.

---

## Key Takeaway

The main idea is:

> **Find one brace pair, replace it with each possible choice, and recursively expand until no braces remain.**

The `set` handles duplicates, and `sorted()` gives the required final ordering.

This turns a complicated-looking grammar problem into a straightforward **recursive search through all possible expansions**.
