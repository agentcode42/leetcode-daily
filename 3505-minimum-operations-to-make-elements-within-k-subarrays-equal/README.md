# 3505. Minimum Operations to Make Elements Within K Subarrays Equal

[LeetCode Problem](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/)

## Problem Summary

Given an integer array `nums` and two integers `x` and `k`, we can increase or decrease any element by 1 in one operation.

We need to find the minimum number of operations required to make at least `k` non-overlapping subarrays of exactly `x` elements, where all elements within each selected subarray are equal.

The key observations are:

1. The minimum cost to make all elements in a window equal is obtained by choosing its median.
2. We can maintain the median and the sum of elements on both sides using two sorted lists.
3. After calculating the cost of every possible window, we can use Dynamic Programming to select `k` non-overlapping windows with minimum total cost.

## Intuition

### 1. Making a Window Equal Using Its Median

For any window, the minimum number of operations required to make all its elements equal is achieved by changing every element to the median.

For example:

```python
window = [1, 3, 2, 6, 4]

sorted_window = [1, 2, 3, 4, 6]
median = 3
```

The number of operations required is:

```text
|1 - 3| + |2 - 3| + |3 - 3| + |4 - 3| + |6 - 3|

= 2 + 1 + 0 + 1 + 3

= 7
```

We could sort every window independently and calculate its median, but that would be inefficient.

Instead, we maintain a sliding window using two SortedLists.

### 2. Maintaining the Sliding Window Median

We divide the current window into two sorted lists:

- `left`: Contains the smaller half of the elements, including the median.
- `right`: Contains the larger half of the elements.

We maintain two important conditions:

```text
len(left) = (x + 1) // 2

Maximum element in left <= Minimum element in right
```

Since `left` contains the smaller half, its last element is always the median:

```python
mid = left[-1]
```

We also maintain the sums of both lists:

```python
left_sum = sum(left)
right_sum = sum(right)
```

Whenever the window slides, we add the incoming element, remove the outgoing element, and rebalance the two lists.

This allows us to maintain the median without sorting the entire window again.

### 3. Calculating the Window Cost in O(1)

Once we have the median and the sums of both halves, we can calculate the minimum operations without iterating through the window.

For the left half, every element is less than or equal to the median.

Therefore:

```text
Left cost = mid * len(left) - left_sum
```

For the right half, every element is greater than or equal to the median.

Therefore:

```text
Right cost = right_sum - mid * len(right)
```

Combining both:

```text
moves = (mid * len(left) - left_sum)
        + (right_sum - mid * len(right))
```

This gives us the minimum cost of making the current window equal in O(1).

We calculate and store the cost of every possible window in the `costs` array.

### 4. Choosing K Non-Overlapping Windows Using DP

After calculating all window costs, we need to select `k` non-overlapping windows with minimum total cost.

Let:

```text
dp[i][j] = minimum operations required to select
           exactly j non-overlapping windows
           using the first i elements.
```

At every position, we have two choices.

**Option 1: Skip the current position**

We don't select a window ending at the current position.

```text
dp[i][j] = dp[i-1][j]
```

**Option 2: Select a window ending at the current position**

A window ending at index `i-1` starts at index `i-x`.

Its cost is:

```python
costs[i-x]
```

Since the selected windows cannot overlap, the previous windows must come from the first `i-x` elements.

Therefore:

```text
take = dp[i-x][j-1] + costs[i-x]
```

We choose the option with the smaller cost:

```text
dp[i][j] = min(skip, take)
```

The complete recurrence is:

```text
dp[i][j] = min(
    dp[i-1][j],
    dp[i-x][j-1] + costs[i-x]
)
```

We only consider the second option when `i >= x`.

Since the problem asks for at least `k` windows, selecting exactly `k` is sufficient. Additional windows cannot reduce the total operations because all window costs are non-negative.

## Approach

1. Initialize two SortedLists, `left` and `right`, with the first window.
2. Maintain the median in `left[-1]` and the sums of both lists.
3. Calculate the minimum operations for the current window using the median and the two sums.
4. Slide the window by adding the incoming element and removing the outgoing element.
5. Rebalance the two lists to maintain the median and size conditions.
6. Store the minimum cost of every window in `costs`.
7. Use a 2D DP table to select exactly `k` non-overlapping windows with minimum total cost.
8. Return `dp[n][k]`.

## Code

```python

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        left  = SortedList(nums[:x])
        right  = SortedList()

        while len(left)>(x+1)//2:
            right.add(left.pop())
        
        left_sum = sum(left)
        right_sum = sum(right)

        def add(num):
            nonlocal left_sum ,right_sum

            if num<=left[-1]:
                left.add(num)
                left_sum+=num
            else:
                right.add(num)
                right_sum+=num

        def remove(num):
            nonlocal left_sum ,right_sum

            if num in left:
                left.remove(num)
                left_sum-=num
            else:
                right.remove(num)
                right_sum-=num
        def balance():
            nonlocal left_sum ,right_sum

            while len(left)>(x+1)//2:
                val = left.pop()
                left_sum-=val
                right.add(val)
                right_sum+=val
            
            while len(left)<(x+1)//2:
                val = right.pop(0)
                right_sum-=val
                left.add(val)
                left_sum+=val
                
        costs = []

        for i in range(n-x+1):
            mid = left[-1]

            moves = (mid*len(left) - left_sum) + (right_sum - mid*len(right))
            costs.append(moves)

            if i<n-x:
                add(nums[i+x])
                remove(nums[i])
                balance()
        
        dp = [[float('inf')]*(k+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=0
        for i in range(1,n+1):
            for j in range(1,k+1):
                dp[i][j]=dp[i-1][j]
                if i>=x:
                    take = dp[i-x][j-1] + costs[i-x]
                    dp[i][j]=min(dp[i][j],take)
        return dp[n][k]

```

*Note: This implementation uses `SortedList` from the `sortedcontainers` package.*

## Complexity Analysis

Let:

- `n` = length of the input array.
- `x` = size of each window.
- `k` = number of non-overlapping windows required.

**Sliding Window Median:**

- Adding an element: O(log x)
- Removing an element: O(log x)
- Rebalancing the lists: O(log x)
- Calculating the window cost: O(1)

We process all windows in O(n log x).

**Dynamic Programming:**

We have `n * k` DP states, and each state requires O(1) work.

Time complexity: O(nk).

**Overall Time Complexity:**

```text
O(n log x + nk)
```

**Space Complexity:**

- Two SortedLists: O(x)
- Window costs: O(n)
- DP table: O(nk)

Overall space complexity:

```text
O(nk + n + x) = O(nk)
```

## Key Takeaways

- The median minimizes the sum of absolute differences.
- Two SortedLists allow us to maintain a sliding window median efficiently.
- Maintaining the sums of both halves makes calculating the window cost O(1).
- Dynamic Programming helps select non-overlapping windows without trying every possible combination.
- Combining Sliding Window Median with DP gives an efficient solution to this problem.