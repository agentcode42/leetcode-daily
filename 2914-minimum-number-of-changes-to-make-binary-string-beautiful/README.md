# 2914. Minimum Number of Changes to Make Binary String Beautiful

## Problem Summary

We are given a binary string `s` consisting of `0`s and `1`s.

A string is considered beautiful if it can be divided into substrings of even length, where every character in each substring is identical.

Our task is to return the minimum number of character changes required to make the string beautiful.

## Intuition

The important observation is that every valid substring must have an even length.

This means every substring starts and ends at even-length boundaries (using zero-based indexing).

Instead of trying every possible way to divide the string, we can look at the string in consecutive pairs:

- Characters at indices `0` and `1`
- Characters at indices `2` and `3`
- Characters at indices `4` and `5`
- And so on.

Why does this work?

Since every substring must have an even length, its boundaries will always fall between these pairs.

Therefore, no valid substring can split a pair.

Now consider each pair:

- If both characters are identical (`00` or `11`), no change is needed.
- If the characters are different (`01` or `10`), we must change at least one character to make that pair identical.

So each mismatched pair requires exactly one change.

## Approach: Greedy Pair Checking

1. Initialize a counter `res = 0`.
2. Traverse the string using a step size of 2.
3. Compare the current character with the next character.
4. If they are different, increment the counter.
5. Return the counter.

We don't need to actually modify the string. We only need to count how many pairs require a change.

## Example Walkthrough

**Input:**

```python
s = "1001"
```

Divide the string into consecutive pairs:

| Pair | Characters | Changes needed |
|---|---|---|
| 1 | `10` | 1 |
| 2 | `01` | 1 |

Both pairs contain different characters, so each requires one change.

Total changes = 1 + 1 = **2**

**Output:**

```python
2
```

One possible beautiful string is `1100`, which can be divided into `11` and `00`.

## Python Solution

```python
class Solution:
    def minChanges(self, s: str) -> int:
        res = 0

        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                res += 1

        return res
```

## C Solution

```c
int minChanges(char* s) {
    int n = strlen(s);
    int result = 0;

    for (int i = 0; i < n; i += 2) {
        if (s[i] != s[i + 1]) {
            result++;
        }
    }

    return result;
}
```

## JavaScript Solution

```javascript
var minChanges = function(s) {
    let n = s.length;
    let res = 0;

    for (let i = 0; i < n; i += 2) {
        if (s[i] != s[i + 1]) {
            res += 1;
        }
    }

    return res;
};
```

## Complexity Analysis

Let `n` be the length of the string.

- **Time Complexity: O(n)** — We visit every character exactly once, comparing characters in pairs.
- **Space Complexity: O(1)** — We only use a counter and a loop variable. No additional data structures are required.

## Key Takeaway

The main observation is that every valid substring has an even length. This guarantees that the string can be treated as independent consecutive pairs.

A mismatched pair always needs exactly one change, while a matching pair needs none.

This turns what initially looks like a string partitioning problem into a simple greedy counting problem.