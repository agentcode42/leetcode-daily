# 3723. Maximize Sum of Squares of Digits

**LeetCode Problem:** [3723. Maximize Sum of Squares of Digits](https://leetcode.com/problems/maximize-sum-of-squares-of-digits/)

## Problem Summary

Given two integers, `num` and `sum`, construct a string of exactly `num` digits whose digits add up to `sum`.

The goal is to maximize the sum of the squares of the digits. If it is impossible to construct such a number, return an empty string.

## Intuition

To maximize the sum of squared digits, we should make the digits as large as possible.

For example, \(9^2 = 81\), which is greater than the square of any other decimal digit. Therefore, we should use as many `9`s as possible, followed by the remaining sum and then zeros.

If the required sum is greater than `num * 9`, constructing a valid number is impossible, so we return an empty string.

## Approach 1: Greedy with Direct String Construction (Python)

Instead of building the number digit by digit, we can calculate how many `9`s we need and construct the result directly.

1. Check whether `sum` exceeds `num * 9`. If it does, return an empty string.
2. Calculate how many `9`s can fit using `sum // 9`.
3. Calculate the remaining sum after using those `9`s.
4. Fill the remaining positions with the leftover digit and zeros.
5. If all digits are `9`, return the string of `9`s directly.

### Python Solution

```python
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        total = sum
        if num * 9 < total:
            return ""

        digit_9 = total // 9
        remain = num - digit_9
        total = total - (digit_9 * 9)

        if remain == 0:
            return "9" * digit_9

        res = "9" * digit_9 + str(total) + "0" * (remain - 1)
        return res
```

## Approach 2: Greedy Digit-by-Digit Construction (C)

In C, we can construct the answer by allocating a character array and filling it from left to right.

1. If `sum > num * 9`, return an empty string.
2. Allocate memory for `num` digits and the null terminator.
3. At each position, choose the smaller of `9` and the remaining sum.
4. Store the digit as a character and subtract it from the remaining sum.
5. Add the null terminator and return the result.

### C Solution

```c
char* maxSumOfSquares(int num, int sum) {
    if (sum > num * 9) return "";

    char* res = (char*)malloc((num + 1) * sizeof(char));

    for (int i = 0; i < num; i++) {
        int digit = (sum < 9) ? sum : 9;
        res[i] = '0' + digit;
        sum -= digit;
    }

    res[num] = '\0';
    return res;
}
```

**Note:** Include `#include <stdlib.h>` for `malloc`. The returned buffer is dynamically allocated; the caller is responsible for freeing it. This code assumes the allocation succeeds.

## Example

**Input:** `num = 5, sum = 20`

**Output:** `"99200"`

**Explanation:**

- Place two `9`s, contributing \(9 + 9 = 18\).
- The remaining sum is `2`, so place `2`.
- Fill the remaining positions with zeros.

The resulting digits add up to \(9 + 9 + 2 + 0 + 0 = 20\), and their squared sum is \(81 + 81 + 4 = 166\).

## Complexity Analysis

Let `num` be the required number of digits.

| Complexity | Python | C |
|---|---|---|
| Time | \(O(num)\) | \(O(num)\) |
| Space | \(O(num)\) | \(O(num)\) |

Although the Python solution uses direct string construction, creating the output still requires time proportional to its length. The C solution explicitly fills each character position.

## Key Takeaway

**Greedy strategy:** Maximize the contribution of each digit by using as many `9`s as possible. Any leftover sum becomes one smaller digit, and the remaining positions are filled with zeros.