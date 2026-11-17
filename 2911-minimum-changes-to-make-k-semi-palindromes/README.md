I’ve added a walkthrough using `s = "abba"` to show exactly how the `cost[i][j]` table is populated, including why we keep the minimum across different divisors. The rest of the README is preserved.

# 2911. Minimum Changes to Make K Semi-palindromes

[LeetCode Problem](https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/)

## Problem Summary

Given a string `s` and an integer `k`, divide the string into exactly `k` non-empty contiguous substrings.

Each substring must be converted into a **semi-palindrome** using character replacements.

Return the minimum total number of character changes required.

A substring is a semi-palindrome if there is at least one valid divisor `d` that allows us to divide its characters into `d` groups, with every group being a palindrome.

A valid `d` must satisfy two conditions:

- `d` must divide the substring's length.
- `d` must be strictly smaller than the substring's length.

This also means a semi-palindrome must have a length of at least `2`.

---

## 1. Understanding the Problem

There are two problems hidden inside this question:

1. **Substring problem:** How many changes are needed to make a particular substring a semi-palindrome?
2. **Partition problem:** How do we divide the original string into exactly `k` substrings while minimizing the total changes?

We solve these separately.

First, we calculate the minimum conversion cost for every possible substring. Then we use those precomputed costs in dynamic programming to find the optimal partition.

---

## 2. Understanding a Semi-palindrome

Let's take a substring of length `6`:

```
abcdef
```

We need to choose a valid divisor `d`.

For a length of `6`, the possible values are:

```
d = 1, 2, 3
```

Each value of `d` creates a different grouping.

### Example: d = 3

We divide the characters into `3` groups.

Each group contains `6 / 3 = 2` characters.

The important detail is that we do not simply divide the substring into three consecutive pieces. Instead, we take characters at intervals of `d`.

The groups become:

```
Group 1: a d
Group 2: b e
Group 3: c f
```

For each group to be a palindrome, its characters must match when read from opposite ends.

Since every group contains two characters, we compare:

```
a with d
b with e
c with f
```

If a pair does not match, we need exactly one replacement to make that pair equal.

For example:

```
a d  ->  a a
```

That costs one change.

### What happens with other divisors?

For the same substring:

```
d = 1  ->  Group: abcdef

d = 2  ->  Groups: ace, bdf

d = 3  ->  Groups: ad, be, cf
```

For `d = 2`, the groups are `ace` and `bdf`. Both groups must independently become palindromes.

The key observation is that **a substring only needs one valid grouping to work**. We try every valid divisor and choose the grouping that requires the fewest changes.

---

## 3. Calculating the Cost of a Substring

Now we need a way to calculate the minimum number of changes for any substring.

We use a two-dimensional array:

```
cost[i][j]
```

It represents the minimum number of changes required to make:

```
s[i:j]
```

a semi-palindrome.

Notice that `i` is the starting index and `j` is the ending boundary, meaning the substring does not include index `j`.

For example:

```
s = "abcdef"

s[1:5] = "bcde"
```

The substring length is:

```
m = j - i
```

### Finding the valid divisors

For every substring, we try every possible `d` from `1` to `m - 1`.

We only continue when `d` divides the substring length:

```
if m % d:
    continue
```

The length of each group is:

```
group_len = m // d
```

We now know:

- `d` is the number of groups.
- `group_len` is the number of characters in each group.

### Finding the characters to compare

For a substring starting at index `i`, group number `r` contains these positions:

```
i + r
i + r + d
i + r + 2*d
...
```

We compare the first character with the last, the second with the second-last, and so on.

Instead of constructing separate strings for each group, we calculate the original string indices directly.

The two indices are:

```
left  = i + r + t*d
right = i + r + (group_len - 1 - t)*d
```

Here is what each variable represents:

