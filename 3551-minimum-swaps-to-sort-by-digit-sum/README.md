# 3551. Minimum Swaps to Sort by Digit Sum — Solution Journey

[LeetCode Problem Link](https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/)

## 1. Problem Summary

We are given an array `nums` containing distinct positive integers.

Our task is to sort the array using the following rules:

1. Sort numbers in increasing order of their **digit sum**.
2. If two numbers have the same digit sum, place the smaller number first.
3. Return the **minimum number of swaps** needed to transform the original array into this sorted order.

A swap means exchanging the values at two different positions.

### Example

**Input:**
```python
nums = [18, 43, 34, 16]
```

Calculate the digit sum of every number:

- `18` → 1 + 8 = 9
- `43` → 4 + 3 = 7
- `34` → 3 + 4 = 7
- `16` → 1 + 6 = 7

Numbers with a smaller digit sum must appear first. When digit sums are equal, the smaller number comes first.

Therefore, the target array is:

```python
[16, 34, 43, 18]
```

We need to transform the original array into this order using the fewest swaps.

**Output:**
```python
2
```

---

## 2. Intuition: Put Each Number in Its Correct Position

The first important observation is that we do not need to invent a new sorting rule. Python can sort the numbers using a tuple containing their digit sum and their actual value.

```python
sorted_nums = sorted(nums, key=lambda x: (digit_sums(x), x))
```

Python compares tuples from left to right:

- First, it compares digit sums.
- If the digit sums are equal, it compares the numbers themselves.

This gives us the exact target order.

However, sorting alone does not tell us the minimum number of swaps needed to reach that order.

We need a way to find each target number's current position quickly.

### The key idea: Track the current index of every number

We build a dictionary called `index`:

```python
index = {}

for i, num in enumerate(nums):
    index[num] = i
```

For example, with:

```python
nums = [18, 43, 34, 16]
```

The dictionary initially contains:

| Number | Current index |
|---:|---:|
| 18 | 0 |
| 43 | 1 |
| 34 | 2 |
| 16 | 3 |

Now, whenever we need a number at a particular position, we can find its current location in approximately constant time using `index[curr]`.

After every swap, we update the dictionary so it always reflects the current positions.

**The main strategy is simple:** Move the required number directly into its correct position instead of swapping numbers randomly.

---

## 3. Approach: Step by Step

### Step 1: Calculate the digit sum

We create a helper function that extracts the last digit, adds it to the running sum, and removes that digit using integer division.

```python
def digit_sums(x):
    s = 0

    while x > 0:
        s += x % 10
        x = x // 10

    return s
```

For example, if `x = 583`:

1. `583 % 10 = 3`, so the sum becomes 3.
2. `583 // 10 = 58`.
3. `58 % 10 = 8`, so the sum becomes 11.
4. `58 // 10 = 5`.
5. `5 % 10 = 5`, so the sum becomes 16.
6. `5 // 10 = 0`, so the loop ends.

The digit sum of `583` is `16`.

### Step 2: Build the target sorted array

```python
sorted_nums = sorted(nums, key=lambda x: (digit_sums(x), x))
```

For our example:

```python
nums       = [18, 43, 34, 16]
sorted_nums = [16, 34, 43, 18]
```

The original array tells us where each number starts. The sorted array tells us where each number should end up.

### Step 3: Record the original positions

```python
index = {}

for i, num in enumerate(nums):
    index[num] = i
```

We use a dictionary because looking up a number's current index is much faster than scanning the entire array each time.

At this point:

```python
index = {
    18: 0,
    43: 1,
    34: 2,
    16: 3
}
```

### Step 4: Visit each target position

```python
res = 0

for i, curr in enumerate(sorted_nums):
    idx = index[curr]

    if idx == i:
        continue
```

Here:

- `i` is the position we are trying to fill.
- `curr` is the number that belongs at position `i`.
- `idx` is the number's current position in the changing `nums` array.

