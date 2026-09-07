# 940. Distinct Subsequences II

## Problem

Given a string `s`, return the number of **distinct non-empty subsequences** of `s`.

A subsequence is created by deleting zero or more characters without changing the relative order of the remaining characters.

For example:

```text
s = "abcde"

"ace"  -> valid subsequence
"aec"  -> not a subsequence
```

Because the answer can become very large, return it modulo:

```text
10^9 + 7
```

---

# 1. First Approach: Brute Force DFS

Since a subsequence can either contain the current character or not contain it, every character gives us two choices:

```text
Take s[i]
Don't take s[i]
```

That naturally leads to DFS.

For example, for:

```text
s = "abc"
```

the recursion looks conceptually like:

```text
                  ""
              /        \
            "a"         ""
           /   \       /  \
        "ab"  "a"    "b"   ""
```

Continuing this process generates every possible subsequence.

## Brute Force Code

```python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        subseq = set()
        MOD = 10**9 + 7

        def dfs(i, curr_s):
            if i == n:
                if curr_s:
                    subseq.add(curr_s)
                return

            # Take the current character
            dfs(i + 1, curr_s + s[i])

            # Don't take the current character
            dfs(i + 1, curr_s)

        dfs(0, "")

        return len(subseq) % MOD
```

## Why does this work?

At every index we make exactly the two choices allowed by the definition of a subsequence:

```text
take
don't take
```

Therefore, every possible subsequence is generated.

The `set` is necessary because different choices of indices can produce the same string.

For example:

```text
s = "aaa"
```

The DFS generates many paths:

```text
"aaa"
"aa"
"aa"
"a"
"aa"
"a"
"a"
""
```

But the distinct non-empty subsequences are only:

```text
"a"
"aa"
"aaa"
```

So the set correctly removes duplicates.

---

# 2. Why Brute Force Is Too Slow

For every character we have two choices.

Therefore the DFS has approximately:

```text
2^n
```

possible paths.

For a string with all different characters, almost all of those paths produce different subsequences.

For example:

```text
s = "abcde"
```

There are:

```text
2^5 = 32
```

total subsequences if we include the empty string.

Therefore there are:

```text
32 - 1 = 31
```

non-empty subsequences.

As `n` becomes large, `2^n` grows extremely quickly.

There is another problem: we are actually constructing and storing all of those strings.

So the brute force solution is useful for **understanding the problem**, but it cannot handle the required input size.

---

# 3. Can We Just Add DFS Memoization?

The first thought might be:

```python
cache[i]
```

But our DFS state is not just `i`.

It is:

```text
(i, curr_s)
```

because the result depends on the string we have already built.

For example:

```text
dfs(3, "a")
dfs(3, "b")
```

have the same remaining characters, but they can produce completely different final strings.

Therefore caching only by `i` is not enough.

We could technically cache:

```text
(i, curr_s)
```

but there can still be an enormous number of different `curr_s` values.

So memoizing the original DFS does not solve the fundamental problem.

We need to stop generating the actual subsequences.

---

# 4. The Important Observation: Every Character Doubles the Possibilities

Suppose we already have some distinct subsequences.

When we add a new character `c`, every existing subsequence can either:

```text
stay as it is
```

or:

```text
append c
```

So conceptually:

```text
old subsequences
        +
old subsequences + c
```

If we temporarily include the empty subsequence, then if there are `count` subsequences before adding `c`, we initially get:

```text
2 * count
```

possibilities.

For example:

```text
s = "ab"
```

Start with:

```text
{""}
```

After adding `a`:

```text
{"", "a"}
```

Count:

```text
2
```

After adding `b`:

```text
{"", "a", "b", "ab"}
```

Count:

```text
4
```

So with all unique characters the count simply doubles.

But repeated characters create duplicates.

---

# 5. Where Do the Duplicates Come From?

Consider:

```text
s = "aaa"
```

After processing the first `a`:

```text
""
"a"
```

Count = `2`

Now process the second `a`.

Appending `a` gives:

```text
"a"
"aa"
```

Together with the old subsequences:

```text
""
"a"
"aa"
```

Count = `3`

Now process the third `a`.

The existing subsequences are:

```text
""
"a"
"aa"
```

Appending another `a` gives:

```text
"a"
"aa"
"aaa"
```

But:

```text
"a"
"aa"
```

already existed.

So only `"aaa"` is new.

The count becomes:

```text
4
```

including the empty string.

Therefore the answer is:

```text
4 - 1 = 3
```

for the non-empty subsequences:

```text
"a"
"aa"
"aaa"
```

---

# 6. The Key Pattern

The important question is:

> When a character appears again, how many of the newly generated subsequences are duplicates?

The answer is:

> Exactly the number of distinct subsequences that existed **before the previous occurrence of that character**.

Why?

Suppose the previous occurrence of `c` happened when there were `old_count` subsequences.

At that time, processing `c` created:

```text
old_count
```

new strings by appending `c` to every existing subsequence.

When `c` appears again later, those same strings are generated again.

Therefore those `old_count` strings are duplicates.

So we only need to remember:

```text
last_total[c]
```

where:

```text
last_total[c] =
number of distinct subsequences before the previous occurrence of c
```

---

# 7. Example: `abca`

Let's work through this carefully.

We include the empty subsequence in our count.

Start:

```text
curr = 1
```

The only subsequence is:

```text
""
```

### Process `a`

Before `a`:

```text
curr = 1
```

There has never been an `a`, so there are no duplicates.

```text
curr = 2 * 1 - 0
     = 2
```

The subsequences are:

```text
""
"a"
```

Before processing `a`, `curr` was `1`, so store:

```text
last_total['a'] = 1
```

---

### Process `b`

Before `b`:

```text
curr = 2
```

No previous `b`.

```text
curr = 2 * 2 - 0
     = 4
```

Subsequences:

```text
""
"a"
"b"
"ab"
```

Store:

```text
last_total['b'] = 2
```

---

### Process `c`

Before `c`:

```text
curr = 4
```

No previous `c`.

```text
curr = 2 * 4
     = 8
```

Store:

```text
last_total['c'] = 4
```

---

### Process the second `a`

Before this `a`:

```text
curr = 8
```

The previous `a` occurred when:

```text
last_total['a'] = 1
```

So exactly `1` newly generated subsequence will be a duplicate.

Therefore:

```text
curr = 2 * 8 - 1
     = 15
```

Finally remove the empty subsequence:

```text
15 - 1 = 14
```

So:

```text
answer = 14
```

---

# 8. Example: `abaa`

This example makes the duplicate behavior especially clear.

The distinct non-empty subsequences are:

```text
a
b
ab
aa
ba
aba
aaa
baa
abaa
```

Answer:

```text
9
```

Let's see how our counting discovers this.

Start:

```text
curr = 1
```

### First `a`

```text
curr = 2
last_total[a] = 1
```

### `b`

```text
curr = 4
last_total[b] = 2
```

### Second `a`

The previous `a` was processed when:

```text
last_total[a] = 1
```

Therefore:

```text
curr = 2 * 4 - 1
     = 7
```

### Third `a`

The previous `a` was processed when:

```text
last_total[a] = 4
```

Therefore:

```text
curr = 2 * 7 - 4
     = 10
```

Remove the empty subsequence:

```text
10 - 1 = 9
```

Answer:

```text
9
```

---

# 9. Example: `abcab`

This example shows why we cannot simply check whether the current character is the same as the immediately previous character.

After processing:

```text
abc
```

there are:

```text
2^3 = 8
```

distinct subsequences including the empty string.

So:

```text
curr = 8
```

The second `a` appears later, not immediately after the first `a`.

Before the first `a`:

```text
last_total[a] = 1
```

Therefore:

```text
curr = 2 * 8 - 1
     = 15
```

Now the second `b` appears.

Before the first `b`:

```text
last_total[b] = 2
```

Therefore:

```text
curr = 2 * 15 - 2
     = 28
```

Remove the empty subsequence:

```text
28 - 1 = 27
```

Answer:

```text
27
```

---

# 10. The Recurrence

Let:

```text
curr = number of distinct subsequences including ""
```

Before processing character `c`:

```text
old = curr
```

Adding `c` creates:

```text
2 * old
```

possibilities.

If `c` appeared before, some of these are duplicates.

The number of duplicates is:

```text
last_total[c]
```

Therefore:

```text
curr = 2 * old - last_total[c]
```

Then we update the information for this character:

```text
last_total[c] = old
```

The order matters.

We must store `old`, not the newly calculated `curr`.

---

# 11. Final Algorithm

For every character:

```text
1. Save the current total.
2. Double the total.
3. Subtract the value stored for this character.
4. Save the old total as the character's latest value.
```

In pseudocode:

```text
curr = 1

for every character c:

    old = curr

    curr = 2 * old - last_total[c]

    last_total[c] = old
```

At the end, subtract `1` because `curr` includes the empty subsequence.

---

# 12. Python Solution