| Variable    | Meaning                                  |
| ----------- | ---------------------------------------- |
| `i`         | Starting index of the substring          |
| `j`         | Ending boundary of the substring         |
| `m`         | Length of the substring                  |
| `d`         | Number of groups                         |
| `group_len` | Number of characters in each group       |
| `r`         | Current group, from `0` to `d - 1`       |
| `t`         | Current mirrored pair inside the group   |
| `left`      | Index of the character on the left side  |
| `right`     | Index of the character on the right side |
| `changes`   | Changes needed for the current divisor   |

We only need to compare half of each group:

```
for t in range(group_len // 2):
```

Why?

Because every comparison handles a pair of mirrored characters. Once we compare the left and right sides, there is no reason to compare them again.

If the group has an odd length, the middle character does not need to change.

Whenever the characters do not match:

```
if s[left] != s[right]:
    changes += 1
```

One replacement is enough to make that pair equal.

After checking every group for the current divisor, we update the minimum cost:

```
cost[i][j] = min(cost[i][j], changes)
```

We repeat this for every valid divisor and every possible substring.

At the end, `cost[i][j]` contains the minimum changes needed to make `s[i:j]` a semi-palindrome.

### A small cost-table walkthrough

Let's use a smaller string so we can see how the table is built:

```
s = "abba"
```

The indices are:

```
Index:  0  1  2  3
String: a  b  b  a
```

Remember that `cost[i][j]` represents `s[i:j]`, so `j` is exclusive.

Let's calculate a few entries.

**1. Substring `s[0:2] = "ab"`**

Its length is `2`, so the only valid divisor is `d = 1`.

The group is:

```
a b
```

The characters do not match, so one replacement is needed.

```
cost[0][2] = 1
```

**2. Substring `s[1:3] = "bb"`**

Again, the only valid divisor is `d = 1`.

```
b b
```

The characters already match.

```
cost[1][3] = 0
```

**3. Substring `s[0:3] = "abb"`**

Its length is `3`. The only valid divisor is `d = 1`.

```
a b b
```

We compare the first and last characters.

They do not match, so one replacement is needed. The middle character does not need to change.

```
cost[0][3] = 1
```

**4. Substring `s[0:4] = "abba"`**

This is where trying multiple divisors matters.

The length is `4`, so the valid divisors are `d = 1` and `d = 2`.

For `d = 1`, we get one group:

```
a b b a
```

Compare the mirrored pairs:

```
a with a  -> match
b with b  -> match
```

Cost = `0`.

For `d = 2`, we get two groups:

```
Group 1: a b
Group 2: b a
```

Both groups have mismatched characters.

Cost = `2`.

We choose the smaller cost:

```
cost[0][4] = min(0, 2) = 0
```

### What does the cost table look like?

The entries calculated above can be represented as:

| Starting index `i` | `j = 2`  | `j = 3`   | `j = 4`    |
| ------------------ | -------- | --------- | ---------- |
| `i = 0`            | 1 (`ab`) | 1 (`abb`) | 0 (`abba`) |
| `i = 1`            | —        | 0 (`bb`)  | 1 (`bba`)  |
| `i = 2`            | —        | —         | 1 (`ba`)   |

The dash means that the substring would have a length smaller than `2`, so it is not considered.

This table illustrates the purpose of preprocessing: instead of calculating the cost of a substring again and again during partitioning, we calculate it once and store the answer.

### Cost preprocessing code

```
cost = [[INF] * (n + 1) for _ in range(n)]

for i in range(n):
    for j in range(i + 2, n + 1):
        m = j - i

        for d in range(1, m):
            if m % d:
                continue

            changes = 0
            group_len = m // d

            for r in range(d):
                for t in range(group_len // 2):
                    left = i + r + t * d
                    right = i + r + (group_len - 1 - t) * d

                    if s[left] != s[right]:
                        changes += 1

            cost[i][j] = min(cost[i][j], changes)
```

We start `j` at `i + 2` because a substring of length `1` cannot be a semi-palindrome.

---

## 4. Partitioning the String Using Dynamic Programming

