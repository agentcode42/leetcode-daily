# 1807. Evaluate the Bracket Pairs of a String

[LeetCode Problem](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/)

## Problem

You are given:

* A string `s` containing lowercase letters, parentheses `(` and `)`, and possibly other characters.
* A list `knowledge`, where each pair contains a key and its corresponding value.

Every pair of parentheses in `s` contains a key.

For each key:

* If the key exists in `knowledge`, replace `(key)` with its corresponding value.
* If the key does not exist, replace `(key)` with `?`.
* Characters outside parentheses remain unchanged.

Return the resulting string.

### Example

```text
Input:
s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]

Output:
"bobistwoyearsold"
```

If a key is missing:

```text
Input:
s = "hi(name)"
knowledge = []

Output:
"hi?"
```

---

## Intuition

The main idea is to separate the problem into two simple tasks:

1. Convert `knowledge` into a dictionary so we can quickly find the value of any key.
2. Scan the string and detect the content between `(` and `)`.

For example:

```text
"hello(name)!"
       ↑    ↑
       key = "name"
```

Once we find `)` we know that the key starts just after the most recent `(`.

So we store the position of `(` in `start`.

When we encounter `)`:

```python
key = s[start + 1:i]
```

Now we can look up the key in our dictionary.

If it exists, append its value.

Otherwise, append `"?"`.

Characters outside parentheses are directly added to the result.

---

## Approach

### 1. Create a dictionary

Convert the `knowledge` list into a dictionary:

```python
k = dict(knowledge)
```

This allows us to check whether a key exists and retrieve its value efficiently.

---

### 2. Scan the string

We iterate through the string using `enumerate()`.

```python
for i, c in enumerate(s):
```

When we see:

```python
c == "("
```

we remember its position:

```python
start = i
```

---

### 3. Process a key when `)` is found

When we encounter `)`:

```python
key = s[start + 1:i]
```

This extracts everything between the parentheses.

For example:

```text
s = "hi(name)"
       ↑   ↑
     start  i
```

The extracted key is:

```text
"name"
```

---

### 4. Replace the key

We initially assume the key does not exist:

```python
val = "?"
```

Then check the dictionary:

```python
if key in k:
    val = k[key]
```

Finally, add the value to the result:

```python
res.append(val)
```

---

### 5. Keep normal characters

If the current character is not inside a bracket pair, we add it directly.

The condition:

```python
elif start < 0:
    res.append(c)
```

ensures that characters before the first `(` are added normally.

Characters between `(` and `)` are skipped because they are part of a key that will be replaced when `)` is reached.

---

## Code

```python
class Solution:

    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        k = dict(knowledge)

        res = []

        start = -1

        for i, c in enumerate(s):

            if c == "(":
                start = i

            if c == ")":
                key = s[start + 1:i]

                val = "?"

                if key in k:
                    val = k[key]

                res.append(val)

            elif start < 0:
                res.append(c)

        return "".join(res)
```

---

## Complexity

Let `n` be the length of the string `s`, and let `m` be the total size of the `knowledge` entries.

### Time Complexity

```text
O(n + m)
```

Creating the dictionary takes time proportional to the size of `knowledge`, while scanning the string takes `O(n)`.

Extracting a key using slicing takes time proportional to the key length, but across the entire input the total amount of key text processed is bounded by the string length.

### Space Complexity

```text
O(n + m)
```

The dictionary stores the knowledge pairs, and the result string/list can contain up to `O(n)` characters.

---

## Key Takeaway

The important observation is that we don't need complicated parsing.

We only need to remember where the current `(` starts.

When `)` appears:

```text
( key )
  ↑   ↑
 start i
```

we extract the key, look it up in the dictionary, and append the replacement value.

This turns the problem into a straightforward **string traversal + hash map lookup**.
