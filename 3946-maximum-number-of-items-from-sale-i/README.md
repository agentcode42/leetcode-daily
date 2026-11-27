# 3946. Maximum Number of Items From Sale I

[LeetCode Problem Link](https://leetcode.com/problems/maximum-number-of-items-from-sale-i/)

## Problem Summary

We are given a list of items, where each item is represented as:

`[factor, price]`

We also have a limited budget.

When we purchase an item for the first time:

- We receive the purchased item.
- We receive one free copy of every other item whose factor is divisible by the purchased item's factor.
- Purchasing additional copies of the same item does not generate additional free copies.

Our goal is to maximize the total number of items obtained without exceeding the budget.

---

## Intuition

The key observation is that purchasing an item for the first time is different from purchasing additional copies.

Suppose we purchase an item with factor `f_i`.

It gives us one copy of every item whose factor satisfies:

`f_j % f_i == 0`

We can calculate how many total copies we receive from the first purchase of each item.

Let:

`free[i] = number of item factors divisible by items[i][0]`

This count includes the purchased item itself.

For example, consider:

```python
items = [
    [2, 4],
    [2, 3],
    [4, 5]
]
```

Purchasing either item with factor `2` gives us three copies:

- The purchased item.
- The other item with factor `2`.
- The item with factor `4`.

Purchasing the item with factor `4` gives us only one copy because no other factor is divisible by `4`.

The important detail is that different purchases can generate free copies of the same item. Every such copy counts toward the answer.

### Separating First Purchases and Additional Purchases

We can divide the problem into two parts:

1. First purchases: Each item type can generate its free-copy reward only once.
2. Additional purchases: Every subsequent purchase gives exactly one additional item.

For additional purchases, we should always choose the cheapest available item.

Therefore, after spending some budget on first purchases, we can use the remaining budget to buy as many additional copies as possible:

`remaining_budget // min_price`

This observation allows us to formulate the problem as a 0/1 Knapsack.

---

## Approach 1: DFS + Memoization (Top-Down DP)

### Idea

We initially solve the problem recursively.

First, we calculate the number of copies obtained from the first purchase of every item type.

Then we define:

`dfs(i, b)`

Where:

- `i` is the current item index.
- `b` is the remaining budget.

For every item, we have two choices.

**1. Skip the item**

Move to the next item without spending anything:

`skip = dfs(i + 1, b)`

**2. Purchase the item for the first time**

If we have enough budget, purchase it and collect its entire free-copy reward:

`take = free[i] + dfs(i + 1, b - price[i])`

We take the maximum of these two choices.

### Base Case

Once we have considered every item type, we can no longer collect any first-purchase bonuses.

We use the remaining budget to buy additional copies of the cheapest item:

`dfs(n, b) = b // min_price`

### Python Code

```python
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        free = [0] * n
        min_price = float('inf')

        for i in range(n):
            min_price = min(min_price, items[i][1])

            for j in range(n):
                if items[j][0] % items[i][0] == 0:
                    free[i] += 1

        @cache
        def dfs(i, b):
            if i == n:
                return b // min_price

            skip = dfs(i + 1, b)
            take = 0

            if items[i][1] <= b:
                take = free[i] + dfs(
                    i + 1,
                    b - items[i][1]
                )

            return max(take, skip)

        return dfs(0, budget)
```

### Why This Solution Exceeded Memory Limit

The recursive solution uses memoization with two state variables:

`(i, b)`

Here:

- `i` can have up to `n` different values.
- `b` can have up to `budget + 1` different values.

Therefore, the maximum number of memoized states is:

`O(n * budget)`

Although the time complexity is reasonable, Python's `@cache` stores every state in a dictionary, including its tuple key and associated value.

This creates significant memory overhead.

The problem is not our recurrence or our logic. It is the amount of memory required to store all the states.

We need a way to preserve the same DP transitions while reducing memory usage.

---

## Approach 2: 1D DP (Bottom-Up Knapsack)

### Idea

Instead of storing every combination of item index and remaining budget, we can process items one at a time using a single DP array.

Define:

`dp[b] = maximum number of items obtained using a budget of at most b`

Initially, every value is zero:

```python
dp = [0] * (budget + 1)
```

For each item, we calculate its first-purchase reward by counting how many item factors are divisible by its factor.

Let:

- `price` = cost of the first purchase.
- `count` = total copies obtained from the first purchase.

We have two choices:

1. Skip the item and retain the current DP value.
2. Purchase it for the first time, pay its price, and receive `count` copies.

The transition becomes:

`dp[b] = max(dp[b], dp[b - price] + count)`

### Why Iterate Backwards?

We iterate from `budget` down to `price`:

```python
for b in range(budget, price - 1, -1):
```

This is essential because we are solving a 0/1 Knapsack problem.

Each item type can contribute its first-purchase reward only once.

If we iterate forwards, an updated DP state could be reused during the same item iteration, allowing us to collect the first-purchase reward multiple times.

Backward iteration prevents this.

### Handling Additional Purchases

After processing every item type, `dp[b]` represents the maximum number of items obtained from first purchases using at most budget `b`.

The remaining budget is:

`budget - b`

We can spend it on additional copies of the cheapest item.

The number of additional copies is:

`(budget - b) // min_price`

Therefore, our final answer is:

```python
max(
    dp[b] + (budget - b) // min_price
    for b in range(budget + 1)
)
```

We check every possible budget allocation between first purchases and additional purchases.

### Python Code

```python
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        dp = [0] * (budget + 1)
        min_price = float('inf')

        for i in range(n):
            factor, price = items[i]
            min_price = min(min_price, price)

            count = 0
            for j in range(n):
                if items[j][0] % factor == 0:
                    count += 1

            for b in range(budget, price - 1, -1):
                dp[b] = max(
                    dp[b],
                    dp[b - price] + count
                )

        return max(
            dp[b] + (budget - b) // min_price
            for b in range(budget + 1)
        )
```

---

## Complexity Analysis

Let:

- `n` = number of items.
- `B` = available budget.

| Operation | Time Complexity |
|---|---|
| Calculate free-copy counts | O(n²) |
| DFS with memoization | O(n × B) |
| 1D Knapsack transitions | O(n × B) |
| Final budget calculation | O(B) |

### Approach 1: DFS + Memoization

- Time: O(n² + n × B)
- Space: O(n × B)

The memoization dictionary stores up to O(n × B) states, resulting in high memory overhead.

### Approach 2: 1D DP

- Time: O(n² + n × B)
- Space: O(B)

By removing the item index from the stored DP states, we reduce the auxiliary DP memory from O(n × B) to O(B).

---

## Key Takeaways

1. Identify the difference between first-time purchases and additional purchases.
2. A first purchase can generate multiple free copies, while subsequent purchases generate only one.
3. When each item type can contribute its special reward only once, the problem can be modeled as 0/1 Knapsack.
4. Backward iteration allows us to optimize 2D Knapsack into 1D DP.
5. When memoization exceeds memory limits, consider whether the same recurrence can be implemented iteratively with reduced state storage.

**The main optimization:** We didn't change the underlying DP logic. We changed how we store and process the states.