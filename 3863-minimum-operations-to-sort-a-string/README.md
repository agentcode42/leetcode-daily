# 3863. Minimum Operations to Sort a String

**LeetCode:** [3863. Minimum Operations to Sort a String](https://leetcode.com/problems/minimum-operations-to-sort-a-string/)  
**Difficulty:** Medium  
**Topics:** String, Greedy, Case Analysis

## 1. Problem Summary

You are given a string `s` containing lowercase English letters.

In one operation, you can choose any **substring except the entire string** and sort that substring in non-decreasing alphabetical order.

Return the minimum number of operations needed to sort the whole string. If it is impossible, return `-1`.

The important restriction is that we cannot sort the whole string in one operation.

## 2. Intuition

Instead of simulating different substring sorts, we can solve the problem by checking just three things:

- Is the string already sorted?
- Where are the **smallest** and **largest** characters?
- Is the string too short to fix?

Let `mins` be the smallest character and `maxs` be the largest character in the string.

### Case 1: The string is already sorted → `0`

If every character is less than or equal to the character after it, no operation is needed.

For example, `"abc"` is already sorted, so the answer is `0`.

### Case 2: The string has length `2` and is not sorted → `-1`

For a string such as `"gf"`, the only proper substrings contain one character. Sorting a one-character substring cannot change the order of the two characters, and sorting the entire string is forbidden. Therefore, the answer is `-1`.

We check whether the string is sorted **before** this case, so a sorted two-character string still correctly returns `0`.

### Case 3: The smallest character is first, or the largest character is last → `1`

If `s[0] == mins`, the smallest character is already in its final position. We can sort the suffix `s[1:]` in one operation.

Similarly, if `s[-1] == maxs`, the largest character is already in its final position. We can sort the prefix `s[:-1]` in one operation.

Both chosen substrings are proper substrings, so this takes exactly one operation when the string was not already sorted.

### Case 4: The smallest or largest character is in the middle → `2`

If the smallest character is somewhere in the middle, we can sort a prefix ending at that character to bring the smallest character to the beginning. Then we sort the remaining suffix. Since the first character is the global minimum, the whole string is now sorted.

Alternatively, if the largest character is in the middle, we can sort a suffix starting at that character to move the largest character to the end. Then we sort the prefix before it.

So, if `mins` or `maxs` appears in `s[1:-1]`, the answer is `2`.

### Case 5: Neither extreme is in the middle, and neither is already correctly placed → `3`

At this point, the string is not sorted, its first character is not the minimum, and its last character is not the maximum. If neither extreme appears in the middle, the largest character must be at the beginning and the smallest character must be at the end.

A proper substring cannot include both ends of the string, so one operation cannot fix both extremes. This case needs three overlapping prefix/suffix sorts.

For example, with `"cba"`:

1. Sort `"cb"` → `"bca"`.
2. Sort `"ca"` → `"bac"`.
3. Sort `"ba"` → `"abc"`.

Therefore, the answer is `3`.

## 3. Approach

1. Find the smallest and largest characters in the string.
2. Scan the string to check whether it is already sorted. If it is, return `0`.
3. If the string is unsorted and has length `2`, return `-1`.
4. If the first character is the minimum or the last character is the maximum, return `1`.
5. Check the middle characters. If any of them is the minimum or maximum, return `2`.
6. If none of the above cases applies, return `3`.

The solution works through a small case analysis, so there is no need to actually sort substrings.

## 4. Python Solution

```python
class Solution:
    def minOperations(self, s: str) -> int:
        mins = min(s)
        maxs = max(s)
        n = len(s)

        sort = True
        for i in range(1, n):
            if s[i] < s[i - 1]:
                sort = False
                break

        if sort:
            return 0

        if n == 2:
            return -1

        if s[0] == mins or s[-1] == maxs:
            return 1

        mid = s[1:-1]
        if mins in mid or maxs in mid:
            return 2

        return 3
```

## 5. C Solution

```c
#include <stdbool.h>
#include <string.h>

int minOperations(char* s) {
    char mins = s[0];
    char maxs = s[0];
    int n = strlen(s);
    bool sort = true;

    for (int i = 1; i < n; i++) {
        if (s[i] < s[i - 1]) {
            sort = false;
        }
        if (s[i] < mins) mins = s[i];
        if (s[i] > maxs) maxs = s[i];
    }

    if (sort) return 0;
    if (n == 2) return -1;
    if (s[0] == mins || s[n - 1] == maxs) return 1;

    for (int i = 1; i < n - 1; i++) {
        if (s[i] == mins || s[i] == maxs) return 2;
    }

    return 3;
}
```

## 6. Complexity Analysis

Let `n` be the length of the string.

- **Time Complexity: `O(n)`** — finding the minimum and maximum, checking whether the string is sorted, and examining the middle characters each take linear time. These scans are performed a constant number of times.
- **Auxiliary Space:**
  - **Python: `O(n)`** — the slice `s[1:-1]` creates a new string.
  - **C: `O(1)`** — only a fixed number of character and integer variables are used.

## 7. Key Takeaway

The trick is not to sort the string directly. The answer depends on whether the string is already sorted and where its smallest and largest characters are located:

- Already sorted → `0`
- Unsorted string of length `2` → `-1`
- Minimum at the beginning or maximum at the end → `1`
- Minimum or maximum in the middle → `2`
- Maximum at the beginning and minimum at the end, with neither in the middle → `3`