If `idx == i`, the correct number is already in place. We skip it.

Otherwise, we swap the number at the current position with the number we need.

### Step 5: Swap and update the dictionary

```python
displaced = nums[i]

nums[i], nums[idx] = nums[idx], nums[i]

index[curr] = i
index[displaced] = idx

res += 1
```

Why do we need to update the dictionary?

Suppose `curr` is at index `3`, but it belongs at index `0`. After swapping, `curr` moves to index `0`, while the number previously at index `0` moves to index `3`.

Therefore, we update the locations of **both numbers**.

Each swap places the required number at its correct position, and we count that swap in `res`.

After all positions have been processed, `res` contains the minimum number of swaps.

---

## 4. Complete Python Solution

```python
class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def digit_sums(x):
            s = 0

            while x > 0:
                s += x % 10
                x = x // 10

            return s

        sorted_nums = sorted(
            nums,
            key=lambda x: (digit_sums(x), x)
        )

        index = {}

        for i, num in enumerate(nums):
            index[num] = i

        res = 0

        for i, curr in enumerate(sorted_nums):
            idx = index[curr]

            if idx == i:
                continue

            displaced = nums[i]

            nums[i], nums[idx] = nums[idx], nums[i]

            index[curr] = i
            index[displaced] = idx

            res += 1

        return res
```

---

## 5. Step-by-Step Examples

### Example 1: One swap is enough

**Input:**
```python
nums = [37, 100]
```

**Step 1: Calculate digit sums**

| Number | Digit sum |
|---:|---:|
| 37 | 10 |
| 100 | 1 |

Because `100` has the smaller digit sum, it must come first.

```python
Original: [37, 100]
Target:   [100, 37]
```

**Step 2: Process the target array**

At position `0`, the required number is `100`.

- Current position of `100`: index `1`.
- Required position: index `0`.
- The positions are different, so we swap `37` and `100`.

```python
Before swap: [37, 100]
After swap:  [100, 37]
```

The target array has been reached.

**Output:**
```python
1
```

Only one swap is required.

### Example 2: The array is already sorted

**Input:**
```python
nums = [22, 14, 33, 7]
```

Calculate the digit sums:

| Number | Digit sum |
|---:|---:|
| 22 | 4 |
| 14 | 5 |
| 33 | 6 |
| 7 | 7 |

The digit sums are already in increasing order.

```python
Original: [22, 14, 33, 7]
Target:   [22, 14, 33, 7]
```

Now process each position:

| Position | Required number | Current index | Action |
|---:|---:|---:|---|
| 0 | 22 | 0 | Already correct |
| 1 | 14 | 1 | Already correct |
| 2 | 33 | 2 | Already correct |
| 3 | 7 | 3 | Already correct |

Every required number is already in its correct position. The loop skips every element without performing any swaps.

**Output:**
```python
0
```

This example shows why we check `if idx == i` before swapping.

### Example 3: Two swaps are required

**Input:**
```python
nums = [18, 43, 34, 16]
```

The digit sums are:

| Number | Digit sum |
|---:|---:|
| 18 | 9 |
| 43 | 7 |
| 34 | 7 |
| 16 | 7 |

The three numbers with digit sum `7` must appear in increasing numerical order.

```python
Original: [18, 43, 34, 16]
Target:   [16, 34, 43, 18]
```

**Initial index dictionary:**

```python
{
    18: 0,
    43: 1,
    34: 2,
    16: 3
}
```

**Swap 1: Put `16` at index `0`**

The first target number is `16`.

```python
i = 0
curr = 16
idx = index[16]  # 3
```

`16` belongs at index `0`, but it is currently at index `3`.

Swap `nums[0]` and `nums[3]`:

```python
Before: [18, 43, 34, 16]
After:  [16, 43, 34, 18]
```

Now update the dictionary:

```python
index[16] = 0
index[18] = 3
```

The swap count becomes `1`.