```python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # last_total[c] stores the number of distinct
        # subsequences before the previous occurrence of c.
        last_total = [0] * 26

        # Start with the empty subsequence.
        curr = 1

        for c in s:
            idx = ord(c) - ord('a')

            # Save the count before processing c.
            old = curr

            # Every existing subsequence can either:
            # 1. stay unchanged
            # 2. append c
            #
            # So we initially double the count.
            # Then remove the duplicates created by c before.
            curr = (2 * old - last_total[idx]) % MOD

            # Remember the count from before this occurrence.
            last_total[idx] = old

        # Remove the empty subsequence.
        return (curr - 1) % MOD
```

---

# 13. Why `curr` Starts at 1

This is an important detail.

We start with:

```python
curr = 1
```

because we are counting:

```text
""
```

the empty subsequence.

Keeping the empty subsequence makes the recurrence much cleaner.

For example, for:

```text
s = "a"
```

we get:

```text
curr = 2
```

representing:

```text
""
"a"
```

But the problem asks only for non-empty subsequences.

So at the end:

```python
return (curr - 1) % MOD
```

---

# 14. Why We Store `old`

This line is extremely important:

```python
old = curr
```

Suppose we are processing `a`.

We need to remember:

```text
number of subsequences BEFORE this a
```

because that is what must be stored for the next occurrence of `a`.

So:

```python
old = curr
curr = 2 * old - last_total[idx]
last_total[idx] = old
```

If we instead wrote:

```python
last_total[idx] = curr
```

we would store the count **after** processing the character, which is not the information required by the recurrence.

---

# 15. Why We Need an Array of 26 Values

The duplicate information is different for each character.

For example:

```text
last_total['a']
last_total['b']
last_total['c']
...
```

So we maintain:

```python
last_total = [0] * 26
```

The character is converted to an index using:

```python
idx = ord(c) - ord('a')
```

For example:

```text
'a' -> 0
'b' -> 1
'c' -> 2
...
'z' -> 25
```

This gives constant-time access to the previous information for each character.

---

# 16. From DFS to the Final Solution

The most useful part of this problem is the progression from the brute-force solution to the optimized solution.

### Step 1 — DFS

Every character gives two choices:

```text
take
don't take
```

So DFS can generate every subsequence.

### Step 2 — Set

Different DFS paths can produce the same string.

So we use a set to keep only distinct subsequences.

### Step 3 — Identify the real problem

DFS is spending most of its time generating strings that we don't actually need.

We only need the **number** of distinct subsequences.

### Step 4 — Count instead of generate

When a new character arrives:

```text
existing subsequences
+
existing subsequences + character
```

So the number initially doubles.

### Step 5 — Remove duplicates intelligently

Repeated characters cause some of those newly created subsequences to already exist.

The duplicates are exactly the subsequences created by the previous occurrence of that same character.

### Step 6 — Store only the necessary information

Instead of storing every subsequence, store:

```text
current total
+
one value for each character
```

That reduces the problem from exponential enumeration to a linear scan.

---

# 17. Complexity

Let:

```text
n = len(s)
```

### Time Complexity

We process every character exactly once:

```text
O(n)
```

### Space Complexity

We store 26 values:

```text
O(26)
```

which is effectively:

```text
O(1)
```

We no longer store all subsequences.

---

# 18. Quick Test Cases

| Input     | Answer | Explanation                                                                             |
| --------- | -----: | --------------------------------------------------------------------------------------- |
| `"a"`     |    `1` | `{a}`                                                                                   |
| `"aa"`    |    `2` | `{a, aa}`                                                                               |
| `"aaa"`   |    `3` | `{a, aa, aaa}`                                                                          |
| `"abc"`   |    `7` | All `2^3 - 1` non-empty subsequences are unique                                         |
| `"aba"`   |    `6` | Duplicate `a` removes previously created possibilities                                  |
| `"abaa"`  |    `9` | Repeated `a` creates more duplicates                                                    |
| `"abca"`  |   `14` | Second `a` does not simply mean "same as previous character"; the earlier state matters |
| `"abcab"` |   `27` | Repeated `a` and `b` each remove their previously created duplicates                    |

---

# 19. Main Takeaway

The key lesson from this problem is not simply the final formula.

It is the transition:

```text
Generate every subsequence with DFS
                ↓
Notice massive duplicate work
                ↓
Count possibilities instead of generating strings
                ↓
2 × previous count
                ↓
Remove duplicates caused by repeated characters
                ↓
Remember only the information needed for each character
                ↓
O(n) DP
```

The original DFS is therefore a useful way to understand the problem, even though it cannot pass the full constraints.

The final solution does not need DFS, a set, or the actual subsequences.

It only needs:

```text
curr
last_total[26]
```

and the recurrence:

```text
curr = 2 * old - last_total[c]
```

with the empty subsequence removed at the end.
