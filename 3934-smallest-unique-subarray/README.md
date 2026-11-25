# 3934. Smallest Unique Subarray

[LeetCode Problem](https://leetcode.com/problems/smallest-unique-subarray/)

## Approach: Binary Search + Rolling Hash (Prefix Hashing)

### Problem Summary

Given an integer array `nums`, find the smallest subarray length such that at least one subarray of that length occurs exactly once.

Instead of storing and comparing every subarray directly, we use **Rolling Hash** to represent each subarray with a single integer.

We then use binary search to find the smallest length that satisfies the condition.

---

### 1. Why Rolling Hash?

A straightforward brute-force approach would generate every subarray of a particular length and compare them to determine which ones are unique.

However, storing complete subarrays or converting them into enormous numbers is inefficient.

For example:

```text
[1, 2, 3] -> 123
[2, 3, 4] -> 234
```

This encoding works conceptually, but the resulting numbers become extremely large as the subarray length increases.

Rolling Hash solves this problem by converting a sequence into a fixed-size integer using modular arithmetic.

Instead of storing the entire subarray, we store its hash value.

This allows us to compare subarrays using integers rather than repeatedly comparing their elements.

### 2. Understanding Polynomial Hashing

We can represent an array using a polynomial expression.

For a subarray `[a, b, c]`, its hash before applying modulo is:

```text
Hash = a * BASE^2 + b * BASE + c
```

For example, using `BASE = 10`:

```text
[1, 2, 3]

Hash = 1 * 10^2 + 2 * 10^1 + 3
     = 123
```

Similarly:

```text
[2, 3, 4]

Hash = 2 * 10^2 + 3 * 10^1 + 4
     = 234
```

Each element occupies a different positional weight, allowing the sequence to be represented by one number.

#### Why do we use BASE = 10007?

The base determines the positional weights assigned to the elements.

We choose a base that is larger than the maximum possible element value. This helps ensure that different sequences have different polynomial representations before applying modulo.

In this solution:

```python
BASE = 10007
```

The maximum element value in the problem is smaller than this base.

A larger base is not strictly necessary for modular hashing, but choosing a suitable base helps avoid ambiguity in the underlying polynomial representation.

#### Why do we use MOD = 10^9 + 7?

Without modulo, polynomial hash values can become extremely large.

We use:

```python
MOD = 10**9 + 7
```

This is a commonly used large prime number.

After applying modulo, every hash value stays within this range:

```text
0 <= hash < MOD
```

This keeps our hash values manageable and allows us to use them as dictionary keys.

**Important:** Modular hashing can produce collisions, meaning two different subarrays can theoretically have the same hash. A large prime modulus makes collisions unlikely but does not eliminate them completely.

---

### 3. Prefix Hashing

Calculating the hash of every subarray from scratch would be inefficient.

Instead, we calculate prefix hashes so that we can obtain the hash of any subarray in O(1) time.

We maintain two arrays:

```python
h = [0] * (n + 1)
prefix = [0] * (n + 1)

prefix[0] = 1
```

- `h[i]` stores the hash of the first `i` elements.
- `prefix[i]` stores `BASE^i % MOD`.

We calculate both arrays in one pass:

```python
for i in range(n):
    h[i + 1] = (h[i] * BASE + nums[i]) % MOD
    prefix[i + 1] = prefix[i] * BASE % MOD
```

#### Example

Consider:

```python
nums = [1, 2, 3, 4]
BASE = 10
MOD = 10**9 + 7
```

The resulting arrays are:

```text
h      = [0, 1, 12, 123, 1234]
prefix = [1, 10, 100, 1000, 10000]
```

For example:

```text
h[3] = 123
```

This represents the hash of `[1, 2, 3]`.

And:

```text
prefix[2] = 100
```

This represents BASE^2.

### 4. Extracting the Hash of Any Subarray

This is the most important part of prefix hashing.

Suppose we want the hash of:

```python
nums[1:3]  # [2, 3]
```

We already have:

```text
h[3] = 123
h[1] = 1
prefix[2] = 100
```

The prefix hash contains the contribution of the elements before our desired subarray.

We remove that contribution using:

```text
subarray_hash = h[r] - h[l] * BASE^(r-l)
```

After applying modulo:

```text
subarray_hash = (h[r] - h[l] * prefix[r-l]) % MOD
```

Substituting our example:

```text
subarray_hash = 123 - (1 * 100)
              = 23
```

The result is exactly the polynomial hash of `[2, 3]`.

In our implementation:

```python
key = (h[j] - h[i] * prefix[l] % MOD + MOD) % MOD
```

Here:

- `i` is the starting index.
- `j` is the ending index (exclusive).
- `l` is the subarray length.

We use `+ MOD` before the final modulo to ensure the intermediate value is non-negative.

This allows us to calculate any subarray hash in constant time without iterating through its elements.

---

### 5. How Rolling Hash Works

Rolling Hash allows us to reuse information from one window when moving to the next.

Consider:

```text
[1, 2, 3]
[2, 3, 4]
[3, 4, 5]
```

When moving from `[1, 2, 3]` to `[2, 3, 4]`:

1. Remove the contribution of the first element.
2. Shift the remaining elements one position to the left in the polynomial representation.
3. Add the new element at the end.
4. Apply modulo.

The transition formula is:

```text
new_hash = (old_hash - outgoing * BASE^(length-1))
           * BASE + incoming
```

Then apply modulo.

Our implementation uses prefix hashing instead of explicitly updating the previous window's hash.

Both techniques belong to the rolling hash family.

The advantage of prefix hashing is that we can calculate the hash of any window directly in O(1) time, even without knowing the previous window's hash.

---

### 6. Checking Whether a Length Works

Once prefix hashes are available, checking a particular subarray length becomes straightforward.

```python
def check(l):
    count = defaultdict(int)

    for i in range(n-l+1):
        j = i+l
        key = (h[j] - h[i] * prefix[l] % MOD + MOD) % MOD
        count[key] += 1

    for c in count.values():
        if c == 1:
            return True

    return False
```

We use a dictionary to count the frequency of every subarray hash.

For a given length:

1. Generate the hash of every possible window.
2. Increase its frequency in the dictionary.
3. Check whether any hash appears exactly once.

If any hash has frequency `1`, that means we found a unique subarray of the given length.

Therefore, the length satisfies the condition.

---

### 7. Why Binary Search?

We need the smallest length for which at least one unique subarray exists.

The important observation is that the condition is monotonic.

If a subarray of length `L` occurs exactly once, extending it by one element produces a longer subarray that can also occur only once.

This means:

- If a length works, every longer length also works.
- If a length does not work, every shorter length also does not work.

For example:

```text
Length:  1  2  3  4  5  6
Works:   F  F  T  T  T  T
```

This is exactly the kind of condition where binary search is useful.

Instead of checking every possible length, we repeatedly check the middle length and narrow our search.

```python
low, high = 1, n

while low < high:
    mid = (low + high) // 2

    if check(mid):
        high = mid
    else:
        low = mid + 1

return low
```

If `check(mid)` returns `True`, we know the answer could be smaller, so we move `high` to `mid`.

Otherwise, we need a larger length, so we move `low` to `mid + 1`.

When `low == high`, we have found the smallest valid length.

---

### 8. Complete Python Solution

```python
from collections import defaultdict
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        BASE = 10007

        n = len(nums)

        h = [0] * (n + 1)
        prefix = [0] * (n + 1)
        prefix[0] = 1

        # Calculate prefix hashes and powers of BASE
        for i in range(n):
            h[i + 1] = (h[i] * BASE + nums[i]) % MOD
            prefix[i + 1] = prefix[i] * BASE % MOD

        def check(l):
            count = defaultdict(int)

            # Calculate the hash of every window of length l
            for i in range(n - l + 1):
                j = i + l

                key = (h[j] - h[i] * prefix[l] % MOD + MOD) % MOD
                count[key] += 1

            # Check if at least one hash appears exactly once
            for c in count.values():
                if c == 1:
                    return True

            return False

        # Binary search for the smallest valid length
        low, high = 1, n

        while low < high:
            mid = (low + high) // 2

            if check(mid):
                high = mid
            else:
                low = mid + 1

        return low
```

---

### 9. Complexity Analysis

Let `n` be the length of the input array.

| Operation | Time Complexity |
|---|---|
| Building prefix hashes | O(n) |
| Building BASE powers | O(n) |
| Checking one length | O(n) |
| Binary search | O(log n) checks |
| Overall | O(n log n) |

**Time Complexity: O(n log n)**

Each binary search iteration calls `check()`, which processes every possible window in O(n) time.

There are O(log n) binary search iterations.

**Space Complexity: O(n)**

We store:

- Prefix hash array: O(n)
- Powers array: O(n)
- Frequency dictionary: O(n)

---

### Key Takeaways

- **Polynomial Hashing:** Represents an entire sequence using a single integer.
- **BASE:** Determines the positional weights of elements in the polynomial.
- **MOD:** Keeps hash values bounded and manageable.
- **Prefix Hashing:** Allows us to calculate the hash of any subarray in O(1).
- **Rolling Hash:** Reuses hash information when moving between overlapping windows.
- **Binary Search:** Finds the smallest valid subarray length because the condition is monotonic.

This problem is a good example of combining two independent techniques: binary search on the answer and rolling hash for efficient subarray comparison.