**Swap 2: Put `34` at index `1`**

The next target number is `34`.

```python
i = 1
curr = 34
idx = index[34]  # 2
```

`34` belongs at index `1`, but it is currently at index `2`.

Swap `nums[1]` and `nums[2]`:

```python
Before: [16, 43, 34, 18]
After:  [16, 34, 43, 18]
```

Update the dictionary:

```python
index[34] = 1
index[43] = 2
```

The swap count becomes `2`.

**Finish the remaining positions**

- At index `2`, `43` is already in place.
- At index `3`, `18` is already in place.

No more swaps are needed.

The final array is:

```python
[16, 34, 43, 18]
```

**Output:**
```python
2
```

This example demonstrates the main advantage of the dictionary: after each swap, we can immediately locate the next required number without searching the array again.

### Example 4: The digit sums are equal

**Input:**
```python
nums = [21, 12, 3]
```

All three numbers have a digit sum of `3`:

- `21` → 2 + 1 = 3
- `12` → 1 + 2 = 3
- `3` → 3

When the digit sums are equal, the smaller number must come first.

Therefore:

```python
Original: [21, 12, 3]
Target:   [3, 12, 21]
```

At index `0`, we need `3`, which is currently at index `2`.

Swap `21` and `3`:

```python
Before: [21, 12, 3]
After:  [3, 12, 21]
```

The entire array is now sorted.

**Output:**
```python
1
```

This example demonstrates why the sorting key must contain both `digit_sums(x)` and `x`. Sorting only by digit sum would not enforce the required tie-breaking rule.

---

## 6. Why Does This Approach Work?

There are three important ideas behind the solution.

**1. We identify the exact target order.**

Sorting by `(digit_sums(x), x)` handles both the primary sorting rule and the tie-breaker.

**2. We place each required number directly.**

When the required number is not at position `i`, we locate it using `index[curr]` and swap it into position `i`. This avoids unnecessary searching and random swaps.

**3. We keep every index updated.**

After a swap, we update the dictionary entries for both affected numbers. That ensures the next lookup points to the number's current position, not its original position.

Because all input numbers are distinct, each number has a unique dictionary entry. Once a position is processed, its correct number stays there while later positions are fixed.

The algorithm uses the fewest possible swaps for the resulting permutation: each swap moves a required number directly into its correct position, rather than taking extra intermediate steps.

---
## Why Does This Algorithm Use the Minimum Number of Swaps?

To prove optimality, we need to show two things:

1. Our algorithm uses a certain number of swaps.
2. No other strategy can sort the array using fewer swaps.

### 1. Think of the target array as the correct arrangement

Consider:

```python
nums = [30, 10, 20]
target = [10, 20, 30]
```

Every number has a specific destination:

- `10` belongs at index `0`.
- `20` belongs at index `1`.
- `30` belongs at index `2`.

The original array has a cycle of misplaced elements:

- `30` belongs at index `2`.
- `20` belongs at index `1`.
- `10` belongs at index `0`.

More formally, the elements form a **cycle of length 3**: each element needs to move to a position occupied by another element in that same cycle.

### 2. A cycle of length \(k\) requires at least \(k-1\) swaps

Consider the example above.

Initially:

```python
[30, 10, 20]
```

**Swap 1:** Move `10` directly to index `0`.

```python
[10, 30, 20]
```

**Swap 2:** Move `20` to index `1`.

```python
[10, 20, 30]
```

The cycle is now completely resolved.

We used two swaps, which is:

\[
k-1=3-1=2
\]

Why can't one swap solve this cycle? Because one swap exchanges only two elements, but this cycle requires all three elements to reach their respective destinations. For a cycle of length \(k\), the minimum is \(k-1\) swaps.

### 3. Why does our algorithm achieve that minimum?

At each index `i`, our algorithm finds the number that belongs there:

```python
curr = sorted_nums[i]
idx = index[curr]
```

