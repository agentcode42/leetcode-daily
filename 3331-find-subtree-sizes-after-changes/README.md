# 3331. Find Subtree Sizes After Changes

[LeetCode Problem](https://leetcode.com/problems/find-subtree-sizes-after-changes/)

## Problem Summary

We are given:

- `parent`: An array representing the original tree. `parent[i]` is the parent of node `i`.
- `s`: A string where `s[i]` represents the character assigned to node `i`.

We need to modify the tree according to the following rule:

For every node (except the root), find its **nearest ancestor with the same character**. If such an ancestor exists, change the node's parent to that ancestor.

After all parent changes are completed, calculate the subtree size of every node in the modified tree.

A subtree includes the node itself and all its descendants.

## Intuition

The first challenge is finding the nearest ancestor with the same character for every node.

A straightforward approach would be to start from every node and travel upward through its ancestors until we find a matching character.

However, this would repeatedly traverse the same paths.

Instead, we can use DFS and maintain an array that remembers the most recent ancestor for each character.

```python
prev = [-1] * 26
```

Each position represents a lowercase English letter.

For example:

- `prev[0]` stores the most recent ancestor with character `'a'`.
- `prev[1]` stores the most recent ancestor with character `'b'`.
- And so on.

The important observation is that during DFS, all nodes currently on the recursion path are ancestors of the node being visited.

Therefore, the most recently encountered node with a particular character is automatically the nearest ancestor with that character.

We don't need to search upward at all.

## Approach

### 1. Build the original tree

First, convert the parent array into an adjacency list.

```python
curr_tree = defaultdict(list)

for i in range(1, n):
    curr_tree[parent[i]].append(i)
```

We need to preserve this original tree because our first DFS must follow the original parent-child relationships, even while we update the `parent` array.

### 2. Find the nearest matching ancestor using DFS

For every node, we perform the following operations:

```python
c = ord(s[node]) - ord('a')
old = prev[c]
```

Here, `c` represents the character's index, and `old` stores the previous occurrence of that character along the current DFS path.

**If a matching ancestor exists:**

```python
if old != -1:
    parent[node] = old
```

We update the node's parent to that nearest matching ancestor.

Next, we mark the current node as the most recent occurrence of its character:

```python
prev[c] = node
```

Then we explore all its children.

Finally, after finishing the current node's entire subtree, we restore the previous value:

```python
prev[c] = old
```

### Why do we restore `prev[c]`?

This is one of the most important parts of the solution.

Consider two different branches of the same tree.

A node visited in the first branch is not an ancestor of a node in the second branch.

If we don't restore `prev`, a node in the second branch could incorrectly identify a node from the first branch as its ancestor.

Restoring the previous value ensures that `prev` always represents only the ancestors along the current DFS path.

In other words:

- Enter a node: Save the previous occurrence.
- Visit its children: Make the current node available as an ancestor.
- Exit the node: Restore the previous occurrence.

This gives us the correct nearest matching ancestor without repeatedly traversing parent pointers.

### 3. Build the modified tree

Once the first DFS is complete, the `parent` array contains all the updated parent relationships.

Now we build a new adjacency list:

```python
new_tree = defaultdict(list)

for i in range(1, n):
    new_tree[parent[i]].append(i)
```

Notice that we build this tree only after completing the first DFS.

### 4. Calculate subtree sizes

Now the remaining task is a standard postorder DFS.

Every node starts with a subtree size of `1`, because the node itself belongs to its subtree.

Then we recursively calculate the sizes of its children and add them to the current node.

```python
def size(node):
    res[node] = 1

    for child in new_tree[node]:
        res[node] += size(child)

    return res[node]
```

Once the recursion finishes, `res[node]` contains the total number of nodes in that node's subtree.

## Example Walkthrough

Consider the following input:

```python
parent = [-1, 0, 0, 1, 1, 2, 2]
s = "abaabbc"
```

The original tree looks like this:

```text
             0(a)
            /    \
         1(b)    2(a)
         /  \    /  \
      3(a) 4(b) 5(b) 6(c)
```

### Step 1: Find the nearest matching ancestor

We traverse the original tree using DFS.

| Node | Character | Original Parent | Nearest Matching Ancestor | New Parent |
|---|---|---:|---:|---:|
| 0 | a | -1 | None | -1 |
| 1 | b | 0 | None | 0 |
| 2 | a | 0 | 0 | 0 |
| 3 | a | 1 | 0 | 0 |
| 4 | b | 1 | 1 | 1 |
| 5 | b | 2 | None | 2 |
| 6 | c | 2 | None | 2 |

Let's look at a few important cases.

**Node 3:**

Its original path to the root is:

```text
3(a) -> 1(b) -> 0(a)
```

The nearest ancestor with character `'a'` is node `0`.

Therefore:

```python
parent[3] = 0
```

**Node 4:**

Its original path to the root is:

```text
4(b) -> 1(b) -> 0(a)
```

The nearest matching ancestor is node `1`.

Its parent already points to node `1`, so nothing changes.

**Node 5:**

Its original path to the root is:

```text
5(b) -> 2(a) -> 0(a)
```

There is no ancestor with character `'b'`.

Therefore, its parent remains node `2`.

This is also where restoring `prev` matters. Node `4` was visited before node `5`, but node `4` is not an ancestor of node `5`. The restoration prevents node `5` from incorrectly seeing node `4` as a matching ancestor.

After processing every node, the modified parent array becomes:

```python
[-1, 0, 0, 0, 1, 2, 2]
```

### Step 2: Construct the modified tree

The resulting tree is:

```text
              0(a)
           /    |    \
        1(b)   2(a)   3(a)
         |     /  \
        4(b)  5(b) 6(c)
```

### Step 3: Calculate subtree sizes

Now we perform the second DFS.

We start from the bottom of the tree and calculate each node's subtree size.

| Node | Children | Subtree Size |
|---|---|---:|
| 3 | None | 1 |
| 4 | None | 1 |
| 5 | None | 1 |
| 6 | None | 1 |
| 1 | 4 | 2 |
| 2 | 5, 6 | 3 |
| 0 | 1, 2, 3 | 7 |

For example:

```text
size(1) = 1 + size(4)
        = 1 + 1
        = 2

size(2) = 1 + size(5) + size(6)
        = 1 + 1 + 1
        = 3

size(0) = 1 + size(1) + size(2) + size(3)
        = 1 + 2 + 3 + 1
        = 7
```

The final result is:

```python
[7, 2, 3, 1, 1, 1, 1]
```

## Python Solution

```python
from collections import defaultdict
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        curr_tree = defaultdict(list)
        for i in range(1, n):
            curr_tree[parent[i]].append(i)

        prev = [-1] * 26

        def dfs(node):
            c = ord(s[node]) - ord('a')
            old = prev[c]

            if old != -1:
                parent[node] = old

            prev[c] = node

            for child in curr_tree[node]:
                dfs(child)

            prev[c] = old

        dfs(0)

        new_tree = defaultdict(list)
        for i in range(1, n):
            new_tree[parent[i]].append(i)

        res = [0] * n

        def size(node):
            res[node] = 1

            for child in new_tree[node]:
                res[node] += size(child)

            return res[node]

        size(0)
        return res
```

## Complexity Analysis

Let `n` be the number of nodes.

**Time Complexity: O(n)**

- Building the original adjacency list takes O(n).
- The first DFS visits every node exactly once: O(n).
- Building the modified adjacency list takes O(n).
- The second DFS calculates every subtree size exactly once: O(n).

Therefore, the overall time complexity is **O(n)**.

**Space Complexity: O(n)**

- The original adjacency list requires O(n) space.
- The modified adjacency list requires O(n) space.
- The result array requires O(n) space.
- The DFS recursion stack can require O(n) space in the worst case.
- The `prev` array has a fixed size of 26.

Therefore, the overall auxiliary space complexity is **O(n)**.

## Key Takeaway

The interesting part of this problem is not calculating subtree sizes. That is a standard DFS problem.

The real challenge is efficiently identifying the nearest ancestor with the same character.

By maintaining the most recent occurrence of every character along the current DFS path, we turn repeated ancestor searches into a single traversal.

The restoration step is what makes this technique work correctly across different branches.

**One DFS to modify the tree, another DFS to calculate the subtree sizes.**