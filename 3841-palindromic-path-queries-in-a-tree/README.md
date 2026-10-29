# 3841. Palindromic Path Queries in a Tree

[LeetCode Problem](https://leetcode.com/problems/palindromic-path-queries-in-a-tree/)

## Problem Summary

We are given a tree with `n` nodes, where each node contains a lowercase English letter. We must process two types of queries:

- **Update:** Change the character at a given node.
- **Query:** Determine whether the characters along the unique path between two nodes can be rearranged to form a palindrome.

A palindrome reads the same forward and backward. Since rearrangement is allowed, the characters do not need to be in palindrome order initially.

For a string to be rearranged into a palindrome, **at most one character can appear an odd number of times**.

## Intuition

Checking every node on a path for every query would be too slow. Instead, we can represent the character frequencies using a bitmask.

Each of the 26 lowercase letters gets one bit. We use XOR to toggle the corresponding bit whenever a character is encountered:

- A bit set to `1` means that character occurs an odd number of times.
- A bit set to `0` means that character occurs an even number of times.

XOR automatically cancels characters that appear an even number of times. Therefore, we only need to count how many bits remain set in the final mask.

If at most one bit is set, the path can be rearranged into a palindrome.

## Approach

### 1. Build the tree and prepare ancestors

Build an adjacency list from `edges`.

Run DFS from node `0` to calculate:

- `tin[u]`: the entry time of node `u`.
- `tout[u]`: the exit time of node `u`.
- `depth[u]`: the depth of node `u`.
- `parent[k][u]`: the ancestor of node `u` reached by moving upward \(2^k\) levels.

Binary lifting lets us find the lowest common ancestor (LCA) of two nodes efficiently.

### 2. Represent characters using bitmasks

Convert each character into a bitmask:

`1 << (ord(c) - 97)`

For example, `a` corresponds to bit 0, `b` to bit 1, and `c` to bit 2.

Store each node's current mask in `char_mask`.

### 3. Maintain subtree information with a Fenwick tree

Use a Fenwick tree that supports XOR updates and prefix XOR queries.

For each node, add its character mask at both `tin[u]` and `tout[u]`. These two events allow us to calculate the XOR of the characters on the path from the root to any node.

The root-to-node mask is:

`prefix_xor(tin[u])`

When a character changes, calculate the XOR difference between its old and new masks. Update both recorded positions in the Fenwick tree using this difference.

This avoids rebuilding the tree information after every update.

### 4. Process update queries

For an update to node `u`:

1. Calculate the new character's bitmask.
2. XOR it with the old mask to obtain the difference.
3. Update the Fenwick tree at `tin[u]` and `tout[u]`.
4. Store the new mask in `char_mask[u]`.

### 5. Process path queries

For a query between nodes `u` and `v`, find their LCA, called `ancestor`.

Calculate the path mask using:

`path_mask = prefix_xor(tin[u]) ^ prefix_xor(tin[v]) ^ char_mask[ancestor]`

The two root-to-node masks cancel their shared portion. The LCA's character is then included once, producing the parity mask for the complete path.

Finally, check:

`(path_mask & (path_mask - 1)) == 0`

This expression is true when the mask contains zero or one set bit. Therefore, it tells us whether the path can be rearranged into a palindrome.

Append the result to `answer` and return the answers for all query operations.

## Example

**Input:**

```python
n = 3
edges = [[0, 1], [1, 2]]
s = "aba"
queries = ["query 0 2", "update 1 c", "query 0 2"]
```

**Explanation:**

The tree is a chain:

```text
0(a) — 1(b) — 2(a)
```

1. `query 0 2`: The path contains `a, b, a`. It is already a palindrome, so the answer is `True`.
2. `update 1 c`: Change the character at node `1` from `b` to `c`.
3. `query 0 2`: The path now contains `a, c, a`. It is still a palindrome, so the answer is `True`.

**Output:**

```python
[True, True]
```

## Complexity Analysis

Let \(n\) be the number of nodes and \(q\) the number of queries.

- **Time Complexity:** \(O(n \log n + q \log n)\)
  - Building the ancestor table takes \(O(n \log n)\).
  - Each update takes \(O(\log n)\).
  - Each path query takes \(O(\log n)\) for LCA and Fenwick tree operations.

- **Space Complexity:** \(O(n \log n)\)
  - The ancestor table requires \(O(n \log n)\) space.
  - The tree, DFS arrays, character masks, and Fenwick tree require \(O(n)\) additional space.

## Key Takeaway

The main idea is to combine **bitmask parity, DFS entry/exit times, a Fenwick tree, and binary lifting**. This allows us to handle character updates and palindrome-path queries efficiently without traversing the entire path for every query.