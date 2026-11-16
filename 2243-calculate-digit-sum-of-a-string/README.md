# 2243. Calculate Digit Sum of a String

[LeetCode Problem](https://leetcode.com/problems/calculate-digit-sum-of-a-string/)

## Problem Summary

Given a string `s` consisting of digits and an integer `k`, repeatedly perform the following operation until the string length is less than or equal to `k`:

1. Divide the string into consecutive groups of `k` characters.
2. For each group, calculate the sum of its digits.
3. Replace each group with its digit sum and concatenate the results.

The final group can contain fewer than `k` characters.

Return the resulting string.

## Approach

We repeatedly process the string until its length becomes less than or equal to `k`.

For each iteration:

1. Create a temporary character array to store the next string.
2. Traverse the current string in steps of `k`.
3. For each group, calculate the sum of its digits.
4. Use `sprintf()` to convert the sum into a string and append it to the temporary array.
5. Null-terminate the temporary string and copy it back into the original string.
6. Update the string length and repeat.

## C Code

```c
char* digitSum(char* s, int k) {
    int len = strlen(s);

    while (len > k) {
        char temp[1001];
        int idx = 0;

        for (int i = 0; i < len; i += k) {
            int sum = 0;

            for (int j = i; j < i + k && j < len; j++) {
                sum += s[j] - '0';
            }

            idx += sprintf(temp + idx, "%d", sum);
        }

        temp[idx] = '\0';
        strcpy(s, temp);
        len = strlen(s);
    }

    return s;
}
```

## Key Concepts

- **String Traversal:** Process the string in groups of `k` characters.
- **Character to Integer Conversion:** `s[j] - '0'` converts a numeric character into its integer value.
- **sprintf():** Converts the calculated digit sum into a string and appends it to the temporary array.
- **String Manipulation:** `strcpy()` updates the original string with the newly generated string.

## Complexity Analysis

Let `n` be the initial length of the string.

- **Time Complexity:** `O(n log_k n)` for `k > 1`. The string length decreases approximately by a factor of `k` after each iteration.
- **Space Complexity:** `O(n)` for the temporary character array.

## Example

**Input:**
```text
s = "11111222223", k = 3
```

**Transformation:**

```text
111 112 222 23
  3   4   6   5
       3465
```

**Output:**
```text
"3465"
```