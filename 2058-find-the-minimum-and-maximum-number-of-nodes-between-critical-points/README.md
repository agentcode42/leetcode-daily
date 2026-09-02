# LeetCode 2058 — Find the Minimum and Maximum Number of Nodes Between Critical Points

## Problem

Given a linked list, find the minimum and maximum distance between any two **critical points**.

A node is a critical point if it is either:

* A local maximum — its value is greater than both neighboring nodes.
* A local minimum — its value is smaller than both neighboring nodes.

Return:

`[minimum distance, maximum distance]`

If fewer than two critical points exist, return `[-1, -1]`.

## Approach 1 — Convert Linked List to Array

The first approach converts the linked list into an array.

Once the values are stored in an array, we can easily check each node against its previous and next values to identify critical points.

After finding all critical-point indices:

* The **minimum distance** is the minimum gap between consecutive critical points.
* The **maximum distance** is the distance between the first and last critical points.

### Complexity

* Time: `O(n)`
* Space: `O(n)`

## Approach 2 — Traverse the Linked List Directly

We can avoid storing the entire linked list in an array.

While traversing the linked list, we keep track of:

* The previous node
* The current node
* The position of the first critical point
* The position of the previous critical point
* The minimum distance found so far

When a critical point is found:

1. Calculate the distance from the previous critical point.
2. Update the minimum distance.
3. Update the position of the latest critical point.

At the end, the distance between the first and last critical points gives the maximum distance.

### Complexity

* Time: `O(n)`
* Space: `O(1)`

## Key Insight

We do not need to store every critical point.

For the **minimum distance**, we only need the distance between consecutive critical points.

For the **maximum distance**, we only need the first and last critical points.

Therefore, the linked-list traversal can solve the problem using **constant extra space**.

## Solutions

* [Python](python/solution.py)