Now that we know the minimum cost of every possible substring, we can solve the second part: dividing the string into exactly `k` semi-palindromes.

We use a two-dimensional DP table:

```
dp[i][p]
```

It represents:

**The minimum number of changes needed to divide the first `i` characters of `s` into exactly `p` semi-palindromic substrings.**

This definition is important.

`i` is a prefix length, not an array index of the last character.

For example:

```
dp[5][2]
```

means we have divided:

```
s[:5]
```

into exactly two semi-palindromic substrings.

### Base case

```
dp[0][0] = 0
```

There is exactly one way to partition an empty string into zero substrings: do nothing, with zero changes.

All other states initially contain infinity because we have not found a valid partition for them yet.

### Deriving the transition

Suppose we want to calculate:

```
dp[i][p]
```

We know the first `i` characters must be divided into `p` groups.

Let's focus on the final group.

Suppose the final group starts at index `j`.

Then the partition looks like this:

```
s[:j]  |  s[j:i]
previous     final group
groups
```

The first part contains `j` characters and must already be divided into `p - 1` semi-palindromic substrings.

Its minimum cost is:

```
dp[j][p - 1]
```

The final substring is:

```
s[j:i]
```

We have already calculated its minimum conversion cost:

```
cost[j][i]
```

Therefore, the total cost for choosing `j` as the start of the final group is:

```
dp[j][p - 1] + cost[j][i]
```

But there can be multiple valid starting positions for the final group.

So we try every possible `j` and keep the minimum:

```
dp[i][p] = min(
    dp[i][p],
    dp[j][p - 1] + cost[j][i]
)
```

This is the DP transition.

### Choosing valid starting positions

Every semi-palindrome must contain at least two characters.

This gives us two restrictions.

**1. Previous groups must have enough characters.**

We need `p - 1` previous groups, and each needs at least two characters.

Therefore, the previous part must contain at least:

```
2 * (p - 1)
```

characters.

That is why we start `j` at:

```
2 * (p - 1)
```

**2. The final group must contain at least two characters.**

The final substring is `s[j:i]`.

For it to contain at least two characters:

```
j <= i - 2
```

Python's `range()` excludes its ending value, so we write:

```
range(2 * (p - 1), i - 1)
```

This checks all valid starting boundaries.

We also skip states that are impossible:

```
if dp[j][p - 1] == INF:
    continue
```

There is no reason to build a partition on top of an invalid previous state.

### DP code

```
dp = [[INF] * (k + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for p in range(1, k + 1):
        for j in range(2 * (p - 1), i - 1):
            if dp[j][p - 1] == INF:
                continue

            dp[i][p] = min(
                dp[i][p],
                dp[j][p - 1] + cost[j][i]
            )
```

After processing all states, our answer is:

```
dp[n][k]
```

This means we have considered the entire string and divided it into exactly `k` semi-palindromic substrings.

---

## 5. Complete Solution

``` Python
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')
        cost = [[INF]*(n+1) for _ in range(n)]

        for i in range(n):
            for j in range(i+2,n+1):
                m = j-i
                for d in range(1,m):
                    if m%d:
                        continue

                    changes = 0
                    group_len = m//d

                    for r in range(d):
                        for t in range(group_len//2):
                            left  = i+r+t*d
                            right = i + r + (group_len - 1 -t)*d

                            if s[left] != s[right]:
                                changes += 1

                    cost[i][j] = min(cost[i][j],changes)

        dp = [[INF]*(k+1) for _ in range(n+1)]
        dp[0][0] = 0

        for i in range(1,n+1):
            for p in range(1,k+1):
                for j in range(2*(p-1),i-1):
                    if dp[j][p-1] == INF:
                        continue

                    dp[i][p] = min(
                        dp[i][p],
                        dp[j][p-1] + cost[j][i]
                    )

        return dp[n][k]
```


