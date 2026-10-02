# LeetCode 22. Generate Parentheses

[LeetCode Problem](https://leetcode.com/problems/generate-parentheses/)

## Problem

Given `n` pairs of parentheses, generate all combinations of well-formed parentheses.

### Example

```text
Input: n = 3

Output:
["((()))","(()())","(())()","()(())","()()()"]
```

---

## Intuition

I can build the parentheses string one character at a time using **DFS + backtracking**.

The important part is making sure I don't create invalid combinations.

I keep track of:

* `i` → how many characters have been added so far.
* `bal` → current balance of parentheses.

  * Add `(` → `bal + 1`
  * Add `)` → `bal - 1`

There are two rules for adding parentheses:

### 1. Add `(` only if I haven't used all `n` opening brackets

```python
if bal < n:
```

Since every `(` increases the balance by `1`, and we can have at most `n` opening brackets, `bal` cannot reach more than `n`.

### 2. Add `)` only if there is an unmatched `(`

```python
if bal > 0:
```

This prevents invalid strings such as:

```text
)(
```

because we cannot close a parenthesis that hasn't been opened.

---

## DFS + Backtracking

For every position, I try the possible choices:

```text
            ""
          /    \
        "("
       /   \
     "(("   "()"
      ...
```

After exploring one choice, I remove it with:

```python
curr.pop()
```

This allows the same `curr` list to be reused for the next branch.

The pattern is:

```python
curr.append(...)
dfs(...)
curr.pop()
```

So we:

1. Choose a parenthesis.
2. Explore that choice.
3. Undo the choice.
4. Try the other possibility.

---

## Why `bal == 0` at the end?

When the string reaches length `2 * n`, we have used all positions.

But reaching the correct length does **not** automatically mean the parentheses are valid.

For example:

```text
((()()
```

has 6 characters when `n = 3`, but it is not balanced.

Therefore, we only add the string when:

```python
if bal == 0:
```

This means every opening parenthesis has been closed.

---

## Code

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        res = []
        curr = []

        def dfs(i, bal):

            if i == 2 * n:
                if bal == 0:
                    res.append("".join(curr))
                return

            if bal < 0:
                return

            if bal < n:
                curr.append("(")
                dfs(i + 1, bal + 1)
                curr.pop()

            if bal > 0:
                curr.append(")")
                dfs(i + 1, bal - 1)
                curr.pop()

        dfs(0, 0)
        return res
```

## Complexity

There are `Cₙ` valid combinations, where `Cₙ` is the `n`th **Catalan number**:

```text
Cₙ = 1/(n+1) * (2n choose n)
```

Since we have to construct every valid string of length `2n`:

**Time:** `O(Cₙ × n)`

**Space:** `O(n)` for the recursion stack and current string, excluding the output.

The result itself requires:

**Output space:** `O(Cₙ × n)`

---

## Key Takeaway

The main idea is not to generate every possible sequence of `(` and `)` and then check it.

Instead, DFS **prunes invalid branches while building the string**:

```text
Can add '(' → only if opening brackets < n
Can add ')' → only if balance > 0
Finished → only keep if balance == 0
```

This turns the problem into a clean **DFS + backtracking** solution.
