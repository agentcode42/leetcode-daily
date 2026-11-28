# 3947. Maximum Number of Items From Sale II

[LeetCode Problem Link](https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/)

## Problem Summary

We are given a list of items, where each item is represented as:

`[factor, price]`

We also have a limited budget.

When purchasing an item, we can receive one free copy of another item whose factor is divisible by the purchased item's factor.

Each purchased copy can generate at most one free item, and each pair of item types can be used only once for this purpose.

Our goal is to maximize the total number of items obtained without exceeding the budget.

---

## Intuition

The important observation is that purchasing an item can give us two items instead of one:

- One purchased item.
- One free item.

However, this bonus is available only while there are still eligible item types that have not been received for free from that particular item type.

We can calculate how many free items each item type can generate using its factor.

Let:

`gain[f] = number of other items whose factors are divisible by f`

For example, if we have:

```python
items = [
    [2, 10],
    [2, 12],
    [3, 8],
    [4, 5],
    [6, 7],
    [6, 9]
]
```

For factor `2`, the divisible factors are:

- 2 (two items)
- 4 (one item)
- 6 (two items)

That gives us five items in total.

We subtract one because an item cannot give itself for free.

Therefore:

`gain[2] = 5 - 1 = 4`

This means purchasing up to four copies of an item with factor 2 can generate four free items.

### Comparing Bonus Purchases With Normal Purchases

Let `min_price` be the cheapest item price.

A bonus purchase costs `price[i]` and gives us two items.

A normal purchase costs `min_price` and gives us one item.

We can compare their costs per item:

`price[i] / 2` versus `min_price`

There are three cases:

| Condition | Decision |
|---|---|
| `price[i] < 2 * min_price` | Bonus purchase is better |
| `price[i] == 2 * min_price` | Both choices are equally good |
| `price[i] > 2 * min_price` | Normal purchases are better |

Therefore, we only need to consider item types whose price is strictly less than twice the minimum price.

### Greedy Strategy

Since every useful bonus purchase gives exactly two items, we should prioritize the cheapest bonus purchases.

We can sort the items by price and process them in ascending order.

For every item:

1. Calculate how many bonus purchases are available using `gain[factor]`.
2. Calculate how many we can afford using the remaining budget.
3. Purchase the minimum of these two values.
4. Add two items for every bonus purchase.
5. Subtract the money spent.

Once we have processed all useful bonus purchases, we use the remaining budget to buy normal items at the cheapest price.

---

## Approach: Frequency Counting + Greedy

### Step 1: Build the Frequency Array

The factors are bounded by the number of items, so instead of checking every pair of items, we can count the frequency of each factor.

```python
freq = [0] * (n + 1)

for factor, price in items:
    freq[factor] += 1
```

### Step 2: Calculate the Number of Free Items

For every possible factor `f`, we visit all its multiples.

```python
gain = [0] * (n + 1)

for f in range(1, n + 1):
    for j in range(f, n + 1, f):
        gain[f] += freq[j]

    gain[f] -= 1
```

Why does this work?

Every factor divisible by `f` is a multiple of `f`.

Instead of checking every item individually, we sum the frequencies of all multiples.

This reduces the calculation from O(n²) to O(n log n).

### Step 3: Sort Items by Price

```python
items.sort(key=lambda x: x[1])
```

Sorting ensures that we process the cheapest bonus purchases first.

We also find the cheapest available item:

```python
min_price = items[0][1]
```

### Step 4: Greedy Purchasing

For each item, we calculate how many bonus purchases we can afford.

```python
res = 0

for factor, price in items:
    if price >= min_price * 2:
        break

    count = min(gain[factor], budget // price)

    res += count * 2
    budget -= count * price
```

Here:

- `gain[factor]` limits the number of free items we can generate.
- `budget // price` limits how many copies we can afford.
- Every bonus purchase gives us two items.

We stop when the price reaches twice the cheapest item price because normal purchases are at least as efficient.

### Step 5: Spend the Remaining Budget

After processing all useful bonus purchases, we buy as many normal items as possible.

```python
res += budget // min_price

return res
```

---

## Complete Python Solution

```python
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        gain = [0] * (n + 1)

        for f in range(1, n + 1):
            for j in range(f, n + 1, f):
                gain[f] += freq[j]

            gain[f] -= 1

        items.sort(key=lambda x: x[1])

        res = 0
        min_price = items[0][1]

        for factor, price in items:
            if price >= min_price * 2:
                break

            count = min(gain[factor], budget // price)

            res += count * 2
            budget -= count * price

        res += budget // min_price

        return res
```

---

## Simulated Example

Consider:

```python
items = [
    [1, 3],
    [2, 4],
    [3, 5]
]

budget = 25
```

First, calculate the gains:

| Factor | Divisible item factors | Gain |
|---:|---|---:|
| 1 | 1, 2, 3 | 2 |
| 2 | 2 | 0 |
| 3 | 3 | 0 |

The minimum price is 3.

The useful bonus purchases must cost less than:

`2 * 3 = 6`

Therefore, we sort and process the items:

| Item | Price | Gain | Bonus purchases | Cost | Items obtained |
|---|---:|---:|---:|---:|---:|
| Factor 1 | 3 | 2 | 2 | 6 | 4 |
| Factor 2 | 4 | 0 | 0 | 0 | 0 |
| Factor 3 | 5 | 0 | 0 | 0 | 0 |

After processing:

- Total bonus items = 4
- Money spent = 6
- Remaining budget = 19

We use the remaining budget to buy normal items at price 3:

`19 // 3 = 6`

Therefore:

`Total = 4 + 6 = 10 items`

---

## Complexity Analysis

Let `n` be the number of items.

| Operation | Time Complexity |
|---|---|
| Build frequency array | O(n) |
| Calculate gains | O(n log n) |
| Sort items | O(n log n) |
| Greedy purchasing | O(n) |

**Total Time Complexity:**

`O(n log n)`

**Space Complexity:**

`O(n)`

We use frequency and gain arrays of size `n + 1`.

---

## Key Takeaways

1. Frequency counting can replace nested pairwise divisibility checks.
2. Visiting multiples allows us to calculate the number of eligible items efficiently.
3. Comparing the cost per item reveals which purchases are worth prioritizing.
4. When every useful bonus purchase gives the same number of items, sorting by price provides an optimal greedy ordering.
5. Once bonus purchases are exhausted, the remaining budget can be spent on the cheapest normal item.

**Main optimization:** Instead of using DP over a potentially enormous budget, we recognize that bonus purchases have a fixed reward of two items and use a greedy strategy based on their prices.