If the number is already at index `i`, no swap is needed.

Otherwise, we swap it directly into its correct position:

```python
nums[i], nums[idx] = nums[idx], nums[i]
```

This breaks the active permutation cycle into smaller cycles, fixing at least one additional position in the process. Repeating this operation resolves a cycle of length \(k\) in exactly \(k-1\) swaps.

The dictionary is crucial because it lets us find the required number's current position and keep track of both elements after every swap.

### 4. What if the array contains multiple cycles?

Each cycle can be solved independently.

Suppose the target permutation contains cycles of lengths \(3\) and \(2\).

The first cycle needs:

\[
3-1=2\text{ swaps}
\]

The second cycle needs:

\[
2-1=1\text{ swap}
\]

Therefore, the total minimum is:

\[
(3-1)+(2-1)=3\text{ swaps}
\]

In general, if the permutation contains \(c\) cycles among \(n\) elements, including cycles of length one for elements already in the correct position, the minimum number of swaps is:

\[
\boxed{n-c}
\]

### Final proof

Any permutation can be decomposed into disjoint cycles. A cycle of length \(k\) requires at least \(k-1\) swaps, and our algorithm resolves that cycle using exactly \(k-1\) swaps. Since the cycles are independent, adding their minimum swap counts gives the global minimum.

Therefore, **our algorithm uses the minimum possible number of swaps to transform the original array into the required sorted order.**

## 7. Complexity Analysis

Let:

- \(n\) = number of elements in `nums`.
- \(d\) = maximum number of digits in any number.

### Time Complexity: \(O(n \log n)\)

We can break down the work into four parts.

**Step 1: Calculate digit sums — \(O(nd)\)**

The `digit_sums()` function processes one digit per loop iteration. For a number with \(d\) digits, the function takes \(O(d)\) time.

Python's `sorted()` computes the key once per element, so calculating digit sums for all numbers takes \(O(nd)\) time.

**Step 2: Sort the array — \(O(n \log n)\)**

Python sorts the numbers using the tuple `(digit_sums(x), x)` as the key.

Sorting \(n\) elements takes \(O(n \log n)\) time.

**Step 3: Build the index dictionary — \(O(n)\)**

We visit every element once and store its current position. Dictionary insertion takes \(O(1)\) time on average, so this step takes \(O(n)\) time.

**Step 4: Process and swap elements — \(O(n)\)**

We visit the sorted array once. For each element, we perform a constant number of average-case dictionary lookups, updates, and possibly one swap.

This step takes \(O(n)\) time.

Combining the costs gives:

\[
O(nd+n\log n+n+n)
\]

Therefore:

\[
\boxed{O(n\log n+nd)}
\]

Under the given constraints, each number is at most \(10^9\), so it has at most 10 digits. That makes \(d\) bounded by a small constant.

The overall time complexity is therefore:

\[
\boxed{O(n\log n)}
\]

### Space Complexity: \(O(n)\)

**Step 1: The sorted array — \(O(n)\)**

`sorted_nums` stores a separate ordered copy containing all \(n\) elements.

**Step 2: The index dictionary — \(O(n)\)**

The `index` dictionary stores one entry for every distinct number.

**Step 3: The digit-sum function — \(O(1)\) auxiliary space**

The function uses only a few variables, such as `s` and `x`. It does not create a separate list of digits.

The sorting operation may also use additional temporary memory, but its space requirement does not change the overall linear bound here.

Combining the auxiliary storage:

\[
O(n)+O(n)+O(1)
\]

Therefore, the overall space complexity is:

\[
\boxed{O(n)}
\]

### Final Complexity

| Complexity | Result |
|---|---|
| Time | \(O(n \log n)\) |
| Space | \(O(n)\) |

**Final takeaway:** Sort once to determine the target order, use a dictionary to find each number's current position, and update that dictionary after every swap. This gives us an efficient way to place each number correctly while keeping the total number of swaps to a minimum.