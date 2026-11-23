# 1352. Product of the Last K Numbers

[LeetCode Problem](https://leetcode.com/problems/product-of-the-last-k-numbers/)

## Problem Summary

Design a data structure that supports two operations:

- `add(num)`: Add a number to the end of the stream.
- `getProduct(k)`: Return the product of the last `k` numbers in the stream.

The goal is to perform both operations in **O(1) time**.

## Intuition: Prefix Products

Instead of multiplying the last `k` numbers every time `getProduct(k)` is called, we can maintain cumulative products using a prefix product array.

The idea is similar to prefix sums, but instead of subtracting two prefix sums, we divide two prefix products.

Suppose we have the following numbers:

```text
[2, 5, 4]
```

Their prefix products are:

```text
Numbers:          [2, 5, 4]
Prefix Products:  [1, 2, 10, 40]
```

The initial `1` is important because it gives us a starting point for multiplication and allows us to handle queries that cover the entire stored sequence.

To calculate the product of the last `k` numbers, we divide the latest prefix product by the prefix product immediately before those `k` numbers.

**Formula:**

```text
Product of last k numbers =
    latest_prefix_product / prefix_product_before_last_k
```

For example, to calculate the product of the last two numbers:

```text
40 / 2 = 20
```

This works because the earlier portion of the cumulative product cancels out, leaving only the product of the requested numbers.

## The Important Problem: Handling Zero

There is one issue with using prefix products: division by zero.

Consider:

```text
[3, 0, 2, 5, 4]
```

If we continue multiplying normally, the prefix products would become:

```text
[1, 3, 0, 0, 0, 0]
```

Once a zero appears, every subsequent prefix product becomes zero, making division impossible.

We can solve this by **resetting the prefix product array whenever we encounter zero**.

After adding zero, we start a fresh prefix product sequence:

```text
[1]
```

We only maintain products of numbers appearing after the most recent zero.

We also maintain the number of elements in this current sequence.

This gives us a simple way to identify whether a query includes a zero:

- If `k` is greater than the number of elements since the last zero, the requested range contains a zero, so return `0`.
- Otherwise, all requested elements belong to the current prefix product sequence, and we can calculate the answer using division.

## Approach

### 1. Initialization

Start with:

```python
self.product_nums = [1]
self.length = 0
```

The prefix product array begins with `1`, and `length` tracks how many non-zero numbers have been added since the latest zero.

The C implementation uses the same idea with an array, `size`, and `capacity`.

### 2. Add Operation

When adding a number:

**If the number is zero:**

- Reset the prefix product array to `[1]`.
- Reset the current length to `0`.

**Otherwise:**

- Multiply the new number by the latest prefix product.
- Append the resulting product.
- Increase the current length.

This ensures that every stored prefix product represents a sequence containing no zeros.

### 3. GetProduct Operation

First, check whether `k` exceeds the number of elements stored since the last zero.

```python
if k > self.length:
    return 0
```

If it does, the requested range includes a zero.

Otherwise, calculate the answer by dividing the latest prefix product by the prefix product immediately before the last `k` elements.

```python
return self.product_nums[-1] // self.product_nums[-(k+1)]
```

In C, the equivalent calculation uses array indices:

```c
return obj->prefix_product[obj->size] /
       obj->prefix_product[obj->size-k];
```

Both implementations perform the same calculation.

## Example Walkthrough

Consider the following operations:

```text
add(3)
add(0)
add(2)
add(5)
add(4)
getProduct(2)
getProduct(3)
getProduct(4)
add(8)
getProduct(2)
```

The prefix products evolve as follows:

| Operation | Prefix Products | Result |
|---|---|---|
| add(3) | [1, 3] | - |
| add(0) | [1] | - |
| add(2) | [1, 2] | - |
| add(5) | [1, 2, 10] | - |
| add(4) | [1, 2, 10, 40] | - |
| getProduct(2) | [1, 2, 10, 40] | 20 |
| getProduct(3) | [1, 2, 10, 40] | 40 |
| getProduct(4) | [1, 2, 10, 40] | 0 |
| add(8) | [1, 2, 10, 40, 320] | - |
| getProduct(2) | [1, 2, 10, 40, 320] | 32 |

Let's examine the queries:

**getProduct(2)**

```text
40 / 2 = 20
```

The last two numbers are `5 * 4`.

**getProduct(3)**

```text
40 / 1 = 40
```

The last three numbers are `2 * 5 * 4`.

**getProduct(4)**

Only three non-zero numbers exist after the most recent zero.

Since `4 > 3`, the requested range contains the zero.

Therefore, return `0`.

**getProduct(2)** after adding `8`:

```text
320 / 10 = 32
```

The last two numbers are `4 * 8`.

## Complexity Analysis

Let `n` be the number of non-zero elements added since the most recent zero.

| Operation | Time Complexity | Explanation |
|---|---|---|
| Initialization | O(1) | Create the initial prefix product |
| add(num) | O(1) | One multiplication and one append |
| getProduct(k) | O(1) | One boundary check and one division |

**Space Complexity: O(n)**

We store one prefix product for every non-zero number added since the most recent zero.

A zero resets this storage, so the required space depends on the current zero-free segment rather than the entire history.

Both implementations achieve the required **O(1) time complexity per operation**.

---

## Python Solution

```python
class ProductOfNumbers:

    def __init__(self):
        self.product_nums = [1]
        self.length = 0

    def add(self, num: int) -> None:
        if num != 0:
            self.product_nums.append(self.product_nums[-1] * num)
            self.length += 1
        else:
            self.product_nums = [1]
            self.length = 0

    def getProduct(self, k: int) -> int:
        if k > self.length:
            return 0

        return self.product_nums[-1] // self.product_nums[-(k+1)]
```

## C Solution

```c
#include <stdlib.h>
#include <stdio.h>

#define MAX_CAPACITY 40001

typedef struct {
    int* prefix_product;
    int size;
    int capacity;
} ProductOfNumbers;


ProductOfNumbers* productOfNumbersCreate() {
    ProductOfNumbers* obj =
        (ProductOfNumbers*)malloc(sizeof(ProductOfNumbers));

    obj->capacity = MAX_CAPACITY;

    obj->prefix_product =
        (int*)malloc(sizeof(int) * obj->capacity);

    obj->size = 0;
    obj->prefix_product[0] = 1;

    return obj;
}

void productOfNumbersAdd(ProductOfNumbers* obj, int num) {

    if (num == 0) {
        obj->size = 0;
        obj->prefix_product[0] = 1;
        return;
    }

    if (obj->size + 1 >= obj->capacity) {
        obj->capacity *= 2;

        obj->prefix_product = (int*)realloc(
            obj->prefix_product,
            sizeof(int) * obj->capacity
        );
    }

    obj->prefix_product[obj->size + 1] =
        obj->prefix_product[obj->size] * num;

    obj->size++;
}

int productOfNumbersGetProduct(ProductOfNumbers* obj, int k) {

    if (k > obj->size)
        return 0;

    return obj->prefix_product[obj->size] /
           obj->prefix_product[obj->size - k];
}

void productOfNumbersFree(ProductOfNumbers* obj) {
    free(obj->prefix_product);
    free(obj);
}
```

