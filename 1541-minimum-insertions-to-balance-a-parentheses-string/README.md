# 1541. Minimum Insertions to Balance a Parentheses String

**LeetCode Problem:** [1541. Minimum Insertions to Balance a Parentheses String](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)

## Problem Summary

We are given a string `s` containing only `(` and `)`.

The string is balanced when every opening parenthesis `(` has **exactly two consecutive closing parentheses `))`** to match it.

We can insert parentheses anywhere in the string. Return the minimum number of insertions needed to make the string balanced.

**Example 1:**

```text
Input: s = "(()))"
Output: 1
```

**Explanation:** Insert one `)` to make the string `"(())))"`.

**Example 2:**

```text
Input: s = "())"
Output: 0
```

**Explanation:** The string already satisfies the required balance.

## Intuition

Each opening parenthesis `(` needs two closing parentheses `))`.

Instead of modifying the string, we can count the insertions we need using two variables:

* `left`: The number of insertions required so far.
* `right`: The number of closing parentheses `)` still needed to balance the opening parentheses we've encountered.

We process the string from left to right and update these counts as we go.

The key idea is to handle two special situations:

1. If we encounter `(` while `right` is odd, we need to insert one `)` first to complete the previous pair.
2. If we encounter `)` when no closing parentheses are needed, we must insert an opening parenthesis `(` to match it.

## Approach

1. Initialize `left = 0` and `right = 0`.
2. Iterate through each character in the string.
3. If the character is `(`:

   * If `right` is odd, insert one `)` by incrementing `left` and decrementing `right`.
   * Increase `right` by `2`, because this opening parenthesis requires two closing parentheses.
4. Otherwise, the character is `)`:

   * Decrease `right` by `1`, because we have found one closing parenthesis.
   * If `right` becomes negative, there was no opening parenthesis available to match it. Insert one `(` by incrementing `left`, then set `right = 1` to account for the one remaining `)` needed to complete its pair.
5. After processing the entire string, add `right` to `left`. These are the closing parentheses still missing.

Return `left + right`.

## Python Solution

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        left = right = 0

        for c in s:
            if c == "(":
                if right % 2 == 1:
                    left += 1
                    right -= 1

                right += 2
            else:
                right -= 1

                if right < 0:
                    left += 1
                    right = 1

        return left + right
```

## C Solution

```c
int minInsertions(char* s) {
    int left = 0;
    int right = 0;
    int n = strlen(s);

    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            if (right % 2 == 1) {
                left++;
                right--;
            }

            right += 2;
        } else {
            right--;

            if (right < 0) {
                left++;
                right = 1;
            }
        }
    }

    return left + right;
}
```

**Note:** The C solution requires `#include <string.h>` for `strlen()`.

## Complexity Analysis

**Time Complexity: O(n)**

We traverse the string once, processing each character in constant time. Here, `n` is the length of the string.

**Space Complexity: O(1)**

We use only two integer variables, `left` and `right`, regardless of the input size.

## Key Takeaway

The trick is to track the number of closing parentheses still required rather than actually inserting parentheses into the string.

By keeping `right` even whenever we encounter a new opening parenthesis and correcting negative counts immediately, we can calculate the minimum insertions in a single pass.
