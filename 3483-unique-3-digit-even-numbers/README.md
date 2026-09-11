# 3483. Unique 3-Digit Even Numbers

## Problem

You are given an array of digits. Find the number of **distinct three-digit even numbers** that can be formed using these digits.

Each copy of a digit can only be used once in a number, and numbers cannot have a leading zero.

### Example

```text
Input: digits = [1,2,3,4]

Output: 6
```

The valid numbers are:

```text
124, 132, 134, 142, 234, 324
```

---

## Approach

Since we only need to form a **three-digit number**, brute force is enough.

A three-digit even number:

* Must start from `100`
* Must end in an even digit
* Can be at most `998`

Therefore, there are only:

```text
450
```

possible three-digit even numbers to check.

Instead of generating permutations of the input, we simply generate every possible three-digit even number and check whether its three digits are available in the input.

### Step 1: Count the available digits

Use `Counter` to store how many copies of each digit are available.

```python
count = Counter(digits)
```

This is important because the same digit may appear multiple times, but each copy can only be used once per number.

### Step 2: Generate every possible candidate

```python
for n in range(100, 1000, 2):
```

This automatically guarantees:

* `n` has three digits
* `n` is even

### Step 3: Extract the three digits

```python
a = n % 10
b = (n // 10) % 10
c = n // 100
```

Here:

* `a` = units digit
* `b` = tens digit
* `c` = hundreds digit

### Step 4: Check whether the digits are available

Before using a digit, check its remaining frequency.

When a digit is used, temporarily decrease its count:

```python
count[a] -= 1
```

Then check the next digit.

After checking the candidate, restore the counts so the next candidate starts with the original frequencies.

This correctly handles repeated digits such as:

```text
[2, 2, 8]
```

where `228` is valid because there are two copies of `2`.

---

## Code

```python
from collections import Counter

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = Counter(digits)
        res = 0

        for n in range(100, 1000, 2):
            a = n % 10
            b = (n // 10) % 10
            c = n // 100

            if count[a] > 0:
                count[a] -= 1

                if count[b] > 0:
                    count[b] -= 1

                    if count[c] > 0:
                        res += 1

                    count[b] += 1

                count[a] += 1

        return res
```

## Complexity

Let `n` be the length of the input array.

### Time: `O(n)`

* Building the `Counter` takes `O(n)`.
* There are only **450** possible three-digit even numbers to check.
* Each `Counter` lookup is `O(1)` on average.

Therefore:

```text
O(n + 450) = O(n)
```

### Space: `O(1)`

There are only 10 possible digits (`0` through `9`), so the `Counter` contains at most 10 entries.

---

## Key Takeaway

This problem is a good example of **not overcomplicating a small search space**.

It is possible to think about combinations and digit frequencies mathematically, but the constraints make that unnecessary.

There are only **450 candidates**, so simply checking every possible three-digit even number is fast, simple, and easy to verify.
