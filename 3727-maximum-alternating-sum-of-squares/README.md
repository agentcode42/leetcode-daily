# 3727. Maximum Alternating Sum of Squares

**LeetCode Problem:** [Maximum Alternating Sum of Squares](https://leetcode.com/problems/maximum-alternating-sum-of-squares/)  
**Difficulty:** Medium  
**Topics:** Array, Greedy, Sorting, Counting

## Problem Summary

You are given an integer array `nums`. You can rearrange its elements in any order to maximize the alternating sum of their squares.

The score is calculated as:

`score = arr[0]² - arr[1]² + arr[2]² - arr[3]² + ...`

Return the maximum possible score after rearranging the array.

### Example

**Input:**
```text
nums = [1, 2, 3]
```

**Output:**
```text
12
```

**Explanation:**

Arrange the elements as `[2, 1, 3]`.

The alternating score is:

`2² - 1² + 3² = 4 - 1 + 9 = 12`

## Approach 1: Greedy + Sorting (Python)

### Intuition

The key observation is that only the squares of the numbers matter. The original signs of the numbers do not affect their squared values.

Even-indexed positions contribute positively, while odd-indexed positions contribute negatively.

To maximize the score, we should place the **largest squares in positive positions** and the **smallest squares in negative positions**.

Instead of rearranging the original numbers, we can square every element and sort the resulting array in ascending order.

### Algorithm

1. Square every element in `nums`.
2. Sort the squared values in ascending order.
3. Calculate `n // 2` to determine how many elements should contribute negatively.
4. Subtract the sum of the smallest `n // 2` squares from the sum of the remaining squares.
5. Return the result.

### Python Solution

```python
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            nums[i] = nums[i] ** 2

        nums.sort()

        return sum(nums[n // 2:]) - sum(nums[:n // 2])
```

### Complexity Analysis

- **Time Complexity:** `O(n log n)` — Squaring the elements takes `O(n)`, sorting takes `O(n log n)`, and calculating the sums takes `O(n)`.
- **Space Complexity:** `O(n)` — Python's sorting implementation can require additional memory, and slicing creates temporary lists.

Here, `n` is the length of the input array.

## Approach 2: Greedy + Frequency Array (C)

### Intuition

The sorting approach works well, but the constraints provide another opportunity for optimization.

Every element satisfies:

`-40000 <= nums[i] <= 40000`

Since squaring removes the sign, we only need the absolute values of the elements.

Instead of sorting, we can use a **frequency array** to count how many times each absolute value appears.

By processing the frequency array from smallest to largest, we effectively process the squared values in ascending order without explicitly sorting them.

We subtract the smallest `n // 2` squares and add all the remaining squares.

### Algorithm

1. Create a frequency array of size `40001`.
2. Count the occurrences of `abs(nums[i])` for every element.
3. Set `k = numsSize / 2` to determine how many of the smallest squares must be subtracted.
4. Iterate through the frequency array from `0` to `40000`.
5. For each occurrence, calculate its square:
   - If fewer than `k` elements have been processed, subtract the square from the score.
   - Otherwise, add the square to the score.
6. Return the final score.

We use `long long` for the squared values and the score to avoid integer overflow.

### C Solution

```c
long long maxAlternatingSum(int* nums, int numsSize) {
    int max_val = 40000;
    int freq[40001] = {0};

    for (int i = 0; i < numsSize; i++) {
        freq[abs(nums[i])]++;
    }

    long long score = 0;
    int processed = 0;
    int k = numsSize / 2;

    for (int i = 0; i <= max_val; i++) {
        while (freq[i] > 0) {
            long long sq = (long long)i * i;

            if (processed < k) {
                score -= sq;
            } else {
                score += sq;
            }

            processed++;
            freq[i]--;
        }
    }

    return score;
}
```

### Complexity Analysis

Let `n` be the number of elements and `M = 40001` be the frequency array size.

- **Time Complexity:** `O(n + M)` — Counting the elements takes `O(n)`, scanning the frequency array takes `O(M)`, and processing all occurrences takes `O(n)`.
- **Space Complexity:** `O(M)` — The frequency array stores counts for all possible absolute values.

Since the value range is bounded, this approach avoids comparison-based sorting and runs in linear time with respect to the input size and value range.

## Key Takeaway

The greedy insight is the same in both solutions: **subtract the smallest half of the squared values and add the remaining largest half.**

Python uses sorting to arrange the squared values. C uses a frequency array to process them in ascending order without explicitly sorting.

The frequency-array approach is particularly effective when the input values come from a known, limited range.