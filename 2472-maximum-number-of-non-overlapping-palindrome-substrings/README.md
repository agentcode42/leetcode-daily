# 2472. Maximum Number of Non-overlapping Palindrome Substrings

## Problem

Given a string `s` and an integer `k`, find the maximum number of **non-overlapping palindromic substrings** of `s` such that every selected palindrome has a length of at least `k`.

A substring must be **contiguous**.

For example:

```text
s = "abacaba"
```

`"aba"` is a substring.

But `"aca"` can only be a substring if those characters occur consecutively. We cannot skip characters inside a substring.

However, when selecting multiple palindromes, we **can leave characters unused** between them.

---

# Initial Thought

The problem can be viewed as two separate tasks:

1. Find palindromic substrings whose length is at least `k`.
2. Select the maximum number of those palindromes without overlap.

At first, it was tempting to think about a sliding window, but palindrome detection does not behave like a normal sliding-window problem.

Adding or removing one character can completely change whether a substring is a palindrome.

So instead of trying to maintain a sliding window, the focus moved toward explicitly finding palindromes.

---

# Attempt 1: Take the Longest Palindrome

One initial idea was:

> Find a long palindrome, take it, remove that part, and continue.

This does not work because the longest palindrome is not necessarily the best choice.

For example:

```text
s = "abacaba"
k = 3
```

The entire string is a palindrome:

```text
abacaba
^^^^^^^
```

Taking it gives:

```text
1 palindrome
```

But we can instead take:

```text
aba c aba
^^^   ^^^
```

giving:

```text
2 palindromes
```

So choosing the longest palindrome can prevent a better overall answer.

---

# Attempt 2: Take the First Palindrome We Find

The next idea was to scan from left to right and take the first valid palindrome starting from the current position.

This is better than choosing the longest palindrome, but there is an important distinction:

> Choosing the first palindrome starting at a position is not the same as the standard interval scheduling greedy rule.

The interval scheduling problem normally chooses the interval with the **earliest ending position**.

Also, simply taking a palindrome whenever one is found does not account for the possibility of skipping the current character.

For example, we might have:

```text
zabaaba
^
```

There is no valid palindrome starting at `z`, so we should be able to skip it and continue searching.

Therefore the state needs to consider both:

```text
skip this position
```

and

```text
take a palindrome starting here
```

This naturally suggests DFS.

---

# Attempt 3: Brute Force + Palindrome Checking

The next approach was to generate every substring whose length is at least `k` and check whether it is a palindrome.

Conceptually:

```text
for every start:
    for every valid end:
        check s[start:end+1]
```

The palindrome check can be done recursively:

```python
@cache
def ispalindrome(left, right):
    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return ispalindrome(left + 1, right - 1)
```

This avoids repeatedly checking the same inner ranges.

Then all valid palindromes can be stored as intervals:

```text
(start, end)
```

---

# Attempt 4: Generate Palindromes and Use Interval Scheduling

After finding all valid palindromes, we can sort them by their ending position.

For example:

```python
palindromes.sort(key=lambda x: x[1])
```

Then greedily take an interval whenever it does not overlap the previously selected interval.

The idea is:

```python
last_end = -1
res = 0

for start, end in palindromes:
    if start > last_end:
        res += 1
        last_end = end
```

This is logically correct because once all valid palindrome intervals are known, selecting the interval with the earliest ending position is the classic optimal strategy for maximizing the number of non-overlapping intervals.

However, this approach eventually hit **Time Limit Exceeded**.

The problem was not the interval scheduling itself.

The expensive part was generating and storing/checking too many palindrome intervals.

With `n` up to around 2000, there can be `O(n²)` possible substrings.

---

# Attempt 5: DFS for the Selection

Instead of generating every possible combination of palindromes, the next idea was to let DFS make the selection.

Define:

```text
dfs(i) = maximum number of valid palindromes we can select
         starting from position i
```

At every position we have two choices.

### Choice 1: Skip the character

```python
dfs(i + 1)
```

### Choice 2: Take a palindrome

If `[i, j]` is a valid palindrome:

```python
1 + dfs(j + 1)
```

So the recurrence becomes:

```python
dfs(i) = max(
    dfs(i + 1),
    1 + dfs(j + 1)
)
```

This is a natural DFS formulation of the problem.

---

# Attempt 6: DFS + Cached Palindrome Checking

The first full DFS version was:

```python
@cache
def ispalindrome(left, right):
    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return ispalindrome(left + 1, right - 1)


@cache
def dfs(i):
    if i >= n:
        return 0

    res = dfs(i + 1)

    for j in range(i + k - 1, n):
        if ispalindrome(i, j):
            res = max(res, 1 + dfs(j + 1))

    return res
```

This was an important improvement.

The selection itself now only has `O(n)` DFS states because `dfs(i)` only depends on the starting position.

Unfortunately, this version passed the correctness tests but hit **Memory Limit Exceeded**.

---

# Why Did It Hit Memory Limit?

The important problem was the palindrome cache:

```python
@cache
def ispalindrome(left, right):
```

There can be `O(n²)` different `(left, right)` pairs.

So even though:

```text
dfs(i)
```

only has `O(n)` states, the palindrome cache can contain:

```text
O(n²)
```

states.

In Python, a cache containing hundreds of thousands or millions of dictionary entries has significant memory overhead.

So the problem was essentially:

```text
DFS selection      -> O(n) memory
Palindrome cache   -> O(n²) memory
```

The palindrome cache was what caused the MLE.

---

# Key Observation

At this point, the important question became:

> Do we really need to know every palindrome starting at every position?

No.

Suppose we have two valid palindromes starting at the same position:

```text
start
  |
  v
  [-------]
  [-------------]
```

If both are valid, the shorter one is always at least as useful.

Why?

Because it ends earlier and therefore leaves more of the string available for future palindromes.

For example:

```text
A = [i ........ j]
B = [i ................ r]
```

with:

```text
j < r
```

If we choose `A`, we can still use everything after `j`.

If we choose `B`, we lose everything from `j + 1` through `r`.

Therefore, for every starting position `i`, we only need:

```text
the earliest ending valid palindrome starting at i
```

We can store this in:

```python
next_end[i]
```

---

# Finding `next_end` Without a 2D Cache

We still need to find palindromes.

Instead of recursively checking every `(left, right)` pair, we can use **center expansion**.

Every palindrome has a center.

There are two possibilities:

### Odd-length palindrome

```text
aba
 ^
center
```

Start with:

```python
left = right = center
```

and expand outward.

### Even-length palindrome

```text
abba
 ^^
center
```

Start with:

```python
left = center
right = center + 1
```

and expand outward.

This allows us to discover all palindromes in `O(n²)` time while using only `O(n)` extra storage for the information we actually need.

---

# Building `next_end`

We initialize:

```python
next_end = [n] * n
```

`n` means:

```text
No valid palindrome has been found yet.
```

For every palindrome we discover:

```python
if right - left + 1 >= k:
    next_end[left] = min(next_end[left], right)
```

So after the center expansions:

```text
next_end[i]
```

contains the earliest ending position of a palindrome starting at `i`.

---

# Final DFS

Now the DFS no longer needs to search through every possible ending position.

At position `i`, there are only two choices.

### Skip

```python
dfs(i + 1)
```

### Take

If a valid palindrome starts at `i`:

```python
1 + dfs(next_end[i] + 1)
```

Therefore:

```python
@cache
def dfs(i):
    if i >= n:
        return 0

    res = dfs(i + 1)

    if next_end[i] < n:
        res = max(res, 1 + dfs(next_end[i] + 1))

    return res
```

This keeps the DFS idea from the earlier solution while removing the expensive two-dimensional palindrome cache.

---

# Final Solution

```python
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        next_end = [n] * n

        for center in range(n):

            # Odd length
            left = right = center

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= k:
                    next_end[left] = min(next_end[left], right)

                left -= 1
                right += 1

            # Even length
            left = center
            right = center + 1

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= k:
                    next_end[left] = min(next_end[left], right)

                left -= 1
                right += 1

        @cache
        def dfs(i):
            if i >= n:
                return 0

            # Skip this position
            res = dfs(i + 1)

            # Take the earliest valid palindrome starting here
            if next_end[i] < n:
                res = max(res, 1 + dfs(next_end[i] + 1))

            return res

        return dfs(0)
```

---

# Complexity

## Center Expansion

There are `n` possible centers.

Each center can expand up to `O(n)` positions.

Therefore:

```text
Time: O(n²)
```

We only store:

```python
next_end = [n] * n
```

which requires:

```text
Space: O(n)
```

---

## DFS

There are only `n` possible values of `i`.

Because of `@cache`, every state is evaluated once.

Therefore:

```text
Time: O(n)
Space: O(n)
```

The overall complexity remains:

```text
Time: O(n²)
Space: O(n)
```

---

# The Evolution of the Solution

The important part of this problem was not immediately finding the final code.

The solution evolved through several ideas:

```text
Sliding Window
      ↓
Longest Palindrome
      ↓
First Palindrome
      ↓
Brute Force All Substrings
      ↓
Interval Scheduling
      ↓
DFS Selection
      ↓
DFS + Cached Palindrome Checking
      ↓
MLE because palindrome cache is O(n²)
      ↓
Realize only earliest palindrome per start is needed
      ↓
Center Expansion
      ↓
O(n) palindrome information
      ↓
DFS + next_end
      ↓
Final O(n²) time / O(n) space solution
```

The main lesson was:

> When a recursive solution is correct but runs out of memory, look at what is being cached. Sometimes the recurrence is fine, but the state representation contains much more information than the final decision actually needs.

Here, the original DFS needed to know every possible palindrome interval.

The final version compresses that information down to just one value per starting position:

```text
next_end[i] = earliest valid palindrome ending at or after i
```

That was enough to keep the DFS approach while reducing the memory usage from `O(n²)` to `O(n)`.