```C
int minimumChanges(char* s, int k) {
    int n = strlen(s);
    int INF = 1e9;

    // Allocate cost[n][n+1]
    int** cost = (int**)malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        cost[i] = (int*)malloc((n + 1) * sizeof(int));
        for (int j = 0; j <= n; j++) {
            cost[i][j] = INF;
        }
    }

    // Precompute conversion costs for semi-palindromes
    for (int i = 0; i < n; i++) {
        for (int j = i + 2; j <= n; j++) {
            int m = j - i;
            for (int d = 1; d < m; d++) {
                if (m % d != 0) continue;
                int changes = 0;
                int group_len = m / d;

                for (int r = 0; r < d; r++) {
                    for (int t = 0; t < group_len / 2; t++) {
                        int left = i + r + t * d;
                        int right = i + r + (group_len - 1 - t) * d;
                        if (s[left] != s[right]) {
                            changes++;
                        }
                    }
                }
                if (changes < cost[i][j]) {
                    cost[i][j] = changes;
                }
            }
        }
    }

    // Allocate dp[n+1][k+1]
    int** dp = (int**)malloc((n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) {
        dp[i] = (int*)malloc((k + 1) * sizeof(int));
        for (int p = 0; p <= k; p++) {
            dp[i][p] = INF;
        }
    }
    dp[0][0] = 0;

    // Dynamic programming transition
    for (int i = 1; i <= n; i++) {
        for (int p = 1; p <= k; p++) {
            for (int j = 2 * (p - 1); j < i - 1; j++) {
                if (dp[j][p - 1] == INF) continue;
                int val = dp[j][p - 1] + cost[j][i];
                if (val < dp[i][p]) {
                    dp[i][p] = val;
                }
            }
        }
    }

    
    return dp[n][k];
}



```
---

## 6. Why Does This Approach Work?

The solution works because we separate the problem into two independent stages.

### Stage 1: Every substring gets its optimal cost

For each possible substring, we try every valid divisor.

Each divisor gives us a specific grouping of characters. We compare mirrored characters inside every group and count the replacements required.

Since one mismatched pair needs exactly one replacement, this gives the minimum number of changes for that particular grouping.

Taking the minimum across all valid divisors gives the true minimum cost of making that substring a semi-palindrome.

### Stage 2: DP finds the optimal partition

Once every substring has a known minimum cost, the partitioning problem becomes a standard DP problem.

For every prefix and every possible number of groups, we try all valid positions where the final group could begin.

Every transition combines:

- The best way to partition the previous prefix into `p - 1` groups.
- The minimum cost of converting the final substring into a semi-palindrome.

Because we consider every valid starting position and keep the minimum, we never miss a better partition.

Finally, `dp[n][k]` gives the minimum total changes for the entire string divided into exactly `k` valid groups.

---

## 7. Complexity Analysis

Let `n` be the length of the string and `k` the required number of substrings.

**Substring cost preprocessing:**

- There are O(n²) possible substrings.
- For each substring, we check possible divisors.
- For every valid divisor, we compare mirrored character pairs.

A conservative upper bound for this preprocessing is **O(n³ log n)**.

**Dynamic programming:**

- There are O(nk) DP states.
- Each state can examine up to O(n) possible starting positions.

Therefore, DP takes **O(kn²)** time.

**Space complexity:**

- The substring cost table uses O(n²) space.
- The DP table uses O(nk) space.

Total space complexity: **O(n² + nk)**.

---

## Final Takeaway

The main idea is to avoid solving the entire problem at once.

First, determine the minimum cost of converting every possible substring into a semi-palindrome. Then use those costs to build the optimal partition with dynamic programming.

The important observations are:

1. A semi-palindrome can be formed using different valid divisors.
2. Each divisor creates groups whose characters must be palindromes.
3. Each mismatched mirrored pair requires exactly one replacement.
4. Precomputing substring costs lets us avoid repeating this work during DP.
5. The final DP transition tries every possible starting point for the last substring and keeps the minimum total cost.

Clarify the divisor grouping ruleAlign the opening with the code