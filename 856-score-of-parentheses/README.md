# LeetCode 856 — Score of Parentheses

[LeetCode 856 — Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/)

## Problem

Given a balanced parentheses string `s`, calculate its score using these rules:

* `()` has a score of `1`.
* `AB` has a score of `A + B`, where `A` and `B` are balanced parentheses strings.
* `(A)` has a score of `2 * A`.

### Example

```text
Input:  s = "()"
Output: 1
```

```text
Input:  s = "(())"
Output: 2
```

```text
Input:  s = "()()"
Output: 2
```

---

## Intuition

The important observation is that we do not need to calculate the score of every nested group separately.

We can scan the string from left to right while tracking the current parenthesis `depth`.

For example:

```text
( ( ) )
0 1 2 1 0
```

Whenever we find a closing parenthesis `)`, we first decrease the depth.

Now, if the previous character was `(`, we have found the smallest unit:

```text
()
```

The score of this `()` depends on how deeply it is nested.

Every level of nesting doubles its score:

```text
()
        = 1

(())
        = 2

((()))
        = 4
```

So when we find `()`, its contribution is:

```text
2 ** depth
```

The key is that `depth` is decreased before calculating the score.

For example:

```text
((()))
```

At the innermost `)`:

```text
depth = 2
score += 2 ** 2
```

So the innermost `()` contributes `4`.

---

## Approach

We keep two variables:

* `depth` → current nesting depth.
* `res` → total score.

Then scan the string:

### When we see `(`

Increase the depth:

```python
depth += 1
```

### When we see `)`

Decrease the depth:

```python
depth -= 1
```

If the previous character was `(`, then we just closed an empty pair:

```text
()
```

So add its score:

```python
res += 2 ** depth
```

At the end, `res` contains the total score.

---

## Code

```python
class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        res = 0
        depth = 0

        for i, c in enumerate(s):

            if c == '(':
                depth += 1

            else:
                depth -= 1

                if s[i - 1] == '(':
                    res += 2 ** depth

        return res
```

```C
int scoreOfParentheses(char* s) {
    int res = 0;
    int depth =0;
    int n = strlen(s);
    
    for (int i=0;i<n;i++)
    {
        if (s[i]=='(')
        {
            depth++;
        }
        else{
            depth--;
            if (s[i-1]=='('){
                res+= 1<<depth;
            }
        }
    }
    return res;
}
```

---

## Example Walkthrough

For:

```text
s = "(()())"
```

We scan each character:

```text
(  -> depth = 1

(  -> depth = 2

)  -> depth = 1
     previous char was '('
     res += 2 ** 1 = 2

(  -> depth = 2

)  -> depth = 1
     previous char was '('
     res += 2 ** 1 = 2

)  -> depth = 0
```

Final result:

```text
res = 4
```

The two inner `()` groups each contribute `2`.

---

## Complexity

**Time:** `O(n)`
We scan the string once.

**Space:** `O(1)`
Only `res` and `depth` are used.
